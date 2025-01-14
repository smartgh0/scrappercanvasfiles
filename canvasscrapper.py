import os
import requests
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FileDownloaderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("File Downloader")
        
        # URL input
        self.url_label = tk.Label(master, text="Enter Page URL:")
        self.url_label.pack(pady=5)
        
        self.url_entry = tk.Entry(master, width=50)
        self.url_entry.pack(pady=5)
        
        # Username input
        self.username_label = tk.Label(master, text="Username:")
        self.username_label.pack(pady=5)
        
        self.username_entry = tk.Entry(master, width=50)
        self.username_entry.pack(pady=5)
        
        # Password input
        self.password_label = tk.Label(master, text="Password:")
        self.password_label.pack(pady=5)
        
        self.password_entry = tk.Entry(master, show="*", width=50)
        self.password_entry.pack(pady=5)
        
        # Download directory input
        self.download_dir_label = tk.Label(master, text="Download Directory:")
        self.download_dir_label.pack(pady=5)
        
        self.download_dir_entry = tk.Entry(master, width=50)
        self.download_dir_entry.pack(pady=5)
        
        self.browse_button = tk.Button(master, text="Browse", command=self.browse_directory)
        self.browse_button.pack(pady=5)
        
        self.start_button = tk.Button(master, text="Start Download", command=self.start_download)
        self.start_button.pack(pady=5)
        
        self.progress = ttk.Progressbar(master, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=5)
        
        self.status_label = tk.Label(master, text="")
        self.status_label.pack(pady=5)

        self.total_files_label = tk.Label(master, text="")
        self.total_files_label.pack(pady=5)

        self.downloaded_files_label = tk.Label(master, text="Downloaded Files: 0")
        self.downloaded_files_label.pack(pady=5)

        self.driver = None

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.download_dir_entry.delete(0, tk.END)
            self.download_dir_entry.insert(0, directory)

    def start_download(self):
        url = self.url_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        download_dir = self.download_dir_entry.get()
        
        if not url or not username or not password or not download_dir:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        self.progress["value"] = 0
        self.status_label.config(text="Downloading...")
        self.total_files_label.config(text="")
        self.downloaded_files_label.config(text="Downloaded Files: 0")
        
        # Start the download in a separate thread
        threading.Thread(target=self.download_files, args=(url, username, password, download_dir)).start()

    def download_files(self, url, username, password, download_dir):
        ALLOWED_EXTENSIONS = ['.pdf',".csv", ".ipynb", '.docx',"doc", '.ppt',"pptx", '.xls', '.xlsx', '.mp4', '.mp3', '.jpg', '.jpeg', '.png', '.gif', '.zip', '.tar.gz']
        self.driver = webdriver.Chrome()  # Ensure you have the correct driver
        wait = WebDriverWait(self.driver, 15)

        try:
            # Step 1: Log in to Canvas
           
            LOGIN_URL = "https://canvas.rice.edu/login/saml/4"
            self.driver.get(LOGIN_URL)
            wait.until(EC.presence_of_element_located((By.NAME, "j_username")))
            self.driver.find_element(By.NAME, "j_username").send_keys(username)
            self.driver.find_element(By.NAME, "j_password").send_keys(password)
            self.driver.find_element(By.NAME, "_eventId_proceed").click()
            self.driver.get(url)
            # Step 2: Navigate to the Files page
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "ef-item-row")))

            # Step 3: Find all file links on the page
            file_links = self.driver.find_elements(By.CSS_SELECTOR, "a")
            total_files = len(file_links)
            self.total_files_label.config(text=f"Total files found: {total_files}")

            # Step 4: Use requests with cookies for authenticated downloads
            session = requests.Session()
            for cookie in self.driver.get_cookies():
                session.cookies.set(cookie['name'], cookie['value'])

            downloaded_count = 0  # Counter for downloaded files

            # Step 5: Process each file link to download files
            for index, file_link in enumerate(file_links):
                try:
                    file_url = file_link.get_attribute("href")
                    file_name = file_link.text.strip()

                    if file_url and any(file_name.lower().endswith(ext) for ext in ALLOWED_EXTENSIONS):
                        response = session.get(file_url, stream=True)
                        file_path = os.path.join(download_dir, file_name)
                        with open(file_path, "wb") as file:
                            for chunk in response.iter_content(chunk_size=10240000000):
                                file.write(chunk)
                        print(f"Downloaded: {file_name} to {file_path}")
                        
                        downloaded_count += 1  # Increment the downloaded count
                        self.downloaded_files_label.config(text=f"Downloaded Files: {downloaded_count}")
                        
                        # Update progress
                        self.progress["value"] = (index + 1) / total_files * 100
                        self.master.update_idletasks()
                except Exception as e:
                    print(f"Error downloading file: {e}")

            messagebox.showinfo("Success", "Download completed!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            self.driver.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = FileDownloaderApp(root)
    root.mainloop()