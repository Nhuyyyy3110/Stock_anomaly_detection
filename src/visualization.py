"""Reusable plotting helpers."""

import matplotlib.pyplot as plt
import pandas as pd


def plot_series(data: pd.Series, title: str = "") -> plt.Axes:
    """Plot a pandas series and return its axes."""
    figure, axes = plt.subplots()
    data.plot(ax=axes)
    axes.set_title(title)
    figure.tight_layout()
    return axes
