# Ejercicio 2 — Descripción PEAS de agentes inteligentes

### 1. Asistente virtual de voz

- **Performance:** Tiempo de respuesta minimizado, alta tasa de éxito al ejecutar órdenes, precisión en el reconocimiento del habla, nivel de satisfacción del usuario.
- **Environment:** Interior de un hogar con ruido de fondo, presencia de múltiples usuarios, conexión a internet. Entorno parcialmente observable, estocástico, secuencial, dinámico y continuo.
- **Actuators:** Altavoz, llamadas a APIs de servicios de terceros, envío de señales a dispositivos de domótica inteligente.
- **Sensors:** Micrófonos, reloj interno, conexión de red.

### 2. Robot aspirador doméstico

- **Performance:** Porcentaje de superficie limpiada, tiempo empleado, conservación de batería, minimización de choques, retorno a la base de carga.
- **Environment:** Superficie del suelo de una casa, muebles estáticos y móviles, presencia de desniveles, mascotas y personas. Entorno parcialmente observable, estocástico, secuencial, dinámico y continuo.
- **Actuators:** Motores en las ruedas de tracción, motor del rodillo de limpieza o cepillos laterales, emisión de alertas sonoras.
- **Sensors:** Sensores de impacto, LIDAR o cámara para mapeo, sensores infrarrojos de desnivel, medidor del nivel de batería.

### 3. Sistema de recomendación de streaming

- **Performance:** Tasa de clics en sugerencias, tiempo de visualización acumulado por sesión, retención del suscriptor.
- **Environment:** Plataforma digital con un catálogo, interfaz web, base de datos de usuarios. Entorno parcialmente observable, estocástico, secuencial, estático y discreto.
- **Actuators:** Modificar la interfaz gráfica de sugerencias, enviar notificaciones push o correos electrónicos promocionales.
- **Sensors:** Historial de reproducciones, botones presionados, palabras clave introducidas en la barra de búsqueda, metadatos del usuario.

### 4. Vehículo autónomo en ciudad

- **Performance:** Minimización de accidentes, cumplimiento de normativas de tráfico, minimización del tiempo de llegada al destino, confort del pasajero en las maniobras.
- **Environment:** Infraestructura urbana, tráfico vehicular mixto, peatones, condiciones climáticas variables. Entorno parcialmente observable, estocástico, secuencial, dinámico y continuo.
- **Actuators:** Acelerador, sistema de frenos, volante, luces, claxon.
- **Sensors:** Múltiples cámaras, sistema LIDAR 360°, radar, GPS, odómetros, acelerómetros y micrófonos.

### 5. Agente de trading algorítmico en bolsa

- **Performance:** Retorno de inversión maximizado, exposición al riesgo minimizada, latencia mínima en la ejecución, mantenimiento de la liquidez.
- **Environment:** Mercados financieros, noticias macroeconómicas en tiempo real. Entorno parcialmente observable, estocástico, secuencial, dinámico y continuo.
- **Actuators:** Emisión de órdenes de compra, órdenes de venta, cancelación de órdenes previas.
- **Sensors:** API de precios del mercado en tiempo real, histórico de volumen de transacciones, reloj atómico.

### 6. Sistema de diagnóstico médico asistido por IA

- **Performance:** Alta sensibilidad y especificidad, minimización del tiempo de análisis de imágenes, mejora de la precisión del médico.
- **Environment:** Base de datos de historiales clínicos, imágenes radiológicas, perfiles biológicos de los pacientes. Entorno parcialmente observable, estocástico, episódico y estático.
- **Actuators:** Resaltar anomalías en pantalla, emitir un reporte de texto con probabilidades diagnósticas, solicitar pruebas adicionales.
- **Sensors:** Carga de archivos de imagen, entrada de texto del médico, lecturas estructuradas de laboratorio.

### 7. Dron de inspección de infraestructura

- **Performance:** Porcentaje de cobertura de la infraestructura evaluado correctamente, cantidad de fallas detectadas, prevención de colisiones, tiempo de vuelo optimizado por carga de batería.
- **Environment:** Espacio aéreo alrededor de estructuras físicas complejas, condiciones meteorológicas. Entorno parcialmente observable, estocástico, secuencial, dinámico y continuo.
- **Actuators:** Variadores de velocidad de los rotores, estabilización y enfoque de la cámara, obturador de cámara.
- **Sensors:** Cámaras RGB y térmicas, altímetro, módulo GPS, sensor de viento, sensores ultrasónicos o LIDAR de proximidad.

### 8. Agente jugador de ajedrez

- **Performance:** Porcentaje de victorias, maximización de ventaja material o posicional, control del reloj, optimización del uso de recursos de procesamiento en hardware.
- **Environment:** Tablero de 8x8, 32 piezas, reglas de juego, reloj de tiempo, acciones del oponente. Entorno totalmente observable, determinista, secuencial, estático y discreto.
- **Actuators:** Interacción con la interfaz gráfica, emitir oferta de tablas, promover peón.
- **Sensors:** Estado exacto del tablero, lista de movimientos previos, tiempo restante en el reloj.
