import requests
import json
import shutil
import os

# Fetch the most recent image data
response = requests.get("https://epic.gsfc.nasa.gov/api/natural")
data = json.loads(response.text)

# Get the most recent image
most_recent = data[0]  # Assuming the first image is the most recent

# Construct the date from the image data
year, month, day = most_recent["date"].split(" ")[0].split("-")

# Construct the image name and source URL
name = most_recent["image"] + ".png"
archive = f"https://epic.gsfc.nasa.gov/archive/natural/{year}/{month}/{day}/png/"
source = archive + name

# Set the download location
destination = os.path.join('/Users/loganlentz/Desktop/', name)

# Download the image
response = requests.get(source, stream=True)
with open(destination, 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response
