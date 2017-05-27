import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data_costo_r_existe_r = pd.read_csv('experimentos/problema3/costo_random_existe_random.csv')
tiempos_cr_er = data_costo_r_existe_r.groupby('n')['tiempo'].mean() / 1000000000

data_costo_i_existe_r = pd.read_csv('experimentos/problema3/costo_igual_existe_random.csv')
tiempos_ci_er = data_costo_i_existe_r.groupby('n')['tiempo'].mean() / 1000000000

data_costo_i_existe_s = pd.read_csv('experimentos/problema3/costo_igual_existe_si.csv')
tiempos_ci_es = data_costo_i_existe_s.groupby('n')['tiempo'].mean() / 1000000000

data_costo_i_existe_n = pd.read_csv('experimentos/problema3/costo_igual_existe_no.csv')
tiempos_ci_en = data_costo_i_existe_n.groupby('n')['tiempo'].mean() / 1000000000

# plt.clf()
# plot_cr_er = tiempos_cr_er.plot(fontsize = 13)
# plot_cr_er.set_title('\n Tiempo medio entre R repeticiones de grafos con Costo Random y Existencia Random \n para diferentes tamaños de grafos', fontsize = 15)
# plot_cr_er.set_xlabel("Cantidad de elementos", size = 14)
# plot_cr_er.set_ylabel("Segundos", size = 14)
# plt.show()

fig, axes = plt.subplots(nrows=2, figsize=(13,10), ncols=2)
fig.subplots_adjust(hspace=.3, wspace=.3)
tiempos_cr_er.plot(ax=axes[0,0]); axes[0,0].set_title('\nCostos: Random - Existencia: Random');
tiempos_ci_er.plot(ax=axes[0,1]); axes[0,1].set_title('\nCostos: Igual - Existencia: Random');
tiempos_ci_es.plot(ax=axes[1,0]); axes[1,0].set_title('\nCostos: Igual - Existencia: Todas');
tiempos_ci_en.plot(ax=axes[1,1]); axes[1,1].set_title('\nCostos: Igual - Existencia: Ninguna');

for i in range(0, 2):
    for j in range(0, 2):
        axes[i,j].set_ylabel("Segundos")
        axes[i,j].set_xlabel("Cantidad de nodos")

plt.show()

