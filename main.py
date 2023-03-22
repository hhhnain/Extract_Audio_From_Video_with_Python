######## To install the moviepy library, SIMPLY ENTER: pip install moviepy into Command prompt

#load library that we are gonna use
from moviepy.editor import VideoFileClip

#load the video file, specify path if not in the folder of script
video = VideoFileClip('yourVideoName.mp4') #change name to your video name

#extract audio from the video file 
the_audio = video.audio 

#save audio
the_audio.write_audiofile('YourAudioName.mp3') #remember the .mp3, .wav extension

