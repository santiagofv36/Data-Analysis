
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Importar datos
def ACP(Filename):
    try:
        data = pd.read_csv(f'{Filename}.csv', sep=';')
    except FileNotFoundError:
        print('El archivo csv no existe')
        exit()
    # Eliminar la columna de nombres de los estudiantes
    data = data.drop(data.columns[0], axis=1)

    # Escalar los datos
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)

    # Calcular los componentes principales
    pca = PCA()
    pca.fit(data_scaled)
    pca_data = pca.transform(data_scaled)

    # Gráfico de la varianza explicada por cada componente principal
    per_var = np.round(pca.explained_variance_ratio_ * 100, decimals=1)

    labels = [f'PC{str(x)}' for x in range(1, len(per_var)+1)]
    plt.bar(x=range(1, len(per_var)+1), height=per_var, tick_label=labels)
    plt.ylabel('Percentage of Explained Variance')
    plt.xlabel('Componentes Principales')
    plt.title(' Gráfico de la varianza explicada por cada componente principal ')
    plt.show()

    # Biplot
    plt.scatter(pca_data[:, 0], pca_data[:, 1], alpha=0.3)
    plt.xlabel(f'PC1 ({str(per_var[0])}%)')
    plt.ylabel(f'PC2 ({str(per_var[1])}%)')

    for i, feature in enumerate(data.columns):
        plt.arrow(0, 0, pca.components_[0, i], pca.components_[1, i], 
                head_width=0.1, head_length=0.1, linewidth=2, color='red')
        plt.text(pca.components_[0, i]*1.15, pca.components_[1, i]*1.15, feature, 
                fontsize=12, color='black')

    plt.show()