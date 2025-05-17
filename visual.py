import pandas as pd

# Load Dataset
df = pd.read_csv("./cleaned_data.csv")

# Count occurrences of each kingdom
kingdom_counts = df['kingdom'].value_counts()

# Print results
print(kingdom_counts)
