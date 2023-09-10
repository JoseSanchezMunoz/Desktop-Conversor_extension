# funcionalidades.py
# Contiene funciones para convertir extensiones de archivos.
# Maneja mensajes de confirmación, error e información.
# Es utilizado por la interfaz gráfica para realizar la conversión.

# Importamos los módulos y bibliotecas necesarios.
import os  # Importamos el módulo os para trabajar con rutas y archivos.
from tkinter import messagebox  # Importamos el módulo messagebox de tkinter para mostrar mensajes de diálogo.

# Definimos la clase Funcionalidades, que contiene métodos para realizar la conversión de extensiones de archivos.
class Funcionalidades:
    def __init__(self):
        pass  # El constructor de la clase no realiza ninguna acción específica.

    # Función para convertir archivos a una nueva extensión en la carpeta de origen a la carpeta de destino.
    def convertir_extensiones(self, carpeta_origen, carpeta_destino, extension_origen, extension_destino):
        # Obtenemos la lista de archivos con la extensión de origen en la carpeta de origen.
        archivos_a_convertir = [f for f in os.listdir(carpeta_origen) if f.endswith(extension_origen)]
        errores = []  # Creamos una lista para rastrear errores durante la conversión.

        # Recorremos la lista de archivos a convertir.
        for archivo in archivos_a_convertir:
            try:
                # Construimos los nombres de archivo con la nueva extensión en la carpeta de destino.
                nuevo_nombre = archivo.replace(extension_origen, extension_destino)
                archivo_origen = os.path.join(carpeta_origen, archivo)
                archivo_destino = os.path.join(carpeta_destino, nuevo_nombre)

                # Renombramos el archivo con la nueva extensión.
                os.rename(archivo_origen, archivo_destino)
            except Exception as e:
                errores.append(f"Error al convertir {archivo}: {str(e)}")  # Capturamos y registramos errores.

        # Si se producen errores, mostramos un mensaje de error con detalles.
        if errores:
            self.mostrar_mensaje_error("Se produjeron errores al convertir algunos archivos:\n\n" + "\n".join(errores))
        else:
            self.mostrar_mensaje_informacion("La conversión de extensiones se completó exitosamente.")  # Mostramos un mensaje de éxito si no hay errores.

    # Función para mostrar un mensaje de confirmación con la lista de archivos a convertir.
    def mostrar_confirmacion(self, mensaje, archivos):
        return messagebox.askyesno("Confirmar Conversión", f"{mensaje}\n\nArchivos a convertir:\n{', '.join(archivos)}")

    # Función para mostrar un mensaje de error.
    def mostrar_mensaje_error(self, mensaje):
        messagebox.showerror("Error", mensaje)

    # Función para mostrar un mensaje de información.
    def mostrar_mensaje_informacion(self, mensaje):
        messagebox.showinfo("Información", mensaje)
