"""
    Simulación de Monte Carlo para calcular la probabilidad de que un grafo sea planar
    dado un grafo de 20 vertices y un número de aristas que varía.
"""


# -----------------------------------------|
# Daniel Vargas
# Santiago Bobadilla  
# Lina Ariza
# -----------------------------------------|

import networkx as nx
import matplotlib.pyplot as plt
import random as rd
from tqdm import tqdm
import numpy as np
from scipy.optimize import curve_fit

# -----------------------------------------|
# Simulación de Monte Carlo
# -----------------------------------------|

N_VERTICES = 20 # El grafó siempre tiene 20 vertices.

def main():

    # -------------------------------------------------------|
    # Simulación de Monte Carlo.

    n = 10000                                                                    # Numero de simulaciones para calcular la probabilidad.
    max_arcos = (N_VERTICES * (N_VERTICES - 1)) // 2                            # Numero máximo de aristas a las que se va a llegar (grafo completo).
    
    probabilidades = []                                                         # Lista para guardar las probabilidades de que el grafo sea planar.                            
    for n_arcos in tqdm(range(1, max_arcos)):                                   # Se recorre el número de aristas desde 1 hasta el máximo.
        prob = probabilidad_de_ser_planar(n_arcos, n)                           # Se calcula la probabilidad de que el grafo sea planar.
        probabilidades.append(prob)                                             # Se guarda la probabilidad en la lista.
    
    teoria = 3 * N_VERTICES - 6                                                 # Se calcula el número máximo de aristas para un grafo planar según la fórmula 3V - 6.
    
    # -------------------------------------------------------|
    # Gráfica

    plt.figure(figsize=(10, 6))
    plt.scatter(list(range(1, max_arcos, 1)), probabilidades, label='Probabilidad Empirica')
    plt.axvline(x=teoria, color='r', linestyle='--', 
                label=f'Teoría (3V-6 = {teoria})')
    
    plt.xlabel('Número de arcos')
    plt.ylabel('Probabilidad de ser planar')
    plt.title(f'V={N_VERTICES}')
    plt.grid(True)
    plt.legend()

    # -------------------------------------------------------|
    # Ajuste de curva sigmoide a los datos. 

    x_data = np.array(range(1, max_arcos))                              # Datos de los arcos.
    y_data = np.array(probabilidades)                                   # Datos de las probabilidades.                         
    p0 = [1.0, teoria, 0.1]                                             # Parámetros iniciales aproximados
    
    try:
        popt, _ = curve_fit(sigmoid, x_data, y_data, p0=p0)             # Ajustar la curva sigmoide a los datos.
        
        x_fit = np.linspace(1, max_arcos-1, 1000)                       # Datos para la curva ajustada.
        y_fit = sigmoid(x_fit, *popt)                                   # Probabilidades ajustadas.
        
        # Añadir la curva a la gráfica
        plt.plot(x_fit, y_fit, 'g-', label='Estimación (Sigmoide)', alpha=0.8)
        
        # Imprimir los parámetros de la función
        print("\nParámetros de la función sigmoide:")
        print(f"L (valor máximo): {popt[0]:.4f}")
        print(f"x0 (punto medio): {popt[1]:.4f}")
        print(f"k (pendiente): {popt[2]:.4f}")
        
    except RuntimeError:
        print("No se pudo ajustar la curva sigmoide a los datos")
    
    plt.grid(False)
    plt.legend()

    # -------------------------------------------------------|
    # Obtener la probabilidad con el ajuste de curva sigmoide.

    probabilidad_teoria = sigmoid(teoria, *popt)
    print(f"\nProbabilidad teórica con ajuste sigmoide: {probabilidad_teoria:.4f}")

    limite = popt[1]
    probabilidad_empirica = sigmoid(limite, *popt)
    print(f"Probabilidad empírica para {limite} arcos con ajuste sigmoide: {probabilidad_empirica:.4f}")


    # -------------------------------------------------------|
    # Guardar resultados en un archivo CSV
    
    with open('planaridad.csv', 'w') as f:
        f.write('Arcos,Probabilidad\n')
        for edges, prob in zip(range(1, max_arcos, 1), probabilidades):
            f.write(f'{edges},{prob}\n')
    
    plt.savefig('planaridad.png')
    plt.show()

# -----------------------------------------|
# Generación de grafos aleatorios
# -----------------------------------------|

def grafo_con_arcos_aleatorios(n_arcos):

    G = nx.Graph()                                                              # Se crea un grafo vacío.
    G.add_nodes_from(range(N_VERTICES))                                         # Se añaden los nodos al grafo = 20.

    arcos = list(nx.complete_graph(N_VERTICES).edges())                         # Se obtienen todas las aristas del grafo completo.
    añadir_ejes = rd.sample(arcos, min(n_arcos, len(arcos)))                    # Se seleccionan n_arcos aristas aleatorias.
    G.add_edges_from(añadir_ejes)                                               # Se añaden las aristas al grafo.                   
    
    return G

# ------------------------------------------------------------|
# Cálculo de la probabilidad de que un grafo sea planar.
# ------------------------------------------------------------|

def probabilidad_de_ser_planar(n_arcos, n=100):

    es_planar = 0.0                                         # Contador que lleva la cantidad de grafos que fueron planares.
    for _ in range(n):                                      # Se realizan n simulaciones. (Minimo 100)
        G = grafo_con_arcos_aleatorios(n_arcos)             # Se genera un grafo aleatorio con n_arcos aristas.
        if nx.check_planarity(G)[0]:                        # Se verifica si el grafo es planar.
            es_planar += 1                                  # Se incrementa el contador si el grafo es planar.
            
    return es_planar / n                                    # Se retorna la probabilidad de que el grafo sea planar.

# ------------------------------------------------------------|
# Función sigmoide para ajustar la curva a los datos.
# ------------------------------------------------------------|

def sigmoid(x, L, x0, k):
        return L / (1 + np.exp(-k*(x-x0)))

# -----------------------------------------|
# Ejecución

if __name__ == "__main__":
    main()