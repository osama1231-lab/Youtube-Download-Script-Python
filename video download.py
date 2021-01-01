from pafy import new 
url= input('Enter video link :')
video = new(url)
stream = video.streams 
print('aviable qualities')
for i in stream:
    print(i)
print('IMPORTANT :','choose 0 for 1st quality & 1 for 2nd quality and 2 for 3rd and so on ')
quality = input('choose your quality : ')
quality = int(quality)
stream[quality].download()

