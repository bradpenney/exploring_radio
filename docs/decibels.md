---
date: "2026-10-09 02:30"
title: "Decibels: Ratios You Can Add"
description: "Why radio measures gain and loss in decibels: 3 dB doubles power, 10 dB multiplies it by ten, chains of gains and losses add, an S-unit is 6 dB, and antenna gain is quoted in dBi or dBd."
---

# Decibels: Ratios You Can Add

!!! abstract "Beginner"
    The second article in the **[Radio Fundamentals](radio_fundamentals.md)** topic, after [What Is a Radio Wave?](what_is_a_radio_wave.md). Covers Basic exam section B-005 (Basic Electronics and Theory), topic B-005-008, plus the S-meter questions in B-002-006 and the dBi questions in B-006.

A transmitter makes 100 watts. The coax loses some of it, an amplifier adds some, the antenna focuses it, the path to a distant station loses almost all of it, and that station's receiver picks up a few hundred-billionths of a milliwatt. Writing that chain in watts means multiplying and dividing numbers that span twelve powers of ten. Writing it in decibels means adding and subtracting small numbers.

Two ideas make that work:

1. **A decibel is a ratio, not an amount.** It says how many times bigger or smaller one power is than another, on a scale where equal steps are equal multiplications.
2. **On that scale, multiplying becomes adding.** Gains and losses in a chain simply add up in dB. Two anchors, +3 dB doubles power and +10 dB multiplies it by ten, are enough to work out every exam question by hand.

