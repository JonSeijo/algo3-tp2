import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data_random_todo = pd.read_csv('experimentos/problema2/random_todo.csv')
tiempos_random_todo = data_random_todo.groupby('n')['tiempo'].mean() / 1000000000

data_aristas_minimas = pd.read_csv('experimentos/problema2/aristas_minimas.csv')
tiempos_aristas_minimas = data_aristas_minimas.groupby('n')['tiempo'].mean() / 1000000000

data_aristas_maximas = pd.read_csv('experimentos/problema2/aristas_maximas.csv')
tiempos_aristas_maximas = data_aristas_maximas.groupby('n')['tiempo'].mean() / 1000000000


# Aristas maximas, aristas random y aristas minimas en el mismo grafico
# --------------------------------------------------------------------------------------------------------------------
plt.clf()
plot_aristas_maximas = tiempos_aristas_maximas.plot(fontsize = 13, color='#C44E52') # Color rojo
plot_aristas_maximas.set_title('\n Problema 2 \n Tiempo medio para diferentes tamaños de grafos', fontsize = 15)
plot_aristas_maximas.set_xlabel("Cantidad de elementos", size = 14)
plot_aristas_maximas.set_ylabel("Segundos", size = 14)

tiempos_random_todo.plot(ax=plot_aristas_maximas, color='#4C72B0') # Color azul
tiempos_aristas_minimas.plot(ax=plot_aristas_maximas, color='#55A868') # Color verde

plot_aristas_maximas.legend(['Aristas maximas', 'Aristas random', 'Aristas minimas'], fontsize = 14)

plt.show()
# --------------------------------------------------------------------------------------------------------------------