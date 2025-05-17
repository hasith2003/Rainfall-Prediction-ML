import pandas as pd

# Load the CSV file
df = pd.read_csv("cleaned_data.csv")

# Create a full set of all (year, month) combinations
all_years = df["Year"].unique()
all_months = range(1, 13)
expected_combinations = {(year, month) for year in all_years for month in all_months}

# Extract actual (year, month) pairs from the dataset
actual_combinations = set(zip(df["Year"], df["Month"]))

# Find missing (year, month) pairs
missing_combinations = expected_combinations - actual_combinations

if missing_combinations:
    print("Missing Year-Month combinations:")
    for year, month in sorted(missing_combinations):
        print(f"Year: {year}, Month: {month}")
else:
    print("No missing months for any year!")
