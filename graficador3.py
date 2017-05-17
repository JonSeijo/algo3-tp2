import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data_random = pd.read_csv('experimentos/problema3/random.csv')
tiempos_random = data_random.groupby('n')['tiempo'].mean() / 1000000000



plt.clf()
plot_random = tiempos_random.plot(fontsize = 13)
plot_random.set_title('\n Tiempo medio entre R repeticiones de grafos random \n para diferentes tamaños de grafos', fontsize = 15)
plot_random.set_xlabel("Cantidad de elementos", size = 14)
plot_random.set_ylabel("Segundos", size = 14)



plt.show()

