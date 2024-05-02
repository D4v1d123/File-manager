# Create PDF from an HTML template.

import os
import jinja2
import pdfkit  

def create_pdf(html_path, output_path, css_path=""):
    html_file_name = html_path.split("/")[-1]
    template_path = html_path.replace(html_file_name, "")
    working_directory = set_working_directory()
    values = {
              "name" : "David Guerrero",
              "position" : "Senior programmer",
              "img_path" : f"{working_directory}/template/img/python logo.png"
    }
    options = {
        "enable-local-file-access" : "",  # Allow wkhtmltopdf access to local host 
        # files during HTML to PDF conversion.
        "page-size" : "Letter",
        "margin-top" : "0.05in",
        "margin-right" : "0.05in",
        "margin-bottom" : "0.05in",
        "margin-left" : "0.05in",
        "encoding" : "UTF-8" 
    }

    config = pdfkit.configuration(wkhtmltopdf="/usr/local/bin/wkhtmltopdf")  # Specifies
    # where the wkhtmltopdf executable is.
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path))  # Create 
    # a runtime environment with the HTML templates located in a path.
    template = env.get_template(html_file_name)  # Extract an HTML template.
    html = template.render(values)  # Replace values (name, position) in the HTML.
    
    pdfkit.from_string(html, output_path, css=css_path, options=options, configuration=config)  # Generate PDF. 
    print("PDF created successfully.")
    
def set_working_directory():
    working_directory = os.getcwd()
    folder = working_directory.split("/")[-1] 
    
    if folder == "Files_manager": 
        return f"{working_directory}/pdf_manager" 
    else:
        return working_directory.replace(folder, "pdf_manager")


working_directory = set_working_directory()
html_path = f"{working_directory}/template/pdf_content.html"
css_path = f"{working_directory}/template/style.css"
output_path = f"{working_directory}/pdf/work_progress.pdf"

create_pdf(html_path, output_path, css_path)