import pandas as pd

# Chargement de la base de données des prix du carbone
prix_df = pd.read_csv('prix_carbone.csv')

# Calcul du prix moyen du carbone pour chaque année
prix_moyen_df = prix_df.groupby('année')['prix_carbone'].mean().reset_index()

# Fusion avec la base de données des transactions de carbone
transactions_df = pd.read_csv('transactions_carbone.csv')
merged_df = pd.merge(transactions_df, prix_moyen_df, on='année')



#Pour faire des liens avec des données de prix du carbone, il est possible de lier la base de données des transactions de carbone avec la base de données des prix. Supposons que nous ayons une base de données des prix contenant les prix du carbone pour chaque année.
