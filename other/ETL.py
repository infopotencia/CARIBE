from pathlib import Path
import pandas as pd

CARPETA = r"DATA\raw"
DIVIPOLA = r"DATA\MUN_DIVIPOLA.xlsx"

KEYS = ["codigo_DANE", "nombre_entidad", "anio"]

# ======================
# Divipola
# ======================

divipola = pd.read_excel(DIVIPOLA)

divipola["codigo_DANE"] = (
    divipola["codigo_DANE"]
    .astype(str)
    .str.replace(".0", "", regex=False)
    .str.zfill(5)
)

nombre_oficial = dict(
    zip(
        divipola["codigo_DANE"],
        divipola["nombre_entidad"]
    )
)

# ======================
# Consolidación
# ======================

df_final = None

for archivo in Path(CARPETA).rglob("*.xlsx"):

    try:

        df = pd.read_excel(
            archivo,
            sheet_name="TABLA"
        )

        df.columns = df.columns.str.strip()

        # Normalizar código
        df["codigo_DANE"] = (
            df["codigo_DANE"]
            .astype(str)
            .str.replace(".0", "", regex=False)
            .str.zfill(5)
        )

        # Nombre oficial desde Divipola
        df["nombre_entidad"] = (
            df["codigo_DANE"]
            .map(nombre_oficial)
        )

        # Mantener claves + indicadores
        df = df[
            [c for c in df.columns]
        ]

        if df_final is None:

            df_final = df

        else:

            nuevas_columnas = [
                c for c in df.columns
                if c not in df_final.columns
                or c in KEYS
            ]

            df_final = pd.merge(
                df_final,
                df[nuevas_columnas],
                on=KEYS,
                how="outer"
            )

        print(f"✓ {archivo.name}")

    except Exception as e:

        print(f"✗ {archivo.name}: {e}")

# Exportar

df_final.to_excel(
    r"DATA\base_maestra.xlsx",
    index=False
)

print(df_final.shape)