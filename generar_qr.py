import qrcode

# Lista de URLs de los archivos PDF
urls = [
    'https://raw.githubusercontent.com/mmh80/protocolos-hospital/main/Criterios_Ingreso_Mantencion_Egreso_Pacientes_UPC.pdf',
    'https://raw.githubusercontent.com/mmh80/protocolos-hospital/main/Monitoreo_Hemodinamico_Invasivo_No_Invasivo.pdf',
    'https://raw.githubusercontent.com/mmh80/protocolos-hospital/main/Norma_IAAS_C_Difficile_2024.pdf',
    'https://raw.githubusercontent.com/mmh80/protocolos-hospital/main/PC_Analgesia_Sedacion_BNM_UPC.pdf',
    'https://raw.githubusercontent.com/mmh80/protocolos-hospital/main/Prono_Paciente_Critico_Adulto.pdf',
    'https://raw.githubusercontent.com/mmh80/protocolos-hospital/main/Protocolo_Instalacion_Manejo_Enfermeria_Linea_Arterial.pdf',
    'https://raw.githubusercontent.com/mmh80/protocolos-hospital/main/Protocolo_Manejo_Linea_Arterial.pdf'
]

# Generar los códigos QR para cada URL
for i, url in enumerate(urls, start=1):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Crear una imagen del QR y guardarla con un nombre único
    img = qr.make_image(fill='black', back_color='white')
    img.save(f'codigo_qr_{i}.png')

print("Códigos QR generados correctamente.")

