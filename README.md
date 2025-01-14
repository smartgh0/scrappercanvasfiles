# Canvas Course Files Downloader App

## Description
I built this python scrapper to enable me download all my course files from canvas after graduation. This is a GUI-based Python application for downloading files from authenticated websites like Canvas. It allows users to log in with credentials, specify a URL, and download files of various formats to a local directory. The app supports file extensions such as `.pdf`, `.docx`, `.pptx`, `.csv`, `.mp4`, `.jpg`, and more.

The app is built using the following technologies:
- **Tkinter**: For the graphical user interface.
- **Selenium**: For web automation and login handling.
- **Requests**: For downloading files with authentication cookies.

## Features
- User-friendly GUI for entering login credentials and selecting a download directory.
- Supports authenticated file downloads from Canvas.
- Downloads multiple file formats, including documents, images, and videos.
- Progress bar to track download progress.
- Displays total and completed file counts.

## Requirements
- Python 3.6 or later
- Google Chrome
- ChromeDriver (compatible with your Chrome version)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/file-downloader.git
   cd file-downloader
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure `chromedriver` is installed and added to your system's PATH.

## Usage
1. Run the application:
   ```bash
   python file_downloader.py
   ```

2. Enter the following details in the GUI:
   - **Page URL**: URL of the Canvas page containing files.
   - **Username**: Your Canvas username.
   - **Password**: Your Canvas password.
   - **Download Directory**: Directory where files will be saved.

3. Click the **Start Download** button to begin downloading files.

## File Types Supported
The app supports the following file extensions:
- `.pdf`, `.docx`, `.doc`
- `.pptx`, `.ppt`, `.xls`, `.xlsx`
- `.mp4`, `.mp3`
- `.jpg`, `.jpeg`, `.png`, `.gif`
- `.zip`, `.tar.gz`

## Notes
- Ensure you have access to the provided URL and valid credentials.
- The app uses Selenium for login automation; ensure `chromedriver` matches your Chrome version.
- Large file downloads may take longer; please be patient.

## Troubleshooting
- **Error: Unable to locate element**: Ensure the provided URL is correct and accessible.
- **ChromeDriver not found**: Verify `chromedriver` is installed and in your system's PATH.
- **Progress bar not updating**: The app updates progress based on file download completion.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
[Solomon Nyamekye]
Contact me if you need any support!!!
