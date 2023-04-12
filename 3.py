import pandas as pd

# Read CSV file
csv_loader = pd.read_csv('./result.csv')

# Get total emissions from installations (excluding aviation) after ETS and ESD
total_emissions = csv_loader['Total emissions from installations (excluding aviation) after ETS and ESD'].sum()

# Get national total emissions
national_total_emissions = csv_loader['National Total'].sum()

# Check if the total emissions from installations matches the national total emissions
if total_emissions == national_total_emissions:
    print("Data is complete.")
else:
    print("Data is incomplete.")
