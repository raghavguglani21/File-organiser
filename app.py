import streamlit as st
import os
import shutil
import pandas as pd

st.set_page_config(page_title="Smart File Organizer", page_icon="📂")

st.title("📂 Smart File Organizer")
st.write("Organize files into folders based on their extension.")

folder = st.text_input("Enter Folder Path")

s = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"],
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
    "Markdown": [".md"]
}

if st.button("🚀 Organize Files"):

    if folder == "":
        st.warning("Please enter a folder path.")

    else:
        moved = []

        if folder:
            if os.path.exists(folder):
                files = os.listdir(folder)
                st.write(files)
            else:
                st.error("Folder not found!")

        progress = st.progress(0)

        for index, file in enumerate(files):

            path = os.path.join(folder, file)

            if os.path.isdir(path):
                continue

            ext = os.path.splitext(file)[1].lower()

            for category in s:

                if ext in s[category]:

                    destination = os.path.join(folder, category)

                    if not os.path.exists(destination):
                        os.mkdir(destination)

                    shutil.move(path, os.path.join(destination, file))

                    moved.append([file, category])

                    break

            progress.progress((index + 1) / len(files))

        st.success("✅ Files Organized Successfully!")

        st.metric("Files Moved", len(moved))

        if moved:

            df = pd.DataFrame(moved, columns=["File Name", "Category"])

            st.subheader("Moved Files")

            st.dataframe(df, use_container_width=True)

            st.subheader("Files by Category")

            st.bar_chart(df["Category"].value_counts())
