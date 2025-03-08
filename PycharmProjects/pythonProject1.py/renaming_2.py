import os

folder_path = 'D:/earth/earth/'
image_files = os.listdir(folder_path)

image_files.sort()

new_name = "Earth_1.jpg"
new_names = ["Sky.jpg", "Rock.jpg", "Mountain.jpg", "Valley.jpg", "Spring.jpg", "Sea.jpg", "Tree.jpg", "River.jpg",
             "Garden.jpg", "Sand.jpg"]

for i in range(min(len(image_files), len(new_names))):
    new_earth_names = new_names[i]
    old_names = image_files[i]

    # specifying old and new paths
    old_path = os.path.join(folder_path, old_names)
    new_path = os.path.join(folder_path, new_earth_names)

    # rename files
    os.rename(old_path, new_path)

    print(f"Photo Rename from: {old_names} → to: {new_earth_names}")








