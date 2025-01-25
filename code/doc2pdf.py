#%

#Importing dependencies
from docx2pdf import convert

word_file_path = 'input.docx'  # Replace with your Word file path
pdf_file_path = 'output.pdf'  # Replace with your desired PDF file path


convert(word_file_path, pdf_file_path)
print(f"Successfully converted {word_file_path} to {pdf_file_path}")
