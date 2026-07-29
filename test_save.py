import io
from docx import Document
import app

with open('/Users/lykenl/Downloads/Junxian_Lyken_Lin_Resume.docx', 'rb') as f:
    original = f.read()

buf = app.apply_revisions_to_docx(io.BytesIO(original), {"mappings": []})
doc2 = Document(buf)
print(doc2.paragraphs[0].text)
