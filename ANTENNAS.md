# Antenna Guide for orbid

A practical guide to building DIY antennas for satellite signal detection with RTL-SDR. Written for someone without a workshop, using only basic tools and hardware store materials.

## Quick reference: which antenna for which tasks?

| Antenna | Band | Frequency | orbid tasks covered | Difficulty | Cost |
|---------|------|-----------|---------------------|------------|------|
| V-Dipole | VHF | 137 MHz | #1-#4, #7-#12, #23-#25 (Meteor-M, NOAA) | Trivial | ~$0 |
| Turnstile | UHF | 435 MHz | #1-#4, #7-#12, #13-#16, #18-#23 (Gonets-M, cubesats, telemetry) | Easy | ~$5-10 |
| Helix or Patch | L-band | 1602 MHz | #1-#4, #7-#12, #23-#25 (GLONASS L1) | Moderate | ~$10-50 |

**Start with the V-Dipole.** It takes 30 minutes to build, costs almost nothing, and guarantees your first satellite reception on day one. The other antennas can wait.

---

## Antenna 1: V-Dipole for 137 MHz (VHF weather satellites)

**What it receives:** NOAA 15/18/19 (APT), Meteor-M N2-3/N2-4 (LRPT)

**Why this design:** A QFH antenna is theoretically 1-2 dB better, but it is hard to build precisely without a workshop, and construction errors easily eat that advantage. The V-Dipole gives 20 dB rejection of terrestrial FM broadcast interference (vs only 3 dB for QFH), which matters more in practice, especially in a city.

### How it works

Two metal rods arranged in a horizontal "V" shape at 120 degrees, oriented North-South. The radiation pattern points skyward in a figure-zero shape, which is ideal for polar-orbiting satellites that always travel roughly N-S or S-N. Horizontal polarization means a 3 dB loss on the circularly polarized satellite signal, but also 20 dB suppression of vertically polarized terrestrial interference.

### Materials

- 2x aluminum or copper rods, each **53.4 cm** long, 3-4 mm diameter (welding rods, stiff wire, or telescopic antenna elements)
- 1x terminal block ("chocolate block" / "choc block") or a PVC pipe end cap with bolts
- 1x coaxial cable (RG-58 or RG-174), 2-5 meters, with SMA connector for RTL-SDR
- Cable ties or tape for mounting

**Total cost:** Under $5 if you buy rods. $0 if you use stiff copper wire.

### Build instructions

1. Cut two rods to exactly **53.4 cm** each (this is lambda/4 for 137.5 MHz, accounting for velocity factor).
2. Strip the coax: connect the center conductor to one rod, the shield to the other rod. Use the terminal block to clamp everything.
3. Spread the rods to form a **120-degree angle** (like a wide V).
4. Mount the antenna **horizontally**, outdoors, with a clear view of the sky. Orient the V so the open end points East or West (the rods point N and S).
5. Elevate it at least 1 meter above the ground or any metal surface.

**Important:** The 53.4 cm length includes the connecting wire up to the terminal block. Keep the wire between the rod and the coax as short as possible (under 2 cm).

### Mounting without a workshop

- Zip-tie the terminal block to a broomstick, PVC pipe, or wooden pole.
- Lean the pole against a balcony railing or tape it to a window frame, pointing up.
- For a more permanent setup: use a PVC end cap with two bolts at 120 degrees as the center piece (no terminal block needed).

### Resources

- **Original design by Adam 9A4QV:** http://lna4all.blogspot.com/2017/02/diy-137-mhz-wx-sat-v-dipole-antenna.html
- **Detailed PDF with theory:** https://w4hhh.org/wp-content/uploads/2022/09/DIY-137MHz-WX-sat-V-dipole-antenna.pdf
- **Video tutorial by Adam 9A4QV:** https://www.youtube.com/watch?v=kf8CytxePkU
- **RTL-SDR Blog summary:** https://www.rtl-sdr.com/simple-noaameteor-weather-satellite-antenna-137-mhz-v-dipole/
- **Video by Baltic Lab** (using RTL-SDR dipole kit as V-dipole): search "Baltic Lab V dipole weather satellite" on YouTube
- **3D-printable 120-degree bracket** (if you have access to a 3D printer): https://www.thingiverse.com/thing:4693498
- **Alternative build with PVC end cap:** https://vu3dxr.in/diy-137-mhz-v-dipole-antenna-for-weather-satellites-reception/

### Validation

Point the antenna outside, tune RTL-SDR to 137.100 MHz (NOAA 19), 137.620 MHz (NOAA 15), or 137.912 MHz (NOAA 18). Use https://www.n2yo.com/ to check when the next pass occurs over your location. You should see a strong signal rising on the waterfall display in SDR++ or SDR# as the satellite crosses the sky.

