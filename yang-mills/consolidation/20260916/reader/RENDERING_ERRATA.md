# Reader rendering record

This record describes presentation changes made only in the generated reader.
The original mathematical Markdown files remain byte-for-byte unchanged and
are identified by their source SHA-256 hashes in `CHAPTER_MANIFEST.json`.

## B32: repair of malformed TeX in the displayed adjacency sum

Source: `yang-mills/continuations/20260915-gauge-native-band/BAND_AND_CERTIFICATE.md`, equation B32.

The source contains the following malformed TeX substring. Its line break is
shown explicitly in this literal block:

```text
p\ {
m in\ plane}\p\sim q
```

The generated TeX renders that substring as:

```tex
p\ {\rm in\ plane}\\p\sim q
```

Thus the summation subscript is displayed on two lines: the plaquette is in
the stated plane, and it is adjacent to the external plaquette. This is the
index set specified by the surrounding compression and complementary-coupling
formula. No coefficient, operator, sign, adjacency condition, or mathematical
claim is changed. The bounded gauge-native audit independently records this
same source-formatting defect. The assembled Markdown retains the malformed
source string; the repair occurs only in the Pandoc presentation tree.

## Typographic treatment of retained source formulas

Original TeX display formulas are scaled down only if they exceed the available
line width, with their original equation tags retained. Whitespace that would
create an empty paragraph inside a boxed equation is removed during rendering.
Comma-separated inline coefficient lists may break across lines inside table
columns. Original plain-text formulas are retained as plain text, with line
wrapping in monospaced blocks and long inline literals. Wrapping inserts no
mathematical operation, renaming, or coordinate change.

The generated TeX is editable and the builder is rerunnable. The chapter
manifest is the authority for which source version each chapter reproduces.
