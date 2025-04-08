import glob
import json
import os
import csv

# Script that creates a json file with all md files of a specified folder and all it's suboflders.

# -----------------------
# prerequisite:
# pip install 
# -----------------------

# Inputs:
# -
# Output:
# questions.json and questions.csv will be created next to the script

inputDirectory = os.path.dirname(os.path.realpath(__file__))

outputFileJson = os.path.join(inputDirectory, "..", "questions.json")
outputFileCsv = os.path.join(inputDirectory, "..", "questions.csv")

print('Input Directory: ', inputDirectory)
print('Output File json: ', outputFileJson)
print('Output File csv: ', outputFileCsv)

# Possible Question File Types
types = ('*.md', '*.markdown')

questions_directory = os.path.join(inputDirectory, "..", 'questions/')

questions = []
csv_header = ['title', 'question']

with open(outputFileCsv, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csv_header)

    for quesiton_type in types:
        for path in glob.glob(questions_directory + '**/' + quesiton_type, recursive=True):
            file_name = os.path.basename(path)        
            relative_path = path.replace(questions_directory, "").replace("\\", "/").split(".")[:-1][0]
            print("Found {0} at path {1}".format(file_name, relative_path))
            
            question_title = ""
            question_content = ""
            question_file = open(path, "r")
            
            is_content_line = False
            
            for line in question_file:
                if line.startswith("title:"):
                    question_title = line.split(":")[1].strip().replace('"', "")
                if is_content_line and line:
                    question_content += line
                if question_title and line.startswith("---"):
                    is_content_line = True
            
            writer.writerow([question_title, question_content.replace("\r", " ").replace("\n", " ")])
            
            question = {
                "path": relative_path
            }
            
            questions.append(question)



with open(outputFileJson, 'w') as f:
    f.write(json.dumps(questions))