from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from anonymous_pii.spans import CharSpan
    from anonymous_pii.taxonomy import PiiLabel


class PiiAdapter(Protocol):
    name: str
    supported_labels: frozenset[PiiLabel]

    def load(self) -> None: ...

    def predict(self, texts: list[str]) -> list[list[CharSpan]]: ...
