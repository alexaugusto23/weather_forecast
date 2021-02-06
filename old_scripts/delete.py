import os

def deletar():
    path_del = os.getcwd()
    os.chdir(path_del) 
    dir = os.listdir(path_del)
    #print(dir)
    #print(path_del)
    #os.system("cls")
    
    for root, dirs, files in os.walk(path_del):
        for file in files:
            file_path = os.path.join(file)
            if "weather.json" == file:
                os.remove(file_path)
            else: print("file não encontrado")
    

deletar()