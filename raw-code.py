import os
import shutil
file=input("enter path of folder")
#C:\Users\ragha\Documents\startGIT
dic={ "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Presentations": [".ppt", ".pptx"],
    "Python": [".py", ".ipynb"],
    "C_CPP": [".c", ".cpp", ".h", ".hpp"],
    "Java": [".java", ".class", ".jar"],
    "Web": [".html", ".css", ".js", ".php", ".json", ".xml"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".bat"],
    "Database": [".db", ".sqlite", ".sql"],
    "md":[".md"]}

fol=os.listdir(fr'{file}')
for each in fol:
    if os.path.isdir(fr'{file}\{each}'):
        continue
    ext = os.path.splitext(each)[1].lower()
    for typef in dic:
        if ext in dic[typef]:
            if not os.path.exists(fr'{file}\{typef}'):
                os.mkdir(fr'{file}\{typef}') 
            shutil.move(fr'{file}\{each}',fr'{file}\{typef}\{each}')
            break
        
    else:
        if not os.path.exists(fr'{file}\other_folder'):
            os.mkdir(fr'{file}\other_folder')
        shutil.move(fr'{file}\{each}', fr'{file}\other_folder\{each}')
            
            

fl=os.listdir(fr'{file}')
for i in fl:
    print(i)
print("\nFolder organized successfully!\n")
