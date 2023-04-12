import pandas as pd

# Chargement de la base de données macroéconomiques
macro_df = pd.read_csv('macro.csv')

# Fusion avec la base de données des émissions de CO2
emissions_df = pd.read_csv('emissions.csv')
merged_df = pd.merge(emissions_df, macro_df, on='année')



#Pour faire des liens avec des données macroéconomiques, il est important de s'assurer que les bases de données ont des variables communes pour pouvoir les fusionner. Supposons que nous ayons une base de données de données macroéconomiques contenant une variable d'indicateur économique pour chaque année.
