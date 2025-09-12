from pytubefix import YouTube

url="https://www.youtube.com/watch?v=lrRgJP8DraA&list=RDlrRgJP8DraA&start_radio=1"

YouTube(url).streams.first().download()