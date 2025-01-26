# Importing the necessary library for video and audio editing
import moviepy.editor

# Importing the file dialog module from tkinter to open file dialogs
from tkinter.filedialog import *

# Open a file dialog for the user to select a video file
vid = askopenfilename()

# Load the selected video file using moviepy
video = moviepy.editor.VideoFileClip(vid)

# Extract the audio from the video file
aud = video.audio

# Save the extracted audio as an MP3 file
aud.write_audiofile("audio.mp3")

# Print a success message after the audio file is created
print("Audio file created successfully.")
