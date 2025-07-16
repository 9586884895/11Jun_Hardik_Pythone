from pytubefix import YouTube

url="https://www.youtube.com/watch?v=U4OsMLDRJeE"

YouTube(url).streams.first().download()