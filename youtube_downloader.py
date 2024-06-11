import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
from pytube import YouTube


gui = tk.Tk()
gui.geometry('500x150')
gui.title('Youtube Downloader')
gui.config(bg='#323232')

video_link = StringVar()
download_path = StringVar()

def functionality():
    title_label = Label(gui, text='Youtube Video Downloader', padx=5, pady=5, bg='#929292', fg='#000000')
    title_label.grid(row=1, column=1, padx=5, pady=5, columnspan=3)

    link_label = Label(gui, text= 'Enter URL: ', bg='#929292', fg='#000000')
    link_label.grid(row=2, column=0, padx=5, pady=5)

    destination_label = Label(gui, text='Download Location:', bg='#929292', fg='#000000')
    destination_label.grid(row=3, column=0, padx=5, pady=5)
    
    gui.linktext = Entry(gui, width=40, textvariable=video_link)
    gui.linktext.grid(row=2, column=1, padx=5, pady=5, columnspan=3)

    gui.destinationtext = Entry(gui, width=40, textvariable=download_path)
    gui.destinationtext.grid(row=3, column=1, padx=5, pady=5, columnspan=3)

    browse_button = Button(gui, text= 'Choose Location', command=choose_location, width= 20, bg= '#929292', relief=RIDGE)
    browse_button.grid(row=4, column=2, padx=5, pady=5)

    download_button = browse_button = Button(gui, text= 'Download', command=downloaded_content, width= 20, bg= '#929292', relief=RIDGE)
    download_button.grid(row=4, column=1, padx=5, pady=5)

def choose_location():
    download_directory = filedialog.askdirectory(initialdir='YOUR PATH', title= 'Save Video')
    download_path.set(download_directory)
    
def downloaded_content():
    youtube_url = video_link.get()
    download_folder = download_path.get()

    try:
        get_video = YouTube(youtube_url)
        videoStream = get_video.streams.get_highest_resolution()
        videoStream.download(download_folder)
        messagebox.showinfo('Your video has been downloaded to ' + download_folder)
    except Exception:
        messagebox.showerror('Error', 'An error has occured')


functionality()

gui.mainloop()