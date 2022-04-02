from docx import Document
import xmlParser
import userInput
import docWorker

tepmplateFile = userInput.chooseTemplate()     # Выбор файла шаблона
templateData = xmlParser.parse(tepmplateFile)  # Парсинг файла
counts = userInput.getTasksCount()
fileName = userInput.getReportName()

document = Document()

for j in range(counts):
    for i in templateData:
        if ("Head" in i):
            docWorker.addHead(document, templateData[i])
        
        elif("Paragraph" in i):
            docWorker.addParagraph(document, templateData[i])

        elif ("FileText" in i):
            docWorker.addFileText(document, templateData[i])

        elif ("Picture" in i):
            docWorker.addPicture(document, templateData[i])

        
    document.add_page_break()


document.save(f'{fileName}.docx')