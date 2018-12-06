
import docx
import os
from docx import Document
from docx.oxml.ns import qn
from docx.shared import Pt
from TranslateTest import translate

file = docx.Document("OriginalTestDoc.docx")
targetDoc = "finalDoc.docx"
print("段落数："+str(len(file.paragraphs)))
print("section数："+str(len(file.sections)))

#for section in file.sections:
#    print(section.start_type)

finalDoc = Document()
finalDoc.styles['Normal'].font.name = 'Times New Roman'
finalDoc.styles['Normal'].font.size = Pt(14)
finalDoc.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')


if os.path.exists(targetDoc):
    os.remove(targetDoc)

for i in range(len(file.paragraphs)):
    finalDoc.add_paragraph(translate(file.paragraphs[i].text))
    print(file.paragraphs[i].style.name)
    print("第"+str(i)+"段的内容是："+file.paragraphs[i].text)
    # format = file.paragraphs[i].text.parfmt.ParagraphFormat

finalDoc.save(targetDoc)