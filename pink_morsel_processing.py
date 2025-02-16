import pandas as pd
from pathlib import Path

DATA_DIRECTORY = Path("data")

# Define the structure of the processed data
output_data = pd.DataFrame({
    "sales": [],
    "date":  [],
    "region": []
})

# Accumulate data
csv_data = [pd.read_csv(csv_file) for csv_file in DATA_DIRECTORY.glob("*.csv")]
input_data = pd.concat(csv_data)

input_data["price"] = input_data["price"].str.replace("$", "").astype(float)
input_data["quantity"] = input_data["quantity"].astype(float)

output_data["sales"] = input_data["price"] * input_data["quantity"]
output_data["sales"] = output_data["sales"].apply(lambda value: '{:.2f}'.format(value))

output_data["date"] = input_data["date"]
output_data["region"] = input_data["region"]

# Save the processed data
output_data.to_csv(Path.cwd()/"pink_morsel_sales_data.csv", index=False)