### If you already have the RTL-SDR Blog dipole kit

You don't need to build anything for VHF. Extend the larger telescopic elements to **53.4 cm** each, angle them to 120 degrees horizontally, and you have a working V-Dipole. Mount it outdoors with the included suction cup or tripod.

---

## Antenna 2: Turnstile for 435 MHz (UHF satellite telemetry)

**What it receives:** CubeSat beacons (435-438 MHz), Gonets-M telemetry (~400 MHz), amateur LEO satellites

**Why this design:** A turnstile is two crossed dipoles fed 90 degrees out of phase, producing right-hand circular polarization (RHCP). It is the simplest circularly polarized antenna you can build, and the SatNOGS community uses it as a standard ground station antenna.

### Materials

- 4x metal rods (copper or aluminum), each **16.4 cm** long for 435 MHz (lambda/4)
- 1x coaxial cable (RG-58), about 3-5 meters, with SMA connector
- 1x short piece of coax for the phasing harness: **11.2 cm** of RG-58 (this is lambda/4 * velocity_factor for 435 MHz; RG-58 velocity factor is 0.66)
- 1x PVC pipe (20 mm diameter, ~30 cm long) for the boom
- Solder, soldering iron, heat shrink tubing
- Optional: 3D-printed holders (see link below)

**Total cost:** $5-10

### Build instructions

1. Cut 4 rods to **16.4 cm** each.
2. Mount two rods as a dipole, centered on the PVC pipe. Cut each in half at the center (two halves of 8.2 cm with a gap between them for the feed point).
3. Mount the second dipole perpendicular to the first, 90 degrees rotated, on the same PVC pipe, slightly above or below the first.
4. Connect coax directly to one dipole (center conductor to one half, shield to the other).
5. Connect the second dipole through the **phasing harness**: a quarter-wave section of coax that introduces the 90-degree phase shift needed for circular polarization.
6. Join both feeds at a common point connected to the main coax going to the RTL-SDR.

This is the one build that requires soldering. If you have never soldered before, watch a 10-minute YouTube tutorial first. The joints don't need to be pretty, just electrically solid.

### Resources

- **Alicja's SatNOGS turnstile tutorial (with 3D printable parts):** https://alicja.space/blog/how-to-build-turnstile-antenna/
- **RTL-SDR Blog on cubesat reception with eggbeater (similar concept):** https://www.rtl-sdr.com/chasing-cubesats-on-a-25-budget-with-an-rtl-sdr-and-homemade-antenna/
- **SatNOGS ground station wiki (antenna section):** https://wiki.satnogs.org/
- **Eggbeater II design by K5OE (more advanced alternative):** http://wb5rmg.somenet.net/k5oe/Eggbeater_2.html
- **ZR6AIC eggbeater build log with dimensions:** https://zr6aic.blogspot.com/2013/03/building-my-eggbeater-ii-omni-leo.html

### Alternative: simple dipole

If soldering the phasing harness seems too complex, start with a plain dipole: two rods of 16.4 cm, straight (not V-shaped like the VHF antenna), mounted vertically. You will lose ~3 dB compared to a turnstile, but many cubesat beacons are strong enough to be received this way.

---

## Antenna 3: L-Band for 1602 MHz (GLONASS L1)

**What it receives:** GLONASS L1 navigation signals (FDMA, 1598-1616 MHz)

**Why this is harder:** RTL-SDR sensitivity degrades significantly above 1.2 GHz. You will almost certainly need a low-noise amplifier (LNA) between the antenna and the dongle. The antenna itself also needs to be more precise, because at 1.6 GHz the wavelength is only ~19 cm and construction tolerances matter more.

**Recommendation:** Unless GLONASS reception is critical for your thesis, skip this antenna initially and focus on VHF + UHF. Come back to L-band later if time permits.

### Option A: DIY 7-turn helix (~$10 + LNA)

A helical antenna wound around a PVC pipe, with a flat metal reflector. This is the highest-performing DIY option for L-band.

**Materials:**
- 1x PVC pipe, ~35 mm diameter, ~30 cm long (as the helix form)
- Copper wire, ~1.5 mm diameter, enough for 7 turns (each turn circumference = pi * 35mm = ~110mm, so about 80 cm total)
- 1x metal plate or mesh for reflector, at least 19x19 cm (one wavelength square)
- 1x SMA connector
- 1x LNA (see below)

**Build:**
1. Wind 7 turns of copper wire around the PVC pipe. Turn spacing (pitch) should be ~lambda/4 = ~47 mm.
2. Mount the reflector plate perpendicular to the PVC pipe at the bottom.
3. Connect the bottom of the helix to the SMA connector mounted on the reflector.
4. If you have a VNA (NanoVNA, ~$30): trim the top turn to get the SWR dip at 1602 MHz. If you don't have a VNA, cut to exactly 7 turns and it will be close enough.

