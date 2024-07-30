import os
import PyPDF2 as pdf

workingDirectory = os.path.dirname(os.path.abspath(__file__))
formulaireDirectory = os.path.join(workingDirectory, 'formulaire')

#print(formulaireDirectory)
#print(type(formulaireDirectory))
formulaireReader = pdf.PdfReader(os.path.join(formulaireDirectory, '2041-rd_4298.pdf'))

print(len(formulaireReader.pages))
print(formulaireReader.pages[0].extract_text())
