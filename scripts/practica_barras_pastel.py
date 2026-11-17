# practica_barras_pastel.py — Práctica guiada 4a-bis (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/practica_barras_pastel.py
#
# Requiere: pandas, matplotlib.
#
# Reglas del buen gráfico que debes aplicar:
#   - título que diga qué se muestra
#   - ejes con unidades ("Días registrados", "Ventas (USD)")
#   - escala desde cero en las barras
#   - barras ordenadas por magnitud y horizontales para etiquetas largas
#   - pastel solo con 2–4 categorías y mensaje de proporción
#   - gráficos guardados como archivo en figuras/

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # permite ejecutar sin pantalla

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter

AZUL, ORO = "#205080", "#8a6d1f"
SALIDA = Path("figuras")
SALIDA.mkdir(exist_ok=True)


def guardar(fig, nombre):
    """Guarda la figura como PNG y libera la memoria."""
    fig.tight_layout()
    fig.savefig(SALIDA / f"{nombre}.png", dpi=150, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def main():
    # ------------------------------------------------------------------
    # TODO 1: carga data/ventas_diarias.csv en `ventas`
    #         Pista: pd.read_csv("data/ventas_diarias.csv")
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # TODO 2: tablas de frecuencia (absoluta y relativa) por región y sucursal
    #         Pista: value_counts() y value_counts(normalize=True)
    #         Verifica que las absolutas suman 280 y las relativas 1.0.
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # TODO 3: barras de días por región
    #         - `plot(kind="bar")`
    #         - título, xlabel "Región", ylabel "Días registrados"
    #         - escala desde cero (set_ylim(0, 200))
    #         - guardar con guardar(fig, "barras_dias_region")
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # TODO 4: barras de días por sucursal
    #         - horizontales: `plot(kind="barh")`
    #         - xlabel "Días registrados", xlim 0–60
    #         - guardar con guardar(fig, "barras_dias_sucursal")
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # TODO 5: volumen por región y por sucursal
    #         Pista: ventas.groupby("region")["ventas"].sum()
    #                ventas.groupby("sucursal")["ventas"].sum()
    #         Calcula también la venta media por día (volumen / días).
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # TODO 6: barras de volumen
    #         - por región: barras verticales, eje Y "Ventas (USD)",
    #           escala desde cero y separador de miles.
    #         - por sucursal: barras horizontales y ordenadas por magnitud,
    #           eje X "Ventas (USD)".
    #         - guardar "barras_volumen_region" y "barras_volumen_sucursal".
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # TODO 7: pastel de región (2 categorías)
    #         - `plot(kind="pie", autopct="%.1f%%", startangle=90)`
    #         - sin ylabel; título "Proporción de días por región"
    #         - guardar "pastel_dias_region"
    #         - En el informe: ¿aporta algo frente a las barras?
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # TODO 8: pastel de sucursal (5 categorías)
    #         - mismo esquema, con la participación por volumen
    #         - guardar "pastel_volumen_sucursal"
    #         - En el informe: ¿se distingue la porción mayor de la segunda?
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # TODO 9: imprime las tablas de referencia y confirma los 6 gráficos
    #         Pista: print(pd.DataFrame({...})) y un print final.
    # ------------------------------------------------------------------

    print(f"Listo: revisa los gráficos en {SALIDA}/")


if __name__ == "__main__":
    main()
