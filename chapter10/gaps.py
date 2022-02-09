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

name = "spam001.txt"

result = regex.search(name)

old_filenames = []
new_filenames = []

# print(result.groups())
"""
if a != b + 1, next number is a + 1
"""

for folder_names, sub_folders, file_names in os.walk(source):
    for file_name in file_names:
        pattern = regex.search(file_name)
        print(pattern[3])
        old_filenames.append(int(pattern[3]))


print(sorted(old_filenames))

old_filenames = sorted(old_filenames)


for i in old_filenames:
    if i != i + 1:
        new_filenames.append(i+1)
    else: 
        new_filenames.append(i)

print(new_filenames)
