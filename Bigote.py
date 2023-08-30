import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def Bigote(Filename):
    try:
        df = pd.read_csv(f'{Filename}.csv', delimiter=';')
    except FileNotFoundError:
        print('El archivo csv no existe')
        exit()
    sns.set(font_scale=1.6)
    sns.boxplot(data=df, width=0.5,fliersize=5)
    plt.show()