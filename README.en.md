# rime-thai · Thai Phonetic (Romanization / Latin Alphabet) & Kedmanee Input Method for Rime

<p align="center">
  <a href="./README.md">简体中文</a> ·
  <b>English</b> ·
  <a href="./README.th.md">ภาษาไทย</a>
</p>

An open-source **Thai input method (IME)** package for the **[Rime Input Method Engine](https://rime.im/)** (Weasel on Windows, Squirrel on macOS, ibus-rime / fcitx5-rime on Linux, Trime on Android). Supports both **typing Thai with Latin / English letters (Thai phonetic / romanization input)** and the standard **Thai Kedmanee keyboard layout**. Architecturally inspired by [rime-cantonese](https://github.com/CanCLID/rime-cantonese) (Jyutping) and [rime-ipa](https://github.com/rime/rime-ipa).

Once installed, three independent Thai input schemas can be enabled in Rime:

| Schema ID | Display Name | Use Case | Key Features |
| :--- | :--- | :--- | :--- |
| **`thai_roman`** | **泰語拼音** (Thai Romanization) | Type Thai phonetically using Latin letters (RTGS / Paiboon) | **23,800+ core words** ranked by corpus frequency; **tone-free typing** by default, vowel-length tolerance, initial-letter abbreviations, single-character lookup for all 44 consonants & vowel marks, and configurable pronunciation hints (`spelling_hints`) |
| **`thai_roman_fuzzy`** | **泰語拼音·模糊音** (Thai Romanization + Fuzzy) | Learners (e.g. Chinese speakers) who cannot reliably distinguish Thai **aspiration / voicing** contrasts | Same as `thai_roman`, plus fuzzy tolerance: dropped-aspiration (`kh→k`, `ph→p`, `th→t`) and voicing confusion (`b↔p`, `d↔t`) |
| **`thai_kedmanee`** | **泰語鍵盤** (Thai Kedmanee) | Touch-typing with the standard Thai keyboard layout | Full **TIS 820-2538 (Kedmanee)** national standard layout inside Rime without switching OS language bars; direct single-key commit |

---

## 1. Installation

### Method 1: Via Weasel GUI on Windows (Recommended)
1. Right-click the Weasel tray icon → select **"Input Method Settings (輸入法設定)"**.
2. Click **"Get more input schemas... (獲取更多輸入方案…)"** at the bottom-left corner.
3. Type the repository path in the console window and press Enter:
   ```text
   flexlpf/rime-thai
   ```
4. Check **"泰語拼音"**, **"泰語拼音·模糊音"** and/or **"泰語鍵盤"** in the pop-up dialog and confirm to deploy.

### Method 2: Via `plum` (`rime-install`) CLI
```bash
bash rime-install flexlpf/rime-thai
```

### Method 3: Manual / Git Clone
Copy all `*.yaml` files into your Rime **User Data Directory** (`%APPDATA%\Rime` on Windows, `~/Library/Rime` on macOS, `~/.config/ibus/rime` or `~/.local/share/fcitx5/rime` on Linux), and enable the schemas in `default.custom.yaml`:
```yaml
patch:
  schema_list:
    - {schema: thai_roman}        # Thai Romanization (precise)
    - {schema: thai_roman_fuzzy}  # Thai Romanization + fuzzy (aspiration/voicing tolerance)
    - {schema: thai_kedmanee}     # Thai Kedmanee Keyboard
```
Then run **Deploy (重新部署)**.

---

## 2. Usage Guide

### Schema 1: `thai_roman` (Thai Romanization)

#### A. Word & Phrase Input (Tone-Free by Default)
You do **not** need to type tone marks for daily typing. Speller algebra automatically handles tone-free input, short/long vowel tolerance (`aa/a`, `ii/i`, `uu/u`, `ee/e`, `oo/o`), Paiboon variants (`bp/p`, `dt/t`, `g/k`, `j/ch`, `eu/ue`, `er/oe`, `or/oo`), and syllable initials:

| Thai | Meaning | Tone-Free Input (Default) | Variant / Long Vowel | With Tone Numbers (1-5) | Initials Abbrev |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **สวัสดี** | Hello | `sawatdi` | `sawatdii` | `sa2wat2dii1` | `swd` |
| **ขอบคุณ** | Thank you | `khopkhun` | `khorpkhun` / `khoopkhun` | `khoop2khun1` | `kk` / `khkh` |
| **ไม่เป็นไร** | No problem | `maipenrai` | `maibpenrai` | `mai3pen1rai1` | `mpr` |
| **ภาษาไทย** | Thai language | `phasathai` | `phaasaathai` | `phaa1saa5thai1` | `pst` / `phsth` |
| **กรุงเทพฯ** | Bangkok | `krungthep` | `grungtheep` | `krung1theep3` | `kt` / `krth` |
| **ใบเสนอราคา** | Quotation | `baisanoerakha` | `baisanerrakha` | `bai1sa2noee5raa1khaa1` | `bsnrk` |

#### B. Tone Filtering (1–5 or Shortcut Keys)
To narrow down homophones, append a tone digit `1`–`5` (or letter shortcut `v / x / q / f / r`) at the end of a syllable:

| Tone Number | Shortcut Key | Thai Tone Name | IPA Pitch | Example |
| :---: | :---: | :--- | :---: | :--- |
| **`1`** | `v` | สามัญ (Mid Tone) | `˧` (33) | `maa1` → มา |
| **`2`** | `x` | เอก (Low Tone) | `˨˩` (21) | `mai2` → ใหม่ |
| **`3`** | `q` | โท (Falling Tone) | `˥˩` (51) | `mai3` → ไม่ / ม่าย |
| **`4`** | `f` | ตรี (High Tone) | `˦˥` (45) | `maa4` → ม้า, `naam4` → น้ำ |
| **`5`** | `r` | จัตวา (Rising Tone) | `˩˩˦` (114) | `maa5` → หมา, `mai5` → ไหม |

#### C. Single-Character & Component Input (44 Consonants, Vowels, Tones, Digits)
- **44 Thai Consonants (2 ways to type)**:
  1. **By consonant sound**: e.g., `k` (`ก`), `kh` (`ค ข ฆ ฃ ฅ`), `ch` (`จ ช ฉ ฌ`), `s` (`ส ซ ศ ษ`), `th` (`ท ถ ธ ฐ ฑ ฒ`).
  2. **By full traditional acrophonic name (exact match)**:
     - Mid class: `kokai` (`ก`), `chochan` (`จ`), `dochada` (`ฎ`), `topatak` (`ฏ`), `dodek` (`ด`), `totao` (`ต`), `bobaimai` (`บ`), `popla` (`ป`), `oang` (`อ`)
     - High class: `khokhai` (`ข`), `khokhuat` (`ฃ`), `choching` (`ฉ`), `thothan` (`ฐ`), `thothung` (`ถ`), `phophueng` (`ผ`), `fofa` (`ฝ`), `sosala` (`ศ`), `soruesi` (`ษ`), `sosuea` (`ส`), `hohip` (`ห`)
     - Low class: `khokhwai` (`ค`), `khokhon` (`ฅ`), `khorakhang` (`ฆ`), `ngongu` (`ง`), `chochang` (`ช`), `soso` (`ซ`), `chochoe` (`ฌ`), `yoying` (`ญ`), `montho` (`ฑ`), `thophuthao` (`ฒ`), `nonen` (`ณ`), `thothahan` (`ท`), `thothong` (`ธ`), `nonu` (`น`), `phophan` (`พ`), `fofan` (`ฟ`), `phosamphao` (`ภ`), `moma` (`ม`), `yoyak` (`ย`), `roruea` (`ร`), `loling` (`ล`), `wowaen` (`ว`), `lochula` (`ฬ`), `honokhuk` (`ฮ`)
- **Vowel & Tone Marks**:
  - `saraa` (`ะ`), `saraaa` / `aa` (`า`), `maihanakat` (`ั`), `saraam` (`ำ`), `sarai` (`ิ`), `saraii` (`ี`), `saraue` (`ึ`), `sarauee` (`ื`), `sarau` (`ุ`), `sarauu` (`ู`), `sarae` (`เ`), `saraae` (`แ`), `sarao` (`โ`), `maimuan` (`ใ`), `maimalai` (`ไ`), `rue` (`ฤ`), `lue` (`ฦ`).
  - `maiek` / `tone2` (`่`), `maitho` / `tone3` (`้`), `maitri` / `tone4` (`๊`), `maichattawa` / `tone5` (`๋`), `maitaikhu` (`็`), `karan` (`์`), `maiyamok` (`ๆ`), `paiyannoi` (`ฯ`), `paiyanyai` (`ฯลฯ`), `baht` or `\` (`฿`).
- **Thai Numerals (`๐`–`๙`)**:
  - `sun` (`๐`), `nueng` (`๑`), `song` (`๒`), `sam` (`๓`), `si` (`๔`), `ha` (`๕`), `hok` (`๖`), `chet` (`๗`), `paet` (`๘`), `kao` (`๙`).

#### D. Pronunciation Hints Toggle (`spelling_hints`)
By default, romanized pronunciation hints are shown next to candidates (e.g., `สวัสดี [sa2 wat2 dii1]`).
- To disable hints, change `spelling_hints: 8` to `0` in `thai_roman.schema.yaml`, or create `thai_roman.custom.yaml`:
  ```yaml
  patch:
    translator/spelling_hints: 0
  ```

---

### Schema 2: `thai_roman_fuzzy` (Thai Romanization + Fuzzy)

Thai distinguishes **aspirated vs. unaspirated** onsets (`k`–`kh`, `p`–`ph`, `t`–`th`) and **voiced vs. voiceless** onsets (`b`–`p`, `d`–`t`), which many Chinese speakers find hard to distinguish by ear. The fuzzy schema derives extra tolerance codes on top of the `thai_roman` lexicon (weight ≈ 0.25 of the base entry, to limit duplicate candidates):

| Fuzzy Direction | Meaning | Type | Example | Matches |
| :--- | :--- | :--- | :--- | :--- |
| `kh → k` | dropped aspiration | unidirectional | `kopkun` | **ขอบคุณ** |
| `ph → p` | dropped aspiration | unidirectional | `pom` | **ผม** |
| `th → t` | dropped aspiration | unidirectional | `tam` / `tii` | **ทำ** / **ที่** |
| `b ↔ p` | voicing confusion | bidirectional | `paan` | **บ้าน** |
| `d ↔ t` | voicing confusion | bidirectional | `tii` / `dong` | **ดี** / **ต้อง** |

> Direction note: dropped-aspiration rules are **unidirectional** — typing the unaspirated form (`k` / `p` / `t`) surfaces aspirated candidates (`kh` / `ph` / `th`), but typing `kh` / `ph` / `th` does **not** surface unaspirated candidates. This keeps the candidate list clean. The `b↔p` and `d↔t` voicing rules are bidirectional. `b↔ph` is deliberately **not** provided (most users can distinguish it). If you don't need fuzzy input, just use `thai_roman`; both schemas can be enabled simultaneously and switched on demand.

---

### Schema 3: `thai_kedmanee` (Thai Kedmanee Keyboard)

Follows the Thai Industrial Standard **TIS 820-2538 (Kedmanee)** layout with direct single-key commit:

```text
┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬──────┐
│ % │ + │ ๑ │ ๒ │ ๓ │ ๔ │ ู │ ฿ │ ๕ │ ๖ │ ๗ │ ๘ │ ๙ │      │
│ _ │ ๅ │ / │ - │ ภ │ ถ │ ุ │ ึ │ ค │ ต │ จ │ ข │ ช │ Bksp │
├───┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬────┤
│ Tab │ ๐ │ " │ ฎ │ ฑ │ ธ │ ํ │ ๊ │ ณ │ ฯ │ ญ │ ฐ │ , │ ฅ  │
│     │ ๆ │ ไ │ ำ │ พ │ ะ │ ั │ ี │ ร │ น │ ย │ บ │ ล │ ฃ  │
├─────┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴────┤
│ Caps │ ฤ │ ฆ │ ฏ │ โ │ ฌ │ ็ │ ๋ │ ษ │ ศ │ ซ │ . │       │
│      │ ฟ │ ห │ ก │ ด │ เ │ ้ │ ่ │ า │ ส │ ว │ ง │ Enter │
├──────┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴───────┤
│ Shift  │ ( │ ) │ ฉ │ ฮ │ ฺ │ ์ │ ? │ ฒ │ ฬ │ ฦ │  Shift  │
│        │ ผ │ ป │ แ │ อ │ ิ │ ื │ ท │ ม │ ใ │ ฝ │         │
└────────┴───┴───┴───┴───┴───┴───┴───┴───┴───┴───┴─────────┘
```

---

## 3. References & Acknowledgements

### References & Data Sources
1. **Romanization Standard**: Royal Society of Thailand, *Principles of Romanization for Thai Script by Transcription Method (RTGS)*, 1999; and Paiboon transcription system.
2. **Keyboard Standard**: Thai Industrial Standards Institute, **TIS 820-2538** (*Standard for Thai Character Keys on Computer Keyboards - Kedmanee Layout*), 1995.
3. **Word Frequency Corpus**: **Thai National Corpus (TNC)**, Department of Linguistics, Faculty of Arts, Chulalongkorn University (`pythainlp/corpus/tnc_freq.txt`, CC0-1.0 Public Domain).
4. **IPA Pronunciation Lexicon**: Charin Polpanumas & Amazon Web Services (AWS Labs), `fastthaig2p_ipa.json` ([awslabs/FastThaiG2P](https://github.com/awslabs/FastThaiG2P), Apache License 2.0).

### Acknowledgements
- **[Rime Input Method Engine](https://rime.im/)**: Created by GONG Chen (@lotem) and the Rime open-source community.
- **[PyThaiNLP Project](https://github.com/PyThaiNLP/pythainlp)**: Wannaphong Phatthiyaphaibun and contributors for open-source Thai NLP corpora and tools.
- **[FastThaiG2P](https://github.com/awslabs/FastThaiG2P) & [TLTK](https://github.com/attapol/tltk)**: Charin Polpanumas and Attapol Thamrongrattanarit (Chulalongkorn University).
- **[rime-cantonese](https://github.com/CanCLID/rime-cantonese) & [rime-ipa](https://github.com/rime/rime-ipa)**: Inspiration for modular dictionary organization and speller algebra.

---

## 4. License

Released under the **[MIT License](./LICENSE)**. Upstream linguistic datasets are used in accordance with their respective open licenses (CC0-1.0 and Apache License 2.0).
