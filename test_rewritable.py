import re
from docx import Document

def _is_rewritable_paragraph(paragraph) -> bool:
    text = paragraph.text.strip()
    if not text or len(text) < 30:
        return False
    if text.startswith(('•', '-', '', '·', '*')):
        return True
    style_name = (paragraph.style.name or "").lower()
    if 'list' in style_name:
        return True
    if len(text) > 100:
        if re.search(r'\b20\d{2}\s*[-–—]\s*(20\d{2}|Present)\b', text, re.IGNORECASE):
            return False
        return True
    return False

doc = Document('/Users/lykenl/Downloads/Junxian_Lyken_Lin_Resume.docx')
for i, p in enumerate(doc.paragraphs):
    text = p.text.strip()
    if not text: continue
    
    is_rw = _is_rewritable_paragraph(p)
    if is_rw:
        print(f"✅ REWRITABLE: {text[:60]}...")
    else:
        print(f"❌ SKIPPED   : {text[:60]}...")
