import PyPDF2
import json

def read_file(file):
    if file.name.endswith('.pdf'):
        try:
            text = ""
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)
            for page_number in range(num_pages):
                page = pdf_reader.pages[page_number]
                text += page.extract_text()
            return text
        except Exception as e:
            raise Exception('Error in reading the PDF file')
    elif file.name.endswith('.txt'):
        return file.read().decode("utf-8")
    
    else:
        raise Exception('unsupported file format, only pdf and text file supooorts')

def get_table_data(quiz_str):
    quiz = json.loads(quiz_str)
    quiz_table = []
    for key,value in quiz.items():
        QNO = value['no']
        mcq = value['mcq']
        options = " | ".join(
            #list comprehension
            [
                f"{option}:{option_value}"
                for option , option_value in value['options'].items()
            ]
        )
        correct = value['correct']
        quiz_table.append({"MCQ":mcq,"Choices":options,"Correct":correct})
    
    return quiz_table