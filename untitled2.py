import librosa
import tkinter as tk
from tkinter import filedialog

# Function to calculate musical key
import librosa
import numpy as np

def calculate_key(file_path):
    # Load the audio file
    y, sr = librosa.load(file_path)
    # Compute the Chroma feature
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)
    # Aggregate chroma features over time (summing across columns)
    chroma_sum = np.sum(chroma, axis=1)
    # Find the pitch class with the highest energy
    key_index = np.argmax(chroma_sum)
    # Map the pitch class index to a note name
    note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    detected_key = note_names[key_index % 12]
    return detected_key

# Function to calculate BPM
def calculate_bpm(file_path):
    y, sr = librosa.load(file_path)
    # Adjusting parameters for beat tracking
    # Using start_bpm as an initial guess for the tempo
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr, hop_length=64, start_bpm=120)
    return tempo

# Function to handle file selection and display results
def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:  # Ensure a file was selected
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