"""
Generación de grafos 
"""

# -----------------------------------------|
# Daniel Vargas
# Santiago Bobadilla  
# Lina Ariza
# -----------------------------------------|

# Importa las librerías necesarias:
# networkx: Para la creación y manipulación de grafos.
# os: Para gestionar archivos.

import networkx as nx
import os
import string
import matplotlib.pyplot as plt

def generar_grafo_planar_conexo_simple(num_vertices, max_intentos=5000):
    p = 0.2
    for _ in range(max_intentos):
        G = nx.gnp_random_graph(num_vertices, p)
        is_planar, _ = nx.check_planarity(G)
        if is_planar and nx.is_connected(G):
            return G
        p *= 0.9 
    print("Error: No se pudo generar un grafo válido.")
    return None

def exportar_grafo_graphml(G, filename):
    file_path = os.path.join(os.getcwd(), filename)
    try:
        nx.write_graphml(G, file_path)
        print(f"Archivo .GRAPHML guardado en: {file_path}")
    except OSError as e:
        print(f"Error al guardar el archivo: {e}")

def visualizar_grafo(G):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    labels = {n: string.ascii_uppercase[n % 26] for n in G.nodes()}
    nx.draw(G, pos, with_labels=True, labels=labels, node_color="lightblue", edge_color="gray", node_size=500, font_size=10)
    plt.title("Grafo Generado")
    plt.show()

if __name__ == "__main__":
    while True:
        try:
            num_vertices = int(input("Ingrese el número de vértices (mínimo 20): "))
            if num_vertices < 20:
                print("El número de vértices debe ser al menos 20.")
                continue
            break
        except ValueError:
            print("Entrada inválida.")
    
    print(f"Generando grafo con {num_vertices} vértices...")
    G = generar_grafo_planar_conexo_simple(num_vertices)
    if G is None:
        exit()
    
    print(f"Número de ejes: {G.number_of_edges()}")
    exportar_grafo_graphml(G, "grafo_planar_conexo_simple.graphml")
    visualizar_grafo(G)

