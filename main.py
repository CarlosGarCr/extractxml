import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import filedialog
import openpyxl

# Crear una ventana de búsqueda de archivos
root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal

# Solicitar al usuario que seleccione un archivo XML
file_path = filedialog.askopenfilename(filetypes=[("Archivos XML", "*.xml")])

# Verificar si se seleccionó un archivo
if file_path:
    # Parsear el archivo XML
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Crear un nuevo archivo Excel
    wb = openpyxl.Workbook()
    ws = wb.active

    # Agregar encabezados de columnas
    headers = ["Unidad", "Descripcion", "ValorUnitario", "Cantidad", "Importe"]
    ws.append(headers)

    # Iterar a través de cada elemento <cfdi:Concepto> dentro de <cfdi:Conceptos>
    for concepto in root.findall('.//{http://www.sat.gob.mx/cfd/4}Conceptos/{http://www.sat.gob.mx/cfd/4}Concepto'):
        unidad = concepto.get('Unidad')
        descripcion = concepto.get('Descripcion')
        valor_unitario = concepto.get('ValorUnitario')
        cantidad = concepto.get('Cantidad')
        importe = concepto.get('Importe')

        # Agregar los datos del concepto a la hoja de cálculo
        concepto_data = [unidad, descripcion, valor_unitario, cantidad, importe]
        ws.append(concepto_data)

    # Guardar el archivo Excel
    excel_file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Archivos Excel", "*.xlsx")])
    if excel_file_path:
        wb.save(excel_file_path)
        print("Los datos se han guardado en el archivo Excel:", excel_file_path)


