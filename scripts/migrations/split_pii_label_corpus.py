#!/usr/bin/env python
"""Split a Anonymous Labels JSONL bundle into no-leakage train/validation splits."""

from anonymous_pii.training.bioes.data.splits import main

if __name__ == "__main__":
    main()
