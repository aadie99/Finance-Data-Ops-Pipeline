from pathlib import Path
import pandas as pd


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace(".", "_", regex=False)
    )
    return df


def run_basic_validations(df: pd.DataFrame) -> None:
    print("\n--- VALIDATION SUMMARY ---")

    row_count = len(df)
    print(f"Row count: {row_count}")

    null_counts = df.isnull().sum()
    print("\nNull counts by column:")
    print(null_counts[null_counts > 0] if null_counts.sum() > 0 else "No null values found.")

    duplicate_count = df.duplicated(subset=["id"]).sum()
    print(f"\nDuplicate ID count: {duplicate_count}")

    if "default_payment_next_month" in df.columns:
        default_rate = df["default_payment_next_month"].mean() * 100
        print(f"\nDefault rate: {default_rate:.2f}%")
    else:
        print("\nTarget column not found after renaming.")


def main() -> None:
    input_path = Path("dataset/UCI_Credit_Card.csv")
    output_dir = Path("data/processed")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / "uci_credit_card_clean.csv"

    print("Reading raw dataset...")
    df = pd.read_csv(input_path)

    print("Standardizing column names...")
    df = standardize_column_names(df)

    print("\nColumns after standardization:")
    print(df.columns.tolist())

    run_basic_validations(df)

    print("\nSaving cleaned dataset...")
    df.to_csv(output_path, index=False)

    print(f"Cleaned file saved to: {output_path}")


if __name__ == "__main__":
    main()