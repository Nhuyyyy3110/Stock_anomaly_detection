"""Run the stock anomaly detection pipeline."""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent


def main() -> None:
    """Entry point for the pipeline scaffold."""
    print(f"Project root: {PROJECT_ROOT}")
    print("Pipeline scaffold created. Add processing steps in src/.")


if __name__ == "__main__":
    main()
