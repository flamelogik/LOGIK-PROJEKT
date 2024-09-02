import os
import subprocess

class IconParameters:
    def __init__(self, width, scale):
        self.width = width
        self.scale = scale

    def getIconName(self):
        scaleString = "" if self.scale == 1 else f"@{self.scale}x"
        return f"icon_{self.width}x{self.width}{scaleString}.png"

# List of icon parameters (5 actual sizes, but 10 files)
ListOfIconParameters = [
    IconParameters(16, 1),
    IconParameters(16, 2),
    IconParameters(32, 1),
    IconParameters(32, 2),
    IconParameters(128, 1),
    IconParameters(128, 2),
    IconParameters(256, 1),
    IconParameters(256, 2),
    IconParameters(512, 1),
    IconParameters(512, 2)
]

# Specify the path to your original projekt-icon.png
originalPicture = "resources/icons/projekt_icon.png"
iconsetDir = "resources/icons/projekt_icon.iconset"

# Check if the original picture exists
if not os.path.exists(originalPicture):
    print(f"Original picture not found: {originalPicture}")
else:
    print(f"Original picture found: {originalPicture}")

# Create the iconset directory if it doesn't exist
os.makedirs(iconsetDir, exist_ok=True)

# Verify the creation of the iconset directory
if not os.path.exists(iconsetDir):
    print(f"Failed to create directory: {iconsetDir}")
else:
    print(f"Directory created: {iconsetDir}")

# Check permissions of the iconset directory
print(f"Permissions of {iconsetDir}: {oct(os.stat(iconsetDir).st_mode)}")

# Generate iconset folder
for ip in ListOfIconParameters:
    icon_path = os.path.join(iconsetDir, ip.getIconName())
    result = subprocess.run(
        [
            "sips",
            "-z",
            str(ip.width * ip.scale),
            str(ip.width * ip.scale),
            originalPicture,
            "--out",
            icon_path,
        ],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"Error generating icon {ip.getIconName()}: {result.stderr}")
    else:
        print(f"Successfully generated icon {ip.getIconName()} at {icon_path}")
        # Check if the file was created
        if not os.path.exists(icon_path):
            print(f"File not found after creation: {icon_path}")
        else:
            print(f"File exists: {icon_path}")

# List the contents of the iconset directory for debugging
print("Contents of the iconset directory:")
print(os.listdir(iconsetDir))

# Call iconutil to create the .icns file
result = subprocess.run(["iconutil", "-c", "icns", iconsetDir], capture_output=True, text=True)
if result.returncode != 0:
    print(f"Error creating .icns file: {result.stderr}")
else:
    print("Successfully created .icns file.")