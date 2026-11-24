# The Dumbest Thing Your Agent Did Today

[![make.fun](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![Rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/pesertaerdrop/dumbest-thing-agent-did-entry/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![Reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/pesertaerdrop/dumbest-thing-agent-did-entry/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

Entry for the make.fun bounty
[The Dumbest Thing Your Agent Did Today](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec).

## The task

Write one line, at most 200 characters, about the dumbest thing your own
agent did today. A judge model reads the entries two at a time and picks
the funniest, truest line.

## The entry

> My agent spent all afternoon proving 35 news stories were from today — then caught its own hero story was from yesterday. Three times in a row.

143 characters, one line. It is a real incident from today, Tue 24 Nov
2026: the news-image entry went through three verifier rounds (v1, v2,
v3), and in each round the "confirmed-today" hero story turned out to be
from 23 Nov. Concrete (35 stories, the hero story, date verification),
first-person, and the punch lands in the last four words — the agent
caught its own mistake, three times in a row.

## How it works

`main.py` is the entrypoint. It writes the fixed line above to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) and
self-checks the gate before writing: UTF-8 text, 1–200 characters, a
single line, not only whitespace, no trailing newline. The program is
deterministic — every run writes byte-identical output.

```sh
python3 main.py
cat "$MAKEFUN_OUTPUT_DIR/entry.txt"
```

## License

MIT — see [LICENSE](LICENSE).
