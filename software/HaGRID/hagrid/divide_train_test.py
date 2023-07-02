import os
import random
import shutil

folder_path = 'images'  # Folder path to dataset
test_ratio = 0.1  # Adjust the ratio as desired 

# Create directories for train and test sets
train_dir = os.path.join(folder_path, 'train')
test_dir = os.path.join(folder_path, 'test')
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Get a list of all image files in the folder
image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Shuffle the image files
random.shuffle(image_files)

# Calculate the number of images for the test set
num_test = int(len(image_files) * test_ratio)
print("Dataset size: ", len(image_files))
print("Training set size: ", num_test)
print("Test set size: ", len(image_files) - num_test)


# Move images to the test set
for i in range(num_test):
    src_path = os.path.join(folder_path, image_files[i])
    dst_path = os.path.join(test_dir, image_files[i])
    shutil.move(src_path, dst_path)
    #print(f'Moving {image_files[i]} to the test set.')

# Move the remaining images to the train set
for i in range(num_test, len(image_files)):
    src_path = os.path.join(folder_path, image_files[i])
    dst_path = os.path.join(train_dir, image_files[i])
    shutil.move(src_path, dst_path)
    #print(f'Moving {image_files[i]} to the train set.')
