from pytube import YouTube
import subprocess
import os

downloadDirectory = '/mnt/c/users/bobi/Desktop'

youTubeLink = input('turi linka: ')
fileName = input('name: ')
fileExtensionMp4 = 'mp4'
fileExtensionMp3 = 'mp3'
mp4File = f'{fileName}.{fileExtensionMp4}'
mp3File = f'{fileName}.{fileExtensionMp3}'

youTube = YouTube(youTubeLink)
streams = youTube.streams
filteredStreams = streams.filter(progressive=True, file_extension=fileExtensionMp4)
streamsOrderedByResolution = filteredStreams.order_by('resolution').desc()
firstStream = streamsOrderedByResolution.first()
firstStream.download(downloadDirectory, filename = mp4File)
ffmpeg = f'ffmpeg -i {downloadDirectory}/{mp4File} -f mp3 -ab 320000 -vn {downloadDirectory}/{mp3File}'
print(f'Converting {mp4File} to {mp3File}')
subprocess.call(ffmpeg, shell=True)
os.remove(f'{downloadDirectory}/{mp4File}')
print('\nGotoo\n')
