import pandas as pd

# Load the dataset
df = pd.read_csv("cleaned_data.csv")

# Calculate overall variance of Rain_Amount
overall_variance = df["Radiation"].var()

# Calculate variance per kingdom
variance_per_kingdom = df.groupby("kingdom")["Radiation"].var()

# Display results
print(f"Overall Rain Amount Variance: {overall_variance}\n")
print("Variance of Rain Amount per Kingdom:")
print(variance_per_kingdom)
