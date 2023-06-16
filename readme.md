# NASA EPIC Imagery Downloader

This python script retrieves the most recent Earth Polychromatic Imaging Camera (EPIC) image from the NASA API, available at [https://epic.gsfc.nasa.gov/api/natural](https://epic.gsfc.nasa.gov/api/natural), and saves it to your desktop.

## Prerequisites

Ensure you have Python3 installed on your machine. You can verify this by running the following command in your terminal:

\```bash
python3 --version
\```

If Python3 is not installed, please follow the guidelines on the official Python website to [download and install Python3](https://www.python.org/downloads/).

## Usage

To use the script, simply open your terminal and run:

\```bash
python3 SatImagery.py
\```

By default, the script will download the latest EPIC image as a .png file and place it on your desktop.

## Note

The script is designed to work with UNIX-like systems (such as Linux or MacOS). If you are using Windows, you might need to adjust the file paths accordingly.