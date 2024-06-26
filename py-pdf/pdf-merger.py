import PyPDF2
import sys

input = sys.argv[2:]
merged_pdf_name = sys.argv[1]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write(merged_pdf_name)

pdf_combiner(input)