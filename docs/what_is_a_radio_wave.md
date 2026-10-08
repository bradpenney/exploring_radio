---
date: "2026-10-09 01:30"
title: "What Is a Radio Wave? Frequency, Wavelength, and the Spectrum"
description: "A radio wave is alternating current set loose from the wire. Frequency and wavelength are one number in two units, wavelength in metres is 300 divided by megahertz, and the ITU's decade bands from VLF to EHF."
---

# What Is a Radio Wave? Frequency, Wavelength, and the Spectrum

!!! abstract "Beginner"
    The first article in the **[Radio Fundamentals](radio_fundamentals.md)** topic, and the next step after [Start Here](start_here.md). Covers Basic exam section B-005 (Basic Electronics and Theory), topic B-005-007, and the wavelength questions of B-006-008.

An operator on 7.150 MHz says they're "on 40 metres." A handheld on 146.520 MHz is "on 2 metres." Neither is slang. The megahertz and the metres are the same fact about the signal, written two ways, and converting between them takes one division you can do in your head.

Two ideas cover it:

1. **A radio wave is alternating current that has left the wire.** The same back-and-forth that [AC vs DC](https://electronics.bradpenney.io/ac_dc/) describes in a circuit, but travelling through space as electric and magnetic fields, at the speed of light.
2. **Frequency and wavelength are one number in two units.** Because every radio wave travels at the same speed, the faster it alternates, the shorter each wave. Wavelength in metres is 300 divided by the frequency in megahertz.

---

## Idea One: AC Set Loose From the Wire

Frequency is the number of complete cycles per second, measured in hertz. Exploring Electronics covers it, along with the period and the sine wave, in [AC vs DC](https://electronics.bradpenney.io/ac_dc/). A 60 Hz household outlet supplies a sine wave that completes 60 cycles every second; a 7.150 MHz radio signal completes 7,150,000.

At radio frequencies, something happens that doesn't at 60 Hz. A current in a wire makes a magnetic field, and a changing magnetic field makes a voltage, as [Magnetism and Electromagnetism](https://electronics.bradpenney.io/magnetism/) explains. When the current reverses millions of times a second, the fields it makes don't collapse back into the wire in time. They detach, and keep regenerating each other as they travel outward. That travelling pair of fields is a radio wave.

<figure markdown>
  ![A radio wave drawn in three dimensions. A red sine wave, the electric field, oscillates in the vertical plane; a blue sine wave, the magnetic field, oscillates in the horizontal plane at right angles to it. Both travel together along an axis marked direction of travel. A bracket over one crest-to-crest cycle marks one wavelength. The two fields are at right angles to each other and to the direction of travel, and move at the speed of light.](images/what_is_a_radio_wave/wave_fields.svg){ width="760" }
  <figcaption>The electric and magnetic fields rise and fall together, at right angles, as the wave moves.</figcaption>
</figure>

- **Two fields, at right angles.** The wave carries an **electric field** and a **magnetic field**, perpendicular to each other and to the direction the wave travels. The orientation of the electric field is the wave's **polarization**: a vertical antenna sends out a vertically polarized wave.
- **The speed of light.** Radio waves are the same kind of wave as light, at a much lower frequency, and they travel at the same speed. In a vacuum that speed is exactly 299,792,458 metres per second, a value fixed by the [International System of Units](https://www.bipm.org/en/publications/si-brochure). For radio work it rounds to **300,000 kilometres per second**, or 300 million metres per second; in air it's barely slower.
- **Slower in cable.** Inside a coaxial cable a signal travels at only a fraction of that speed, set mainly by the insulation between the conductors. That fraction, the velocity factor, matters when cutting feedlines to length.

---

## Idea Two: One Number, Two Units

**Wavelength** is the distance a wave travels during one complete cycle: crest to crest, or any point to the same point on the next cycle. In one second a wave travels 300 million metres and completes *f* cycles, so each cycle covers 300 million ÷ *f* metres.

$$
\lambda = \frac{c}{f} \quad\Longrightarrow\quad \lambda\ (\text{metres}) = \frac{300}{f\ (\text{MHz})}
$$

The second form is the one to remember. The millions cancel: divide 300 by the frequency in megahertz and the answer is in metres.

<figure markdown>
  ![Bars on a logarithmic scale showing wavelength equals 300 divided by frequency in megahertz, for six amateur frequencies: 1.9 megahertz in the 160 metre band, 158 metres; 7.15 megahertz in the 40 metre band, 42 metres; 14.2 megahertz in the 20 metre band, 21 metres; 28.8 megahertz in the 10 metre band, 10.4 metres; 146 megahertz in the 2 metre band, 2.05 metres; 440 megahertz in the 70 centimetre band, 68 centimetres. Double the frequency and the wavelength halves.](images/what_is_a_radio_wave/wavelength_bars.svg){ width="760" }
  <figcaption>The band names are these wavelengths, rounded.</figcaption>
</figure>

A few worked examples:

| Frequency | 300 ÷ f | Wavelength |
|---|---|---|
| 2 MHz | 300 ÷ 2 | 150 m |
| 25 MHz | 300 ÷ 25 | 12 m |
| 7.150 MHz | 300 ÷ 7.15 | 42 m, the "40 m" band |
| 146 MHz | 300 ÷ 146 | 2.05 m, the "2 m" band |
| 440 MHz | 300 ÷ 440 | 0.68 m, the "70 cm" band |

The relationship is inverse. **As frequency increases, wavelength decreases**; as wavelength gets shorter, frequency rises. Double one and the other halves. That's why the bands named in metres run the opposite way to the bands named in megahertz: 160 m is the lowest-frequency band a Basic with Honours holder commonly uses, and 70 cm is far higher. The band names are wavelengths rounded to a convenient figure, as the [table of Canadian bands](what_you_may_transmit.md#where-the-bands) shows.

Wavelength matters because antennas are built to it. A half-wave dipole for 7.150 MHz is about 20 metres long, and one for 146 MHz is about a metre. That's a topic of its own, but the starting number is always 300 ÷ f.

---

## The Radio Spectrum

The International Telecommunication Union (ITU) divides the spectrum into bands a decade wide, each ten times the frequency of the one before. The names come from Article 2 of the ITU Radio Regulations, which the United States reproduces in [47 CFR 2.101](https://www.ecfr.gov/current/title-47/part-2/section-2.101).

<figure markdown>
  ![The radio spectrum divided into the ITU's decade bands, each with its frequency and wavelength range: VLF 3 to 30 kilohertz, 100 to 10 kilometres; LF 30 to 300 kilohertz; MF 0.3 to 3 megahertz; HF 3 to 30 megahertz, 100 to 10 metres; VHF 30 to 300 megahertz, 10 to 1 metres; UHF 0.3 to 3 gigahertz; SHF 3 to 30 gigahertz; EHF 30 to 300 gigahertz, 1 centimetre to 1 millimetre. Amateur bands are marked on a log scale: 160, 80, 40, 20 and 10 metres in MF and HF, 6 and 2 metres in VHF, 70 and 23 centimetres in UHF. Audio, about 20 hertz to 20 kilohertz, sits below the radio spectrum. 7,125 kilohertz, or 7.125 megahertz, is in HF.](images/what_is_a_radio_wave/spectrum.svg){ width="760" }
  <figcaption>The amateur bands Basic holders use most sit in HF, VHF, and UHF.</figcaption>
</figure>

| Band | Name | Frequency | Wavelength |
|---|---|---|---|
| MF | Medium Frequency | 300 kHz to 3 MHz | 1 km to 100 m |
| HF | High Frequency | 3 to 30 MHz | 100 m to 10 m |
| VHF | Very High Frequency | 30 to 300 MHz | 10 m to 1 m |
| UHF | Ultra High Frequency | 300 MHz to 3 GHz | 1 m to 10 cm |

The 30 MHz line between HF and VHF is the same one that divides Basic from Basic with Honours privileges. The amateur bands below it are mostly HF; 160 m, at 1.8 to 2.0 MHz, is technically MF. A signal on 7,125 kHz, which is 7.125 MHz, is in the HF range.

Below the radio spectrum are **audio frequencies**, roughly 20 Hz to 20 kHz: the range the human ear can hear as sound. Your voice into a microphone is an audio-frequency signal. It's not a radio wave until a transmitter puts it onto a radio-frequency signal.

---

## Two Words for Comparing Waves

Two more terms describe how one wave relates to another.

<figure markdown>
  ![Two panels. Phase: two sine waves of the same frequency, one shifted a quarter-cycle, 90 degrees, after the other; both complete a cycle in the same time. Harmonics: a 2 kilohertz fundamental, a 4 kilohertz second harmonic and a 6 kilohertz third harmonic, whole-number multiples of the fundamental; a transmitter on 7.1 megahertz can leak energy at 14.2 and 21.3 megahertz.](images/what_is_a_radio_wave/phase_harmonics.svg){ width="760" }
  <figcaption>Phase compares timing; harmonics compare frequency.</figcaption>
</figure>

- **Phase** is the timing difference between two waves of the same frequency whose cycles don't start at the same instant. It's measured in degrees of a cycle: a wave that peaks a quarter-cycle after another is 90° behind it, and one that peaks exactly when the other dips is 180° out of phase.
- **Harmonics** are whole-number multiples of a frequency. If the original, the **fundamental**, is 2 kHz, then 4 kHz is its second harmonic and 6 kHz its third. They matter to every transmitter operator: a transmitter on 7.1 MHz that isn't properly filtered also radiates a little at 14.2 MHz, 21.3 MHz, and above, where it can interfere with other stations.

---

## Common Misconceptions

- **"Radio waves are a kind of sound."** Sound is pressure waves in air, at audio frequencies. Radio waves are electromagnetic, need no air, and travel almost a million times faster.
- **"Higher frequency means a longer wave."** The reverse: wavelength falls as frequency rises.
- **"The 40 m band is exactly 40 metres."** The name is rounded; 7.0 to 7.3 MHz is about 41 to 43 metres.
- **"A radio wave travels at the speed of light only in space."** It travels at nearly that speed in air too; it's inside cables that it slows markedly.

---

## Practice

??? question "1. Wavelength at 25 MHz"

    What's the free-space wavelength of a 25 MHz signal?

    ??? tip "Solution"
        \( 300 \div 25 = 12 \) metres.

??? question "2. Wavelength at 2 MHz"

    What's the free-space wavelength of a 2 MHz signal?

    ??? tip "Solution"
        \( 300 \div 2 = 150 \) metres.

??? question "3. Which Band?"

    Is 7,125 kHz in the MF, HF, or VHF range?

    ??? tip "Solution"
        **HF.** 7,125 kHz is 7.125 MHz, inside 3 to 30 MHz.

??? question "4. Going Up"

    You retune from 3.7 MHz to 14.2 MHz. What happens to the wavelength?

    ??? tip "Solution"
        It **decreases**, from about 81 m to about 21 m. Frequency went up roughly four times, so wavelength fell to roughly a quarter.

??? question "5. The 4 kHz Signal"

    A signal contains 2 kHz and 4 kHz components. What's the 4 kHz one called?

    ??? tip "Solution"
        A **harmonic**: specifically the second harmonic of the 2 kHz fundamental.

??? question "6. Same Frequency, Different Start"

    Two AC waveforms have the same frequency, but one starts its cycle a little after the other. What's that difference called?

    ??? tip "Solution"
        **Phase.**

---

## Quick Recap

<div class="grid cards two-col" markdown>

-   **A radio wave**

    ---

    AC set loose from the wire: electric and magnetic fields at right angles, travelling together.

-   **The speed**

    ---

    The speed of light: about 300,000 km/s in free space. Slower in cable.

-   **Wavelength**

    ---

    The distance travelled in one cycle. λ (m) = 300 ÷ f (MHz).

-   **Inverse**

    ---

    Frequency up, wavelength down. Band names are rounded wavelengths.

-   **The spectrum**

    ---

    Decade bands: MF 0.3–3 MHz, HF 3–30 MHz, VHF 30–300 MHz, UHF 300–3,000 MHz. Audio is about 20 Hz to 20 kHz.

-   **On the exam**

    ---

    Frequency is cycles per second; 60 Hz is 60 cycles per second; household power is a sine wave. Humans hear about 20 Hz to 20 kHz. 7,125 kHz is HF. Wavelength is the distance travelled in one cycle; it falls as frequency rises. 25 MHz is 12 m; 2 MHz is 150 m. Radio waves travel at the speed of light, 300,000 km/s. Phase is a timing difference; a 4 kHz signal with a 2 kHz fundamental is a harmonic.

</div>

---

## What's Next

Frequency and wavelength describe a signal; the next question is how strong it is, and how much of it survives the trip. [Decibels](decibels.md) is the unit radio uses for that, and the one that turns a chain of gains and losses into simple addition.

---

## Further Reading

**Standards**

- [ITU Radio Regulations, 2024 Edition (PDF)](https://www.itu.int/dms_pub/itu-r/oth/0C/0A/R0C0A0000110086PDFE.pdf) — Article 2, the band nomenclature
- [47 CFR 2.101](https://www.ecfr.gov/current/title-47/part-2/section-2.101) — the same table, in a readable web form
- [The International System of Units (SI Brochure)](https://www.bipm.org/en/publications/si-brochure) — the speed of light as a defining constant

**On Exploring Electronics**

- [AC vs DC](https://electronics.bradpenney.io/ac_dc/) — frequency, period, sine waves, and RMS
- [Magnetism and Electromagnetism](https://electronics.bradpenney.io/magnetism/) — the fields that become radio waves, and how Maxwell and Hertz found them

**Related Articles**

- [Start Here: The Electricity Behind Radio](start_here.md) — the foundations, in order
- [What You May Transmit: Bands, Power, and Identification](what_you_may_transmit.md) — the Canadian bands this spectrum contains
