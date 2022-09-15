import glob
import json
import os

# Script that creates a json file with all md files of a specified folder and all it's suboflders.

# -----------------------
# prerequisite:
# pip install 
# -----------------------

# Inputs:
# -
# Output:
# questions.json will be created next to the script

inputDirectory = os.path.dirname(os.path.realpath(__file__))

outputFile = os.path.join(inputDirectory, "questions.json")
print('Input Directory: ', inputDirectory)
print('Output File: ', outputFile)

# Possible Question File Types
types = ('*.md', '*.markdown')

questions_directory = inputDirectory + '/_questions/'

questions = []

for quesiton_type in types:
    for path in glob.glob(questions_directory + '**/' + quesiton_type, recursive=True):
        file_name = os.path.basename(path)        
        relative_path = path.replace(questions_directory, "").replace("\\", "/").split(".")[:-1][0]
        print("Found {0} at path {1}".format(file_name, relative_path))
        
        question = {
            "path": relative_path
        }
        
        questions.append(question)


with open(outputFile, 'w') as f:
    f.write(json.dumps(questions))