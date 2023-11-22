import os
import shutil

import pandas as pd

def convert(namecsv):
    file_csv = pd.read_csv(f"Data/{namecsv}", sep=",")
    list_csv=[list(x) for x in file_csv.values]
    with open(f"Data_txt/{namecsv[0:8]}.txt","w+") as file:
        for els in list_csv:
            for el in els:
                file.write(f"{el}       ")
            file.write("\n")  
        lines = file.readlines()
    with open(f"Data_txt/{namecsv[0:8]}.txt","r+") as fil:
        lines = fil.readlines()
        fil.seek(0)
        fil.truncate()
        fil.writelines(lines[1:])
def findfileinfolder(path,fileformat):
    nat_list = []
    for file in os.listdir(path):
        if file.endswith(fileformat):
            element = os.path.join(file)
            nat_list.append(element)
    return nat_list

def delete_folder():
    path = folder_path+"/Data_txt"
    return shutil.rmtree(path)
def clear_folder(folder_path):
    if os.path.exists(folder_path):
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

        print(f"Folder '{folder_path}' has been cleared.")
    else:
        print(f"Folder '{folder_path}' does not exist.")
script_path = os.path.abspath(__file__)
folder_path = os.path.dirname(script_path)
new_folder = folder_path+"/Data_txt"
os.makedirs(new_folder, exist_ok=True)


#------- Find csv file code ------------
Dataall_csv = findfileinfolder(folder_path+"/Data", ".csv")
#------- Convert csv to txt ------------
for data_txt in Dataall_csv:
    convert(data_txt)

