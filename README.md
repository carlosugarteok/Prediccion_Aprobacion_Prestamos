# PREDICCION DE APROBACION DE PRESTAMOS - Con Aprendizaje Automático

Proyecto de **clasificación supervisada** con datos **100 % sintéticos**. Predice la etiqueta de aprobación artificial `Y/N`; **no estima riesgo de impago ni sirve para aprobar préstamos reales**.

## Alcance y metodología

- 614 solicitudes ficticias, 13 columnas; semilla 42; siete variables con valores faltantes.
- División estratificada 80/20; imputación, codificación y estandarización dentro de un Pipeline.
- Comparación de línea base mayoritaria, regresión logística y SVC RBF con validación cruzada estratificada de cinco pliegues (solo entrenamiento).
- Evaluación final con accuracy, balanced accuracy, F1 macro, ROC AUC, average precision, Brier y matriz de confusión.
- Análisis exploratorio de umbrales; exportación de resultados y gráficos.

## Ejecución

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
python -m pip install -r requirements.txt
jupyter notebook notebooks/Prediccion_Aprobacion_Prestamos.ipynb
```

Ejecutar todas las celdas desde `notebooks/` o desde la raíz. El notebook crea archivos en `data/`, `outputs/` y `figures/`; no necesita descargar información externa.

## Estructura

- `notebooks/`: notebook ejecutable y explicado en castellano.
- `docs/`: informe técnico en Word, con Takeaways y Glosario.
- `data/`: solicitudes sintéticas generadas.
- `outputs/`: métricas, validación cruzada y predicciones simuladas.
- `figures/`: gráficos exportados.
- `tests/`: comprobaciones básicas de integridad.

## Advertencia metodológica

Los resultados dependen de la regla artificial de generación y de la partición de prueba. No representan desempeño sobre clientes reales. El uso operativo de variables personales o sensibles requiere revisión legal, ética y técnica. **No hay validación externa, temporal ni de equidad.**