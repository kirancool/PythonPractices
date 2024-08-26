import os
import shutil
from datetime import datetime

source_folder = "C:\\Users\\Kiran Adhav\\datasets"

base_destination_folder = "C:\\Users\\Kiran Adhav\\OneDrive\\Desktop\\kiran"

current_date = datetime.now().strftime('%Y-%m-%d')

destination_folder = os.path.join(base_destination_folder, current_date)

os.makedirs(destination_folder, exist_ok=True)

files = os.listdir(source_folder)

for file_name in files:
   
    if file_name.endswith('.csv'):
     
        source_file_path = os.path.join(source_folder, file_name)
      
        destination_file_path = os.path.join(destination_folder, file_name)
        
        shutil.move(source_file_path, destination_file_path)
        
        print(f'Moved: {file_name} to {destination_folder}')