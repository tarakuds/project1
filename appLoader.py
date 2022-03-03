from instaloader import instaloader, Profile
runIg = instaloader.Instaloader()

image = input('what is the display name you wish to download profile picture: ')

print('Your download has started ...')

runIg.download_profile(image, profile_pic_only = True)
print('Download completed')
