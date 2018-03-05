import Interpriter
Interpriter.interprit.tagger('console.write.line("EnSim Shell")')
while(True):
    cmd = input(">")
    if(";" not in cmd ):
        cmd+=";"
    try:
        Interpriter.interprit.tagger(cmd)
    except:
        print("Error in shell")

