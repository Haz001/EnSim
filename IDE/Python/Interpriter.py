import Functions;
#import string
Functions.console.show("True")
Functions.console.write.line("Booting");
##parts_t = [""];
##function_path;
Functions.console.show("False")
class interpriter:
    def tagger(comand):
        if("(" in comand):
            parts_t = str(comand).split("(");
            parts_t[1] = parts_t[1].replace(")","")
            parts_t[1] = parts_t[1].replace(";","")
            # parts_t[1] = parts_t[1].replace("'","")
            # parts_t[1] = parts_t[1].replace('"',"")
            #parts_t[1] = string.replace(str(parts_t[1]),");","")
        elif("=" in comand):
            parts_t = str(comand).split("=");
        interpriter.functionexe(parts_t)
    
    def functionexe(parts):
        if("." in parts[0]):
            function_path = str(parts[0]).split(".");
        elif(">" in parts[0]):
            function_path = str(parts[0]).split(">");
        else:
            function_path = ["console","error"]
        
        if(function_path[0].lower() == "console"):
            if(function_path[1].lower() == "show"):
                tmp_string = parts[1].replace('"',"")
                tmp_string = tmp_string.replace("'","")
                Functions.console.show(tmp_string)  
            elif(function_path[1].lower() == "error"):
                print("error");
            elif(function_path[1].lower() == "write"):
                if(function_path[2].lower() == "line"):
                    tmp_string = parts[1].replace('"',"")
                    tmp_string = tmp_string.replace("'","")
                    Functions.console.write.line(tmp_string) 

        
#interpriter.tagger("console.show('true')")#first line of code to run
interpriter.tagger("console.write.line('hey')")#second line of code to run
