import os
import sys

# Script that creates a new markdown question file in the _questions folder.

# -----------------------
# prerequisite:
# pip install 
# -----------------------

# Inputs:
# - Question Title
# - Question 
# Output:
# question.md named according to the title passed

base_directory = os.path.dirname(os.path.realpath(__file__))

if len(sys.argv) != 3:
    print("Need exactly 2 inputs - Title and Question Body")

question_title = sys.argv[1]
question_body_raw = sys.argv[2]

question_body = ""
is_content_line = False

for line in question_body_raw.splitlines():
    line = line.strip()
    
    if is_content_line:
        question_body += "{0}\r".format(line)
        
    if line.startswith("---"):
        is_content_line = True
        

output_file = os.path.join(base_directory, "_questions", "{0}.md".format(question_title.lower().replace(" ", "_")))

print('Output File: ', output_file)

with open(output_file, 'w') as f:
    f.write(question_body)