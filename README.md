# Práctica guiada 4a-bis: Barras y pastel con datos de ventas

**Caso empresarial:** RetailAndina S.A., cadena ecuatoriana de tiendas de consumo masivo.

## El contexto

El equipo de Business Intelligence prepara el reporte semanal para gerencia. La diapositiva 92 del curso mostró dos gráficos de la misma variable categórica: **barras** con los días de venta por región y **pastel** con la proporción de días. Ahora toca reproducirlos con datos reales y llevar la práctica un paso más allá: **la misma categoría se puede contar por días o por dólares**, y el gráfico cambia de lectura.

**Tu rol:** analista del equipo de BI. Construyes las tablas de frecuencia, los gráficos de barras y los pasteles, aplicas las reglas del buen gráfico y escribes una interpretación con cifras. La pregunta que debes poder responder al final: **¿qué región vende más por día y por qué no coincide con la que tiene más días?**

> Esta práctica **complementa** el Laboratorio 4a: profundiza en las barras y el pastel y añade la comparación días vs. volumen. Se puede usar antes, durante o después del lab 4a.

## Qué vas a practicar

- Tablas de frecuencia absoluta y relativa.
- Barras con título, ejes con unidades y escala desde cero.
- Barras ordenadas y horizontales para etiquetas largas.
- La diferencia entre **días** (frecuencia) y **dólares** (volumen).
- Pastel solo con 2–4 categorías y mensaje de proporción.
- El mismo análisis en **pandas/matplotlib** y en **R/ggplot2**.

## Archivos del repositorio

- `README.md`: este documento, con el contexto y las tareas.
- `informe.md`: el informe para gerencia (entregable, la plantilla indica qué secciones completar).
- `data/ventas_diarias.csv`: 280 registros, 5 sucursales durante 8 semanas.
- `scripts/practica_barras_pastel.py` y `.R`: archivos con pasos pendientes (**TODOs**) para que escribas el análisis.
- `EVALUACION.md`: la rúbrica con la que se evalúa la práctica.

## Cómo ejecutar

Completa los TODOs de los scripts y ejecútalos desde la raíz del repositorio:

```bash
python scripts/practica_barras_pastel.py

Rscript scripts/practica_barras_pastel.R
```

Los scripts leen `data/ventas_diarias.csv` y deben guardar los seis gráficos en `figuras/`.

## Tareas

1. **Frecuencia:** tabla de días por región y por sucursal (absoluta y relativa); verificar que suman 280 y 1.0.
2. **Barras de días:** por región y por sucursal, con título, ejes con unidades y escala desde cero.
3. **Volumen:** ventas totales por región y por sucursal; barras ordenadas, horizontales para las sucursales.
4. **Comparación días vs. volumen:** completar la tabla de la región (días, % días, ventas, % volumen, venta media por día) y explicar la diferencia.
5. **Pastel de región:** generarlo y evaluar si aporta algo frente a las barras.
6. **Pastel de sucursal:** generarlo con las 5 categorías y explicar por qué no permite comparar; proponer la alternativa.
7. **Interpretación final:** 3–4 líneas con la respuesta a gerencia.

## Cómo entregar

1. Haz un **fork** de este repositorio a tu cuenta de GitHub.
2. Clona **tu fork** y trabaja ahí: completa `informe.md` y los scripts.
3. Haz un **commit por tarea**, con mensajes claros; la historia del repositorio se revisa.
4. Sube los cambios a tu fork con `git push`.
5. Entrega el **enlace de tu fork** en el aula virtual.

## Entregable

El informe `informe.md` con las tablas, los seis gráficos y las interpretaciones. Los criterios están en `EVALUACION.md`.

*Práctica guiada 4a-bis, IDSD422, Estadística y Programación para Ciencia de Datos I, 2026-B.*
