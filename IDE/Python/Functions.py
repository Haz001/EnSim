class console:#class of console
    c_show_var = False;#varible for console show
    def show(cmd1):#show comand
        
        try:
            if (str(cmd1).lower() == "get"):
                #print("Get")
                return console.c_show_var;                
            else:
                
                console.c_show_var = bool(str(cmd1).capitalize());
                #print("Set")
        except:
            print("Error in functions");
    
    class write:
        def line(cmd1):
            if(console.c_show_var):
                print(cmd1)

            
                

            
            
                

