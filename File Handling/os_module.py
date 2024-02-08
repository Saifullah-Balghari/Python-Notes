import os

# ---> TO CHANGE THE CURRENT WORKING DIRECTORY...
path_to_change_the_directory = "..."
os.chdir("")

# ---> TO MAKE A DIRECTORY THE CURRENT WORKING DIRECTORY...
os.mkdir(f"{f+1}")

# ---> TO GET THE CURRENT WORKING DIRECTORY...
os.getcwd()

# --->  STORES THE FILES NAME AS A LIST...
folders = os.listdir("directory_path")

# --->  LISTS THE FILES INSIDE THE CURRENT WORKING DIRECTORY...
dir_path = "..."
os.listdir(f"data/{dir_path}")

# --->  TO RENAME...
current_name = "..."
new_name = "..."
os.rename(f"data/{current_name}",f"data/folder{new_name}")
