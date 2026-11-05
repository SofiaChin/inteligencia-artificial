# Análisis de Inferencia Lógica - Problema de la Biblioteca

## 1. Resultados de las Consultas
* `AccesoNoche(Ana)`: **SI**. El motor forward chaining genera secuencialmente: `Miembro(Ana)`, `Miembro(Marta)`, `Becario(Ana)`, `AccesoNoche(Ana)` y `AccesoNoche(Marta)`. El motor backward chaining logra la prueba anidando `R_acceso` y `R_miembro_est`.
* `AccesoNoche(Luis)`: **NO**. Falla la comprobación ya que carece de credencial.
* `AccesoNoche(Marta)`: **SI**. Probado exitosamente a través de `R_acceso` y resolviendo `R_miembro_prof`.

## 2. Cuestionario Analítico

**A. Aparición de Becario(Ana) en algoritmos**
El encadenamiento hacia adelante computa la clausura deductiva completa del sistema, detonando cualquier regla válida en base a los hechos disponibles (como `R_beca`). En contraparte, el encadenamiento hacia atrás solo expande las dependencias directas del objetivo principal; al no existir relación causal entre `AccesoNoche` y `Becario`, esta última regla nunca se incorpora al árbol de exploración.

**B. Evaluación de Marta en R_miembro_est**
El motor de inferencia sigue un proceso estrictamente determinista basado en el orden de definición. La regla `R_miembro_est` es la primera opción disponible para deducir `Miembro(x)`. El sistema realiza la unificación con Marta e inspecciona las condiciones; al no encontrar evidencia de Marta como estudiante, retrocede (backtracking) y pasa a evaluar la regla pertinente de profesor.

**C. Modificación: Incorporación de TieneCredencial(Luis)**
Con la inserción de este nuevo hecho, el sistema logra inferir nuevos predicados para Luis en este orden: `Miembro(Luis)`, seguido de `Becario(Luis)` y por último `AccesoNoche(Luis)`. Tras el cambio, la consulta pasa a ser evaluada como **cierta (SI)** por ambos métodos algorítmicos.
