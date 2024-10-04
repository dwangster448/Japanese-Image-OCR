import sys
import os
import re
import pytesseract
from PIL import ImageGrab
from bs4 import BeautifulSoup

# Function to initialize the HTML file
def initialize_html(file_name):
    with open(file_name, "w") as file:  # Open in write mode to create or overwrite
        file.write("<html>\n")
        file.write("        <meta charset=\"UTF-8\">\n")
        file.write("    </head><body>\n")
        #file.write("        <a id=\"fileLink\" href=\"test_1.html\">Load test_1.html</a>\n")
        file.write("        <script src=\"https://code.jquery.com/jquery-3.6.0.min.js\"></script>\n")
        file.write("    <script src=\"updates.js\"></script>\n")
        file.write("    <link href=\"styles.css\" rel=\"stylesheet\" type=\"text/css\"/>\n")
        file.write("        <h3>Japanese Clipboard Text</h3>\n")
        file.write("    </head>\n")  # Close the head section
        file.write("    <body>\n")  # Open the body section
        file.write("        <button id=\"my-button\" onclick=\"clearContent()\">Clear</button>\n")  # Button should be in body
        file.write("        <div id='content'></div>\n")  # Content div should also be in body
        file.write("    </head>\n")
        file.write("    </body>\n")  # Close the body section
        file.write("</html>\n")  # Close the html section

# Function to append each row entry to the HTML file
def append_to_html(file_name, new_content):
    # Open the file in append mode to add new content
    with open(file_name, "a") as file:
        file.write(new_content + "\n")

# Function to finalize the HTML file
def finalize_html(file_name):
    with open(file_name, "a") as file:  # Open in append mode to close the HTML structure
        file.write("</body>\n</html>")

# Function to transcript text on image using Tesseract
def ocr_read(input_img):
    if (input_img):
        ocr_result = pytesseract.image_to_string(img, lang="Japanese_vert")
        ocr_result = ocr_result.split("\n")

        return ocr_result

#Checks if user provided a filename
if len(sys.argv) < 2:
    print("Usage: python3 program.py <file_name>")
    sys.exit(1)  # Exit the program if no filename is provided

# Get the filename from the command-line argument
file_name = sys.argv[1]

#Checks if filename clear 
if len(sys.argv) >= 3:
    print("Detecting clear")
    if(sys.argv[2] == "clear"):
        initialize_html(file_name)

if os.path.isfile(file_name):
    print(f"{file_name} exists and is a file.")
else:
    print(f"{file_name} does not exist or is not a file.")
    initialize_html(file_name)

with open(file_name, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'lxml')

# Find the <div> with id="content"
content_div = soup.find('div', id='content')

results = [] #store raw entries into results

#Object to store macOS clipboard element
img = ImageGrab.grabclipboard()

#Peforms transcripting upon successful image load
if (img):


    ocr_result =  ocr_read(img)
    for item in ocr_result:
        item = re.sub(r'\s+', '', item)
        results.append(item)

    entities = []
    for item in results:
        if len(item) > 0:
            entities.append(item)
    print(entities)
    for item in entities:
        new_paragraph = soup.new_tag('p')
        new_paragraph.string = item
        content_div.append(new_paragraph)

    # Save the changes back to the HTML file
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(str(soup))


