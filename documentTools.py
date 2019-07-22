# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'documentTools.py'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import docx
import os
from docx import Document
from docx.oxml.ns import qn
from docx.shared import Pt
# from TranslateTest import translate
from googletrans import Translator

def beginTranslate(App, src='', target=''):
    file = docx.Document(src)
    totalParagraphs = len(file.paragraphs)
    # print("段落数：" + str(len(file.paragraphs)))
    # print("section数：" + str(len(file.sections)))

    finalDoc = Document()
    finalDoc.styles['Normal'].font.name = 'Times New Roman'
    finalDoc.styles['Normal'].font.size = Pt(14)
    finalDoc.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')

    if os.path.exists(target):
        os.remove(target)

    translator = Translator()
    for i in range(len(file.paragraphs)):
        result = translator.translate(file.paragraphs[i].text, dest="zh-CN")
        result.replace("（", "(")
        result.replace("）", ")")
        finalDoc.add_paragraph(result.text)
        print("正在处理第" + str(i) + "段")
        App.updateProgress(i/totalParagraphs, "正在处理第" + str(i) + "段")
        # print(file.paragraphs[i].style.name)
        # print("第" + str(i) + "段的内容是：" + file.paragraphs[i].text)
        # print("翻译结果: "+translate('早上好'))
        # print("翻译结果:" + translate(file.paragraphs[i].text))
        # format = file.paragraphs[i].text.parfmt.ParagraphFormat

    finalDoc.save(target)