**Resources:**
- **thebaldgeek L-Band guide (comprehensive):** https://thebaldgeek.github.io/L-Band.html
- **Adam 9A4QV L-Band patch build:** https://www.rtl-sdr.com/building-and-testing-an-l-band-patch-antenna-for-inmarsat-c-reception/
- **3D-printable helicone design (for NOAA HRPT, similar frequency):** search "helicone antenna thingiverse" for printable scaffold

### Option B: Buy the RTL-SDR Blog L-Band Patch (~$50)

A ready-made active patch antenna covering 1525-1660 MHz with built-in LNA and SAW filter. Powered via bias-T from the RTL-SDR V3.

- **Store:** https://www.rtl-sdr.com/product/rtl-sdr-blog-l-band-1525-1637-inmarsat-to-iridium-patch-antenna-set/
- Covers GLONASS L1 (1602 MHz) at the edge of its range.
- No soldering, no construction. Point at sky and go.
- Requires RTL-SDR V3 or V4 (for bias-T power).

For a thesis project where L-band is secondary, this is the pragmatic choice.

---

## LNA (Low Noise Amplifier): do you need one?

**For VHF 137 MHz:** Not required if your coax cable is short (under 5 meters). Recommended if cable is longer or if you are in a city with strong FM interference. Best option: **Nooelec SAWbird+ NOAA** (~$30), which combines an LNA with a SAW bandpass filter centered on 137 MHz. Powers via bias-T.

**For UHF 435 MHz:** Usually not required for strong cubesat beacons. Helps with weaker telemetry signals. Options: Nooelec SAWbird+ 435 MHz, or a generic wideband LNA.

**For L-band 1602 MHz:** Required. The RTL-SDR is nearly deaf at 1.6 GHz without amplification. The RTL-SDR Blog Patch includes a built-in LNA. For the DIY helix, use a **Nooelec SAWbird+ GOES/L-Band LNA** (~$30).

**Important:** If using an LNA, place it as close to the antenna as possible (directly at the antenna feed point), not at the SDR end of the cable. Signal degrades in the cable; amplifying after the cable amplifies the noise too.

---

## FM bandstop filter (for VHF only)

If you live in a city and your RTL-SDR is being overloaded by FM broadcast stations (88-108 MHz), add an FM bandstop filter between the antenna and the SDR. You can buy one for ~$10 (RTL-SDR Blog FM Reject Filter) or build one from a quarter-wave stub of coax:

Cut a piece of RG-58 coax to **71 cm** (quarter wavelength of ~98 MHz * velocity factor 0.66). Connect one end to a T-adapter on your main coax line. Leave the other end open. This creates a notch at ~98 MHz that suppresses FM stations.

---

## What to buy: minimal shopping list

For a student starting from scratch with an RTL-SDR V3/V4:

**Phase 1 (VHF, ~$0-5):**
- 2x aluminum rods 53.4 cm (hardware store) or use the RTL-SDR dipole kit
- 1x terminal block (hardware store, ~$1)
- Coax cable (comes with RTL-SDR kit)

**Phase 2 (UHF, ~$5-10):**
- 4x copper/aluminum rods 16.4 cm
- Short piece of RG-58 for phasing (11.2 cm)
- PVC pipe, solder, SMA connector
- Optional: 3D printed holders from Alicja's design

**Phase 3 (L-band, ~$30-50):**
- Nooelec SAWbird+ LNA ($30) + DIY helix ($10 materials)
- OR: RTL-SDR Blog L-Band Patch ($50, no build required)

**Optional but recommended:**
- Nooelec SAWbird+ NOAA ($30) for VHF LNA+filter
- RTL-SDR Blog FM Reject Filter ($10) if in a city
- NanoVNA ($30) for antenna tuning/verification (reusable across all builds)

---

## Task coverage matrix

| orbid task | What you receive | Antenna needed |
|------------|-----------------|----------------|
| [P09] #8 Test: record NOAA APT at 137 MHz | NOAA 15/18/19 APT | V-Dipole 137 MHz |
| [P14] #12 Test: detect NOAA/Meteor in IQ | NOAA APT, Meteor LRPT | V-Dipole 137 MHz |
| [P23] #23 Integration test (NOAA/Meteor) | Full pipeline on weather sat | V-Dipole 137 MHz |
| [P24] #24 Ground truth validation | Multiple known satellites | V-Dipole + Turnstile |
| UHF telemetry detection | Gonets-M, cubesats | Turnstile 435 MHz |
| GLONASS L1 detection | GLONASS navigation sats | L-band helix or patch |

The entire thesis can be completed with **only the V-Dipole** if you limit ground truth to NOAA and Meteor satellites. The turnstile and L-band antennas expand the scope but are not strictly required.
