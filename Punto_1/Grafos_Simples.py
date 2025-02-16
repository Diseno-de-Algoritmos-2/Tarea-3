"""
Generación de un grafo simple y su exportación a GraphML para su visualización en Cytoscape.
"""

# -----------------------------------------|
# Daniel Vargas
# Santiago Bobadilla  
# Lina Ariza
# -----------------------------------------|

# Importa las librerías necesarias:
# networkx: Para la creación y manipulación de grafos.
# random: Para generar valores aleatorios.
# os: Para gestionar archivos.

import networkx as nx
import random
import os

# -----------------------------------------|
# Funciones Auxiliares
# -----------------------------------------|

# 1. Función para generar un grafo simple aleatorio.
#    Args:
#        num_vertices: Número de vértices
#        probabilidad: Probabilidad de conexión entre nodos
#    Returns:
#        G: Grafo simple generado

def generar_grafo_simple(num_vertices=20, probabilidad=0.2):
    while True:
        G = nx.erdos_renyi_graph(num_vertices, probabilidad)
        if nx.is_connected(G):  # Nos aseguramos de que sea conexo
            return G

# 2. Función para exportar el grafo en formato GraphML
#    Args:
#        G: Grafo simple generado
#    Returns:
#        file_path: Ruta del archivo generado

def exportar_grafo_graphml(G):
    local_dir = os.getcwd()  # Directorio actual
    file_path = os.path.join(local_dir, "grafo_simple.graphml")
    nx.write_graphml(G, file_path)
    return file_path

# 3. Función para visualizar el grafo generado.
#    Args:
#        G: Grafo simple generado

def visualizar_grafo(G):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)  # Disposición de nodos
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=500, font_size=10)
    plt.title("Grafo Simple Generado")
    plt.show()

# -----------------------------------------|
# Ejecución Principal
# -----------------------------------------|

if __name__ == "__main__":
    num_vertices = random.randint(20, 30)  # Se elige aleatoriamente entre 20 y 30
    G = generar_grafo_simple(num_vertices)
    
    print(f"Grafo generado con {num_vertices} vértices.")
    
    # Exportar el grafo
    file_path = exportar_grafo_graphml(G)
    print(f"Grafo exportado en: {file_path}")
    
    # Visualizar el grafo
    visualizar_grafo(G)

