#

# -------------------------------------------------------------------------- #

# DISCLAIMER:       This file is part of LOGIK-PROJEKT.
#                   Copyright © 2024 man-made-mekanyzms
                
#                   LOGIK-PROJEKT creates directories, files, scripts & tools
#                   for use with Autodesk Flame and other software.

#                   LOGIK-PROJEKT is free software.

#                   You can redistribute it and/or modify it under the terms
#                   of the GNU General Public License as published by the
#                   Free Software Foundation, either version 3 of the License,
#                   or any later version.
 
#                   This program is distributed in the hope that it will be
#                   useful, but WITHOUT ANY WARRANTY; without even the
#                   implied warranty of MERCHANTABILITY or FITNESS FOR A
#                   PARTICULAR PURPOSE.

#                   See the GNU General Public License for more details.

#                   You should have received a copy of the GNU General
#                   Public License along with this program.

#                   If not, see <https://www.gnu.org/licenses/>.
                
#                   Contact: phil_man@mac.com

# -------------------------------------------------------------------------- #

# File Name:        download_dji_lut_files.py
# Version:          0.0.1
# Created:          2024-01-19
# Modified:         2024-08-31

# ========================================================================== #
# This section defines the import statements and directory paths.
# ========================================================================== #

# https://terra-1-g.djicdn.com/851d20f7b9f64838a34cd02351370894/M3/DJI%20Mavic%203%20D-Log%20M%20to%20Rec.709%20V1.cube
# https://terra-1-g.djicdn.com/851d20f7b9f64838a34cd02351370894/mavic%203/DJI%20Mavic%203%20D-Log%20to%20Rec.709%20vivid%20V1.cube
# https://terra-1-g.djicdn.com/851d20f7b9f64838a34cd02351370894/260%20downloads/DJI%20Mavic%203%20D-Log%20to%20Rec.709%20V1.cube
# https://terra-1-g.djicdn.com/851d20f7b9f64838a34cd02351370894/avata2%20d-log/DJI%20Avata%202%20D-Log%20M%20to%20Rec.709%20V1._.cube
# https://terra-1-g.djicdn.com/851d20f7b9f64838a34cd02351370894/140%20lut/DJI%20Mini%204%20Pro%20D-Log%20M%20to%20Rec.709%20V1_.cube
# https://terra-1-g.djicdn.com/851d20f7b9f64838a34cd02351370894/DJI%20Air%203%20Lut/DJI%20Air%203%20D-Log%20M%20to%20Rec.709%20V1_.cube
# https://terra-1-g.djicdn.com/851d20f7b9f64838a34cd02351370894/203/DJI%20OSMO%20Action%204%20D-Log%20M%20to%20Rec.709%20V1.cube
# https://www-dl.djicdn.com/5e45168b46b342d5b88f72c458ba6e79/OP3%20LUT%E6%96%87%E4%BB%B6%E7%89%B9%E6%AE%8A%E5%A4%84%E7%90%86/DJI%20OSMO%20Pocket%203%20D-Log%20M%20to%20Rec.709%20V1.cube
# https://mydjiflight.dji.com/file/links/DJI_ZENMUSE_X9_DLOG_TO_REC2020HLG_3D_LUT_V1
# https://mydjiflight.dji.com/file/links/DJI_ZENMUSE_X9_DLOG_TO_REC709_3D_LUT_V1


import os
import urllib.request
import zipfile

def download_and_extract(url, extract_to):
    local_filename = os.path.join(extract_to, url.split('/')[-1])
    print(f"Downloading {url}...\n")
    urllib.request.urlretrieve(url, local_filename)
    print(f"Downloaded {local_filename}\n")
    
    print(f"Extracting {local_filename}...\n")
    with zipfile.ZipFile(local_filename, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted {local_filename}\n")

def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create a new folder
    new_folder = os.path.join(script_dir, 'ARRI_Alexa_LUTs')
    os.makedirs(new_folder, exist_ok=True)
    print(f"Creating folder: {new_folder}\n")
    
    # URLs of the zip files to download
    zip_urls = [
        'https://dl.djicdn.com/downloads/zenmuse_x5s/X5_series_Dlog_3DLUT.zip'
        'https://dl.djicdn.com/downloads/zenmuse+x7/20180104/Linear+to+D-Log.zip'
        'https://dl.djicdn.com/downloads/zenmuse+x7/20171017/D-Log+to+Rec709.zip'
        'https://dl.djicdn.com/downloads/phantom_4/Phantom_4_Dlog_3DLUT_20160606.zip'
        'https://dl.djicdn.com/downloads/phantom_3/Phantom_3_Dlog_3DLUT.zip'
        'https://terra-1-g.djicdn.com/851d20f7b9f64838a34cd02351370894/ACES/ACES%20Workflow%20Guide%20.zip'
    ]

    # Download and extract each zip file
    for url in zip_urls:
        download_and_extract(url, new_folder)
        print(f"Completed processing {url}\n")

if __name__ == '__main__':
    main()

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #

# Changelist:       

# -------------------------------------------------------------------------- #
# version:          0.0.1
# modified:         2024-08-31 - 16:51:09
# comments:         prep for release - code appears to be functional
# -------------------------------------------------------------------------- #
