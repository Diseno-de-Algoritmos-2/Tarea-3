"""
Generación de grafos aleatorios con opción para seleccionar:
- Grafo simple
- Grafo conexo
- Grafo planar

El grafo se exporta a formato GraphML para visualizar en Cytoscape.
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
    return file_path

# 5. Función para visualizar el grafo generado.
#    Args:
#        G: Grafo generado

def visualizar_grafo(G):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=500, font_size=10)
    plt.title("Grafo Generado")
    plt.show()

# -----------------------------------------|
# Ejecución Principal
# -----------------------------------------|

if __name__ == "__main__":
    print("Seleccione el tipo de grafo a generar:")
    print("1. Grafo Simple")
    print("2. Grafo Conexo")
    print("3. Grafo Planar")
    opcion = input("Ingrese la opción (1/2/3): ")
    
    while True:
        try:
            num_vertices = int(input("Ingrese el número de vértices (mínimo 20): "))
            if num_vertices >= 20:
                break
            else:
                print("Debe ingresar un número mayor o igual a 20.")
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")
    
    if opcion == "1":
        G = generar_grafo_simple(num_vertices)
        filename = "grafo_simple.graphml"
    elif opcion == "2":
        G = generar_grafo_conexo(num_vertices)
        filename = "grafo_conexo.graphml"
    elif opcion == "3":
        G = generar_grafo_planar(num_vertices)
        filename = "grafo_planar.graphml"
    else:
        print("Opción inválida. Saliendo del programa.")
        exit()
    
    print(f"Grafo generado con {num_vertices} vértices.")
    file_path = exportar_grafo_graphml(G, filename)
    print(f"Grafo exportado en: {file_path}")
    visualizar_grafo(G)



