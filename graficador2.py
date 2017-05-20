import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data_costo_r_existe_r = pd.read_csv('experimentos/problema2/random_todo.csv')
tiempos_cr_er = data_costo_r_existe_r.groupby('n')['tiempo'].mean() / 1000000000


plt.clf()
plot_cr_er = tiempos_cr_er.plot(fontsize = 13)
plot_cr_er.set_title('\n Problema 2 \n Tiempo medio entre R repeticiones de grafos Random \n para diferentes tamaños de grafos', fontsize = 15)
plot_cr_er.set_xlabel("Cantidad de elementos", size = 14)
plot_cr_er.set_ylabel("Segundos", size = 14)
plt.show()

# fig, axes = plt.subplots(nrows=2, ncols=2)
# fig.subplots_adjust(hspace=.7, wspace=.7)
# tiempos_cr_er.plot(ax=axes[0,0]); axes[0,0].set_title('\nCosto Random - Existe Random');
# tiempos_ci_er.plot(ax=axes[0,1]); axes[0,1].set_title('\nCosto Igual - Existe Random');
# tiempos_ci_es.plot(ax=axes[1,0]); axes[1,0].set_title('\nCosto Igual - Existe Si');
# tiempos_ci_en.plot(ax=axes[1,1]); axes[1,1].set_title('\nCosto Igual - Existe No');

# for i in range(0, 2):
#     for j in range(0, 2):
#         axes[i,j].set_ylabel("Segundos")
#         axes[i,j].set_xlabel("Cantidad de nodos")

# plt.show()

