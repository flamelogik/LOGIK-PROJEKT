import os
import subprocess
import platform
from PIL import Image

class IconParameters:
    def __init__(self, width, scale):
        self.width = width
        self.scale = scale

    def getIconName(self):
        scaleString = "" if self.scale == 1 else f"@{self.scale}x"
        return f"icon_{self.width}x{self.width}{scaleString}.png"

# Icon sizes
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

# Paths
originalPicture = "cfg/site-cfg/logik-projekt-cfg/icons/logik_projekt_icon_2026.png"
iconsetDir = "cfg/site-cfg/logik-projekt-cfg/icons/logik_projekt_icon.iconset"
outputIcns = "cfg/site-cfg/logik-projekt-cfg/icons/logik_projekt_icon.icns"

# Check original image
if not os.path.exists(originalPicture):
    print(f"❌ Original picture not found: {originalPicture}")
    exit(1)
else:
    print(f"✅ Original picture found: {originalPicture}")

# Create iconset directory
os.makedirs(iconsetDir, exist_ok=True)

# Detect platform
system = platform.system()
print(f"🖥️ Detected platform: {system}")

# Resize images
for ip in ListOfIconParameters:
    icon_path = os.path.join(iconsetDir, ip.getIconName())
    size = (ip.width * ip.scale, ip.width * ip.scale)

    if system == "Darwin":  # macOS
        result = subprocess.run(
            ["sips", "-z", str(size[1]), str(size[0]), originalPicture, "--out", icon_path],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            print(f"❌ Error generating icon {ip.getIconName()}: {result.stderr}")
        else:
            print(f"✅ macOS icon generated: {icon_path}")
    else:  # Linux or other
        try:
            img = Image.open(originalPicture)
            resized = img.resize(size, Image.LANCZOS)
            resized.save(icon_path)
            print(f"✅ Linux icon generated: {icon_path}")
        except Exception as e:
            print(f"❌ Error generating icon {ip.getIconName()}: {e}")

# Create .icns file
if system == "Darwin":
    result = subprocess.run(["iconutil", "-c", "icns", iconsetDir, "-o", outputIcns], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Error creating .icns file: {result.stderr}")
    else:
        print(f"🎉 macOS .icns file created: {outputIcns}")
else:
    # Collect PNGs for png2icns
    png_files = [os.path.join(iconsetDir, ip.getIconName()) for ip in ListOfIconParameters]
    result = subprocess.run(["png2icns", outputIcns] + png_files, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Error creating .icns file with png2icns: {result.stderr}")
    else:
        print(f"🎉 Linux .icns file created: {outputIcns}")
