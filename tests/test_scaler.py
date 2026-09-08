import pandas as pd

from src.scaler import scale_features


def test_scale_features_preserves_shape_and_columns():
    data = pd.DataFrame({"a": [1, 2, 3], "b": [10, 20, 30]})

    scaled, _ = scale_features(data)

    assert scaled.shape == data.shape
    assert list(scaled.columns) == ["a", "b"]
