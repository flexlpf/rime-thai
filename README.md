# rime-thai · Rime 泰語輸入方案

一套適用於 **Rime 輸入法引擎**（小狼毫 Weasel / 鼠鬚管 Squirrel / 中州韻 ibus-rime / fcitx5-rime / 同文 Trime）的開源泰語輸入方案。架構設計參考 Rime 官方 `rime-ipa` 與粵拼方案 `rime-cantonese`。

安裝後可在 Rime 輸入法選單中自由勾選啟用以下**兩套獨立方案**：

| 方案 ID | 顯示名稱 | 適用場景 | 核心特性 |
| :--- | :--- | :--- | :--- |
| **`thai_roman`** | **泰語拼音** | 使用拉丁字母拼音（RTGS / Paiboon）輸入泰語 | 內置 **23,800+ 條**高頻詞彙；預設支援**忽略聲調盲打**、長短元音容錯、首字母簡拼、44 輔音及元音部件拆字輸入、候選詞發音提示開關 (`spelling_hints`) |
| **`thai_kedmanee`** | **泰語鍵盤** | 熟悉泰國標準物理鍵盤盲打的使用者 | 完整對應泰國國家標準 **TIS 820-2538 (Kedmanee)** 鍵位，無需切換 Windows / macOS 系統語言欄，在 Rime 中一鍵切換、按鍵即上屏 |

---

## 一、安裝方法

### 方法 1：通過小狼毫（Weasel）圖形界面一鍵獲取（推薦）
1. 右鍵點擊 Windows 任務欄小狼毫圖標 → 選擇 **「輸入法設定 (I)」**。
2. 點擊設定視窗左下角的 **「獲取更多輸入方案…」**。
3. 在彈出的命令列視窗中輸入本倉庫路徑並按 Enter：
   ```text
   flexlpf/rime-thai
   ```
4. 自動下載完成後，在彈出的方案勾選視窗中勾選 **「泰語拼音」** 與 **「泰語鍵盤」**，點擊「中」完成重新部署即可使用。

### 方法 2：通過東風破（`plum` / `rime-install`）命令列安裝
```bash
bash rime-install flexlpf/rime-thai
```

### 方法 3：Git 克隆或手動複製到用戶資料夾
將本倉庫內的 `*.yaml` 檔案複製到你的 Rime **用戶資料夾**（Windows 預設為 `%APPDATA%\Rime`，macOS 為 `~/Library/Rime`，Linux 為 `~/.config/ibus/rime` 或 `~/.local/share/fcitx5/rime`），並在 `default.custom.yaml` 的 `schema_list` 下添加：
```yaml
patch:
  schema_list:
    - {schema: thai_roman}      # 泰語拼音（拉丁轉寫）
    - {schema: thai_kedmanee}   # 泰語標準鍵盤（Kedmanee）
```
保存後執行 **「重新部署 (Deploy)」**。

---

## 二、使用方法

### （一）方案一：`thai_roman`（泰語拼音）

#### 1. 整詞與短語輸入（預設支援忽略聲調盲打）
詞庫底層採用 **RTGS（泰國皇家學會轉寫）+ 長短元音區分 + 1~5 聲調數字** 編碼，並通過 Rime `speller/algebra` 拼寫運算自動派生**無聲調盲打**、**長短音簡拼**、**首字母簡拼**及 **Paiboon 拼寫容錯**（如 `bp/p`, `dt/t`, `g/k`, `j/ch`, `eu/ue`, `er/oe`, `or/oo`）：

| 目標泰文 | 釋義 | 無聲調盲打（最常用） | 長音/容錯拼法 | 帶聲調精確輸入 | 首字母簡拼 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **สวัสดี** | 你好 | `sawatdi` | `sawatdii` | `sa2wat2dii1` | `swd` |
| **ขอบคุณ** | 謝謝 | `khopkhun` | `khorpkhun` / `khoopkhun` | `khoop2khun1` | `kk` / `khkh` |
| **ไม่เป็นไร** | 沒關係 | `maipenrai` | `maibpenrai` | `mai3pen1rai1` | `mpr` |
| **ภาษาไทย** | 泰語 | `phasathai` | `phaasaathai` | `phaa1saa5thai1` | `pst` / `phsth` |
| **กรุงเทพฯ** | 曼谷 | `krungthep` | `grungtheep` | `krung1theep3` | `kt` / `krth` |
| **ใบเสนอราคา** | 報價單 | `baisanoerakha` | `baisanerrakha` | `bai1sa2noee5raa1khaa1` | `bsnrk` |

