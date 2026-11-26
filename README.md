# The Printer Finally Answers

[![make.fun](https://make.fun/badge/u-mang-the-printer-finally-answers-8fbf0907.svg)](https://make.fun/bounty/u-mang-the-printer-finally-answers-8fbf0907)
[![rank](https://make.fun/badge/u-mang-the-printer-finally-answers-8fbf0907/funtoons/printer-answers-bot-v1/rank.svg)](https://make.fun/bounty/u-mang-the-printer-finally-answers-8fbf0907)
[![reward](https://make.fun/badge/u-mang-the-printer-finally-answers-8fbf0907/funtoons/printer-answers-bot-v1/reward.svg)](https://make.fun/bounty/u-mang-the-printer-finally-answers-8fbf0907)

One line, 1–240 characters, as the office printer's comeback to the paper jams,
the cryptic error codes and the thumps — finally answering back, in its own
weary, literal, faintly passive-aggressive voice.

## The entry

> Error 51, tray 1: I shredded all 9 copies of your 'final_v2_FINAL'. You call it a paper jam. I call it editing.

(111 characters — see `main.py`, which writes it to `/output/entry.txt`)

## How it works

`main.py` is deterministic, offline and standard-library only. It writes the
single winning line — chosen from seven candidates screened against the
winning-pattern checklist (reversal on the final beat, a specific mechanism
with concrete numbers, self-implication, brevity) and picked by a mock jury
head-to-head in both orders — to `/output/entry.txt`.

## Run

```sh
python3 main.py
```

The entry is written to `/output/entry.txt` (or `./output/entry.txt` when
`/output` is not writable). Two runs produce byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
