"""Metrics registry placeholder. No runtime behavior changes."""

class MetricsRegistry:
    def counter(self, name: str, **kwargs):
        return None

    def histogram(self, name: str, **kwargs):
        return None
