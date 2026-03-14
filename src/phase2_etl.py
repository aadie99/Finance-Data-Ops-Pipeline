import pandas as pd
import logging
from pathlib import Path
import traceback

# Create outputs directory if it doesn't exist
log_dir = Path("outputs")
log_dir.mkdir(exist_ok=True)

log_file = log_dir / "pipeline.log"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# File handler (writes to log file)
file_handler = logging.FileHandler(log_file, mode="w")
file_handler.setLevel(logging.INFO)

# Console handler (shows logs in terminal)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Log format
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace(".", "_", regex=False)
    )
    return df


def run_basic_validations(df):

    row_count = len(df)
    null_counts = df.isnull().sum()
    duplicate_count = df.duplicated(subset=["id"]).sum()

    default_rate = df["default_payment_next_month"].mean() * 100

    summary = f"""
--- VALIDATION SUMMARY ---

Row count: {row_count}

Null counts by column:
{null_counts[null_counts > 0] if null_counts.sum() > 0 else "No null values found."}

Duplicate ID count: {duplicate_count}

Default rate: {default_rate:.2f}%
"""

    return summary

def main() -> None:

    try:   
        logging.info("----- Pipeline Run Started -----") 
        input_path = Path("data/raw/UCI_Credit_Card.csv")
        output_dir = Path("data/processed")
        output_dir.mkdir(parents=True, exist_ok=True) 

        summary_path = Path("outputs/validation_summary.txt")
        output_path = output_dir / "uci_credit_card_clean.csv"

        logging.info("Reading raw dataset...")
        df = pd.read_csv(input_path)

        logging.info("Standardizing column names...")
        df = standardize_column_names(df)

        logging.info("Columns after standardization:")
        logging.info(df.columns.tolist())

        logging.info("Running basic validations...")
        validation_summary = run_basic_validations(df)

        summary_path.write_text(validation_summary, encoding="utf-8")
        logging.info(f"Validation summary saved to: {summary_path}")

        logging.info("Saving cleaned dataset...")
        df.to_csv(output_path, index=False)
        logging.info(f"Cleaned file saved to: {output_path}")

        logging.info("----- Pipeline Run Finished -----")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")
        logging.error(traceback.format_exc())

if __name__ == "__main__":
    main()
