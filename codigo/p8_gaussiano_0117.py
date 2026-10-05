#Matias Lopez 0117
import cv2

# Cargar la imagen
imagen = cv2.imread("imagenes/zebradios.jpg")

imagen = cv2.imread("imagenes/zebradios.jpg")

if imagen is None:
    print("ERROR: No encuentro zebradios.jpg")
    print("Revisa que esté en la carpeta imagenes")
    exit()
else:
    print("Imagen cargada correctamente")

# Aplicar filtro de mediana
imagen_filtrada = cv2.medianBlur(
    imagen,
    5
)

# Mostrar imágenes
cv2.imshow("Imagen original", imagen)
cv2.imshow("Imagen con filtro de mediana", imagen_filtrada)

# Guardar resultado
cv2.imwrite(
    "../resultados/zebradios_mediana.jpg",
    imagen_filtrada
)

print("Filtro de mediana aplicado correctamente.")
print("Resultado guardado en:")
print("../resultados/zebradios_mediana.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()
print("Matias Lopez NC 0117")