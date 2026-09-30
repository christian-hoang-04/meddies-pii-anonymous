#!/usr/bin/env python
"""Build Anonymous Labels span JSONL plus migration audit sidecars."""

from anonymous_pii.training.bioes.data.build_legacy_pii_label_corpus import main

if __name__ == "__main__":
    main()
