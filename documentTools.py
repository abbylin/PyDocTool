
import docx
from TranslateTest import translate

file = docx.Document("OriginalTestDoc.docx")
print("段落数："+str(len(file.paragraphs)))
print("section数："+str(len(file.sections)))

#for section in file.sections:
#    print(section.start_type)

for i in range(10):
    print(file.paragraphs[i].style.name)
    print("第"+str(i)+"段的内容是："+file.paragraphs[i].text)
    print(translate(file.paragraphs[i].text))
    #format = file.paragraphs[i].text.parfmt.ParagraphFormat
