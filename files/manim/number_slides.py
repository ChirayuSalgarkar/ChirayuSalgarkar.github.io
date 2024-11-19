# number_slides.py
# number_slides.py
from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import io
from datetime import date

def add_footer(input_pdf='slides.pdf', output_pdf='slides_numbered.pdf'):
    # Read the PDF
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Configuration
    PRESENTATION_TITLE = "Mathematical Animations"
    PRESENTER_NAME = "Chirayu Salgarkar"
    CURRENT_DATE = date.today().strftime("%B %d, %Y")
    FONT_SIZE = 10

    # Create page numbers and footer
    for page_num in range(len(reader.pages)):
        # Create a page with footer
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFillColor(white)

        # Set up footer positions (adjust these values as needed)
        footer_y = 20  # Distance from bottom
        title_x = 50   # Left side
        name_x = 250   # Center-left
        date_x = 400   # Center-right
        page_x = 550   # Right side

        # Draw footer elements
        can.setFont("Helvetica-Bold", FONT_SIZE)  # Using Helvetica-Bold as it's similar to Manim's default font
        can.drawString(title_x, footer_y, PRESENTATION_TITLE)
        
        can.setFont("Helvetica", FONT_SIZE)  # Regular weight for other elements
        can.drawString(name_x, footer_y, PRESENTER_NAME)
        can.drawString(date_x, footer_y, CURRENT_DATE)
        can.drawString(page_x, footer_y, f"Page {page_num + 1}")

        # Add a subtle line above the footer (optional)
        can.setLineWidth(0.5)
        can.line(40, footer_y + 15, 570, footer_y + 15)

        can.save()
        packet.seek(0)
        number_page = PdfReader(packet).pages[0]

        # Get the page from original PDF and merge
        page = reader.pages[page_num]
        page.merge_page(number_page)
        writer.add_page(page)

    # Save the result
    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)

if __name__ == '__main__':
    add_footer()