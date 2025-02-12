import numpy as np
from scipy.spatial.distance import pdist

# --- 1. Création de la matrice 15x15 ---
matrix = np.zeros((15, 15), dtype=int)

# Dessiner la lettre 'J'
matrix[0:8, 2] = 1  # Trait vertical
matrix[8, 1:4] = 1  # Base
matrix[7, 1] = 1    # Courbe

# Dessiner la lettre 'V'
for i in range(9):  
    matrix[i, 6] = 1   # Partie gauche du 'V'
    matrix[i, 10] = 1  # Partie droite du 'V'
matrix[9, 7] = 1
matrix[10, 8] = 1
matrix[9, 9] = 1

# --- 2. Calculs demandés ---
# Colonnes contenant au moins un 1
cols_with_ones = (matrix.sum(axis=0) > 0)
mean_ones_per_col = matrix[:, cols_with_ones].sum() / cols_with_ones.sum()

# Lignes contenant au moins un 1
rows_with_ones = (matrix.sum(axis=1) > 0)
mean_ones_per_row = matrix[rows_with_ones, :].sum() / rows_with_ones.sum()

# Hauteur et largeur des lettres
j_height = np.sum(matrix[:, 2])  # Hauteur = nombre de 1 sur une colonne de 'J'
j_width = np.max(np.sum(matrix[:9, 1:4], axis=0))  # Largeur max
v_height = np.max(np.sum(matrix[:, [6, 10]], axis=0))  # Hauteur = max de colonnes de 'V'
v_width = np.max(np.sum(matrix[9:11, 7:9], axis=1))  # Largeur max

# Vérifier les colonnes et lignes dupliquées
unique_cols = np.unique(matrix, axis=1).shape[1] < matrix.shape[1]
unique_rows = np.unique(matrix, axis=0).shape[0] < matrix.shape[0]

# Distance maximale entre les '1' (Euclidienne)
ones_positions = np.argwhere(matrix == 1)
max_euclidean_dist = np.max(pdist(ones_positions, metric='euclidean'))

# --- 3. Affichage des résultats ---
print("Матрица 15x15:")
print(matrix)

print("\nСреднее количество единиц в столбцах:", mean_ones_per_col)
print("Среднее количество единиц в строках:", mean_ones_per_row)
print(f"Высота J: {j_height}, Ширина J: {j_width}")
print(f"Высота V: {v_height}, Ширина V: {v_width}")
print("Повторяющиеся столбцы:", unique_cols)
print("Повторяющиеся строки:", unique_rows)
print("Максимальное расстояние по Евклиду между единицами:", max_euclidean_dist)
