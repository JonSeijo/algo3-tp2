import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data_random_todo = pd.read_csv('experimentos/problema1/arista_random_premium_random.csv')
tiempos_random_todo = data_random_todo.groupby('n')['tiempo'].mean() / 1000000000

data_premium_minimas = pd.read_csv('experimentos/problema1/arista_random_premium_minimas.csv')
tiempos_premium_minimas = data_premium_minimas.groupby('n')['tiempo'].mean() / 1000000000

data_premium_maximas = pd.read_csv('experimentos/problema1/arista_random_premium_maximas.csv')
tiempos_premium_maximas = data_premium_maximas.groupby('n')['tiempo'].mean() / 1000000000

data_premium_25 = pd.read_csv('experimentos/problema1/arista_random_premium_25.csv')
tiempos_premium_25 = data_premium_25.groupby('n')['tiempo'].mean() / 1000000000

data_premium_10 = pd.read_csv('experimentos/problema1/arista_random_premium_10.csv')
tiempos_premium_10 = data_premium_10.groupby('n')['tiempo'].mean() / 1000000000

data_premium_3 = pd.read_csv('experimentos/problema1/arista_random_premium_3.csv')
tiempos_premium_3 = data_premium_3.groupby('n')['tiempo'].mean() / 1000000000

data_premium_0_5 = pd.read_csv('experimentos/problema1/arista_random_premium_0_5.csv')
tiempos_premium_0_5 = data_premium_0_5.groupby('n')['tiempo'].mean() / 1000000000


# Premium maximas, premium random y premium minimas en el mismo grafico
# --------------------------------------------------------------------------------------------------------------------
plt.clf()
plot_premium_maximas = tiempos_premium_maximas.plot(fontsize = 13, color='#C44E52') # Color rojo
plot_premium_maximas.set_title('\n Problema 1 \n Aristas random, K random \n Tiempo medio para diferentes tamaños de grafos', fontsize = 15)
plot_premium_maximas.set_xlabel("Cantidad de elementos", size = 14)
plot_premium_maximas.set_ylabel("Segundos", size = 14)

tiempos_random_todo.plot(ax=plot_premium_maximas, color='#4C72B0') # Color azul
tiempos_premium_25[:30].plot(ax=plot_premium_maximas, color='#C422C4') # Color violeta
tiempos_premium_10.plot(ax=plot_premium_maximas, color='#C4C422') # Color amarillo
tiempos_premium_3.plot(ax=plot_premium_maximas, color='#22C4C4') # Color celeste
tiempos_premium_0_5.plot(ax=plot_premium_maximas, color='#000000') # Color negro
tiempos_premium_minimas.plot(ax=plot_premium_maximas, color='#55A868') # Color verde


plot_premium_maximas.legend(['Premium 100%', 'Premium random', 'Premium 25%', 'Premium 10%', 'Premium 3%', 'Premium 0.5%', 'Premium 0%'], fontsize = 14)

plt.show()
# --------------------------------------------------------------------------------------------------------------------