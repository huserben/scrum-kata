import os
import sys
import csv

base_directory = os.path.dirname(os.path.realpath(__file__))

if len(sys.argv) != 2:
    print("Need exactly 1 inputs - Path to csv file")

input_csv = sys.argv[1]
print("Using the following input file: {0}".format(input_csv))

with open(input_csv, newline='', encoding='utf-8') as csvfile:
    question_reader = csv.reader(csvfile, delimiter=';', quotechar='|')
    
    is_header_row = True
    
    for row in question_reader:
        if is_header_row:
            is_header_row = False
            continue
        
        if len(row) < 2:
            continue
        
        question_title = row[0]        
        question_body_raw = row[1]

        if not question_title or not question_body_raw:
            print("No a valid Question - skipping. Question: {0} - {1}".format(question_title, question_body_raw))
            continue
        
        question_body = """---
layout: post
title: \"{0}\"
parent: Katas
---
{1}
""".format(question_title, question_body_raw)                

        title_as_filename = question_title.lower().replace("?", "").strip().replace(" ", "_")
        output_file = os.path.join(base_directory, "..", "questions", "{0}.md".format(title_as_filename))

        print('Output File: ', output_file)

        with open(output_file, 'w', encoding="utf-8") as f:
            f.write(question_body)