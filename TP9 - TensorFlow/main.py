import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

# Chargement des données depuis le fichier Excel
data_2018 = pd.read_excel("DAT_XLSX_EURUSD_M1_2018.xlsx", header=None)
data_2019 = pd.read_excel("DAT_XLSX_EURUSD_M1_2019.xlsx", header=None)

# Concaténation des données de 2018 et 2019
data = pd.concat([data_2018, data_2019], ignore_index=True)

# Sélection de la quatrième colonne (indice 3) correspondant à la clôture (close)
close_prices = data.iloc[:, 3].values

# Création des étiquettes (direction du cours)
labels = np.where(close_prices[1:] > close_prices[:-1], 1, 0)

# Division des données en ensembles d'apprentissage et de test
X_train, X_test, y_train, y_test = train_test_split(close_prices[:-1], labels, test_size=0.2, random_state=42)

# Fonction pour prédire la direction du cours en se basant sur la tendance précédente
def naive_model_predictions(prices):
    predictions = []
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            predictions.append(1)  # La tendance est à la hausse
        else:
            predictions.append(0)  # La tendance est à la baisse
    return predictions

# Prédictions du modèle naïf sur les données de test
naive_predictions = naive_model_predictions(X_test)

# Calcul du taux de réussite
accuracy = np.sum(naive_predictions == y_test[:-1]) / len(y_test[:-1])
print(f"Taux de réussite du modèle naïf : {accuracy * 100:.2f}%")
