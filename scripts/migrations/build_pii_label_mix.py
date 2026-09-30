#!/usr/bin/env python
"""Build a mixed Anonymous Labels JSONL bundle: medical anchor plus general-domain PII."""

from anonymous_pii.training.bioes.data.mixed_build import main

if __name__ == "__main__":
    main()