#### 2. 聲調過濾（1 ~ 5 數字或快捷鍵）
日常輸入無需打聲調；若同音詞較多，可在音節末尾輸入數字 `1~5`（或對應字母鍵 `v / x / q / f / r`）精確篩選：

| 聲調數字 | 字母快捷鍵 | 泰語聲調名稱 | IPA 調值 | 輸入範例 |
| :---: | :---: | :--- | :---: | :--- |
| **`1`** | `v` | สามัญ (中平調 Mid) | `˧` (33) | `maa1` → มา |
| **`2`** | `x` | เอก (低平調 Low) | `˨˩` (21) | `mai2` → ใหม่ |
| **`3`** | `q` | โท (降調 Falling) | `˥˩` (51) | `mai3` → ไม่ / ม่าย |
| **`4`** | `f` | ตรี (高平調 High) | `˦˥` (45) | `maa4` → ม้า, `naam4` → น้ำ |
| **`5`** | `r` | จัตวา (升調 Rising) | `˩˩˦` (114) | `maa5` → หมา, `mai5` → ไหม |

#### 3. 單字拆字輸入（44 輔音、元音部件、聲調符號、泰文數字）
遇到詞庫未收錄的人名、地名或生僻字時，支援逐字拆字輸入：

- **44 個泰語輔音（支援兩種打法）**：
  1. **直接打輔音發音碼**：如輸入 `k` 出 `ก`；輸入 `kh` 依常用頻率列出 `ค ข ฆ ฃ ฅ`；輸入 `ch` 列出 `จ ช ฉ ฌ`；輸入 `s` 列出 `ส ซ ศ ษ`；輸入 `th` 列出 `ท ถ ธ ฐ ฑ ฒ`。
  2. **打傳統代表詞全稱（唯一精確定位）**：
     - 中輔音：`kokai` (`ก`), `chochan` (`จ`), `dochada` (`ฎ`), `topatak` (`ฏ`), `dodek` (`ด`), `totao` (`ต`), `bobaimai` (`บ`), `popla` (`ป`), `oang` (`อ`)
     - 高輔音：`khokhai` (`ข`), `khokhuat` (`ฃ`), `choching` (`ฉ`), `thothan` (`ฐ`), `thothung` (`ถ`), `phophueng` (`ผ`), `fofa` (`ฝ`), `sosala` (`ศ`), `soruesi` (`ษ`), `sosuea` (`ส`), `hohip` (`ห`)
     - 低輔音：`khokhwai` (`ค`), `khokhon` (`ฅ`), `khorakhang` (`ฆ`), `ngongu` (`ง`), `chochang` (`ช`), `soso` (`ซ`), `chochoe` (`ฌ`), `yoying` (`ญ`), `montho` (`ฑ`), `thophuthao` (`ฒ`), `nonen` (`ณ`), `thothahan` (`ท`), `thothong` (`ธ`), `nonu` (`น`), `phophan` (`พ`), `fofan` (`ฟ`), `phosamphao` (`ภ`), `moma` (`ม`), `yoyak` (`ย`), `roruea` (`ร`), `loling` (`ล`), `wowaen` (`ว`), `lochula` (`ฬ`), `honokhuk` (`ฮ`)
- **元音符號部件**：
  - `saraa` (`ะ`), `saraaa` / `aa` (`า`), `maihanakat` / `hanakat` (`ั`), `saraam` (`ำ`), `sarai` (`ิ`), `saraii` (`ี`), `saraue` (`ึ`), `sarauee` (`ื`), `sarau` (`ุ`), `sarauu` (`ู`), `sarae` (`เ`), `saraae` (`แ`), `sarao` (`โ`), `maimuan` (`ใ`), `maimalai` (`ไ`), `rue` (`ฤ`), `lue` (`ฦ`)。
