import os
import shutil


home = os.path.expanduser("~")
downloads_folder = os.path.join(home, "Downloads")

print("Organizando arquivos da pasta:", downloads_folder)

for file in os.listdir(downloads_folder):
    filename, file_extension = os.path.splitext(file)
    file_extension = file_extension[1:]  

    if file_extension:  
        folder_to_organize_file = os.path.join(downloads_folder, file_extension)

      
        if not os.path.isdir(folder_to_organize_file):
            os.mkdir(folder_to_organize_file)

       
        shutil.move(
            os.path.join(downloads_folder, file),
            os.path.join(folder_to_organize_file, file)
        )

print("✅ Organização concluída!")
