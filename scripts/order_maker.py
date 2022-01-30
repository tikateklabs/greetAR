import uuid as id
import logging
import os
import pyqrcode
import shutil

print("""https://jeromeetienne.github.io/AR.js/three.js/examples/marker-training/examples/generator.html""")


logging.info("Generating a new UUID")
uuid = id.uuid4()
# uuid = "12c0b1f3-4f89-4ae0-83f5-b85f496e698a"
uuid = str(uuid)
print(f"UUID: {str(uuid)}")
logging.info(f"UUID generated : {str(uuid)}")

logging.info("Creating a folder inside magic_window")
path_parent = os.path.dirname(os.getcwd())
target_dir = os.path.join(path_parent, "magic_window", str(uuid))
os.makedirs(target_dir, exist_ok=True)

comments = input("Add comments for this order:")
with open("order_info.txt", 'a') as info:
    info.write(f"{uuid} | {comments}\n")

# Read in the file
with open('template.html', 'r') as template_file:
    filedata = template_file.read()

# Replace the target string
filedata = filedata.replace('new_uuid', str(uuid))

target_view = os.path.join(target_dir, "view.html")
# Write the file out again
with open(target_view, 'w') as file:
    file.write(filedata)

patt_file = input("Enter the path to the patt file: ")
marker_file = input("Enter the marker file path:")
video_file = input("Enter the video file path:")

os.rename(patt_file, os.path.join(target_dir, f"{uuid}.patt"))
os.rename(marker_file, os.path.join(target_dir, f"{uuid}.PNG"))
os.rename(video_file, os.path.join(target_dir, f"{uuid}.mp4"))
shutil.copy2("card_inside.docx", os.path.join(target_dir, "card_inside.docx"))
shutil.copy2("card_outside.docx", os.path.join(target_dir, "card_outside.docx"))

web_url = f"https://tikateklabs.com/greetAR/magic_window/{uuid}/view.html"
# Generate QR code
url = pyqrcode.create(web_url)

# Create and save the png file naming "myqr.png"
url.png(os.path.join(target_dir, f'QR_{uuid}.png'), scale=6)
