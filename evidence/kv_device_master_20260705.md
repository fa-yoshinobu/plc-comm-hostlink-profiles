# KEYENCE KV Host Link Device Master 2026-07-05

## Scope

Authoritative master list of KEYENCE KV Host Link devices: official device name,
device code (hex), default device-number range, data width, default data format,
bit-access support, and model-specific notes. Used as the primary source of truth
for `device-ranges/kv_device_ranges.json` rows, `device_name` labels, and the
device sets recognized by the downstream parsers.

## Sources

| Manual | File | Role |
| --- | --- | --- |
| KV-XLE02 Ethernet Unit User's Manual (L64GB) | Maintainer-local PDF copy (not tracked) | Host Link chapter 13 device-name table, XYM expression table (13-33). Older unit: does **not** support CTH/CTC, so they are absent from its tables. |
| KV-8000/7000/5000/3000 CPU User's Manual (O30GB) | Maintainer-local PDF copy (not tracked) | Confirms CTH=04H / CTC=05H (High-speed counter / comparator) and per-model / per-unit availability. |

## Host Link Device Master (native expression)

"Default value" is the device's native type per the manual (not the only
accessible width). "Bit access" is the *Bit* specify-format column (single-bit /
contact). See the data-format note below: every device also accepts Word and
2-word specification (batch access).

| Device name | Code | Range (default) | Default value | Format | Bit access | Model notes |
| --- | --- | --- | --- | --- | --- | --- |
| Relay | R | 00H | 00000 to 199915 | Bit | - | Yes | KV-7000 CPU ver. <= 2.2: 00000 to 99915 |
| Link relay | B | 1BH | 0000 to 7FFF | Bit | - | Yes | |
| Internal auxiliary relay | MR | 11H | 00000 to 399915 | Bit | - | Yes | |
| Latch relay | LR | 12H | 00000 to 99915 | Bit | - | Yes | |
| Control relay | CR | 01H | 0000 to 7915 | Bit | - | Yes | |
| Work relay | VB | 14H | 0000 to F9FF | Bit | - | Yes | KV-8000/7000 only |
| Data memory | DM | 06H | 00000 to 65534 | Word | .U | No | |
| Extended data memory | EM | 17H | 00000 to 65534 | Word | .U | No | |
| File register | FM | 19H | 00000 to 32767 | Word | .U | No | |
| File register | ZF | 2CH | 000000 to 524287 | Word | .U | No | |
| Link register | W | 1CH | 0000 to 7FFF | Word | .U | No | EtherNet/IP table labels this "Link relay" |
| Temporary data memory | TM | 08H | 000 to 511 | Word | .U | No | |
| Index register | Z | 30H | 01 to 10 | 2-word | - | No | KV-8000/7000: 01 to 12 |
| Timer | T | 02H | 0000 to 3999 | 2-word | .D | Yes | |
| Timer (current value) | TC | 20H | 0000 to 3999 | 2-word | .D | No | Same instance space as T |
| Timer (set value) | TS | 21H | 0000 to 3999 | 2-word | .D | No | Same instance space as T |
| Counter | C | 03H | 0000 to 3999 | 2-word | .D | Yes | |
| Counter (current value) | CC | 22H | 0000 to 3999 | 2-word | .D | No | Same instance space as C |
| Counter (set value) | CS | 23H | 0000 to 3999 | 2-word | .D | No | Same instance space as C |
| High-speed counter | CTH | 04H | 0 to 3 (model dep.) | 2-word | .D | - | Availability is unit x CPU dependent; KV-XLE02 unsupported. KV-nano 0-3; upper models reduced or unsupported |
| High-speed counter comparator | CTC | 05H | 0 to 7 (model dep.) | 2-word | .D | - | Same availability rules as CTH |
| Digital trimmer | AT | 26H | 0 to 7 | 2-word | .D | No | KV-8000/7000 only |
| Control memory | CM | 07H | 0000 to 7599 | Word | .U | No | KV-7000: 0000 to 5999 |
| Work memory | VM | 1EH | 00000 to 589823 | Word | .U | No | KV-8000/7000 only; KV-7000: 00000 to 50999 |

Notes:
- **Data formats (batch access).** The manual's device table separates the
  *Default value* (native type) from the specifiable data formats (*Word* /
  *2-word* / *Bit* columns). **Every device supports Word and 2-word
  specification**, so a bit device such as `R` can be read/written 16 bits at a
  time (Word) or 32 bits (2-word) as a batch. This does **not** make `R` a word
  device -- its native type is still Bit. The *Bit access* column above reflects
  only whether single-bit (contact) specification is allowed (bit devices and the
  `T`/`C` contacts). Do not treat the "Word: Yes" batch capability as evidence of
  native width.
- A single timer instance `Tn` has three elements addressed by distinct device
  names: contact (`T`, bit), current value (`TC`, word), set value (`TS`, word).
  Counter `Cn` likewise: `C` / `CC` / `CS`. Therefore `TC`/`TS` share the exact
  instance range of `T`, and `CC`/`CS` share that of `C` (no separate range).
- `T` and `C` support bit access (contact); the current/set value devices do not.

## XYM Expression (13-33)

Relay, internal auxiliary relay, latch relay, data memory, extended data memory,
and file register can also be addressed with MELSEC-style XYM device letters.

| KEYENCE device | KEYENCE expr | XYM expr | XYM range |
| --- | --- | --- | --- |
| Relay | R | X and Y | 0000 to 1999F (KV-7000 CPU ver. <= 2.2: 0000 to 999F) |
| Internal auxiliary relay | MR | M | 00000 to 63999 |
| Latch relay | LR | L | 00000 to 15999 |
| Data memory | DM | D | 00000 to 65534 |
| Extended data memory | EM | E | 00000 to 65534 |
| File register | FM | F | 00000 to 32767 |

## Reconciliation with current implementation and catalog (2026-07-05)

| Device set | In parser (`device.py` etc.) | In catalog (`kv_device_ranges.json`) |
| --- | --- | --- |
| `TC` / `TS` / `CC` / `CS` | Present (0-3999 flat envelope) | **Absent** |
| `CTH` / `CTC` | **Absent** | Present (per-model, `-` where unsupported) |

Both gaps are addressed by the drift-resolution GOAL: add `TC`/`TS`/`CC`/`CS`
rows to the catalog (ranges mirroring `T`/`C` per model) and add `CTH`/`CTC`
(codes 04H/05H) to the parsers (max envelope; per-model availability stays in the
catalog). Representation follows the family convention (flat `device_type` rows,
matching SLMP's `TS`/`TC`/`TN`/`CS`/`CC`/`CN`). Device-letter meanings are per the
KEYENCE definitions above and are not shared with SLMP's identical spellings.

## Live communication

No live PLC communication was performed. This record is a documentation source
derived from the two KEYENCE manuals cited above.
