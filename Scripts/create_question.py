import os
import sys

# Script that creates a new markdown question file in the questions folder.

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

question_body = """---
layout: post
title: \"{0}\"
parent: Katas
---
""".format(question_title)

is_content_line = False

for line in question_body_raw.splitlines():
    line = line.strip()
    
    if is_content_line:
        question_body += "{0}\n".format(line)
        
    if line.startswith("---"):
        is_content_line = True
        
title_as_filename = question_title.lower().replace("?", "").replace(" ", "_")
output_file = os.path.join(base_directory, "..", "questions", "{0}.md".format(title_as_filename))

if not question_title or not is_content_line:
    print("No a valid Question - stopping")
    exit(0)

print('Output File: ', output_file)

with open(output_file, 'w') as f:
    f.write(question_body)