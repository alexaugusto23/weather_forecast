import os
import json

class DelCre:
    
    def delcre():
        #Deletando e criando json
        os.chdir("C:/git/weather_forecast") #local
        #os.chdir("/home/site/wwwroot") #azure
        path = os.getcwd()
        path1 = os.path.join(path,"weather_forecast")
        path2 = os.path.join(path1,"weather_forecast")

        print(f'path2: {path2}')
        chdir = os.chdir(path2)
        path_file = os.path.join(path2,"weather.json")
        print(path_file)
        for root, dirs, files in os.walk(".", topdown=False):
            for file_name in files:
                #print(os.path.join(root, file_name))
                if "weather.json" == file_name:
                    print(True)
                    os.remove(path_file)
                    print("-"*80)
                    print("Arquivo weather.json removido.......")
                else:
                    print("Criando weather.json")
        os.system("scrapy crawl weather -o weather.json")
        os.system("cls")
        print("-"*80)
        print("Criação do weather.json concluído.......")
        return path_file