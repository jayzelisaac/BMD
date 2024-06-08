import librosa
import tkinter as tk
from tkinter import filedialog

# Function to calculate BPM
def calculate_bpm(file_path):
    y, sr = librosa.load(file_path)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    return tempo

# Function to calculate musical key
def calculate_key(file_path):
    y, sr = librosa.load(file_path)
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    key = librosa.key.reference_key(chroma)
    return key


# Function to handle file selection and display results
def select_file():
    file_path = filedialog.askopenfilename()
    bpm = calculate_bpm(file_path)
    key = calculate_key(file_path)
    display_results(bpm, key)

# Function to display BPM and key results
def display_results(bpm, key):
    result_label.config(text=f"BPM: {bpm}\nKey: {key}")

# Create the main application window
root = tk.Tk()
root.title("Music Analyzer")

# Create GUI elements
label = tk.Label(root, text="Select an audio file:")
label.pack()

select_button = tk.Button(root, text="Select File", command=select_file)
select_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()
