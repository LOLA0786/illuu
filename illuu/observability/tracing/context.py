"""Tracing context placeholder. No runtime behavior changes."""

TRACEPARENT_HEADER = "traceparent"
TRACESTATE_HEADER = "tracestate"


def extract_trace_headers(headers: dict) -> dict:
    return {
        TRACEPARENT_HEADER: headers.get(TRACEPARENT_HEADER),
        TRACESTATE_HEADER: headers.get(TRACESTATE_HEADER),
    }
