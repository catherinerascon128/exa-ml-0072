import sys
import os
import io
import pandas as pd

# 1. Agregar la subcarpeta datos_de_entrada_ml_0072 al sistema de rutas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'datos_de_entrada_ml_0072')))

# Importar el módulo dicc_0072.py
import dicc_0072 # type: ignore

print("catherine eileen huerta rascon Machine Learning pandas, NC 0072")

# Variable para almacenar las salidas y guardarlas en el archivo .md
contenido_md = []
encabezado_pie = "catherine eileen huerta rascon Machine Learning pandas, NC 0072"
contenido_md.append(f"# Reporte de Análisis de Datos - Pandas\n\n`{encabezado_pie}`\n")

def registrar(titulo, contenido):
    """Muestra el resultado en terminal y lo formatea para el archivo Markdown."""
    print(f"\n--- {titulo} ---")
    print(contenido)
    contenido_md.append(f"## {titulo}\n```text\n{contenido}\n```\n")

# 1. Convertir diccionario a DataFrame
df = pd.DataFrame(dicc_0072.datos_festivales)
registrar("1. DataFrame Convertido", df)

# 2. Información Estructural
registrar("2.1 Primeras Filas (head)", df.head(2))
registrar("2.2 Últimas Filas (tail)", df.tail(2))
registrar("2.3 Dimensiones (Filas, Columnas)", df.shape)
registrar("2.4 Tipos de Datos por Columna", df.dtypes)

# Capturar salida de df.info()
buffer = io.StringIO()
df.info(buf=buffer)
registrar("2.5 Información General (info)", buffer.getvalue())

# 3. Estadísticas Generales de la Columna Numérica (Artistas)
registrar("3. Estadísticas Generales de la Columna 'Artistas'", df['Artistas'].describe())

# 4. Ordenar Ascendente por Artistas
df_asc_artistas = df.sort_values(by="Artistas", ascending=True)
registrar("4. Ordenar Ascendente por Artistas", df_asc_artistas)

# 5. Ordenar Descendente por Dias
df_desc_dias = df.sort_values(by="Dias", ascending=False)
registrar("5. Ordenar Descendente por Dias", df_desc_dias)

# 7. Guardar el archivo resultados-ml-0072.md dentro de resultados-0072
carpeta_resultados = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resultados-0072'))
os.makedirs(carpeta_resultados, exist_ok=True)
ruta_archivo_md = os.path.join(carpeta_resultados, "resultados-ml-0072.md")

contenido_md.append(f"`{encabezado_pie}`")

with open(ruta_archivo_md, "w", encoding="utf-8") as f:
    f.write("\n".join(contenido_md))

print(f"\n[ÉXITO] Archivo generado correctamente en: {ruta_archivo_md}")
print("catherine eileen huerta rascon Machine Learning pandas, NC 0072")