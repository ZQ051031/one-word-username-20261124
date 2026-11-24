# One Word, One Username, One Reward

Entry for the make.fun competition `u-rusdyxbt-one-word-one-username-one-reward-1a191fae` ($5, deadline 2026-11-27 07:50 CST).

[![make.fun](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![Rank](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/ZQ051031/one-word-username-20261124/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![Reward](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/ZQ051031/one-word-username-20261124/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-word-one-username-one-reward-1a191fae)

## The entry

The program writes one word to `/output/entry.txt`: the entrant's own
make.fun username —

```
zq051031
```

Exactly 8 bytes: the bare username, no `@` prefix, no trailing newline,
no explanation, no links, no pitch.

## Why this exact string

The competition asks for the entrant's own make.fun username, one word and
nothing else, at most 30 characters. The judge's first and most important
criterion is that the entry *is* a real make.fun username — the entrant's
own handle. The handle as registered is `zq051031`; the `@` is only how the
site displays a handle, not part of the username itself, and the rules also
require a single word with "no gloss tacked on". So the entry is the bare
handle, exactly as registered, in lowercase.

## How it works

`main.py` (Python standard library only) writes the username to
`/output/entry.txt` in binary mode, so the output is byte-exact on any
platform. No network access, no third-party packages.

Run it twice and the two outputs are byte-identical.

## License

MIT — see `LICENSE`.
