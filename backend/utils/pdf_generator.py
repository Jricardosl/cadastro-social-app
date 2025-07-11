from reportlab.lib.pagesizes import letter # type: ignore
from reportlab.pdfgen import canvas # type: ignore
from io import BytesIO
from flask import send_file # type: ignore

def generate_pdf(inscricao):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Ficha de Inscrição - Programa Social")

    c.setFont("Helvetica", 12)
    y = height - 100
    line_height = 20

    for key, value in inscricao.items():
        c.drawString(50, y, f"{key.capitalize()}: {value}")
        y -= line_height

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer
