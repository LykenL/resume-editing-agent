from docx import Document
doc = Document('/Users/lykenl/Downloads/Junxian_Lyken_Lin_Resume.docx')
p = doc.paragraphs[0]
for i, r in enumerate(p.runs):
    print(f"Run {i}: bold={r.bold} text='{r.text}'")
