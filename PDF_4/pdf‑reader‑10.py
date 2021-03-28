# Напомним, что PyMuPDF импортируется как fitz
import fitz

input_file = "source/Computer-Vision-Resources.pdf"
output_file = "dist/Computer-Vision-Resources-rearranged.pdf"

# Определите страницы для сохранения - 1, 2 и 4
file_handle = fitz.open(input_file)
pages_list = [0, 1, 3]

# Выберите страницы и сохраните вывод
file_handle.select(pages_list)
file_handle.save(output_file)
