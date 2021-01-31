import os

def deletar():
    path = os.getcwd()
    #print(path)
    os.chdir(path+'/weather_forecast/weather_forecast/')
    path = os.getcwd()
    #print(path)

    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(file)
            if "weather.json" == file:
                os.remove(file_path)
            else: print("file não encontrado")

#deletar()