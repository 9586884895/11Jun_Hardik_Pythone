from pytubefix import YouTube

url="https://www.youtube.com/watch?v=iYueDsR5-Sk&list=RDiYueDsR5-Sk&start_radio=1"

YouTube(url).streams.first().download()