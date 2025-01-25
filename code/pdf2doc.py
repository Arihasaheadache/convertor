#%

#Importing dependencies
from pdf2docx import Converter

pdf_file_path = 'input.pdf'  # Replace with your PDF file path
word_file_path = 'output.docx'  # Replace with your desired Word file path

cv = Converter(pdf_file_path)
cv.convert(word_file_path, start=0, end=None)
cv.close()

print(f"Successfully converted {pdf_file_path} to {word_file_path}")