Ratios of power come straight from [Ohm's Law and Power](https://electronics.bradpenney.io/ohms_law/) on Exploring Electronics; everything here is about comparing those powers.

---

## Idea One: A Ratio, Not an Amount

The decibel compares two powers. The definition is ten times the base-10 logarithm of their ratio:

$$
\text{dB} = 10 \log_{10} \frac{P_2}{P_1}
$$

The logarithm counts powers of ten. A ratio of 10 is one power of ten, so 10 dB; a ratio of 100 is two, so 20 dB; a ratio of 1,000 is 30 dB. A ratio of 2 works out to 3.01 dB, which everyone rounds to 3. So "10 dB of gain" doesn't say how many watts you have; it says you have ten times as many as you started with, whatever that was.

<figure markdown>
  ![A decibel ruler from minus 10 to plus 30 dB with the matching power ratios: minus 10 dB divides by 10, minus 6 dB divides by 4, minus 3 dB divides by 2, 0 dB is the same, plus 3 dB doubles, plus 6 dB is 4 times, plus 10 dB is 10 times, plus 13 dB is 20 times, plus 20 dB is 100 times and plus 30 dB is 1,000 times. Losses are negative dB, gains positive.](images/decibels/ruler.svg){ width="760" }
  <figcaption>Every step to the right multiplies the power; every step to the left divides it.</figcaption>
</figure>

- **Gains are positive, losses negative.** +3 dB doubles the power; −3 dB halves it. 0 dB means no change.
- **The two anchors.** +3 dB is ×2 and +10 dB is ×10. Everything else on the ruler is built from them, because adding decibels multiplies ratios: 6 dB is 3 + 3, so ×2 × 2 = ×4. 9 dB is 3 + 3 + 3, so ×8. 13 dB is 10 + 3, so ×20. 20 dB is 10 + 10, so ×100.
- **Why radio uses it.** Real signals span enormous ranges. A transmitter's 100 W and a received signal at S9 on HF differ by about 123 dB, a number you can hold in your head.

### When the Decibel Has a Reference

A decibel on its own is a ratio. Add a fixed reference and it becomes an amount. The most common is **dBm**, decibels relative to one milliwatt: 0 dBm is 1 mW, +30 dBm is 1 W, and +50 dBm is 100 W. Receivers deal in negative dBm. The International Amateur Radio Union's Region 1 standard for S-meters, described below, puts S9 on the HF bands at −73 dBm, about 50 billionths of a milliwatt.

Voltages compare differently. Power goes as the square of voltage, so the decibel for a voltage ratio uses 20 instead of 10: doubling the voltage is 6 dB, because it quadruples the power.

---

## Idea Two: Chains Add Up

A station is a chain: transmitter, maybe an amplifier, a feedline, an antenna. In watts, each stage multiplies or divides. In decibels, each stage adds or subtracts.

<figure markdown>
  ![Two signal chains. A 2 watt handheld feeds an amplifier with plus 9 dB of gain, which is times 8, giving 16 watts. A 100 watt transmitter feeds a feedline with 6 dB of loss, which is divide by 4, leaving 25 watts at the antenna. With several stages, add their decibels first, for example plus 20 minus 3 minus 2 is plus 15 dB, then convert once.](images/decibels/chain.svg){ width="760" }
  <figcaption>Convert the total once, at the end.</figcaption>
</figure>

Two exam-style examples:

- **An amplifier on a handheld.** A 9 dB amplifier is 3 + 3 + 3 dB, so ×2 × 2 × 2 = ×8. A 2 W handheld becomes 16 W.
- **A lossy feedline.** A feedline with 6 dB of loss is −3 − 3 dB, so ÷2 ÷ 2 = ÷4. A 100 W transmitter delivers 25 W to the antenna. Three-quarters of the power warms the coax.

The same reasoning runs backward. An amplifier that takes 5 W to 50 W multiplies by 10, so its gain is 10 dB. Going from 1 W to 2 W is 3 dB, and so is going from 100 W to 200 W: the decibel cares only about the ratio. A device marked "Gain = 10 dB" is almost certainly an amplifier.

The Canadian rules use the same idea. RBR-4 section 10.1 says an amplifier installed at an amateur station "shall not be capable of exceeding by more than 3 dB" the power limits for your qualification: it may be built to reach no more than twice the limit, as [What You May Transmit](what_you_may_transmit.md#how-strong-power) explains.

---

## S-Meters: Decibels on Your Receiver

Most receivers have a signal-strength meter, the **S-meter**, scaled in **S-units** from S1 to S9, then in decibels over S9.

<figure markdown>
  ![An S-meter dial marked S1 to S9 in black, then plus 20, plus 40 and plus 60 dB over S9 in red, with the needle at S9. One S-unit is 6 dB, four times the power. A station heard at S9 with 100 watts reads S8 at 25 watts; one heard at 20 dB over S9 with 150 watts reads 10 dB over S9 at 15 watts.](images/decibels/smeter.svg){ width="760" }
  <figcaption>Above S9, the scale switches from S-units to plain decibels.</figcaption>
</figure>

The IARU Region 1 standard sets **one S-unit at 6 dB**, a factor of 4 in power. The exam assumes it, though plenty of real receivers are calibrated loosely. That gives quick answers:

| You do this | Power change | The other station's meter |
|---|---|---|
| 100 W → 25 W | ÷4, −6 dB | drops one S-unit, S9 → S8 |
| S8 → S9 | +6 dB | needs ×4 the power |
| 200 W → 20 W | ÷10, −10 dB | "10 dB over S9" → S9 |
| 150 W → 15 W | ÷10, −10 dB | "20 dB over S9" → "10 dB over S9" |
| 100 W → 0.1 W | ÷1,000, −30 dB | "30 dB over S9" → S9 |

The last row is a courtesy lesson as much as arithmetic. A local station reading you 30 dB over S9 on 2 m simplex would hear you perfectly well at a tenth of a watt, and the extra 99.9 W only spreads your signal further over everyone else on the frequency.

---

## Antenna Gain: dBi and dBd

An antenna can't create power, but it can concentrate it in some directions at the expense of others. Its gain is the ratio of its strongest signal to that of a reference antenna, and the reference is part of the unit.

<figure markdown>
  ![Two radiation patterns. An isotropic radiator, an ideal point radiating equally in every direction, has 0 dBi. A half-wave dipole, drawn vertically, pulls energy from its ends into its sides, forming a figure-eight pattern that reaches 2.15 dB beyond the isotropic circle: 2.15 dBi, which is 0 dBd. So dBi equals dBd plus 2.15.](images/decibels/antenna_gain.svg){ width="760" }
  <figcaption>The same antenna has two gain figures, 2.15 dB apart.</figcaption>
</figure>

- **dBi** compares the antenna with an **isotropic** radiator: an ideal point that radiates equally in every direction. It can't be built, but it's the cleanest reference.
- **dBd** compares it with a **half-wave dipole**. An ideal dipole has 2.15 dB of gain over isotropic, so **dBi = dBd + 2.15**. An antenna quoted at 4.1 dBi has about 2.0 dB of gain over a dipole.
- **Two antennas, twice the power.** Stacking two identical antennas, correctly phased, ideally doubles the forward gain: +3 dB. Two 10 dBi Yagis stacked give about 13 dBi.

---

## Common Misconceptions

- **"10 dB is ten times louder."** It's ten times the *power*. Your ear judges it as roughly twice as loud.
- **"A decibel is a unit of power."** A plain dB is a ratio. Only with a reference, such as dBm, does it become an amount.
- **"Doubling from 100 W to 200 W gains more than doubling from 1 W to 2 W."** Both are 3 dB.
- **"Antenna gain adds power."** It redirects power; what's gained in one direction is lost in others.
- **"dBi and dBd are interchangeable."** The same antenna reads 2.15 higher in dBi.

---

## Practice

??? question "1. Double the Power"

    You double your transmitter's output. How many dB is that?

    ??? tip "Solution"
        **+3 dB.**

??? question "2. Six dB Up"

    What change in power gives a 6 dB increase?

    ??? tip "Solution"
        **×4.** 6 dB is 3 + 3, so ×2 × 2.

??? question "3. The Feedline"

    Your transmitter makes 100 W and your feedline loses 6 dB. How much reaches the antenna?

    ??? tip "Solution"
        **25 W.** −6 dB is ÷4.

??? question "4. The Amplifier"

    You add a 9 dB amplifier to a 2 W handheld. What's the output?

    ??? tip "Solution"
        **16 W.** 9 dB is 3 + 3 + 3, so ×8.

??? question "5. Turning It Down"

    You're heard at 20 dB over S9 with 150 W. What will the other station read if you drop to 15 W?

    ??? tip "Solution"
        **10 dB over S9.** 150 W to 15 W is ÷10, or −10 dB.

??? question "6. dBi to dBd"

    An antenna has a gain of 4.1 dBi. What's its gain over a half-wave dipole?

    ??? tip "Solution"
        About **2.0 dB** (dBd): 4.1 − 2.15 ≈ 1.95.

---

## Quick Recap

<div class="grid cards two-col" markdown>

-   **A ratio**

    ---

    dB = 10 log₁₀(P₂ ÷ P₁). It compares two powers; it isn't an amount.

-   **Two anchors**

    ---

    +3 dB = ×2, +10 dB = ×10. Negative dB divides: −3 dB halves, −6 dB quarters.

-   **Chains add**

    ---

    Add the dB of every stage, then convert once.

-   **References**

    ---

    dBm: relative to 1 mW. dBi: relative to isotropic. dBd: relative to a dipole. dBi = dBd + 2.15.

-   **S-meters**

    ---

    One S-unit = 6 dB = ×4 power (IARU). Above S9, readings are in dB over S9.

-   **On the exam**

    ---

    The decibel measures the ratio of two signals. ×2 = 3 dB; ÷2 = −3 dB; ×4 = 6 dB; 5 W to 50 W = 10 dB. 2 W + 9 dB = 16 W. 100 W − 6 dB = 25 W. 200 W at S9+10 dropped to 20 W reads S9; 100 W at S9+30 needs only 0.1 W for S9. S9 at 100 W reads S8 at 25 W. dBi's "i" is isotropic; 4.1 dBi ≈ 2.0 dBd; two stacked 10 dBi Yagis ≈ 13 dBi.

</div>

---

## What's Next

Decibels measure how much of a signal survives a chain. The next question is why parts of that chain treat different frequencies differently: [Reactance and Impedance](reactance_and_impedance.md) puts numbers on how coils and capacitors respond to each frequency.

---

## Further Reading

**Related Articles**

- [What Is a Radio Wave? Frequency, Wavelength, and the Spectrum](what_is_a_radio_wave.md) — the previous article in Radio Fundamentals
- [What You May Transmit: Bands, Power, and Identification](what_you_may_transmit.md) — the power limits, and the 3 dB amplifier rule

**On Exploring Electronics**

- [Ohm's Law and Power](https://electronics.bradpenney.io/ohms_law/) — the watts that decibels compare
