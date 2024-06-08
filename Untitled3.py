import librosa
import librosa.display
import matplotlib.pyplot as plt

# Step 1: Load the audio file
file_path = '/path/to/your/audio/file.mp3'  # Replace with your audio file path
y, sr = librosa.load(file_path)

# Step 2: Compute the chroma features
chroma = librosa.feature.chroma_stft(y=y, sr=sr)

# Optional: Display the chroma features
plt.figure(figsize=(10, 4))
librosa.display.specshow(chroma, y_axis='chroma', x_axis='time')
plt.colorbar()
plt.title('Chroma Features')
plt.tight_layout()
plt.show()