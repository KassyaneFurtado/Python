'''O PROGRAMA DEVE PEGAR O ARQUIVO .CSV E DE ACORDO COM OS CAMPOS GERAR UMA ETIQUETA'''

import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import qrcode
from PIL import Image
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont



def create_pdf(data, output_filename):
    c = canvas.Canvas(output_filename, pagesize=landscape((30*mm, 25*mm)))
    
    field_positions = [
        (2, 20),  # Posição do campo CODENTRADA (x, y)
        (20,2),  # Posição do campo CODBARRAS (x, y)
        (2, 10),  # Posição do campo DATA (x, y)
        (2, 8),  # Posição do campo OBS (x, y)
        (2, 15), #Posição do campo CODBARRASqr
    ]
    field_widths = [10, 10, 10, 10]  # Largura máxima para cada campo
    field_font_sizes = [2, 2, 2, 2]  # Tamanho da fonte para cada campo
    
    for _, row_data in data.iterrows():
        c.showPage()  # Inicia uma nova página para cada linha do arquivo CSV
        for i, (position, value, width, font_size) in enumerate(zip(field_positions, [row_data["CODENTRADA"], row_data["CODBARRAS"], row_data["DATA"], row_data["OBS"]], field_widths, field_font_sizes)):
            c.setFont("Helvetica", font_size)  # Define o tamanho da fonte
            if i == 1:  # Se for o campo "CODBARRAS", gera o QR Code
                qr_img = generate_qr_code(row_data["CODBARRASqr"])
                c.drawImage(qr_img, position[0], position[1], width=10, height=10)  # Coloca a imagem do QR Code
            else:
                c.drawString(position[0], position[1], f"{value[:width]}")  # Limita o comprimento do campo ao valor especificado em field_widths
    
    c.save()

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img_path = "qrcode.png"
    img.save(img_path)
    return img_path

def read_csv(filename):
    return pd.read_csv(filename)

if __name__ == "__main__":
    filename = "ETIQUETASNB.csv"  # Nome do arquivo CSV
    data = read_csv(filename)
    output_filename = "output.pdf"  # Nome do arquivo PDF de saída
    create_pdf(data, output_filename)
