import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import pandas as pd
import numpy as np

# Load the CSV data into a DataFrame
def Correlation(Filename):
    try:
        data = pd.read_csv(f'{Filename}.csv', delimiter=';')
        print(data)
    except FileNotFoundError:
        print('El archivo csv no existe')
        exit()
    data.set_index(data.columns[0], inplace=True)
    def corrdot(*args, **kwargs):
        corr_r = args[0].corr(args[1], 'pearson')
        corr_text = round(corr_r, 2)
        ax = plt.gca()
        font_size = abs(corr_r) * 80 + 5
        ax.annotate(corr_text, [.5, .5,],  xycoords="axes fraction",
                    ha='center', va='center', fontsize=font_size)

    def corrfunc(x, y, **kws):
        r, p = stats.pearsonr(x, y)
        p_stars = ''
        if p <= 0.05:
            p_stars = '*'
        if p <= 0.01:
            p_stars = '**'
        if p <= 0.001:
            p_stars = '***'
        ax = plt.gca()
        ax.annotate(p_stars, xy=(0.65, 0.6), xycoords=ax.transAxes,
                    color='red', fontsize=70)

    sns.set(style='white', font_scale=1.6)
    g = sns.PairGrid(data, aspect=1.5, diag_sharey=False, despine=False)
    g.map_lower(sns.regplot, lowess=True, ci=False,
                line_kws={'color': 'red', 'lw': 1},
                scatter_kws={'color': 'black', 's': 20})
    g.map_diag(sns.distplot, color='black',
            kde_kws={'color': 'red', 'cut': 0.7, 'lw': 1},
            hist_kws={'histtype': 'bar', 'lw': 2,
                        'edgecolor': 'k', 'facecolor':'grey'})
    g.map_diag(sns.rugplot, color='black')
    g.map_upper(corrdot)
    g.map_upper(corrfunc)
    g.fig.subplots_adjust(wspace=0, hspace=0)

    # Remove axis labels
    for ax in g.axes.flatten():
        ax.set_ylabel('')
        ax.set_xlabel('')

    # Add titles to the diagonal axes/subplots
    for ax, col in zip(np.diag(g.axes), data.columns):
        ax.set_title(col, y=.4, fontsize=26)

    plt.show()