# Create a document from an text template and a spreadsheet.

import os
import pandas
from docx.shared import Mm
from docxtpl import DocxTemplate, InlineImage

def readDataSpreadsheet(path, sheet):
    data_frame = pandas.read_excel(path, sheet)  # Extract data from the spreadsheet 
    # to a data frame.

    return data_frame

def createDocumet(data_frame, template_path, output_path, img_path=""):
    for _, row_values in data_frame.iterrows():  # Iterate over spreadsheet data 
        # (data frame).
        template = DocxTemplate(template_path)  # Process template.
        img = InlineImage(template, img_path, width=Mm(7))  # Open and put image in 
        # the template or document.
        values = {  
            "company_logo" : img,
            "company_name" : "Apple",
            "company_address" : "120 Bremner Blvd Suite 1600, Toronto, ON M5J 0A8," \
            "Canada",
            "phone_number" : "800–692–7753",
            "date" : "01 - May - 2027",
            "guest_name" : row_values["Name"],
            "guest_address" : row_values["Address"],
            "event_date" : "20 - June - 2027",
            "event_address" : "McEnery Convention Center, 150 West San Carlos Street," \
            "San Jose, CA 95113, Estados Unidos",
            "event_title" : "Apple WWDC",
            "sender_name" : "Mouhamed Diane",
            "sender_charge" : "Software Engineering",
            "sender_phone_number" : "(415) 852-7226",
            "sender_mail" : "MouhaDi@apple.com"
        }
        
        template.render(values)  # Replace the template variables or placeholders.
        doc_name = f"Invitation {row_values["Name"]}.docx"
        template.save(f"{output_path}/{doc_name}")  # Create DOCX document.
        print("Document created successfully.")

def set_working_directory():
    working_directory = os.getcwd()
    folder = working_directory.split("/")[-1] 
    
    if folder == "Files_manager": 
        return f"{working_directory}/document_manager" 
    else:
        return working_directory.replace(folder, "document_manager")


working_directory = set_working_directory()
output_path = f"{working_directory}/documents"
spreadsheet_path = f"{working_directory}/template/guest.xlsx"
template_path = f"{working_directory}/template/Letter of invitation.docx"
img_path = f"{working_directory}/img/Apple Logo.png"

guest_data_frame = readDataSpreadsheet(spreadsheet_path, "Employees")  # Extract data
# from spreadsheet.
createDocumet(guest_data_frame, template_path, output_path, img_path)  # Create DOCX
# documents.