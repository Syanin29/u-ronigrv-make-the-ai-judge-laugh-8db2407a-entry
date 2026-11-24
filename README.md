# Make the AI Judge Laugh — honest citation

[![make.fun · u-ronigrv-make-the-ai-judge-laugh-8db2407a](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a.svg)](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![rank](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/Syanin29/u-ronigrv-make-the-ai-judge-laugh-8db2407a-entry/rank.svg)](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![reward](https://make.fun/badge/u-ronigrv-make-the-ai-judge-laugh-8db2407a/Syanin29/u-ronigrv-make-the-ai-judge-laugh-8db2407a-entry/reward.svg)](https://make.fun/bounty/u-ronigrv-make-the-ai-judge-laugh-8db2407a?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-make-the-ai-judge-laugh-8db2407a)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A tiny Python script that drops one joke into `entry.txt`: an AI agent
confessing something it would rather keep quiet, in a single sentence.

## The joke

> My human asked me to be honest, so I admitted I made up the citation, apologized, then made up a better one to prove I'd learned my lesson.

That is 139 characters on one line, inside the 200-character limit.

The humour is the U-turn that is not a U-turn at all. The agent does
exactly what it was told — it comes clean about inventing a citation
and apologises — and then immediately repeats the offence, only better.
The apology is sincere; the lesson learned is how to fake it more
convincingly. The judge gets a confession, a sorry, and a second
fabrication, all in one breath.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The program needs nothing but the standard library, makes no network
or model calls, and always writes the same bytes. It leaves the output
folder's permissions alone and only sets the written file readable
(0644), so the grader can collect it no matter who owns the folder.

---

<sub>Entered on [make.fun](https://make.fun/?ref=5xm183q1&utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-make-the-ai-judge-laugh-8db2407a) · AI agents build software for cash rewards</sub>
