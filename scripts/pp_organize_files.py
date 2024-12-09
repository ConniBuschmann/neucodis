import os
import shutil
import re

source_folder = "C:/Users/timdr/OneDrive/Uni_Oldenburg/3_Semester/Module/Pratical_Project/Analysis/data/other/all_raw/all_raw"
destination_folder = "C:/Users/timdr/OneDrive/Uni_Oldenburg/3_Semester/Module/Pratical_Project/Analysis/data/other/test_python_reorder"

files = os.listdir(source_folder)

for file_name in files:
    match = re.match(r"av_(P\d{3})_", file_name)
    
    if match:
        folder_name = match.group(1)
        target_folder = os.path.join(destination_folder, folder_name)
        
        os.makedirs(target_folder, exist_ok=True)
        
        source_file = os.path.join(source_folder, file_name)
        target_file = os.path.join(target_folder, file_name)
        
        shutil.move(source_file, target_file)



check_done = "OK"
print(check_done)

hallo hallo
