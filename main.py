import tkinter as tk
import pytube

root = tk.Tk()
root.geometry("400x200")

link_entry = tk.Entry(root)
link_entry.pack()

def download_video():
    url = link_entry.get()
    video = pytube.YouTube(url)
    video.streams.filter(progressive=True).first().download()
    
    # Create a show box which shows that video is downloaded
    show_box = tk.Label(root, text = "video downloaded!")
    show_box.pack()

# Creating buttons
button = tk.Button(root, text="Download Video", command=download_video)
button.pack()
quit_button = tk.Button(root, text = "Quit", command = root.destroy)
quit_button.pack()



root.mainloop()