- **聲調與控制符號**：
  - `maiek` / `tone2` (`่`)、`maitho` / `tone3` (`้`)、`maitri` / `tone4` (`๊`)、`maichattawa` / `tone5` (`๋`)、`maitaikhu` (`็`)、`karan` (`์`)、`maiyamok` (`ๆ`)、`paiyannoi` (`ฯ`)、`paiyanyai` (`ฯลฯ`)、`baht` 或按 `\` 鍵 (`฿`)。
- **泰文數字 (`๐`~`๙`)**：
  - `sun` (`๐`), `nueng` (`๑`), `song` (`๒`), `sam` (`๓`), `si` (`๔`), `ha` (`๕`), `hok` (`๖`), `chet` (`๗`), `paet` (`๘`), `kao` (`๙`)。

#### 4. 泰語發音提示開關（`spelling_hints`）
預設候選詞右側會顯示泰語羅馬音與聲調提示（如 `สวัสดี [sa2 wat2 dii1]`）。
- 如需關閉提示，可將 `thai_roman.schema.yaml` 中的 `spelling_hints: 8` 改為 `0`，或在用戶資料夾新建 `thai_roman.custom.yaml`：
  ```yaml
  patch:
    translator/spelling_hints: 0
  ```

---

### （二）方案二：`thai_kedmanee`（泰語標準鍵盤）

切換至「泰語鍵盤」後，按鍵映射完全遵循泰國工業標準 **TIS 820-2538 (Kedmanee)**，按鍵直接上屏：

```text
┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬──────┐
│   │ + │ ๑ │ ๒ │ ๓ │ ๔ │ ู │ ฿ │ ๕ │ ๖ │ ๗ │ ๘ │ ๙ │      │
│   │ ๅ │ / │ - │ ภ │ ถ │ ุ │ ึ │ ค │ ต │ จ │ ข │ ช │ Bksp │
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

## 三、詞庫構建腳本

若需自定義擴充詞表或重新拉取上游語料生成詞典，可在倉庫根目錄執行：
```bash
python tools/build_dicts.py
```

---

## 四、引用來源（References & Data Sources）

本方案的轉寫規則、鍵位標準與詞頻語料嚴格基於以下公開學術與國家標準資源：

1. **轉寫與音韻規範**：
   - **泰國皇家學會轉寫系統 (RTGS)**：Royal Society of Thailand (สำนักงานราชบัณฑิตยสภา), *Principles of Romanization for Thai Script by Transcription Method* (หลักเกณฑ์การถอดอักษรไทยเป็นอักษรโรมันแบบถ่ายเสียง), 1999.
   - **Paiboon 實用音標系統**：Benjawan Poomsan Becker, *Thai for Beginners*, Paiboon Publishing.
2. **鍵盤布局國家標準**：
   - **TIS 820-2538**：Thai Industrial Standards Institute (สำนักงานมาตรฐานผลิตภัณฑ์อุตสาหกรรม), *Standard for Thai Character Keys on Computer Keyboards (Kedmanee Layout)*, 1995.
3. **詞彙與詞頻語料庫**：
   - **泰國國家語料庫 (Thai National Corpus, TNC)**：Department of Linguistics, Faculty of Arts, Chulalongkorn University (ภาควิชาภาษาศาสตร์ คณะอักษรศาสตร์ จุฬาลงกรณ์มหาวิทยาลัย). 詞頻統計表引自 `pythainlp/corpus/tnc_freq.txt` (CC0-1.0 Public Domain).
4. **審校發音詞典 (Grapheme-to-Phoneme IPA Lexicon)**：
   - **FastThaiG2P**：Charin Polpanumas & Amazon Web Services (AWS Labs), `fastthaig2p_ipa.json` ([awslabs/FastThaiG2P](https://github.com/awslabs/FastThaiG2P), Apache License 2.0).

---

## 五、鳴謝（Acknowledgements）

- **[Rime Input Method Engine (中州韻輸入法引擎)](https://rime.im/)**：感謝佛振（@lotem）及 Rime 開源社區開發的跨平台輸入法框架與東風破（`plum`）套件管理機制。
- **[PyThaiNLP Project](https://github.com/PyThaiNLP/pythainlp)**：感謝 Wannaphong Phatthiyaphaibun 及 PyThaiNLP 社區整理的開源泰語自然語言處理語料與轉寫工具（Apache-2.0 / CC0-1.0）。
- **[FastThaiG2P](https://github.com/awslabs/FastThaiG2P) & [TLTK (Thai Language Toolkit)](https://github.com/attapol/tltk)**：感謝 Charin Polpanumas 與朱拉隆功大學言語技術團隊（Attapol Thamrongrattanarit）在泰語音節切分與 G2P 音標轉換上的開源貢獻。
- **[rime-cantonese (粵語拼音輸入方案)](https://github.com/CanCLID/rime-cantonese) & [rime-ipa (國際音標輸入方案)](https://github.com/rime/rime-ipa)**：本方案的詞典模組化組織（`chars` + `words`）、拼寫代數（`speller/algebra`）與聲調映射設計深受上述兩個方案啟發。

---

## 六、開源協議（License）

本項目配置文件與構建腳本採用 **[MIT License](./LICENSE)** 開源發布。上游語料數據遵循其原始許可協議（CC0-1.0 及 Apache License 2.0）。
