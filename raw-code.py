import os
import shutil
j=input("enter path of folder")
#C:\Users\ragha\Documents\startGIT
s={ "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"],
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
    "md":[".md"],
    "other_folder":["",' ',".","."]}

f=os.listdir(fr'{j}')
for i in f:
    ext = os.path.splitext(i)[1].lower()
    for x in s:
        if ext in s[x]:
            if not os.path.exists(fr'{j}\{x}'):
                os.mkdir(fr'{j}\{x}') 
            shutil.move(fr'{j}\{i}',fr'{j}\{x}\{i}')
        else:
            continue

fl=os.listdir(fr'{j}')
for i in fl:
    print(i)