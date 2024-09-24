# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 22:02:39 2024

@author: user
"""

import os
import shutil

# Dynamically get the Downloads folder path for the current user
downloads_folder = os.path.join(os.path.expanduser("~"), 'Downloads')

# Define the destination folders for different file types
destinations = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'PDFs': ['.pdf'],
    'Documents': ['.doc', '.docx', '.txt', '.ppt', '.pptx', '.xls', '.xlsx'],
    'Spreadsheets': ['.csv'],
    'Videos': ['.mp4', '.mkv', '.mov', '.avi'],
    'Music': ['.mp3', '.wav', '.flac'],
    'Archives': ['.zip', '.rar', '.7z'],
    'Programs': ['.exe', '.msi'],
}

# Function to create destination folders if they don't exist
def create_folders():
    for folder in destinations.keys():
        folder_path = os.path.join(downloads_folder, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

# Function to move files to their respective folders
def organize_files():
    # Get all files in the Downloads folder
    for filename in os.listdir(downloads_folder):
        # Ignore folders, focus only on files
        if os.path.isfile(os.path.join(downloads_folder, filename)):
            file_extension = os.path.splitext(filename)[1].lower()
            
            # Move file to the corresponding folder based on file type
            moved = False
            for folder, extensions in destinations.items():
                if file_extension in extensions:
                    shutil.move(os.path.join(downloads_folder, filename), os.path.join(downloads_folder, folder, filename))
                    print(f"Moved {filename} to {folder}")
                    moved = True
                    break
            
            # If no matching folder was found, move it to "Others"
            if not moved:
                others_folder = os.path.join(downloads_folder, 'Others')
                if not os.path.exists(others_folder):
                    os.makedirs(others_folder)
                shutil.move(os.path.join(downloads_folder, filename), os.path.join(others_folder, filename))
                print(f"Moved {filename} to Others")

# Run the file organizer
if __name__ == "__main__":
    create_folders()  # Create necessary folders in the Downloads directory
    organize_files()  # Organize files into their designated folders
