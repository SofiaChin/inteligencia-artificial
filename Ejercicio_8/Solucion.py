import random
import csv

# Constantes y parámetros del problema
ALFA = 0.5
GAMA = 1.0
EPS = 0.1
MAX_EPISODIOS = 500
LIMITE_PASOS = 200
SEMILLA = 42

# Definimos el tablero y las coordenadas clave
FILAS = 4
COLUMNAS = 12
INICIO = (3, 0)
META = (3, 11)

# Acciones: 0 = Norte, 1 = Este, 2 = Sur, 3 = Oeste
ACCIONES = [0, 1, 2, 3]

def crear_tabla_q():
    """Inicializa la tabla Q con ceros para todos los estados y acciones."""
    Q = {}
    for f in range(FILAS):
        for c in range(COLUMNAS):
            Q[(f, c)] = {a: 0.0 for a in ACCIONES}
    return Q

def simular_paso(estado, accion):
    """Aplica la accion y devuelve (nuevo_estado, recompensa, terminado)."""
    fila, col = estado
    
    if accion == 0: fila -= 1
    elif accion == 1: col += 1
    elif accion == 2: fila += 1
    elif accion == 3: col -= 1

    # Si el agente choca con una pared, se queda donde está
    if fila < 0 or fila >= FILAS or col < 0 or col >= COLUMNAS:
        return estado, -1.0, False

    nuevo_estado = (fila, col)

    # Revisar si llegó a la meta
    if nuevo_estado == META:
        return nuevo_estado, -1.0, True

    # Revisar si cayó al acantilado (fila 3, columnas del 1 al 10)
    if nuevo_estado[0] == 3 and 1 <= nuevo_estado[1] <= 10:
        return INICIO, -100.0, False

    # Paso normal
    return nuevo_estado, -1.0, False

def obtener_mejor_accion(Q, estado):
    """Devuelve la accion con mayor valor Q. Desempata por el orden en ACCIONES."""
    return max(ACCIONES, key=lambda a: Q[estado][a])

def entrenar_agente():
    """Ejecuta el ciclo principal de Q-learning."""
    generador = random.Random(SEMILLA)
    Q = crear_tabla_q()
    historial_recompensas = []

    for _ in range(MAX_EPISODIOS):
        estado = INICIO
        suma_recompensas = 0.0
        
        for _ in range(LIMITE_PASOS):
            # Explorar o explotar (Epsilon-greedy)
            if generador.random() < EPS:
                accion = generador.choice(ACCIONES)
            else:
                accion = obtener_mejor_accion(Q, estado)

            estado_sig, recompensa, terminado = simular_paso(estado, accion)

            # Actualizacion Q-learning
            max_q_sig = max(Q[estado_sig].values()) if not terminado else 0.0
            
            valor_actual = Q[estado][accion]
            Q[estado][accion] = valor_actual + ALFA * (recompensa + GAMA * max_q_sig - valor_actual)

            suma_recompensas += recompensa
            estado = estado_sig

            if terminado:
                break
                
        historial_recompensas.append(suma_recompensas)

    return Q, historial_recompensas

if __name__ == '__main__':
    tabla_final, retornos = entrenar_agente()

    # Escribir el CSV con el registro
    with open('recompensas.csv', 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(['episodio', 'recompensa', 'media_movil_10'])
        
        for i, recompensa in enumerate(retornos):
            ventana_inicio = max(0, i + 1 - 10)
            pedazo = retornos[ventana_inicio : i+1]
            media = sum(pedazo) / len(pedazo)
            escritor.writerow([i + 1, recompensa, media])

    # Prueba final con política óptima
    estado_actual = INICIO
    pasos_totales = 0
    recompensa_final = 0.0
    
    for _ in range(LIMITE_PASOS):
        mejor = obtener_mejor_accion(tabla_final, estado_actual)
        estado_actual, rec, fin = simular_paso(estado_actual, mejor)
        recompensa_final += rec
        pasos_totales += 1
        if fin:
            break

    print("Resultados de la evaluacion final:")
    print(f"- Retorno obtenido (política greedy): {recompensa_final}")
    print(f"- Cantidad de pasos tomados: {pasos_totales}")
    print("- El archivo 'recompensas.csv' ha sido creado en este directorio.")