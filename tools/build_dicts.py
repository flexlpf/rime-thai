#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_dicts.py - 構建 Rime 泰語輸入方案詞庫 (rime-thai)
包含：
  1. thai_roman.chars.dict.yaml  (44 輔音、元音部件、聲調符號、泰文數字、標點拆字表)
  2. thai_roman.words.dict.yaml  (約 22,000 條高頻泰語詞彙，帶標準音節切分與聲調 1-5)
  3. thai_kedmanee.dict.yaml     (TIS 820-2538 泰國標準 Kedmanee 鍵盤映射表)

資料來源：
  - 泰國皇家學會轉寫系統 (RTGS / Royal Institute of Thailand)
  - 朱拉隆功大學泰國國家語料庫詞頻 (Thai National Corpus / TNC)
  - PyThaiNLP & FastThaiG2P IPA 審校發音詞典 (Apache-2.0)
"""

from __future__ import annotations

import json
import re
import urllib.request
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

IPA_URL = "https://raw.githubusercontent.com/PyThaiNLP/pythainlp/dev/pythainlp/corpus/fastthaig2p_ipa.json"
TNC_URL = "https://raw.githubusercontent.com/PyThaiNLP/pythainlp/dev/pythainlp/corpus/tnc_freq.txt"

# 泰語 5 個聲調的 IPA 調值與數字編號對應表：
# 1: สามัญ (Mid, ˧)
# 2: เอก (Low, ˨˩)
# 3: โท (Falling, ˥˩)
# 4: ตรี (High, ˦˥)
# 5: จัตวา (Rising, ˩˩˦)
TONE_MAP = {
    "˩˩˦": "5",
    "˨˩": "2",
    "˥˩": "3",
    "˦˥": "4",
    "˧": "1",
}

ONSET_MAP = {
    "t͡ɕʰ": "ch",
    "t͡ɕ": "ch",
    "kʰ": "kh",
    "pʰ": "ph",
    "tʰ": "th",
    "ŋ": "ng",
    "j": "y",
    "g": "k",
}


def ipa_syllable_to_roman(syl: str) -> str | None:
    """將單個 IPA 音節轉為 RTGS/Paiboon 兼容的拉丁字母 + 聲調數字 (1-5)。"""
    syl = syl.strip()
    if not syl:
        return None

    tone = "1"
    for t_ipa, t_num in sorted(TONE_MAP.items(), key=lambda x: -len(x[0])):
        if syl.endswith(t_ipa):
            tone = t_num
            syl = syl[: -len(t_ipa)]
            break

    # 移除唯閉音符號 (̚) 與喉塞音 (ʔ)
    syl = syl.replace("̚", "").replace("ʔ", "")
    if not syl:
        return None

    m = re.match(r"^(t͡ɕʰ|t͡ɕ|kʰ|pʰ|tʰ|[kptbdmŋnsrlwjfhg]?)([rlw]?)(.+)$", syl)
    if not m:
        return None
    c1, c2, rhyme = m.groups()
    onset = ONSET_MAP.get(c1, c1) + c2

    # 複合元音 (Diphthongs)
    rhyme = rhyme.replace("ia̯", "ia").replace("ɯa̯", "uea").replace("ua̯", "ua")
    # 長元音 (Long vowels)
    rhyme = (
        rhyme.replace("aː", "aa")
        .replace("iː", "ii")
        .replace("ɯː", "uee")
        .replace("uː", "uu")
        .replace("eː", "ee")
        .replace("ɛː", "aee")
        .replace("oː", "oo")
        .replace("ɔː", "oo")
        .replace("ɤː", "oee")
    )
    # 短元音 (Short vowels)
    rhyme = (
        rhyme.replace("ɯ", "ue")
        .replace("ɛ", "ae")
        .replace("ɔ", "o")
        .replace("ɤ", "oe")
    )

    # 韻尾轉換 (Final consonants / glides)
    if rhyme.endswith("ŋ"):
        rhyme = rhyme[:-1] + "ng"
    elif rhyme.endswith("j"):
        rhyme = rhyme[:-1] + "i"
    elif rhyme.endswith("w"):
        rhyme = rhyme[:-1] + "o"

    rom = onset + rhyme
    # 確保僅包含純小寫英文字母
    if not re.match(r"^[a-z]+$", rom):
        return None
    return f"{rom}{tone}"


def ipa_word_to_roman(ipa_str: str) -> str | None:
    """將整詞 IPA 轉為空格分隔的 Rime 音節編碼。"""
    clean = ipa_str.strip().strip("/")
    if not clean:
        return None
    parts = [p for p in clean.split(".") if p.strip()]
    if not parts:
        return None
    rom_syls = []
    for p in parts:
        r = ipa_syllable_to_roman(p)
        if not r:
            return None
        rom_syls.append(r)
    return " ".join(rom_syls)


def build_chars_dict() -> None:
    """生成 thai_roman.chars.dict.yaml：44 輔音、元音部件、聲調、數字拆字表。"""
    header = """# Rime dictionary
