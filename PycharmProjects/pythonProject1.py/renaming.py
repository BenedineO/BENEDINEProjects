
import os

# Directing the os to the folder path
folder_path = "D:/bg_photos/rename"

# Creating an empty list to store my photos
photo_file = os.listdir(folder_path)

# Arranging photos alphabetically
photo_file.sort()

# Looping to rename the photos in th list
for i in range(len(photo_file)):
    old_name = photo_file[i]
    new_name = f'Serene_{i+1}.png'
    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, new_name)

    os.rename(old_path, new_path)

print('Renaming of photos completed as instructed!')

'http://books.toscrape.com/'