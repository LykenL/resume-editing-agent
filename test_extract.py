import app
from docx import Document

paras = app.extract_paragraphs_from_docx('/Users/lykenl/Downloads/Junxian_Lyken_Lin_Resume.docx')
for p in paras[:5]:
    print(f"Extracted: {p}")