# encoding: utf-8
#
# thai_roman.chars - 泰語單字、44 輔音、元音部件、聲調與數字拆字詞庫
#
# 支援兩種單字輸入方式：
#   1. 輸入輔音發音（如 k, kh, ch, s, t, th, p, ph）列出同音輔音
#   2. 輸入傳統代表詞全稱（如 kokai -> ก, khokhai -> ข, khokhwai -> ค）精確定位唯一輔音
#   3. 輸入 sara + 元音名（如 saraa -> า, sarai -> ิ/ี）或 mai + 聲調名（如 maiek -> ่）輸出部件

---
name: thai_roman.chars
version: "2026.11.12"
sort: by_weight
use_preset_vocabulary: false
...
"""
    # 44 泰語輔音：(泰文字母, 發音簡碼, 代表詞全拼, 權重)
    consonants = [
        ("ก", "k", "kokai", "ko1 kai2", 1000),
        ("ข", "kh", "khokhai", "kho5 khai2", 950),
        ("ฃ", "kh", "khokhuat", "kho5 khuat2", 100),
        ("ค", "kh", "khokhwai", "kho1 khwaai1", 980),
        ("ฅ", "kh", "khokhon", "kho1 khon1", 100),
        ("ฆ", "kh", "khorakhang", "kho1 ra4 khang1", 400),
        ("ง", "ng", "ngongu", "ngoo1 nguu1", 990),
        ("จ", "ch", "chochan", "choo1 chaan1", 980),
        ("ฉ", "ch", "choching", "choo5 ching2", 750),
        ("ช", "ch", "chochang", "choo1 chaang4", 960),
        ("ซ", "s", "soso", "soo1 soo3", 800),
        ("ฌ", "ch", "chochoe", "choo1 choee1", 300),
        ("ญ", "y", "yoying", "yoo1 ying5", 850),
        ("ฎ", "d", "dochada", "doo1 cha4 daa1", 450),
        ("ฏ", "t", "topatak", "too1 pa2 tak2", 450),
        ("ฐ", "th", "thothan", "thoo5 thaan5", 500),
        ("ฑ", "th", "montho", "thoo1 mon1 thoo1", 400),
        ("ฒ", "th", "thophuthao", "thoo1 phuu3 thao3", 350),
        ("ณ", "n", "nonen", "noo1 neen1", 700),
        ("ด", "d", "dodek", "doo1 dek2", 990),
        ("ต", "t", "totao", "too1 tao2", 990),
        ("ถ", "th", "thothung", "thoo5 thung5", 880),
        ("ท", "th", "thothahan", "thoo1 tha4 haan5", 990),
        ("ธ", "th", "thothong", "thoo1 thong1", 820),
        ("น", "n", "nonu", "noo1 nuu5", 990),
        ("บ", "b", "bobaimai", "boo1 bai1 mai4", 990),
        ("ป", "p", "popla", "poo1 plaa1", 990),
        ("ผ", "ph", "phophueng", "phoo5 phueng3", 880),
        ("ฝ", "f", "fofa", "foo5 faa5", 800),
        ("พ", "ph", "phophan", "phoo1 phaan1", 980),
        ("ฟ", "f", "fofan", "foo1 fan1", 900),
        ("ภ", "ph", "phosamphao", "phoo1 sam5 phao1", 780),
        ("ม", "m", "moma", "moo1 maa4", 990),
        ("ย", "y", "yoyak", "yoo1 yak4", 980),
        ("ร", "r", "roruea", "roo1 ruea1", 990),
        ("ล", "l", "loling", "loo1 ling1", 990),
        ("ว", "w", "wowaen", "woo1 waen5", 990),
        ("ศ", "s", "sosala", "soo5 saa5 laa1", 750),
        ("ษ", "s", "soruesi", "soo5 rueu1 sii5", 700),
        ("ส", "s", "sosuea", "soo5 suea5", 990),
        ("ห", "h", "hohip", "hoo5 hiip2", 990),
        ("ฬ", "l", "lochula", "loo1 chu2 laa1", 350),
        ("อ", "o", "oang", "oo1 aang2", 990),
        ("ฮ", "h", "honokhuk", "hoo1 nok4 huuk3", 700),
    ]

    # 獨立元音與組合元音符號拆字表
    vowels_and_marks = [
        # 元音部件 (可用 sara... 或直接打元音碼)
        ("ะ", "a", 900),
        ("ะ", "saraa", 950),
        ("า", "aa", 990),
        ("า", "saraaa", 990),
        ("ั", "maihanakat", 900),
        ("ั", "hanakat", 900),
        ("ำ", "am", 950),
        ("ำ", "saraam", 950),
        ("ิ", "i", 900),
        ("ิ", "sarai", 950),
        ("ี", "ii", 950),
        ("ี", "saraii", 950),
        ("ึ", "ue", 880),
        ("ึ", "saraue", 900),
        ("ื", "uee", 900),
        ("ื", "sarauee", 900),
        ("ุ", "u", 900),
        ("ุ", "sarau", 950),
        ("ู", "uu", 950),
        ("ู", "sarauu", 950),
        ("เ", "e", 950),
        ("เ", "ee", 980),
        ("เ", "sarae", 950),
        ("แ", "ae", 950),
        ("แ", "saraae", 950),
        ("โ", "o", 900),
        ("โ", "oo", 950),
        ("โ", "sarao", 950),
        ("ใ", "ai", 920),
        ("ใ", "maimuan", 950),
        ("ไ", "ai", 960),
        ("ไ", "maimalai", 950),
        ("ฤ", "rue", 850),
        ("ฤๅ", "ruee", 700),
        ("ฦ", "lue", 500),
        ("ฦๅ", "luee", 400),
        # 聲調符號與控制符 (Tone marks & diacritics)
        ("่", "maiek", 990),
        ("่", "ek", 900),
        ("่", "tone2", 900),
        ("้", "maitho", 990),
        ("้", "tho", 900),
        ("้", "tone3", 900),
        ("๊", "maitri", 990),
        ("๊", "tri", 900),
        ("๊", "tone4", 900),
        ("๋", "maichattawa", 990),
        ("๋", "chattawa", 900),
        ("๋", "tone5", 900),
        ("็", "maitaikhu", 950),
        ("็", "taikhu", 900),
        ("์", "karan", 990),
        ("์", "thanthakhat", 950),
        ("ๆ", "maiyamok", 990),
        ("ๆ", "yamok", 950),
        ("ฯ", "paiyannoi", 950),
        ("ฯลฯ", "la", 980),
        ("ฯลฯ", "paiyanyai", 950),
        ("฿", "baht", 990),
        # 泰文數字 (Thai digits)
        ("๐", "sun", 850),
        ("๑", "nueng", 850),
        ("๒", "song", 850),
        ("๓", "sam", 850),
        ("๔", "si", 850),
        ("๕", "ha", 850),
        ("๖", "hok", 850),
        ("๗", "chet", 850),
        ("๘", "paet", 850),
        ("๙", "kao", 850),
    ]

    lines = [header.strip()]
    for ch, short_code, full_name, spaced_name, weight in consonants:
        lines.append(f"{ch}\t{short_code}\t{weight}")
        lines.append(f"{ch}\t{full_name}\t{weight}")
        lines.append(f"{ch}\t{spaced_name}\t{weight}")

    for ch, code, weight in vowels_and_marks:
        lines.append(f"{ch}\t{code}\t{weight}")

    out_path = ROOT_DIR / "thai_roman.chars.dict.yaml"
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[OK] Wrote {out_path} ({len(lines)} lines)")


def build_words_dict() -> None:
    """從 FastThaiG2P 與 TNC 詞頻構建約 22,000 條高頻核心詞庫。"""
    print("Downloading FastThaiG2P IPA dictionary & TNC word frequencies...")
    with urllib.request.urlopen(IPA_URL, timeout=30) as r:
        ipa_dict: dict[str, str] = json.loads(r.read().decode("utf-8"))

    with urllib.request.urlopen(TNC_URL, timeout=30) as r:
        tnc_lines = r.read().decode("utf-8").splitlines()

    tnc_freq: dict[str, int] = {}
    for line in tnc_lines:
        parts = line.split("\t")
        if len(parts) == 2:
            w, f = parts[0].strip(), int(parts[1])
            tnc_freq[w] = f

    # 手動保底補充核心高頻日常會話與商務短語（確保複合詞即使不在單詞表也必有）
    curated_phrases = [
        ("สวัสดี", "sa2 wat2 dii1", 999999),
        ("สวัสดีครับ", "sa2 wat2 dii1 khrap4", 950000),
        ("สวัสดีค่ะ", "sa2 wat2 dii1 kha3", 950000),
        ("ขอบคุณ", "khoop2 khun1", 999999),
        ("ขอบคุณครับ", "khoop2 khun1 khrap4", 920000),
        ("ขอบคุณค่ะ", "khoop2 khun1 kha3", 920000),
        ("ขอบคุณมาก", "khoop2 khun1 maak3", 900000),
        ("ไม่เป็นไร", "mai3 pen1 rai1", 950000),
        ("ขอโทษ", "khoo5 thoot3", 920000),
        ("ประเทศไทย", "pra2 theet3 thai1", 950000),
        ("กรุงเทพมหานคร", "krung1 theep3 ma4 haa5 na4 khoon1", 920000),
        ("กรุงเทพฯ", "krung1 theep3", 930000),
        ("ภาษาไทย", "phaa1 saa5 thai1", 920000),
        ("ยินดีที่ได้รู้จัก", "yin1 dii1 thii3 dai3 ruu4 chak2", 850000),
        ("เท่าไหร่", "thao3 rai2", 880000),
        ("ห้องน้ำ", "hong3 naam4", 880000),
        ("อร่อย", "a2 roi2", 890000),
        ("สบายดีไหม", "sa2 baai1 dii1 mai5", 860000),
        ("สบายดี", "sa2 baai1 dii1", 880000),
        ("คิดถึง", "khit4 thueng5", 870000),
        ("โชคดี", "chook3 dii1", 860000),
        ("ใบเสนอราคา", "bai1 sa2 noee5 raa1 khaa1", 820000),
        ("ใบแจ้งหนี้", "bai1 chaeng3 nii3", 800000),
        ("บริษัท", "boo1 ri4 sat2", 900000),
        ("ลูกค้า", "luuk3 khaa4", 900000),
    ]

    entries: dict[tuple[str, str], int] = {}
    for w, rom, freq in curated_phrases:
        entries[(w, rom)] = freq

    # 1. 先處理所有在 TNC 語料庫中有真實詞頻的純泰文詞條
    tnc_matched = []
    unmatched = []
    thai_word_re = re.compile(r"^[ก-๙]+$")

    for word, ipa in ipa_dict.items():
        if not thai_word_re.match(word):
            continue
        rom = ipa_word_to_roman(ipa)
        if not rom:
            continue
        # 過濾掉過長（超過 6 個音節）的罕見專有名詞以保持詞庫精煉
        if rom.count(" ") >= 6:
            continue
        if word in tnc_freq:
            tnc_matched.append((word, rom, tnc_freq[word]))
        else:
            unmatched.append((word, rom, 5))

    # 按詞頻降序排列
    tnc_matched.sort(key=lambda x: (-x[2], x[0]))

    # 取全部 TNC 匹配詞條（約 24,000 條，篩除詞頻極低 < 2 的噪音）
    for word, rom, freq in tnc_matched:
        if freq < 2 and len(entries) >= 22000:
            continue
        # 將 TNC 原始詞頻平滑縮放到適合 Rime 的權重區間 (10 ~ 800000)
        weight = min(800000, max(10, freq))
        if (word, rom) not in entries:
            entries[(word, rom)] = weight

    header = """# Rime dictionary
