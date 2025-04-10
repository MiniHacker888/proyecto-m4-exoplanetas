import pandas as pd
import matplotlib.pyplot as plt
import math as m
import numpy as np

plt.rcParams.update({'font.size': 12})

# Requerimiento 0
def cargar_datos(nombre_archivo: str) -> pd.DataFrame:
    return pd.read_csv(nombre_archivo)

# Requerimiento 1
def histograma_descubrimiento(datos: pd.DataFrame) -> None:
    plt.figure(figsize=(10, 6))
    datos['DESCUBRIMIENTO'].hist(bins=30)
    plt.title('Número de descubrimientos por año')
    plt.xlabel('Año')
    plt.ylabel('Cantidad de planetas')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Requerimiento 2
def estado_publicacion_por_descubrimiento(datos: pd.DataFrame) -> None:
    plt.figure(figsize=(8, 8))
    datos.boxplot(column='DESCUBRIMIENTO', by='ESTADO_PUBLICACION', rot=90)
    plt.title('Descubrimiento por estado de publicación')
    plt.suptitle('')
    plt.xlabel('Estado de publicación')
    plt.ylabel('Año')
    plt.tight_layout()
    plt.show()

# Requerimiento 3
def deteccion_por_descubrimiento(datos: pd.DataFrame) -> None:
    plt.figure(figsize=(8, 8))
    datos.boxplot(column='DESCUBRIMIENTO', by='TIPO_DETECCION', rot=90)
    plt.title('Descubrimiento por tipo de detección')
    plt.suptitle('')
    plt.xlabel('Tipo de detección')
    plt.ylabel('Año')
    plt.tight_layout()
    plt.show()

# Requerimiento 4
def deteccion_y_descubrimiento(datos: pd.DataFrame, anho: int) -> None:
    if anho != 0:
        datos = datos[datos['DESCUBRIMIENTO'] == anho]
    conteo = datos['TIPO_DETECCION'].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(conteo, labels=conteo.index, autopct='%1.1f%%', startangle=140)
    titulo = f'Tipo de detección en el año {anho}' if anho != 0 else 'Tipo de detección en todos los años'
    plt.title(titulo)
    plt.tight_layout()
    plt.show()

# Requerimiento 5
def cantidad_y_tipo_deteccion(datos: pd.DataFrame) -> None:
    tabla = datos.groupby(['DESCUBRIMIENTO', 'TIPO_DETECCION']).size().unstack(fill_value=0)
    tabla.plot(figsize=(12, 6))
    plt.title('Cantidad de descubrimientos por tipo y año')
    plt.xlabel('Año')
    plt.ylabel('Cantidad de planetas')
    plt.tight_layout()
    plt.show()

# Requerimiento 6
def masa_promedio_y_tipo_deteccion(datos: pd.DataFrame) -> None:
    tabla = datos.groupby(['DESCUBRIMIENTO', 'TIPO_DETECCION'])['MASA'].mean().unstack()
    tabla.plot(figsize=(12, 6))
    plt.title('Masa promedio por tipo de detección y año')
    plt.xlabel('Año')
    plt.ylabel('Masa promedio')
    plt.tight_layout()
    plt.show()

# Requerimiento 7
def masa_planetas_vs_masa_estrellas(datos: pd.DataFrame) -> None:
    plt.figure(figsize=(10, 6))
    plt.scatter(datos['MASA_ESTRELLA'], datos['MASA'])
    plt.yscale('log')
    plt.xlabel('Masa de la estrella más cercana')
    plt.ylabel('Masa del planeta (escala log)')
    plt.title('Masa de los planetas vs masa de las estrellas')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Requerimiento 8
def graficar_cielo(datos: pd.DataFrame) -> list:
    colores = {
        'Microlensing': [0.94, 0.10, 0.10],
        'Radial Velocity': [0.10, 0.50, 0.94],
        'Imaging': [0.34, 0.94, 0.10],
        'Primary Transit': [0.10, 0.94, 0.85],
        'Other': [0.94, 0.10, 0.85],
        'Astrometry': [0.94, 0.65, 0.10],
        'TTV': [1.0, 1.0, 1.0]
    }
    imagen = np.zeros((100, 200, 3))
    for _, fila in datos.iterrows():
        ra = m.radians(fila['RA'])
        dec = m.radians(fila['DEC'])
        fila_idx = int(99 - abs(m.sin(ra) * m.cos(dec) * 100))
        col_idx = int(m.cos(ra) * m.cos(dec) * 100) + 100
        if 0 <= fila_idx < 100 and 0 <= col_idx < 200:
            color = colores.get(fila['TIPO_DETECCION'], [1.0, 1.0, 1.0])
            imagen[fila_idx, col_idx] = color
    plt.figure(figsize=(10, 5))
    plt.imshow(imagen)
    plt.axis('off')
    plt.title('Cielo de exoplanetas')
    plt.show()
    return imagen

# Requerimiento 9
def filtrar_imagen_cielo(imagen: list) -> None:
    mascara = np.array([[-1, -1, -1],
                        [-1,  9, -1],
                        [-1, -1, -1]])
    resultado = np.copy(imagen)
    for canal in range(3):
        for i in range(1, imagen.shape[0] - 1):
            for j in range(1, imagen.shape[1] - 1):
                region = imagen[i-1:i+2, j-1:j+2, canal]
                resultado[i, j, canal] = np.clip(np.sum(region * mascara), 0, 1)
    plt.figure(figsize=(10, 5))
    plt.imshow(resultado)
    plt.axis('off')
    plt.title('Cielo afinado')
    plt.show()
