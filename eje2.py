import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Graficando FMP
n, p = 30, 0.4 # parametros de forma de la distribución binomial
n_1, p_1 = 20, 0.3 # parametros de forma de la distribución binomial
x = np.arange(stats.binom.ppf(0.01, n, p),
              stats.binom.ppf(0.99, n, p))

fmp = stats.binom.pmf(x, n, p) # Función de Masa de Probabilidad


plt.hist(x, edgecolor = '#76acb0', color='#97dade', linewidth=1.5 )
plt.title('Función de Masa de Probabilidad')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()