"""
Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt, 
and so on, in a single folder and locates any gaps in the numbering
(such as if there is a spam001.txt and spam003.txt but no spam002.txt). 
Have the program rename all the later files to close this gap.
As an added challenge, write another program that can insert gaps into numbered files 
so that a new file can be added.

Solution by Mischa van den Burg
www.mischavandenburg.com

work in progress!
"""

from pathlib import Path, PurePath
import os, re

regex = re.compile(r"(([a-zA-Z])*)(([0-9])+)(\.txt)+$")
source = Path(Path.home() / 'python' / 'automatetheboringstuff' / 'chapter10' / 'textfiles' )

old_filenames = []
new_filenames = []

for folder_names, sub_folders, file_names in os.walk(source):
    for file_name in file_names:
        pattern = regex.search(file_name)
        old_filenames.append(pattern[3])

old_filenames = sorted(old_filenames)
first_number = int(old_filenames[0])
a = str(first_number)

b = []

for i in range(len(old_filenames)):
    x = str(first_number + i)
    b.append(x.zfill(3))
    # print(first_number + i)

print(b)
