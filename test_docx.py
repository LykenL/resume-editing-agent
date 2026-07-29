from docx import Document

doc = Document('/Users/lykenl/Downloads/Junxian_Lyken_Lin_Resume.docx')
for i, p in enumerate(doc.paragraphs):
    text = p.text.strip()
    if not text: continue
    
    style_name = p.style.name if p.style else "None"
    
    # Check bold runs
    runs = p.runs
    bold_runs = sum(1 for r in runs if r.bold and r.text.strip())
    total_text_runs = sum(1 for r in runs if r.text.strip())
    all_bold = (bold_runs == total_text_runs) and total_text_runs > 0
    
    print(f"[{i}] Style: {style_name:20} | Length: {len(text):3} | AllBold: {all_bold} | Text: {text[:80]}")
