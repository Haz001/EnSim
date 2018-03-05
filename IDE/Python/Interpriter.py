import Functions;
#import string
Functions.console.show("True")
Functions.console.write.line("Booting");
##parts_t = [""];
##function_path;
Functions.console.show("False")
class interprit:
    def tagger(comand):
        parts_t = ["console.error"+"what"]
        if("(" in comand):
            parts_t = str(comand).split("(");
            parts_t[1] = parts_t[1].replace(")","")
        elif("=" in comand):
            parts_t = str(comand).split("=");
        
        if(";" in parts_t[1]):
            parts_t[1] = parts_t[1].replace(";","")
        interprit.functionexe(parts_t)
    
    def functionexe(parts):
        if("." in parts[0]):
            function_path = str(parts[0]).split(".");
        elif(">" in parts[0]):
            function_path = str(parts[0]).split(">");
        else:
            function_path = ["console","error"]
        
        if(function_path[0].lower() == "console"):
            if(function_path[1].lower() == "show"):
                tmp_string = interprit.argint(parts[1])
                
                Functions.console.show(tmp_string)  
            elif(function_path[1].lower() == "error"):
                print("Error forced");
            elif(function_path[1].lower() == "write"):
                if(function_path[2].lower() == "line"):
                    tmp_string = interprit.argint(parts[1])
                    Functions.console.write.line(tmp_string)
    def argint(arg):
        if ('"' in arg):
            return(arg.replace('"',""))
        elif("'" in arg):
            return(arg.replace("'",""))
            
                
##            open_speach
##            for (char in arg):
                

        
#interprit.tagger("console.show('true')")#first line of code to run
#interprit.tagger("console.write.line('hey')")#second line of code to run
