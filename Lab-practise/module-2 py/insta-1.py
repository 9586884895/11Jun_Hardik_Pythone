import instaloader

instaID=input("Enter any Instagram Id=")

insta=instaloader.Instaloader()

insta.download_profile(instaID)

print("Download Sucessfully")