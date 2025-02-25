import qrcode
from PIL import Image, ImageDraw, ImageFont

archivos = [
    ("Criterios_Ingreso_Mantencion_Egreso_Pacientes_UPC", "https://github.com/mmh80/protocolos-hospital/raw/main/Criterios_Ingreso_Mantencion_Egreso_Pacientes_UPC.pdf"),
    ("Monitoreo_Hemodinamico_Invasivo_No_Invasivo", "https://github.com/mmh80/protocolos-hospital/raw/main/Monitoreo_Hemodinamico_Invasivo_No_Invasivo.pdf"),
    ("Norma_IAAS_C_Difficile_2024", "https://github.com/mmh80/protocolos-hospital/raw/main/Norma_IAAS_C_Difficile_2024.pdf"),
    ("PC_Analgesia_Sedacion_BNM_UPC", "https://github.com/mmh80/protocolos-hospital/raw/main/PC_Analgesia_Sedacion_BNM_UPC.pdf"),
    ("Prono_Paciente_Critico_Adulto", "https://github.com/mmh80/protocolos-hospital/raw/main/Prono_Paciente_Critico_Adulto.pdf"),
    ("Protocolo_Instalacion_Manejo_Enfermeria_Linea_Arterial", "https://github.com/mmh80/protocolos-hospital/raw/main/Protocolo_Instalacion_Manejo_Enfermeria_Linea_Arterial.pdf"),
    ("Protocolo_Manejo_Linea_Arterial", "https://github.com/mmh80/protocolos-hospital/raw/main/Protocolo_Manejo_Linea_Arterial.pdf")
]

# Función para generar el QR con el nombre del archivo
def generar_qr_con_texto(url, nombre_archivo):
    # Generar QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Crear imagen del QR
    img_qr = qr.make_image(fill='black', back_color='white')

    # Asegurarse de que la imagen del QR esté en modo RGB
    img_qr = img_qr.convert('RGB')

    # Crear imagen final con espacio para el nombre del archivo
    imagen_final = Image.new('RGB', (img_qr.width, img_qr.height + 50), color='white')
    imagen_final.paste(img_qr, (0, 0))

    # Añadir el nombre del archivo debajo del QR
    draw = ImageDraw.Draw(imagen_final)
    font = ImageFont.load_default()
    text = nombre_archivo

    # Obtener el tamaño del texto con textbbox
    text_bbox = draw.textbbox((0, 0), text, font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Posicionar el texto en el centro
    text_position = ((imagen_final.width - text_width) // 2, img_qr.height + 10)

    # Dibujar el texto sobre la imagen
    draw.text(text_position, text, font=font, fill='black')

    # Guardar la imagen final
    imagen_final.save(f"{nombre_archivo}.png")

# Generar los códigos QR
for nombre, url in archivos:
    generar_qr_con_texto(url, nombre)

