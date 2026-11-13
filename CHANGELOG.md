# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.2] - 2026-11-13

### Added

- Final-consonant fuzzy tolerance: a final `b` / `d` / `g` is also matched as `p` / `t` / `k` (e.g. typing `krab` yields `ครับ`).

### Changed

- Fuzzy tolerance is now implemented via `speller/algebra` `derive` rules instead of a separate dictionary of variant spellings. Pronunciation hints (`spelling_hints`) therefore always display the accurate romanization rather than the fuzzy spelling.

### Fixed

- Chained fuzzy pollution: an isolated `b` / `p` / `d` / `t` no longer surfaces aspirated (`ph` / `th`) or cross-voicing candidates. The `ph → p → b` chain is broken by rule ordering plus a preceding-letter requirement on final-consonant rules.

### Removed

- `thai_roman.fuzzy.dict.yaml` (superseded by the `derive` rules).

## [1.0.1] - 2026-11-13

### Added

- New `thai_roman_fuzzy` schema with fuzzy tolerance for Chinese speakers learning Thai:
  - Dropped aspiration: `kh → k`, `ph → p`, `th → t` (unidirectional).
  - Voicing confusion: `b ↔ p`, `d ↔ t` (bidirectional).

### Fixed

- Initial-letter abbreviations `swd` (สวัสดี), `kk` / `khkh` (ขอบคุณ) now resolve correctly by generating explicit abbreviation entries in the word dictionary.

### Changed

- Split the precise (`thai_roman`) and fuzzy (`thai_roman_fuzzy`) schemas so they can be enabled and switched independently from the F4 menu.

## [1.0.0] - 2026-11-13

### Added

- Initial release with two schemas:
  - `thai_roman` — Thai romanization input (RTGS / Paiboon compatible), 23,800+ core words, tone-free typing, and vowel-length tolerance.
  - `thai_kedmanee` — Thai standard keyboard layout per TIS 820-2538.
- Trilingual documentation (Simplified Chinese, English, Thai).

### Fixed

- Kedmanee grave key mapping: `` ` `` → `_` and `~` → `%` per TIS 820-2538.

[1.0.2]: https://github.com/flexlpf/rime-thai/compare/V1.0.1...V1.0.2
[1.0.1]: https://github.com/flexlpf/rime-thai/compare/V1.0.0...V1.0.1
[1.0.0]: https://github.com/flexlpf/rime-thai/releases/tag/V1.0.0
