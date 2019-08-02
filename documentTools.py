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
from googletrans import Translator


def beginTranslate(App, src='', target=''):
    file = docx.Document(src)
    totalParagraphs = len(file.paragraphs)

    finalDoc = Document()
    finalDoc.styles['Normal'].font.name = 'Times New Roman'
    finalDoc.styles['Normal'].font.size = Pt(14)
    finalDoc.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')

    if os.path.exists(target):
        os.remove(target)

    translator = Translator()
    for i in range(len(file.paragraphs)):
        result = translator.translate(file.paragraphs[i].text, dest="zh-CN")
        result.text.replace("（", "(")
        result.text.replace("）", ")")
        finalDoc.add_paragraph(result.text)
        print("正在处理第" + str(i) + "段")
        App.updateProgress(i/totalParagraphs, "正在处理第" + str(i) + "段")

    finalDoc.save(target)