# encoding: utf-8
#
# thai_roman.words - 泰語核心詞彙表
#
# 資料來源：
#   - 朱拉隆功大學泰國國家語料庫 (Thai National Corpus / TNC)
#   - PyThaiNLP & FastThaiG2P IPA 審校詞典
# 編碼格式：RTGS/Paiboon 兼容音節 + 聲調數字 (1-5)

---
name: thai_roman.words
version: "2026.11.12"
sort: by_weight
use_preset_vocabulary: false
...
"""
    sorted_entries = sorted(entries.items(), key=lambda x: (-x[1], x[0][0]))
    lines = [header.strip()]
    for (word, rom), weight in sorted_entries:
        lines.append(f"{word}\t{rom}\t{weight}")

    out_path = ROOT_DIR / "thai_roman.words.dict.yaml"
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    size_kb = out_path.stat().st_size / 1024
    print(
        f"[OK] Wrote {out_path} ({len(sorted_entries)} words, {size_kb:.1f} KB)"
    )


def build_kedmanee_dict() -> None:
    """生成泰國國家標準 TIS 820-2538 (Kedmanee) 鍵位映射詞典。"""
    header = """# Rime dictionary
# encoding: utf-8
#
# thai_kedmanee - 泰國標準 Kedmanee (TIS 820-2538) 鍵盤映射表

