import Interpriter
import os

directory = os.getcwd()+"\\"

file_paths = []
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.es'):
            file_paths.append(file);
##            print(file_paths)
            print(str(file_paths.index(file))+" - "+file)


    int_c = int(input("choose file:\n>"))
    es_file = open(file_paths[int_c])
    x = es_file.read()
    cmds = x.split("\n")
    Interpriter.interprit.tagger(cmds)

