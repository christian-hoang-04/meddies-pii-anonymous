"""OCR geometry and runtime facade."""

from anonymous_pii.pdf_redaction.ocr_backends import (
    RapidOcrEngineFactory,
    SubprocessTesseractRunner,
)
from anonymous_pii.pdf_redaction.ocr_geometry import RapidOcrAdapter, TesseractTsvAdapter
from anonymous_pii.pdf_redaction.ocr_types import (
    GeometryOcr,
    OcrAdapterError,
    OpenVinoPerformanceHint,
    PixelToPageTransform,
    RapidOcrBackend,
    RapidOcrModelTier,
    RapidOcrRuntimeConfig,
    RasterPage,
    TesseractRunner,
)

__all__ = [
    "GeometryOcr",
    "OcrAdapterError",
    "OpenVinoPerformanceHint",
    "PixelToPageTransform",
    "RapidOcrAdapter",
    "RapidOcrBackend",
    "RapidOcrEngineFactory",
    "RapidOcrModelTier",
    "RapidOcrRuntimeConfig",
    "RasterPage",
    "SubprocessTesseractRunner",
    "TesseractRunner",
    "TesseractTsvAdapter",
]
