import aspose.words as aw

# Load the word document
name_of_document = "CMS Testing Checklist.docx"
document = aw.Document(name_of_document)

name_of_document = name_of_document[:len(name_of_document) - 5]
document.save(name_of_document + ".pdf")