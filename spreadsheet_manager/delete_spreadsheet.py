import os

def set_working_directory():
    working_directory = os.getcwd()
    folder = working_directory.split("/")[-1] 
    
    if folder == "Files_manager": 
        return f"{working_directory}/spreadsheet_manager" 
    else:
        return working_directory.replace(folder, "spreadsheet_manager")

def delete_documents(path):
    files = os.listdir(path)
    
    for file in files:
        files_path = f"{path}/{file}"
        
        try:
            os.remove(files_path)
            print("The document has been deleted.")
        except Exception:
            print("An error has occurred while deleting the document.")


working_directory = set_working_directory()
pdf_path = f"{working_directory}/spreadsheet"
delete_documents(pdf_path)
