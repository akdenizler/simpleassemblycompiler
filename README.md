# simpleassemblycompiler

# simpleassemblycompiler

Tiny assembler that turns a toy assembly language into 8-bit machine code bytes in the `00AABBCC` format.

- **A** = dest register (00..11)
- **B** = source register (00..11)
- **C** = opcode (00=xor, 01=eq, 10=add, 11=mov)
- Top bits are always `00`
- **Result is stored into register A**

Outputs one **8-bit binary string per line**.

---

## Why this exists

It’s a minimal end-to-end “compiler” (strictly, an assembler) for teaching:
- tokenizing a simple language,
- parsing instructions,
- emitting a fixed binary format.

Speed is not a priority; clarity is.

---

## Instruction Set (ISA)

| Mnemonic | CC | Semantics                                 |
|---------:|:--:|--------------------------------------------|
| `xor`    | 00 | `regA ← regA XOR regB`                    |
| `eq`     | 01 | `regA ← (regA == regB)` (1 if equal else 0) |
| `add`    | 10 | `regA ← regA + regB`                      |
| `mov`    | 11 | `regA ← regB`                             |

**Registers**: `reg0`, `reg1`, `reg2`, `reg3`

**Binary mapping**:
- `reg0` → `00`
- `reg1` → `01`
- `reg2` → `10`
- `reg3` → `11`

**Aliases**:
- `==` is accepted as an alias for `eq`.

---

Notes:
- Comma is optional; if present, it’s ignored by the lexer.
- Comments start with `;` and run to end of line.
- Case-insensitive: everything is lowercased during lexing.

---

## Binary Encoding

Each instruction becomes **one byte**: `00 A A B B C C`


