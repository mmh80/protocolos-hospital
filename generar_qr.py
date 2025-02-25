import qrcode

archivos = [
    ("Criterios_Ingreso_Mantencion_Egreso_Pacientes_UPC", "https://github.com/mmh80/protocolos-hospital/raw/main/Criterios_Ingreso_Mantencion_Egreso_Pacientes_UPC.pdf"),
    ("Monitoreo_Hemodinamico_Invasivo_No_Invasivo", "https://github.com/mmh80/protocolos-hospital/raw/main/Monitoreo_Hemodinamico_Invasivo_No_Invasivo.pdf"),
    ("Norma_IAAS_C_Difficile_2024", "https://github.com/mmh80/protocolos-hospital/raw/main/Norma_IAAS_C_Difficile_2024.pdf"),
    ("PC_Analgesia_Sedacion_BNM_UPC", "https://github.com/mmh80/protocolos-hospital/raw/main/PC_Analgesia_Sedacion_BNM_UPC.pdf"),
    ("Prono_Paciente_Critico_Adulto", "https://github.com/mmh80/protocolos-hospital/raw/main/Prono_Paciente_Critico_Adulto.pdf"),
    ("Protocolo_Instalacion_Manejo_Enfermeria_Linea_Arterial", "https://github.com/mmh80/protocolos-hospital/raw/main/Protocolo_Instalacion_Manejo_Enfermeria_Linea_Arterial.pdf"),
    ("Protocolo_Manejo_Linea_Arterial", "https://github.com/mmh80/protocolos-hospital/raw/main/Protocolo_Manejo_Linea_Arterial.pdf")
]

for nombre, url in archivos:
    qr = qrcode.make(url)
    qr.save(f"{nombre}.png")

