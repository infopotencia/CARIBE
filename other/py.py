import  pandas as pd

df = pd.read_excel(r"DATA\base_maestra.xlsx")
print(df.columns)

df.columns = [
    'codigo_dane',
    'nombre_entidad',
    'anio',
    'poblacion_total',
    'poblacion_rural',
    'poblacion_urbana',
    'nbi',
    'valor_agregado',
    'peso_relativo_va',
    'actividades_primarias',
    'actividades_secundarias',
    'actividades_terciarias',
    'ingresos_tributarios_percapita',
    'icld',
    'gastos_funcionamiento',
    'deuda_publica',
    'categoria',
    'area_km2',
    'cobertura_acueducto',
    'cobertura_alcantarillado'
]

df.to_csv(
    "indicadores_municipales.csv",
    index=False,
    encoding="utf-8-sig"
)