# rime-thai · Rime 泰语输入方案 / Thai Input Method for Rime / แป้นพิมพ์ภาษาไทยสำหรับ Rime

<p align="center">
  <a href="#简体中文"><b>简体中文</b></a> ·
  <a href="#english"><b>English</b></a> ·
  <a href="#ภาษาไทย"><b>ภาษาไทย</b></a>
  <br/>
  <sub>Standalone files: <a href="./README.md">简体中文 (README.md)</a> | <a href="./README.en.md">English (README.en.md)</a> | <a href="./README.th.md">ภาษาไทย (README.th.md)</a></sub>
</p>

---

<a id="简体中文"></a>

## 🇨🇳 简体中文说明

一套适用于 **[Rime 输入法引擎](https://rime.im/)**（小狼毫 Weasel / 鼠须管 Squirrel / 中州韵 ibus-rime / fcitx5-rime / 同文 Trime）的开源泰语输入方案。架构设计参考 Rime 官方**[rime-cantonese (粤拼)](https://github.com/CanCLID/rime-cantonese)** 与**[rime-ipa](https://github.com/rime/rime-ipa)**。

安装后可在 Rime 输入法菜单中自由勾选启用以下**两套独立方案**：

| 方案 ID | 显示名称 | 适用场景 | 核心特性 |
| :--- | :--- | :--- | :--- |
| **`thai_roman`** | **泰語拼音** | 使用拉丁字母拼音（RTGS / Paiboon）输入泰语 | 内置 **23,800+ 条**高频词汇；默认支持**忽略声调盲打**、长短元音容错、首字母简拼、44 辅音及元音部件拆字输入、候选词发音提示开关 (`spelling_hints`) |
| **`thai_kedmanee`** | **泰語鍵盤** | 熟悉泰国标准物理键盘盲打的用户 | 完整对应泰国国家标准 **TIS 820-2538 (Kedmanee)** 键位，无需切换 Windows / macOS 系统语言栏，在 Rime 中一键切换、按键即上屏 |

### 一、安装方法

#### 方法 1：通过小狼毫（Weasel）图形界面一键获取（推荐）
1. 右键点击 Windows 任务栏小狼毫图标 → 选择 **“输入法设定 (I)”**。
2. 点击设定窗口左下角的 **“获取更多输入方案…”**。
3. 在弹出的命令行窗口中输入本仓库路径并按回车（Enter）：
   ```text
   flexlpf/rime-thai
   ```
4. 自动下载完成后，在弹出的方案勾选窗口中勾选 **“泰語拼音”** 与 **“泰語鍵盤”**，点击确定完成重新部署即可使用。

#### 方法 2：通过东风破（`plum` / `rime-install`）命令行安装
```bash
bash rime-install flexlpf/rime-thai
```

#### 方法 3：Git 克隆或手动复制到用户文件夹
将本仓库内的 `*.yaml` 文件复制到你的 Rime **用户文件夹**（Windows 默认为 `%APPDATA%\Rime`，macOS 为 `~/Library/Rime`，Linux 为 `~/.config/ibus/rime` 或 `~/.local/share/fcitx5/rime`），并在 `default.custom.yaml` 的 `schema_list` 下添加：
```yaml
patch:
  schema_list:
    - {schema: thai_roman}      # 泰语拼音（拉丁转写）
    - {schema: thai_kedmanee}   # 泰语标准键盘（Kedmanee）
```
保存后执行 **“重新部署 (Deploy)”**。

---

### 二、使用方法

#### （一）方案一：`thai_roman`（泰语拼音）

##### 1. 整词与短语输入（默认支持忽略声调盲打）
词库底层采用 **RTGS（泰国皇家学会转写）+ 长短元音区分 + 1~5 声调数字** 编码，并通过 Rime `speller/algebra` 拼写运算自动派生**无声调盲打**、**长短音简拼**、**首字母简拼**及 **Paiboon 拼写容错**（如 `bp/p`, `dt/t`, `g/k`, `j/ch`, `eu/ue`, `er/oe`, `or/oo`）：

| 目标泰文 | 释义 | 无声调盲打（最常用） | 长音/容错拼法 | 带声调精确输入 | 首字母简拼 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **สวัสดี** | 你好 | `sawatdi` | `sawatdii` | `sa2wat2dii1` | `swd` |
| **ขอบคุณ** | 谢谢 | `khopkhun` | `khorpkhun` / `khoopkhun` | `khoop2khun1` | `kk` / `khkh` |
| **ไม่เป็นไร** | 没关系 | `maipenrai` | `maibpenrai` | `mai3pen1rai1` | `mpr` |
| **ภาษาไทย** | 泰语 | `phasathai` | `phaasaathai` | `phaa1saa5thai1` | `pst` / `phsth` |
| **กรุงเทพฯ** | 曼谷 | `krungthep` | `grungtheep` | `krung1theep3` | `kt` / `krth` |
| **ใบเสนอราคา** | 报价单 | `baisanoerakha` | `baisanerrakha` | `bai1sa2noee5raa1khaa1` | `bsnrk` |

##### 2. 声调过滤（1 ~ 5 数字或字母快捷键）
日常输入无需打声调；若同音词较多，可在音节末尾输入数字 `1~5`（或对应字母键 `v / x / q / f / r`）精确筛选：

| 声调数字 | 字母快捷键 | 泰语声调名称 | IPA 调值 | 输入示例 |
| :---: | :---: | :--- | :---: | :--- |
| **`1`** | `v` | สามัญ (中平调 Mid) | `˧` (33) | `maa1` → มา |
| **`2`** | `x` | เอก (低平调 Low) | `˨˩` (21) | `mai2` → ใหม่ |
| **`3`** | `q` | โท (降调 Falling) | `˥˩` (51) | `mai3` → ไม่ / ม่าย |
| **`4`** | `f` | ตรี (高平调 High) | `˦˥` (45) | `maa4` → ม้า, `naam4` → น้ำ |
| **`5`** | `r` | จัตวา (升调 Rising) | `˩˩˦` (114) | `maa5` → หมา, `mai5` → ไหม |

##### 3. 单字拆字输入（44 辅音、元音部件、声调符号、泰文数字）
遇到词库未收录的人名、地名或生僻字时，支持逐字拆字输入：

- **44 个泰语辅音（支持两种打法）**：
  1. **直接打辅音发音码**：如输入 `k` 出 `ก`；输入 `kh` 按常用频率列出 `ค ข ฆ ฃ ฅ`；输入 `ch` 列出 `จ ช ฉ ฌ`；输入 `s` 列出 `ส ซ ศ ษ`；输入 `th` 列出 `ท ถ ธ ฐ ฑ ฒ`。
  2. **打传统代表词全称（唯一精确定位）**：
     - 中辅音：`kokai` (`ก`), `chochan` (`จ`), `dochada` (`ฎ`), `topatak` (`ฏ`), `dodek` (`ด`), `totao` (`ต`), `bobaimai` (`บ`), `popla` (`ป`), `oang` (`อ`)
     - 高辅音：`khokhai` (`ข`), `khokhuat` (`ฃ`), `choching` (`ฉ`), `thothan` (`ฐ`), `thothung` (`ถ`), `phophueng` (`ผ`), `fofa` (`ฝ`), `sosala` (`ศ`), `soruesi` (`ษ`), `sosuea` (`ส`), `hohip` (`ห`)
     - 低辅音：`khokhwai` (`ค`), `khokhon` (`ฅ`), `khorakhang` (`ฆ`), `ngongu` (`ง`), `chochang` (`ช`), `soso` (`ซ`), `chochoe` (`ฌ`), `yoying` (`ญ`), `montho` (`ฑ`), `thophuthao` (`ฒ`), `nonen` (`ณ`), `thothahan` (`ท`), `thothong` (`ธ`), `nonu` (`น`), `phophan` (`พ`), `fofan` (`ฟ`), `phosamphao` (`ภ`), `moma` (`ม`), `yoyak` (`ย`), `roruea` (`ร`), `loling` (`ล`), `wowaen` (`ว`), `lochula` (`ฬ`), `honokhuk` (`ฮ`)
- **元音符号部件**：
  - `saraa` (`ะ`), `saraaa` / `aa` (`า`), `maihanakat` / `hanakat` (`ั`), `saraam` (`ำ`), `sarai` (`ิ`), `saraii` (`ี`), `saraue` (`ึ`), `sarauee` (`ื`), `sarau` (`ุ`), `sarauu` (`ู`), `sarae` (`เ`), `saraae` (`แ`), `sarao` (`โ`), `maimuan` (`ใ`), `maimalai` (`ไ`), `rue` (`ฤ`), `lue` (`ฦ`)。
- **声调与控制符号**：
  - `maiek` / `tone2` (`่`)、`maitho` / `tone3` (`้`)、`maitri` / `tone4` (`๊`)、`maichattawa` / `tone5` (`๋`)、`maitaikhu` (`็`)、`karan` (`์`)、`maiyamok` (`ๆ`)、`paiyannoi` (`ฯ`)、`paiyanyai` (`ฯลฯ`)、`baht` 或按 `\` 键 (`฿`)。
- **泰文数字 (`๐`~`๙`)**：
  - `sun` (`๐`), `nueng` (`๑`), `song` (`๒`), `sam` (`๓`), `si` (`๔`), `ha` (`๕`), `hok` (`๖`), `chet` (`๗`), `paet` (`๘`), `kao` (`๙`)。

##### 4. 泰语发音提示开关（`spelling_hints`）
默认候选词右侧会显示泰语罗马音与声调提示（如 `สวัสดี [sa2 wat2 dii1]`）。
- 如需关闭提示，可将 `thai_roman.schema.yaml` 中的 `spelling_hints: 8` 改为 `0`，或在用户文件夹新建 `thai_roman.custom.yaml`：
  ```yaml
  patch:
    translator/spelling_hints: 0
  ```

#### （二）方案二：`thai_kedmanee`（泰语标准键盘）
切换至“泰语键盘”后，按键映射完全遵循泰国工业标准 **TIS 820-2538 (Kedmanee)**，按键直接上屏：

<img width="1920" height="640" alt="image" src="https://github.com/user-attachments/assets/5fdd89bb-2c48-43f6-95b5-2d1c9a7b47e6" />


### 三、引用来源与鸣谢

#### 引用来源（References & Data Sources）
1. **转写与音韵规范**：泰国皇家学会转写系统 (RTGS, Royal Society of Thailand, 1999) 及 Paiboon 实用音标系统。
2. **键盘布局国家标准**：泰国工业标准学会 TIS 820-2538 (*Standard for Thai Character Keys on Computer Keyboards - Kedmanee Layout*, 1995)。
3. **词汇与词频语料库**：朱拉隆功大学语言学系泰国国家语料库 (Thai National Corpus, TNC)，词频表引自 `pythainlp/corpus/tnc_freq.txt` (CC0-1.0 Public Domain)。
4. **审校发音词典**：Charin Polpanumas & AWS Labs, `fastthaig2p_ipa.json` ([FastThaiG2P](https://github.com/awslabs/FastThaiG2P), Apache License 2.0)。

#### 鸣谢（Acknowledgements）
- **[Rime Input Method Engine (中州韵输入法引擎)](https://rime.im/)**：感谢佛振（@lotem）及 Rime 开源社区。
- **[PyThaiNLP Project](https://github.com/PyThaiNLP/pythainlp)**：感谢 Wannaphong Phatthiyaphaibun 及 PyThaiNLP 社区。
- **[FastThaiG2P](https://github.com/awslabs/FastThaiG2P) & [TLTK](https://github.com/attapol/tltk)**：感谢 Charin Polpanumas 与朱拉隆功大学语言技术团队。
- **[rime-cantonese (粤拼)](https://github.com/CanCLID/rime-cantonese) & [rime-ipa](https://github.com/rime/rime-ipa)**：架构与拼写运算设计参考。

---

<a id="english"></a>

## 🇬🇧 English Documentation

An open-source **Thai input method** package for the **Rime Input Method Engine** (Weasel on Windows, Squirrel on macOS, ibus-rime / fcitx5-rime on Linux, Trime on Android). Architecturally inspired by `rime-cantonese` (Jyutping) and `rime-ipa`.

Once installed, two independent Thai input schemas are available:

| Schema ID | Display Name | Use Case | Key Features |
| :--- | :--- | :--- | :--- |
| **`thai_roman`** | **泰語拼音** (Thai Romanization) | Type Thai phonetically using Latin letters (RTGS / Paiboon) | **23,800+ core words** ranked by corpus frequency; **tone-free typing** by default, vowel-length tolerance, initial-letter abbreviations, single-character lookup for all 44 consonants & vowel marks, and configurable pronunciation hints (`spelling_hints`) |
| **`thai_kedmanee`** | **泰語鍵盤** (Thai Kedmanee) | Touch-typing with the standard Thai keyboard layout | Full **TIS 820-2538 (Kedmanee)** national standard layout inside Rime without switching OS language bars; direct single-key commit |

### 1. Installation

#### Option A: Via Weasel GUI on Windows (Recommended)
1. Right-click the Weasel tray icon → select **"Input Method Settings (輸入法設定)"**.
2. Click **"Get more input schemas... (獲取更多輸入方案…)"** at the bottom-left corner.
3. Type the repository name in the console window and press Enter:
   ```text
   flexlpf/rime-thai
   ```
4. Check **"泰語拼音"** and/or **"泰語鍵盤"** in the pop-up dialog and confirm to deploy.

#### Option B: Via `plum` (`rime-install`) CLI
```bash
bash rime-install flexlpf/rime-thai
```

#### Option C: Manual / Git Clone
Copy all `*.yaml` files into your Rime **User Data Directory** (`%APPDATA%\Rime` on Windows, `~/Library/Rime` on macOS, `~/.config/ibus/rime` or `~/.local/share/fcitx5/rime` on Linux), and enable the schemas in `default.custom.yaml`:
```yaml
patch:
  schema_list:
    - {schema: thai_roman}
    - {schema: thai_kedmanee}
```
Then run **Deploy (重新部署)**.

### 2. Usage Guide (`thai_roman`)

#### Word & Phrase Input (Tone-Free by Default)
You do **not** need to type tone marks for daily typing. Speller algebra automatically handles tone-free input, short/long vowel tolerance (`aa/a`, `ii/i`, `uu/u`, `ee/e`, `oo/o`), Paiboon variants (`bp/p`, `dt/t`, `g/k`, `j/ch`, `eu/ue`, `er/oe`, `or/oo`), and syllable initials:

| Thai | Meaning | Tone-Free Input (Default) | Variant / Long Vowel | With Tone Numbers (1-5) | Initials Abbrev |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **สวัสดี** | Hello | `sawatdi` | `sawatdii` | `sa2wat2dii1` | `swd` |
| **ขอบคุณ** | Thank you | `khopkhun` | `khorpkhun` / `khoopkhun` | `khoop2khun1` | `kk` / `khkh` |
| **ไม่เป็นไร** | No problem | `maipenrai` | `maibpenrai` | `mai3pen1rai1` | `mpr` |
| **ภาษาไทย** | Thai language | `phasathai` | `phaasaathai` | `phaa1saa5thai1` | `pst` |
| **กรุงเทพฯ** | Bangkok | `krungthep` | `grungtheep` | `krung1theep3` | `kt` |
| **ใบเสนอราคา** | Quotation | `baisanoerakha` | `baisanerrakha` | `bai1sa2noee5raa1khaa1` | `bsnrk` |

#### Tone Filtering (1–5 or Shortcut Keys)
To narrow down homophones, append a tone digit `1`–`5` (or letter shortcut `v / x / q / f / r`) at the end of a syllable:
- **`1`** (`v`): Mid tone (สามัญ, `˧`) — e.g., `maa1` → มา
- **`2`** (`x`): Low tone (เอก, `˨˩`) — e.g., `mai2` → ใหม่
- **`3`** (`q`): Falling tone (โท, `˥˩`) — e.g., `mai3` → ไม่
- **`4`** (`f`): High tone (ตรี, `˦˥`) — e.g., `maa4` → ม้า, `naam4` → น้ำ
- **`5`** (`r`): Rising tone (จัตวา, `˩˩˦`) — e.g., `maa5` → หมา, `mai5` → ไหม

#### Single-Character & Component Input
- **44 Consonants**: Type either the consonant sound (`k`, `kh`, `ch`, `s`, `th`, `ph`, etc.) or its traditional acrophonic name (`kokai` → `ก`, `khokhai` → `ข`, `khokhwai` → `ค`, `ngongu` → `ง`, `chochan` → `จ`, `sosuea` → `ส`, `thothahan` → `ท`, `popla` → `ป`, `phophan` → `พ`, `moma` → `ม`, `roruea` → `ร`, `loling` → `ล`, `wowaen` → `ว`, `oang` → `อ`, `hohip` → `ห`, etc.).
- **Vowels & Diacritics**: `saraa` (`ะ`), `saraaa` (`า`), `maihanakat` (`ั`), `saraam` (`ำ`), `sarai` (`ิ`), `saraii` (`ี`), `saraue` (`ึ`), `sarauee` (`ื`), `sarau` (`ุ`), `sarauu` (`ู`), `sarae` (`เ`), `saraae` (`แ`), `sarao` (`โ`), `maimuan` (`ใ`), `maimalai` (`ไ`), `maiek` (`่`), `maitho` (`้`), `maitri` (`๊`), `maichattawa` (`๋`), `maitaikhu` (`็`), `karan` (`์`), `maiyamok` (`ๆ`), `paiyannoi` (`ฯ`), `baht` or `\` (`฿`).
- **Thai Numerals (`๐`–`๙`)**: `sun` (`๐`), `nueng` (`๑`), `song` (`๒`), `sam` (`๓`), `si` (`๔`), `ha` (`๕`), `hok` (`๖`), `chet` (`๗`), `paet` (`๘`), `kao` (`๙`).

#### Pronunciation Hints Toggle (`spelling_hints`)
By default, romanized pronunciation hints are shown next to candidates (`spelling_hints: 8`). To disable them, set `translator/spelling_hints: 0` in `thai_roman.custom.yaml`.

---

<a id="ภาษาไทย"></a>

## 🇹🇭 คำอธิบายภาษาไทย (Thai Documentation)

**`rime-thai`** คือชุดแป้นพิมพ์ภาษาไทยแบบโอเพนซอร์สสำหรับ **Rime Input Method Engine** (รองรับทั้ง Weasel บน Windows, Squirrel บน macOS, ibus-rime / fcitx5-rime บน Linux และ Trime บน Android) ออกแบบโครงสร้างตามมาตรฐานของ `rime-cantonese` และ `rime-ipa`

ประกอบด้วยผังการพิมพ์ **2 รูปแบบ** ที่เลือกเปิดใช้งานได้พร้อมกัน:

| รหัสผัง (Schema ID) | ชื่อที่แสดง | ลักษณะการใช้งาน | จุดเด่น |
| :--- | :--- | :--- | :--- |
| **`thai_roman`** | **泰語拼音** (พินอินภาษาไทย / คาราโอเกะ) | พิมพ์ภาษาไทยด้วยอักษรโรมันตามเสียงอ่าน (RTGS / Paiboon) | คลังคำศัพท์ความถี่สูงกว่า **23,800+ คำ**; พิมพ์ได้ทันที**โดยไม่ต้องใส่วรรณยุกต์**, รองรับการย่อเสียงสระสั้น-ยาว, พิมพ์ตัวย่อพยัญชนะต้น, พิมพ์พยัญชนะไทยครบทั้ง 44 ตัว และมีสวิตช์เปิด/ปิดคำใบ้การออกเสียง (`spelling_hints`) |
| **`thai_kedmanee`** | **泰語鍵盤** (แป้นพิมพ์เกษมณี) | พิมพ์สัมผัสตามผังแป้นพิมพ์ภาษาไทยมาตรฐาน | ตรงตามมาตรฐานผลิตภัณฑ์อุตสาหกรรม **มอก. 820-2538 (Kedmanee)** ทุกปุ่ม สลับภาษาภายใน Rime ได้ทันทีโดยไม่ต้องเปลี่ยนภาษาของระบบปฏิบัติการ |

### 1. วิธีการติดตั้ง (Installation)

#### วิธีที่ 1: ติดตั้งผ่านหน้าต่างตั้งค่าของ Weasel บน Windows (แนะนำ)
1. คลิกขวาที่ไอคอน Weasel บนแถบงาน (Taskbar) → เลือก **"ตั้งค่าแป้นพิมพ์ (輸入法設定)"**
2. คลิกปุ่ม **"รับผังแป้นพิมพ์เพิ่มเติม... (獲取更多輸入方案…)"** ที่มุมซ้ายล่าง
3. พิมพ์ชื่อคลังโค้ดด้านล่างลงในหน้าต่างคำสั่งแล้วกด Enter:
   ```text
   flexlpf/rime-thai
   ```
4. เมื่อดาวน์โหลดเสร็จสิ้น ให้ติ๊กเลือก **"泰語拼音"** และ/หรือ **"泰語鍵盤"** แล้วกดยืนยันเพื่อประมวลผล (Deploy)

#### วิธีที่ 2: ติดตั้งผ่านบรรทัดคำสั่ง `plum` (`rime-install`)
```bash
bash rime-install flexlpf/rime-thai
```

#### วิธีที่ 3: คัดลอกไฟล์ด้วยตนเอง (Manual Installation)
คัดลอกไฟล์ `*.yaml` ทั้งหมดไปยังโฟลเดอร์ข้อมูลผู้ใช้ของ Rime (`%APPDATA%\Rime` บน Windows หรือ `~/Library/Rime` บน macOS) จากนั้นเพิ่มรายการในไฟล์ `default.custom.yaml`:
```yaml
patch:
  schema_list:
    - {schema: thai_roman}
    - {schema: thai_kedmanee}
```
บันทึกไฟล์แล้วสั่ง **Deploy (重新部署)**

### 2. วิธีใช้งาน `thai_roman` (การพิมพ์ด้วยอักษรโรมัน)

- **พิมพ์คำศัพท์โดยไม่ต้องใส่วรรณยุกต์**:
  - พิมพ์ `sawatdi` หรือ `sawatdii` หรือตัวย่อ `swd` → **สวัสดี**
  - พิมพ์ `khopkhun` หรือ `kk` → **ขอบคุณ**
  - พิมพ์ `maipenrai` หรือ `mpr` → **ไม่เป็นไร**
  - พิมพ์ `phasathai` → **ภาษาไทย**
  - พิมพ์ `krungthep` → **กรุงเทพฯ**
  - พิมพ์ `baisanoerakha` → **ใบเสนอราคา**
- **การระบุเสียงวรรณยุกต์ (เลข `1`–`5` หรือปุ่มลัด `v / x / q / f / r` ท้ายพยางค์)**:
  - `1` (`v`) = เสียงสามัญ (เช่น `maa1` → มา)
  - `2` (`x`) = เสียงเอก (เช่น `mai2` → ใหม่)
  - `3` (`q`) = เสียงโท (เช่น `mai3` → ไม่)
  - `4` (`f`) = เสียงตรี (เช่น `maa4` → ม้า, `naam4` → น้ำ)
  - `5` (`r`) = เสียงจัตวา (เช่น `maa5` → หมา, `mai5` → ไหม)
- **การพิมพ์พยัญชนะเดี่ยวทั้ง 44 ตัว สระ วรรณยุกต์ และตัวเลขไทย**:
  - พิมพ์ชื่อพยัญชนะโดยตรง เช่น `kokai` (`ก`), `khokhai` (`ข`), `khokhwai` (`ค`), `ngongu` (`ง`), `chochan` (`จ`), `sosuea` (`ส`), `thothahan` (`ท`), `popla` (`ป`), `phophan` (`พ`), `moma` (`ม`), `roruea` (`ร`), `loling` (`ล`), `wowaen` (`ว`), `oang` (`อ`), `hohip` (`ห`)
  - พิมพ์สระและวรรณยุกต์ เช่น `saraa` (`ะ`), `saraaa` (`า`), `sarai` (`ิ`), `saraii` (`ี`), `maiek` (`่`), `maitho` (`้`), `maitri` (`๊`), `maichattawa` (`๋`), `karan` (`์`), `maiyamok` (`ๆ`), `baht` (`฿`)
  - พิมพ์ตัวเลขไทย (`๐`–`๙`) ด้วยคำอ่าน: `sun` (`๐`), `nueng` (`๑`), `song` (`๒`), `sam` (`๓`), `si` (`๔`), `ha` (`๕`), `hok` (`๖`), `chet` (`๗`), `paet` (`๘`), `kao` (`๙`)
- **การเปิด/ปิดคำใบ้การออกเสียง (`spelling_hints`)**:
  - หากต้องการซ่อนคำใบ้เสียงอ่านภาษาอังกฤษท้ายคำตัวเลือก ให้แก้ไขค่า `spelling_hints: 0` ในไฟล์ `thai_roman.schema.yaml` หรือกำหนดใน `thai_roman.custom.yaml`

### 3. แหล่งอ้างอิงและกิตติกรรมประกาศ (References & Acknowledgements)
- **หลักเกณฑ์การถอดอักษรไทยเป็นอักษรโรมันแบบถ่ายเสียง (RTGS)** โดยสำนักงานราชบัณฑิตยสภา
- **มาตรฐานผลิตภัณฑ์อุตสาหกรรม มอก. 820-2538** สำหรับผังแป้นพิมพ์เกษมณี (Kedmanee Layout)
- **คลังข้อมูลภาษาไทยแห่งชาติ (Thai National Corpus - TNC)** ภาควิชาภาษาศาสตร์ คณะอักษรศาสตร์ จุฬาลงกรณ์มหาวิทยาลัย (CC0-1.0)
- **โครงการ PyThaiNLP และ FastThaiG2P** สำหรับฐานข้อมูลสัทอักษรสากล (IPA Lexicon, Apache License 2.0)
- **โครงการ Rime Input Method Engine, rime-cantonese และ rime-ipa** สำหรับสถาปัตยกรรมระบบพิมพ์

---

## 📜 License

Released under the **[MIT License](./LICENSE)**. Upstream linguistic datasets are used in accordance with their respective open licenses (CC0-1.0 and Apache License 2.0).
