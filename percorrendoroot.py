import os 

path = os.getcwd()
print(path)

for root, dirs, files in os.walk(path ,topdown=True):
    for dir in dirs:
        print(os.path.join(root, dir))
        comp = str(dir)
        print(f"comp: {comp}")
        if comp == "weather_forecast":
            print(f"econtrei {dir}")
            break