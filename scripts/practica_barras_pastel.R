# practica_barras_pastel.R — Práctica guiada 4a-bis (R)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   Rscript scripts/practica_barras_pastel.R
#
# Requiere: ggplot2, dplyr, scales.
#
# Reglas del buen gráfico que debes aplicar:
#   - título que diga qué se muestra
#   - ejes con unidades ("Días registrados", "Ventas (USD)")
#   - escala desde cero en las barras
#   - barras ordenadas por magnitud y horizontales para etiquetas largas
#   - pastel solo con 2–4 categorías y mensaje de proporción
#   - gráficos guardados como archivo en figuras/

library(ggplot2)
library(dplyr)
library(scales)

AZUL <- "#205080"; ORO <- "#8a6d1f"
dir.create("figuras", showWarnings = FALSE)


guardar <- function(p, nombre, width = 7, height = 4) {
  ggsave(file.path("figuras", paste0(nombre, ".png")),
         p, width = width, height = height, dpi = 150, bg = "white")
}


# ---------------------------------------------------------------------------
# TODO 1: carga data/ventas_diarias.csv en `ventas`
#         Pista: read.csv("data/ventas_diarias.csv")
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# TODO 2: tablas de frecuencia (absoluta y relativa) por región y sucursal
#         Pista: count(region) |> mutate(prop = n / sum(n))
#         Verifica que las absolutas suman 280 y las relativas 1.0.
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# TODO 3: barras de días por región
#         - geom_col() con reorder(region, -n)
#         - labs(title, x = "Región", y = "Días registrados")
#         - escala desde cero: scale_y_continuous(limits = c(0, 200))
#         - guardar con guardar(p, "barras_dias_region")
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# TODO 4: barras de días por sucursal
#         - horizontales: aes(x = n, y = reorder(sucursal, n)) + geom_col()
#         - x = "Días registrados", y = NULL
#         - scale_x_continuous(limits = c(0, 60))
#         - guardar "barras_dias_sucursal"
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# TODO 5: volumen por región y por sucursal
#         Pista: group_by(region) |> summarise(ventas = sum(ventas))
#                group_by(sucursal) |> summarise(ventas = sum(ventas))
#         Calcula también la venta media por día (volumen / días).
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# TODO 6: barras de volumen
#         - por región: geom_col(), eje Y "Ventas (USD)",
#           escala desde cero y labels = label_comma().
#         - por sucursal: horizontales y ordenadas por magnitud,
#           eje X "Ventas (USD)".
#         - guardar "barras_volumen_region" y "barras_volumen_sucursal".
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# TODO 7: pastel de región (2 categorías)
#         - geom_col(width = 1) + coord_polar("y") + theme_void()
#         - etiquetas con percent(prop, accuracy = 0.1) y geom_text()
#         - guardar "pastel_dias_region"
#         - En el informe: ¿aporta algo frente a las barras?
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# TODO 8: pastel de sucursal (5 categorías)
#         - mismo esquema, con la participación por volumen
#         - guardar "pastel_volumen_sucursal"
#         - En el informe: ¿se distingue la porción mayor de la segunda?
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# TODO 9: imprime las tablas de referencia y confirma los 6 gráficos
#         Pista: print(...) y cat("Listo: revisa los gráficos en figuras/\n")
# ---------------------------------------------------------------------------

cat("Listo: revisa los gráficos en figuras/\n")
