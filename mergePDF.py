import os
from PyPDF2 import PdfMerger

def merge_pdfs(directory):
    # Create a PdfMerger object
    merger = PdfMerger()

    # Get the list of PDF files in the specified directory
    pdf_files = [f for f in os.listdir(directory) if f.endswith('.pdf')]

    # Sort the PDF files alphabetically
    pdf_files.sort()

    # Loop through all the PDF files in the specified directory
    for filename in pdf_files:
        # Open the PDF file in read-binary mode
        file = open(f'{directory}/{filename}', 'rb')
        # Add the PDF file to the merger
        merger.append(fileobj=file)
        # Close the PDF file
        file.close()

    # Create the output PDF file
    output = open(f'{directory}/merged.pdf', 'wb')
    # Write all the merged PDFs to the output file
    merger.write(output)
    # Close the output PDF file
    output.close()

# Get the directory containing the PDF files as an input
directory = input('Enter the directory containing the PDF files: ')

# Call the function to merge the PDFs in the specified directory
merge_pdfs(directory)
