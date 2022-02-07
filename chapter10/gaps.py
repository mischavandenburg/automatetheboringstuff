"""
Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt, 
and so on, in a single folder and locates any gaps in the numbering
(such as if there is a spam001.txt and spam003.txt but no spam002.txt). 
Have the program rename all the later files to close this gap.
As an added challenge, write another program that can insert gaps into numbered files 
so that a new file can be added.

Solution by Mischa van den Burg
www.mischavandenburg.com
"""

from pathlib import Path, PurePath
import os, re

regex = re.compile('spam')
source = Path(Path.home() / 'python' / 'automatetheboringstuff' / 'chapter10' / 'textfiles' )

"""
TO DO
create 3 regex statements
start with the .txt file extention and remove that
i already made this in one of the programs, make it that it removes it

regex matching all letters
regex matching all numbers

for matching the numbers

it only needs to do gaps, no need to think about all the other cases
keep it simple

if a != b + 1, next number is a + 1



"""


for folder_names, sub_folders, file_names in os.walk(source):
    for file_name in file_names:

print(working_list)
#            print(test)
           # print(file_name)
