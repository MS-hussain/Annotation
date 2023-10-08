import os

# Path to the directory containing the original images
source_folder = r'E:\image\clear_images'

# Path to the directory where you want to save the renamed images
destination_folder = r'E:\image\NEW_images'

# Make sure the destination folder exists
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Get a list of all files in the source folder
image_files = os.listdir(source_folder)

# Sort the image files in ascending order
image_files.sort()

# Initialize a counter for numbering the images
counter = 1

# Iterate through the sorted image files and rename them
for image_file in image_files:
    # Get the file extension (e.g., .jpg, .png)
    _, file_extension = os.path.splitext(image_file)
    
    # Create the new filename with a numeric prefix
    new_filename = f'{counter:04d}{file_extension}'  # 4-digit padded number
    
    # Build the full paths for the source and destination files
    source_path = os.path.join(source_folder, image_file)
    destination_path = os.path.join(destination_folder, new_filename)
    
    # Rename the file
    os.rename(source_path, destination_path)
    
    # Increment the counter
    counter += 1

print(f'Renamed {len(image_files)} images.')
