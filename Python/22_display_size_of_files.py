import os
def list_files(dir):
    if os.path.exists(dir):
        for file_name in os.listdir(dir):
            file_path=os.path.join(dir,file_name)
            if os.path.isfile(file_path):
                print(f"{file_name}: {os.path.getsize(file_path)}")
    else:
        print("Directory does not exists")

directory=input("Enter directory: ")
list_files(directory)
