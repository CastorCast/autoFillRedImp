import os
import PyPDF2 as pdf

workingDirectory = os.path.dirname(os.path.abspath(__file__))
formulaireDirectory = os.path.join(workingDirectory, 'formulaire')

#print(formulaireDirectory)
#print(type(formulaireDirectory))
formulaireReader = pdf.PdfReader(os.path.join(formulaireDirectory, '2041-rd_4298.pdf'))

print("Page =", len(formulaireReader.pages))
#first_page = formulaireReader.pages[0].extract_text()
first_page = formulaireReader.pages[0]
print(type(first_page))
content_FP = first_page.get_contents()

data = content_FP.get_data()
#print(type(data))
decoded_data = data.decode('utf-8')

lines = decoded_data.splitlines()
#print(type(lines[0]))
lines[0] = "Tomate !!!"
output = ""
for line in lines :
    output += line + '\n'

encoded_data = output.encode('utf-8')
if content_FP.decoded_self is not None :
    content_FP.decoded_self.set_data(encoded_data)
else :
    content_FP.set_data(encoded_data)
#first_page.get_contents().set_data(encoded_data)

first_page["/Contents"] = content_FP.decoded_self
#print(type(first_page))

#print(first_page["/Contents"])

writer = pdf.PdfWriter()
#writer.add_page(first_page)

#writer.write('Output.pdf')
