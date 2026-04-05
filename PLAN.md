# orbid

Automated LEO satellite signal detection and attribution framework using SDR.

## Scope

Framework do automatycznego wykrywania i klasyfikacji sygnałów satelitarnych w paśmie VHF/UHF/L-band przy użyciu odbiornika RTL-SDR. System koreluje detekcje RF z predykcją przelotów orbitalnych, umożliwiając atrybucję sygnału do konkretnego obiektu na orbicie.

## Architecture

```
┌─────────────┐     ┌─────────────┐     ┌──────────────┐
│  predictor   │────▶│   scanner    │────▶│   detector   │
│  (TLE/SGP4)  │     │  (RTL-SDR)   │     │  (DSP/FFT)   │
└─────────────┘     └─────────────┘     └──────┬───────┘
                                               │
                    ┌─────────────┐     ┌──────▼───────┐
                    │  correlator  │◀────│  classifier  │
                    │  (report)    │     │  (sigprint)  │
                    └─────────────┘     └──────────────┘
```

### Modules

**predictor** - harmonogram przelotów satelitów nad zadaną lokalizacją.
- Źródła TLE: CelesTrak, Space-Track (wymaga konta)
- Propagacja: SGP4 (`skyfield` lub `python-sgp4`)
- Filtrowanie po NORAD ID, COSPAR designator, grupach orbitalnych
- Output: okna czasowe (AOS/LOS) z azimuth/elevation

**scanner** - sterowanie odbiornikiem RTL-SDR, nagrywanie IQ.
- Backend: `pyrtlsdr` lub `SoapySDR`
- Tryb survey: `rtl_power`-compatible sweep po zdefiniowanych pasmach
- Tryb targeted: nagrywanie IQ w oknach przelotów z predictor
- Konfiguracja: centrum, bandwidth, gain, sample rate

**detector** - analiza widmowa, wykrywanie sygnałów powyżej progu szumu.
- FFT z oknem (Hanning/Blackman), uśrednianie widmowe
- Detekcja peak: adaptacyjny próg SNR ponad noise floor
- Estymacja parametrów: częstotliwość centralna, bandwidth zajęty, drift dopplerowski
- Output: lista detekcji z timestampem i parametrami

**classifier** - identyfikacja typu sygnału na podstawie sygnatury.
- Baza sygnatur: modulacja (FM, QPSK, BPSK, FSK), symbol rate, bandwidth
- Źródła referencyjne: SatNOGS DB (API), SigIDWiki
- Metoda: porównanie cech z bazą, scoring podobieństwa
- Rozszerzenie (opcjonalne): klasyfikator ML na spektrogramach (CNN)

**correlator** - łączenie detekcji RF z predykcją orbitalną.
- Korelacja czasowa: detekcja w oknie AOS-LOS satelity?
- Korelacja częstotliwościowa: czy freq pasuje do znanego transmitera?
- Korelacja dopplerowska: czy drift pasuje do predykcji orbitalnej?
- Output: raport atrybucji z confidence score

## Target frequency bands

| Pasmo | Zakres | Sygnały |
|-------|--------|---------|
| VHF | 136-138 MHz | APT/LRPT (meteo), NOAA, Meteor-M |
| VHF | 144-146 MHz | amatorskie LEO |
| UHF | 400-403 MHz | telemetria LEO, Gonets-M |
| UHF | 435-438 MHz | amatorskie LEO, cubesaty |
| L-band | 1598-1616 MHz | GLONASS L1 (FDMA) |

## Data sources

- **TLE**: CelesTrak (`celestrak.org`), Space-Track (`space-track.org`)
- **Satellite transmitters**: SatNOGS DB (`db.satnogs.org/api/`)
- **Signal reference**: SigIDWiki (`sigidwiki.com`)
- **Satellite catalog**: filtrowanie po operatorze/kraju pochodzenia (COSPAR prefix, NORAD catalog)

## Directory structure

```
orbid/
├── orbid/
│   ├── __init__.py
│   ├── predictor.py
│   ├── scanner.py
│   ├── detector.py
│   ├── classifier.py
│   ├── correlator.py
│   ├── config.py
│   └── db/
│       ├── __init__.py
│       ├── tle.py          # TLE fetch & cache
│       └── sigdb.py         # SatNOGS/SigID interface
├── data/
│   ├── tle/                 # cached TLE sets
│   ├── signatures/          # signal signature database
│   └── recordings/          # IQ recordings (gitignored)
├── notebooks/               # Jupyter - analiza, prototypy
├── tests/
├── config.yaml              # lokalizacja, pasma, parametry SDR
├── requirements.txt
├── PLAN.md
└── README.md
```