---
name: thai_kedmanee
version: "2026.11.12"
sort: original
use_preset_vocabulary: false
...
"""
    # 標準 TIS 820-2538 Kedmanee 鍵盤映射 (US QWERTY 按鍵 -> 泰文字符)
    kedmanee_map = [
        # Number row (Unshifted)
        ("1", "ๅ"),
        ("2", "/"),
        ("3", "-"),
        ("4", "ภ"),
        ("5", "ถ"),
        ("6", "ุ"),
        ("7", "ึ"),
        ("8", "ค"),
        ("9", "ต"),
        ("0", "จ"),
        ("-", "ข"),
        ("=", "ช"),
        # Number row (Shifted)
        ("!", "+"),
        ("@", "๑"),
        ("#", "๒"),
        ("$", "๓"),
        ("%", "๔"),
        ("^", "ู"),
        ("&", "฿"),
        ("*", "๕"),
        ("(", "๖"),
        (")", "๗"),
        ("_", "๘"),
        ("+", "๙"),
        # Top QWERTY row (Unshifted)
        ("q", "ๆ"),
        ("w", "ไ"),
        ("e", "ำ"),
        ("r", "พ"),
        ("t", "ะ"),
        ("y", "ั"),
        ("u", "ี"),
        ("i", "ร"),
        ("o", "น"),
        ("p", "ย"),
        ("[", "บ"),
        ("]", "ล"),
        ("\\", "ฃ"),
        # Top QWERTY row (Shifted)
        ("Q", "๐"),
        ("W", '"'),
        ("E", "ฎ"),
        ("R", "ฑ"),
        ("T", "ธ"),
        ("Y", "ํ"),
        ("U", "๊"),
        ("I", "ณ"),
        ("O", "ฯ"),
        ("P", "ญ"),
        ("{", "ฐ"),
        ("}", ","),
        ("|", "ฅ"),
        # Home row (Unshifted)
        ("a", "ฟ"),
        ("s", "ห"),
        ("d", "ก"),
        ("f", "ด"),
        ("g", "เ"),
        ("h", "้"),
        ("j", "่"),
        ("k", "า"),
        ("l", "ส"),
        (";", "ว"),
        ("'", "ง"),
        # Home row (Shifted)
        ("A", "ฤ"),
        ("S", "ฆ"),
        ("D", "ฏ"),
        ("F", "โ"),
        ("G", "ฌ"),
        ("H", "็"),
        ("J", "๋"),
        ("K", "ษ"),
        ("L", "ศ"),
        (":", "ซ"),
        ('"', "."),
        # Bottom row (Unshifted)
        ("z", "ผ"),
        ("x", "ป"),
        ("c", "แ"),
        ("v", "อ"),
        ("b", "ิ"),
        ("n", "ื"),
        ("m", "ท"),
        (",", "ม"),
        (".", "ใ"),
        ("/", "ฝ"),
        # Bottom row (Shifted)
        ("Z", "("),
        ("X", ")"),
        ("C", "ฉ"),
        ("V", "ฮ"),
        ("B", "ฺ"),
        ("N", "์"),
        ("M", "?"),
        ("<", "ฒ"),
        (">", "ฬ"),
        ("?", "ฦ"),
    ]

    lines = [header.strip()]
    for key, thai_char in kedmanee_map:
        lines.append(f"{thai_char}\t{key}")

    out_path = ROOT_DIR / "thai_kedmanee.dict.yaml"
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[OK] Wrote {out_path} ({len(kedmanee_map)} keys)")


if __name__ == "__main__":
    build_chars_dict()
    build_words_dict()
    build_kedmanee_dict()
