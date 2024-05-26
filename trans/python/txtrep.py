import fitz
from PyPDF2 import PdfReader

# Extract text from PDF
te = []
reader = PdfReader("rem.pdf")
for i in range(len(reader.pages)):
    page = reader.pages[i]
    te.append(page.extract_text())

# Function to replace text in the PDF
def replace_text_in_pdf(input_pdf_path, output_pdf_path, replacements):
    # Open the input PDF
    pdf_document = fitz.open(input_pdf_path)

    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        
        for old_text, new_text in replacements.items():
            text_instances = page.search_for(old_text)
            
            # Check if text_instances is not None
            if text_instances:
                # Loop through all instances of the text to be replaced
                for inst in text_instances:
                    rect = fitz.Rect(inst)  # Get the rectangle of the found text
                    # Remove the old text by covering it with a white rectangle
                    page.add_freetext_annot(rect, "", fontsize=12, fontname="helv", text_color=(1, 1, 1), fill_color=(1, 1, 1))
                    # Insert new text at the same location
                    page.insert_text(rect.tl, new_text, fontsize=12, color=(0, 0, 0))
    
    # Save the modified PDF to a new file
    pdf_document.save(output_pdf_path)
    pdf_document.close()

# Prepare the replacements dictionary
replacements = {}
for page_text in te:
    words = page_text.split()
    for word in words:
        replacements[word] = 'new text'

# Perform the replacements
input_pdf_path = 'rem.pdf'
output_pdf_path = 'output.pdf'
replace_text_in_pdf(input_pdf_path, output_pdf_path, replacements)

print(f"Text replacements complete. Output saved to {output_pdf_path}")
