#%

#Importing dependencies
from pytube import YouTube

video_url = ''  # Add your video URL

try:

    yt = YouTube(video_url)
    video_stream = yt.streams.get_highest_resolution()
    video_stream.download(output_path='.', filename='downloaded_video.mp4')  # Replace file name with video name you want and/or a specific file location
    print(f"Downloaded: {yt.title}")

except Exception as e:
    print(f"An error occurred: {e}")
