from pypdf import PdfReader
import pdfplumber
import nltk
from nltk.stem import WordNetLemmatizer 
import fitz
from PyPDF2 import PdfReader
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from io import BytesIO
import os
from reportlab.lib.pagesizes import letter

#Data extraction
#text
te=[]
ta=[]
tl=[]
lem=[]

reader=PdfReader("rem.pdf")
for i in range(len(reader.pages)):
    page=reader.pages[i]
    te.append(page.extract_text())
    '''for j in page.images:
        with open(j.name,"wb") as f:
            f.write(j.data
                    )'''


#table extraction
readerp=pdfplumber.open("rem.pdf")
for i in readerp.pages:
    ta.append(i.extract_tables())

#tokenisation
for i in te:
    tokens = nltk.word_tokenize(i)
    tl.append(tokens)
#wordlemtization
wl = WordNetLemmatizer()

# Lemmatize each token individually
lemmatized_tokens = []
for tokens in tl:
    lemmatized_sentence = [wl.lemmatize(token) for token in tokens]
    lemmatized_tokens.append(lemmatized_sentence)
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
def entn():
    from transformers import MBartForConditionalGeneration,MBart50TokenizerFast
    model=MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-one-to-many-mmt")
    tokenizer=MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-one-to-many-mmt",src_lang="en_XX")

    c=0
    tra=[]
    for i in lemmatized_tokens:
        tr=[]
        for j in i: 
            print(c)
            article_en=str(j)
            model_inputs=tokenizer(article_en,return_tensors="pt")
            genrated_token=model.generate(**model_inputs,forced_bos_token_id=tokenizer.lang_code_to_id["ta_IN"])
            translation=tokenizer.batch_decode(genrated_token,skip_special_tokens=True)
            tra.append(str(translation[0]))
            c+=1
    print(tra)
    replacements = {}
    cl=0
    while(cl<len(tra)):
        for page_text in te:
            words = page_text.split()
            for word in words:
                replacements[word] = str(tra[cl])
                cl+=1

    # Perform the replacements
    print(replacements)
    input_pdf_path = 'rem.pdf'
    output_pdf_path = 'output.pdf'
    replace_text_in_pdf(input_pdf_path, output_pdf_path, replacements)

    print(f"Text replacements complete. Output saved to {output_pdf_path}")

def enhi():
    from transformers import MBartForConditionalGeneration,MBart50TokenizerFast
    model=MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-one-to-many-mmt")
    tokenizer=MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-one-to-many-mmt",src_lang="en_XX")

    c=0
    tra=[]
    for i in lemmatized_tokens:
        tr=[]
        for j in i: 
            print(c)
            article_en=str(j)
            model_inputs=tokenizer(article_en,return_tensors="pt")
            genrated_token=model.generate(**model_inputs,forced_bos_token_id=tokenizer.lang_code_to_id["hi_IN"])
            translation=tokenizer.batch_decode(genrated_token,skip_special_tokens=True)
            tra.append(str(translation[0]))
            c+=1
    print(tra)
def enma():
    from transformers import MBartForConditionalGeneration,MBart50TokenizerFast
    model=MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-one-to-many-mmt")
    tokenizer=MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-one-to-many-mmt",src_lang="en_XX")

    c=0
    tra=[]
    for i in lemmatized_tokens:
        tr=[]
        for j in i: 
            print(c)
            article_en=str(j)
            model_inputs=tokenizer(article_en,return_tensors="pt")
            genrated_token=model.generate(**model_inputs,forced_bos_token_id=tokenizer.lang_code_to_id["ml_IN"])
            translation=tokenizer.batch_decode(genrated_token,skip_special_tokens=True)
            tr.append(translation)
            c+=1
        tra.append(tr)
    print(tra)
def ente():
    from transformers import MBartForConditionalGeneration,MBart50TokenizerFast
    model=MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-one-to-many-mmt")
    tokenizer=MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-one-to-many-mmt",src_lang="en_XX")

    c=0
    tra=[]
    for i in lemmatized_tokens:
        tr=[]
        for j in i: 
            print(c)
            article_en=str(j)
            model_inputs=tokenizer(article_en,return_tensors="pt")
            genrated_token=model.generate(**model_inputs,forced_bos_token_id=tokenizer.lang_code_to_id["te_IN"])
            translation=tokenizer.batch_decode(genrated_token,skip_special_tokens=True)
            tr.append(translation)
            c+=1
        tra.append(tr)
    print(tra)
def enmr():
    from transformers import MBartForConditionalGeneration,MBart50TokenizerFast
    model=MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-one-to-many-mmt")
    tokenizer=MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-one-to-many-mmt",src_lang="en_XX")

    c=0
    tra=[]
    for i in lemmatized_tokens:
        tr=[]
        for j in i: 
            print(c)
            article_en=str(j)
            model_inputs=tokenizer(article_en,return_tensors="pt")
            genrated_token=model.generate(**model_inputs,forced_bos_token_id=tokenizer.lang_code_to_id["mr_IN"])
            translation=tokenizer.batch_decode(genrated_token,skip_special_tokens=True)
            tr.append(translation)
            c+=1
        tra.append(tr)
    print(tra)
def engu():
    from transformers import MBartForConditionalGeneration,MBart50TokenizerFast
    model=MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-one-to-many-mmt")
    tokenizer=MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-one-to-many-mmt",src_lang="en_XX")

    c=0
    tra=[]
    for i in lemmatized_tokens:
        tr=[]
        for j in i: 
            print(c)            
            article_en=str(j)
            model_inputs=tokenizer(article_en,return_tensors="pt")
            genrated_token=model.generate(**model_inputs,forced_bos_token_id=tokenizer.lang_code_to_id["gu_IN"])
            translation=tokenizer.batch_decode(genrated_token,skip_special_tokens=True)
            tr.append(translation)
            c+=1
        tra.append(tr)
    print(tra)
entn()

