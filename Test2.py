import os
import fitz  # PyMuPDF

workingDirectory = os.path.dirname(os.path.abspath(__file__))
formulaireDirectory = os.path.join(workingDirectory, 'formulaire')

# Chemin du fichier PDF existant
input_pdf_path = os.path.join(formulaireDirectory, '2041-rd_4298.pdf')

# Chemin du fichier PDF de sortie
output_pdf_path = os.path.join(workingDirectory, 'Output.pdf')

# Ouvrir le PDF existant
document = fitz.open(input_pdf_path)

# Sélectionner la première page
first_page = document.load_page(0)

# Ajouter du contenu à la page
content = "Tomate !!!"
first_page.insert_text((100, 100), content, fontsize=12, color=(0, 0, 0))

# Sauvegarder le PDF modifié
document.save(output_pdf_path)

# Fermer le document
document.close()
