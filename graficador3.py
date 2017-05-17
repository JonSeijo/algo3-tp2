import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data_costo_r_existe_r = pd.read_csv('experimentos/problema3/costo_random_existe_random.csv')

tiempos_cr_er = data_costo_r_existe_r.groupby('n')['tiempo'].mean() / 1000000000

plt.clf()
plot_cr_er = tiempos_cr_er.plot(fontsize = 13)
plot_cr_er.set_title('\n Tiempo medio entre R repeticiones de grafos random \n para diferentes tamaños de grafos', fontsize = 15)
plot_cr_er.set_xlabel("Cantidad de elementos", size = 14)
plot_cr_er.set_ylabel("Segundos", size = 14)

plt.show()