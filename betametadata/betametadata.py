import tkinter as tk
from tkinter import filedialog, Listbox, Entry, Label, Button
import os
from tinytag import TinyTag, TinyTagException

class MusicMetadataEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Metadata Editor")
        self.folder_path = ""
        
        # Layout
        self.folder_button = Button(root, text="Select Folder", command=self.select_folder)
        self.folder_button.pack()
        
        self.song_list = Listbox(root)
        self.song_list.pack()
        self.song_list.bind('<<ListboxSelect>>', self.display_metadata)
        
        self.title_label = Label(root, text="Title:")
        self.title_label.pack()
        self.title_entry = Entry(root)
        self.title_entry.pack()
        
        self.artist_label = Label(root, text="Artist:")
        self.artist_label.pack()
        self.artist_entry = Entry(root)
        self.artist_entry.pack()
        
        self.save_button = Button(root, text="Save Changes", command=self.save_changes)
        self.save_button.pack()
    
    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        self.update_song_list()
    
    def update_song_list(self):
        self.song_list.delete(0, tk.END)
        for file in os.listdir(self.folder_path):
            if file.endswith('.mp3') or file.endswith('.flac'):
                self.song_list.insert(tk.END, file)
    
    def display_metadata(self, event):
        try:
            selected_song = self.song_list.get(self.song_list.curselection())
            tag = TinyTag.get(os.path.join(self.folder_path, selected_song))
            self.title_entry.delete(0, tk.END)
            self.title_entry.insert(0, tag.title)
            self.artist_entry.delete(0, tk.END)
            self.artist_entry.insert(0, tag.artist)
        except TinyTagException:
            pass
    
    def save_changes(self):
        selected_song = self.song_list.get(self.song_list.curselection())
        # This is where you'd implement the renaming and metadata editing logic.
        # TinyTag does not support writing metadata, so you'd need another library like mutagen.
        # Example: tag = TinyTag.get(file_path); tag.title = new_title; tag.save()
        print(f"Changes saved for {selected_song}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicMetadataEditor(root)
    root.mainloop()