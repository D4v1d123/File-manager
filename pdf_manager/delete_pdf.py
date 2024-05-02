import os

def set_working_directory():
    working_directory = os.getcwd()
    folder = working_directory.split("/")[-1] 
    
    if folder == "Files_manager": return f"{working_directory}/pdf_manager" 
    elif folder == "pdf_manager": return working_directory


pdf_path = f"{set_working_directory()}/pdf/work_progress.pdf"

try:
    os.remove(pdf_path)
    print("The document has been deleted.")
except Exception:
    print("An error has occurred while deleting the document.")