from pathlib import Path
import pandas as pd

BASE = Path("data")
SOURCE_FOLDERS = ["Testing data", "Training data"]
OUTPUT_ROOT = BASE / "clean"


def clean_csv(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path, index_col=False)

    # turn blank strings into missing values
    df = df.replace(r"^\s*$", pd.NA, regex=True)

    # remove rows where every value is empty
    df = df.dropna(axis=0, how="all")

    # remove columns where every value is empty
    df = df.dropna(axis=1, how="all")

    return df


def main():
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

    for source_name in SOURCE_FOLDERS:
        source_root = BASE / source_name

        if not source_root.exists():
            print(f"Skipped missing folder: {source_root}")
            continue

        for csv_path in source_root.rglob("*.csv"):
            relative_path = csv_path.relative_to(source_root)
            output_path = OUTPUT_ROOT / source_name / relative_path

            output_path.parent.mkdir(parents=True, exist_ok=True)

            try:
                cleaned_df = clean_csv(csv_path)
                cleaned_df.to_csv(output_path, index=False)
                print(f"Saved: {output_path}")
            except Exception as e:
                print(f"Failed on {csv_path}: {e}")


if __name__ == "__main__":
    main()