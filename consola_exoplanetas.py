# -*- coding: utf-8 -*-
import exoplanetas as mod
import pandas as pd

from exoplanetas import *

def menu():
    print("\n--- Proyecto M4: Exoplanetas ---")
    print("1. Histograma de descubrimientos")
    print("2. Boxplot por estado de publicación")
    print("3. Boxplot por tipo de detección")
    print("4. Pie chart tipo de detección (por año o total)")
    print("5. Descubrimientos por tipo y año")
    print("6. Masa promedio por tipo y año")
    print("7. Dispersión de masa planetaria vs estelar")
    print("8. Graficar cielo de exoplanetas")
    print("9. Aplicar filtro a cielo de exoplanetas")
    print("0. Salir")

if __name__ == '__main__':
    archivo = input("Ingrese el nombre del archivo CSV (por ejemplo, exoplanetas.csv): ")
    datos = cargar_datos(archivo)
    imagen = []

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            histograma_descubrimiento(datos)
        elif opcion == "2":
            estado_publicacion_por_descubrimiento(datos)
        elif opcion == "3":
            deteccion_por_descubrimiento(datos)
        elif opcion == "4":
            try:
                anho = int(input("Ingrese el año (o 0 para todos): "))
                deteccion_y_descubrimiento(datos, anho)
            except ValueError:
                print("Año inválido.")
        elif opcion == "5":
            cantidad_y_tipo_deteccion(datos)
        elif opcion == "6":
            masa_promedio_y_tipo_deteccion(datos)
        elif opcion == "7":
            masa_planetas_vs_masa_estrellas(datos)
        elif opcion == "8":
            imagen = graficar_cielo(datos)
        elif opcion == "9":
            if len(imagen) > 0:
                filtrar_imagen_cielo(imagen)
            else:
                print("Primero debes generar la imagen del cielo (opción 8).")
        elif opcion == "0":
            print("\nGracias por usar el sistema de análisis de exoplanetas. ¡Hasta pronto!")
            break
        else:
            print("\nOpción no válida. Intente de nuevo.")
