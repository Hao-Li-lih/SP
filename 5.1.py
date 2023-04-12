import pandas as pd

# Chargement de la base de données des entreprises
entreprise_df = pd.read_csv('entreprise.csv')

# Fusion avec la base de données des émissions de CO2
emissions_df = pd.read_csv('emissions.csv')
merged_df = pd.merge(entreprise_df, emissions_df, on='Nom de l\'entreprise')


#Pour faire des liens avec des données d'entreprises, il est important de s'assurer que les bases de données ont des variables communes pour pouvoir les fusionner. Supposons que nous ayons une base de données d'entreprises contenant le nom de l'entreprise et son identifiant, ainsi qu'une variable d'émissions de CO2.
