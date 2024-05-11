import os
import PyPDF2
import json
import traceback

def read_file(file):
    if file.name.endswith('.pdf'):
        try:
            pdf_reader = PyPDF2.PdfFileReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            raise Exception('Error in reeading the PDF file')
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
        quiz_table.append({"Q.NO.":QNO,"MCQ":mcq,"Choices":options,"Correct":correct})
    
    return quiz_table