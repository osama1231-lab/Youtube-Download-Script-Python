from pafy import new
#---------------------------------------------------
import pytube 
link = input('Enter your link here : ')
url = link
playlist= pytube.Playlist(url)
print('Number of videos %s' % len(playlist.video_urls))
#---------------------------------------------------
video = new(link)
stream = video.streams 
for i in stream:
    print(i)
print('IMPORTANT :','choose 0 for 1st quality & 1 for 2nd quality and 2 for 3rd and so on ')
quality = input('choose your quality : ')
quality = int(quality)
for i in playlist.video_urls:
    youtube = pytube.YouTube(i)
    video = youtube.streams
    video[quality].download()