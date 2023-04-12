import pandas as pd

# Load the data
emissions = pd.read_csv('Emissions.csv')
national_totals = pd.read_csv('NationalTotals.csv')

# Calculate the sum of emissions for each country in the Emissions table
emissions_sum = emissions.groupby(['Country', 'Year'])['Emissions'].sum().reset_index()

# Join the emissions_sum table with the NationalTotals table
national_emissions = pd.merge(emissions_sum, national_totals, on=['Country', 'Year'])

# Check if the total emissions match for each country
for index, row in national_emissions.iterrows():
    if row['Emissions'] != row['Total']:
        print(f"Data integrity check failed for {row['Country']} in year {row['Year']}")
