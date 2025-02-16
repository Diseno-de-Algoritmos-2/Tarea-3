"""
Generación de grafos aleatorios completamente aleatoria:
- Grafo simple
- Grafo conexo
- Grafo planar

El programa genera un tipo de grafo al azar, indica qué tipo de grafo ha generado,
la cantidad de vértices y aristas, y lo exporta en formato GraphML para visualizar en Cytoscape.
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
import string

# -----------------------------------------|
# Funciones Auxiliares
# -----------------------------------------|

# 1. Función para generar un grafo simple.
#    Args:
#        num_vertices: Número de vértices (mínimo 20)
#    Returns:
#        G: Grafo generado

def generar_grafo_simple(num_vertices):
    G = nx.gnp_random_graph(num_vertices, p=0.5)  # Probabilidad media de conexión
    return G

# 2. Función para generar un grafo conexo.
#    Args:
#        num_vertices: Número de vértices (mínimo 20)
#    Returns:
#        G: Grafo generado

def generar_grafo_conexo(num_vertices):
    while True:
        G = nx.gnp_random_graph(num_vertices, p=0.3)  # Probabilidad más baja para evitar grafos densos
        if nx.is_connected(G):
            return G

# 3. Función para generar un grafo planar.
#    Args:
#        num_vertices: Número de vértices (mínimo 20)
#    Returns:
#        G: Grafo generado

def generar_grafo_planar(num_vertices):
    while True:
        G = nx.gnp_random_graph(num_vertices, p=0.2)  # Probabilidad baja para cumplir condición planar
        is_planar, _ = nx.check_planarity(G)
        if is_planar:
            return G

# 4. Función para exportar el grafo en formato GraphML
#    Args:
#        G: Grafo generado
#    Returns:
#        file_path: Ruta del archivo generado

def exportar_grafo_graphml(G, filename):
    local_dir = os.getcwd()
    file_path = os.path.join(local_dir, filename)
    nx.write_graphml(G, file_path)
    print(f"Archivo .GRAPHML guardado en: {file_path}.")
    return file_path

# 5. Función para visualizar el grafo generado con etiquetas A, B, C...
#    Args:
#        G: Grafo generado

def visualizar_grafo(G):
    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    
    # Crear etiquetas personalizadas (A, B, C... AA, AB si hay más de 26 nodos)
    labels = {n: string.ascii_uppercase[n % 26] + (string.ascii_uppercase[n // 26 - 1] if n >= 26 else "") for n in G.nodes()}
    
    nx.draw(G, pos, with_labels=True, labels=labels, node_color="lightblue", edge_color="gray", node_size=500, font_size=10)
    plt.title("Grafo Generado")
    plt.show()

# -----------------------------------------|
# Ejecución Principal
# -----------------------------------------|

if __name__ == "__main__":
    # Generación completamente aleatoria
    num_vertices = random.randint(20, 50)  # Se elige un número aleatorio de vértices entre 20 y 50
    opcion = random.choice(["1", "2", "3"])  # Se elige un tipo de grafo aleatoriamente
    
    tipo_grafo = "Simple" if opcion == "1" else "Conexo" if opcion == "2" else "Planar"
    print(f"Generando un grafo aleatorio del tipo: {tipo_grafo}")
    print(f"Número de vértices: {num_vertices}")
    
    if opcion == "1":
        G = generar_grafo_simple(num_vertices)
        filename = "grafo_simple.graphml"
    elif opcion == "2":
        G = generar_grafo_conexo(num_vertices)
        filename = "grafo_conexo.graphml"
    elif opcion == "3":
        G = generar_grafo_planar(num_vertices)
        filename = "grafo_planar.graphml"
    
    num_aristas = G.number_of_edges()
    print(f"Número de ejes: {num_aristas}")
    
    exportar_grafo_graphml(G, filename)
    visualizar_grafo(G)
