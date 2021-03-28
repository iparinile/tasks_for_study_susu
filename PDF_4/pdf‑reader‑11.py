# Напомним, что PyMuPDF импортируется как fitz
import fitz

original_pdf_path = "source/Computer-Vision-Resources.pdf"
extra_page_path = "dist/example-updated.pdf"
output_file_path = "dist/example-extended.pdf"

original_pdf = fitz.open(original_pdf_path)
extra_page = fitz.open(extra_page_path)

original_pdf.insertPDF(extra_page)
original_pdf.save(output_file_path)
