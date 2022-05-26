#from pytube import YouTube

# yt = YouTube('https://www.youtube.com/watch?v=XIZBxIQX10g')
# yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

#YouTube("https://www.youtube.com/watch?v=XIZBxIQX10g").streams.filter(only_audio=True).order_by('resolution').desc().first().download()

from pytube import YouTube
import os
import subprocess
import time

cwd = os.getcwd()

while True:
    url = input("URL: ")

    # Title and Time
    print("...")
    # print(((YouTube(url)).title), "//", (int(var1)/60),"mins")
    # print("...")

    # Filename specification
    # Prevents any errors during conversion due to illegal characters in name
    _filename = input("Filename: ")

    # Downloading
    print("Downloading....")
    YouTube(url).streams.first().download(filename=_filename)
    time.sleep(1)

    # Converting
    mp4 = "'%s'.mp4" % cwd + _filename
    mp3 = "./'%s'.mp3" % _filename
    ffmpeg = ('ffmpeg -i %s ' % mp4 + mp3)
    subprocess.call(ffmpeg, shell=True)

    # Completion
    print("\nCOMPLETE\n")