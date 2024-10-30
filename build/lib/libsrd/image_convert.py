from PIL import Image
import os
import sys

# Converts all files with initalExt to files with the finalext.
def convert_images(InputPath, InitialExtention, FinalExtention):
	# Prefixes extensions with dots, of not already.
	if FinalExtention[0] != '.':
		FinalExtention = "." + FinalExtention
	if InitialExtention[0] != '.':
		InitialExtention = "." + InitialExtention

	# Check the path exists.
	if not os.path.exists(InputPath):
		print('The given path does not exist.')
		return

	# Get all files in folder.
	files = os.listdir(InputPath)
	Images = []

	# Get all images in files.
	for file in files:
		if InitialExtention.lower() in file.lower():
			Images.append(file)

	# Abort if no images found.
	if len(Images) < 1:
		print("No suitable images found.")
		return

	# Create output folder.
	outputPath = os.path.join(InputPath, "Ouput")
	os.makedirs(outputPath, exist_ok=True)

	for image in Images:
		withoutExtension = image.partition('.')[0] 
		im = Image.open(os.path.join(InputPath, image))
		im.save(os.path.join(outputPath, f"{withoutExtension}{FinalExtention}"), FinalExtention[1:].upper())
	
	print("Complete!\n")


def script():
	if len(sys.argv) == 3:
		folderPath = os.getcwd()
		convert_images(folderPath, sys.argv[1], sys.argv[2])
	else:
		print(sys.argv)
		print("Expected two arguments (InitalExtension, FinalExtension)")