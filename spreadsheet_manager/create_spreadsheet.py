import pandas

def create_spreadsheet(file_name, data_frame):
    output_path = f"spreadsheet_manager/spreadsheet/{file_name}"

    writer = pandas.ExcelWriter(output_path)  # Create a object to write the spreadsheet.
    data_frame.to_excel(writer, sheet_name = "Employees information", index = False)  # Create
    # spreadsheet.
    writer._save()  # Save spreadsheet.
    print("Spreadsheet created successfully.")
    

file_name = "Employees.xlsx"
data = pandas.DataFrame({
    "Name" : ["Sandra", "Pablo", "Katherine"],
    "Age" : [21, 25, 32],
    "Address" : ["San@gmail.com", "Pabk3@outlook.com", "Kth@gmail.com"]
})

create_spreadsheet(file_name, data)