## Milestones

### M1: Predictor (tydzień 1-2)
- [ ] Fetch TLE z CelesTrak (grupy: weather, navigation, military, cubesat)
- [ ] Cache TLE lokalnie z timestampem aktualności
- [ ] Predykcja przelotów dla zadanej lokalizacji (lat/lon/alt)
- [ ] Filtrowanie po COSPAR country code / operatorze
- [ ] Generowanie harmonogramu w formacie JSON
- [ ] Testy: porównanie z Heavens-Above / N2YO

### M2: Scanner (tydzień 3-4)
- [ ] Interfejs pyrtlsdr: set freq, gain, sample rate
- [ ] Tryb survey: sweep pasma, zapis PSD (power spectral density)
- [ ] Tryb targeted: nagrywanie IQ w oknie przelotu z M1
- [ ] Zapis metadanych: timestamp, freq, gain, lokalizacja
- [ ] Format zapisu: SigMF (metadata) + raw IQ (.cf32)
- [ ] Test: nagranie przelotu NOAA APT na 137 MHz

### M3: Detector (tydzień 5-6)
- [ ] Pipeline FFT: okno, averaging, noise floor estimation
- [ ] Algorytm detekcji: CFAR (Constant False Alarm Rate) lub adaptive threshold
- [ ] Estymacja Dopplera: śledzenie driftu w czasie przelotu
- [ ] Estymacja bandwidth zajętego
- [ ] Output: lista detekcji (freq, BW, SNR, timestamp, duration)
- [ ] Test: detekcja NOAA/Meteor w nagraniach z M2

### M4: Classifier (tydzień 7-9)
- [ ] Pobieranie bazy transmiterów z SatNOGS API
- [ ] Budowa lokalnej bazy sygnatur (modulacja, baudrate, BW)
- [ ] Feature extraction ze spektrogramu: bandwidth, periodyczność, kształt widma
- [ ] Scoring: metryka podobieństwa detekcja vs sygnatura
- [ ] Opcjonalnie: klasyfikator CNN na waterfall images (transfer learning)
- [ ] Test: rozróżnienie NOAA APT vs Meteor LRPT vs Meteor HRPT

### M5: Correlator + integration (tydzień 10-12)
- [ ] Korelacja czasowa: detekcja ∩ okno przelotu
- [ ] Korelacja częstotliwościowa: detekcja.freq ∈ transmiter.freq ± doppler
- [ ] Walidacja dopplerowska: porównanie obserwowanego driftu z predykcją SGP4
- [ ] Confidence scoring: multi-factor (czas, freq, doppler, sygnatura)
- [ ] Raport: JSON + opcjonalnie dashboard (Streamlit / Grafana)
- [ ] Integration test: pełny pipeline od TLE do raportu atrybucji

### M6: Ewaluacja i dokumentacja (tydzień 13-14)
- [ ] Ground truth: walidacja na znanych sygnałach (NOAA, Meteor, GLONASS)
- [ ] Metryki: precision, recall, confusion matrix per klasa satelity
- [ ] Analiza ograniczeń: false positives z RFI, sygnały naziemne w tych pasmach
- [ ] Dokumentacja techniczna
- [ ] Przykłady użycia (Jupyter notebooks)

## Hardware requirements

- RTL-SDR v3 (lub kompatybilny)
- Antena: discone (szerokopasmowa) lub turnstile/QFH (137 MHz) + antena L-band
- Opcjonalnie: LNA (np. Nooelec SAWbird dla 137 MHz lub L-band)
- Komputer z Linuxem (natywny lub WSL2)

## Key dependencies

- `pyrtlsdr` lub `SoapySDR` - kontrola SDR
- `skyfield` - predykcja orbitalna (preferowane nad `python-sgp4` - wyższa precyzja)
- `numpy`, `scipy` - DSP
- `matplotlib` - wizualizacja widm i waterfall
- `requests` - API calls (CelesTrak, SatNOGS)
- `sigmf` - standard metadanych IQ

## References

- SatNOGS: https://satnogs.org / https://db.satnogs.org
- SigIDWiki: https://sigidwiki.com
- CelesTrak: https://celestrak.org
- SigMF: https://sigmf.org
- RTL-SDR blog: https://rtl-sdr.com
