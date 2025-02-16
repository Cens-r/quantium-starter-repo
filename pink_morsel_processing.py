import pandas as pd
from pathlib import Path

DATA_DIRECTORY = Path("data")
OUTPUT_FILE_PATH = Path("pink_morsel_sales_data.csv")

def get_pink_morsel_data(update=True):
    # Support reuse of existing pink morsel data
    if (not update) and OUTPUT_FILE_PATH.exists():
        return pd.read_csv(OUTPUT_FILE_PATH)

    # Define the structure of the processed data
    output_data = pd.DataFrame({
        "sales": [],
        "date": [],
        "region": []
    })

    # Accumulating the input data
    csv_data = [pd.read_csv(csv_file) for csv_file in DATA_DIRECTORY.glob("*.csv")]
    input_data = pd.concat(csv_data)

    # Cleaning up the input data
    input_data["price"] = input_data["price"].str.replace("$", "").astype(float)
    input_data["quantity"] = input_data["quantity"].astype(float)

    # Populating the input data into the output dataframe
    output_data["sales"] = input_data["price"] * input_data["quantity"]
    output_data["sales"] = output_data["sales"].round(2)
    output_data["date"] = input_data["date"]
    output_data["region"] = input_data["region"]

    # Save the processed data
    output_data.to_csv(OUTPUT_FILE_PATH, index=False, mode="w+")
    return output_data

if __name__ == "__main__":
    get_pink_morsel_data()