# evaldiff

Diff two LLM eval runs and score the delta.

## Install
```bash
pip install evaldiff
```

## Usage
```bash
evaldiff baseline.json candidate.json
```

Machine-readable output for CI:
```bash
evaldiff baseline.json candidate.json --json
```

## Why
Comparing eval runs by hand is slow and error-prone. evaldiff gives you a scored, colorized diff in one command.

Built by [@ayaqen](https://github.com/ayaqen).
