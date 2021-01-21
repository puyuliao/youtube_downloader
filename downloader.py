##################################################################################################################
# A youtube downloader practice project
# require package: pytube3
# made by puyuliao in 2021/01/21
# reference: 
# https://towardsdatascience.com/build-a-youtube-downloader-with-python-8ef2e6915d97
# https://docs.python.org/3/library/argparse.html#name-or-flags
# https://stackoverflow.com/questions/54028675/pytube-library-receiving-pytube-exceptions-regexmatcherror-regex-pattern-er
# https://stackoverflow.com/questions/775049/how-do-i-convert-seconds-to-hours-minutes-and-seconds/775075
# https://pip.pypa.io/en/stable/reference/pip_freeze/
##################################################################################################################

from pytube import YouTube
import argparse
import datetime
import sys

parser = argparse.ArgumentParser(description='Download youtube videos according to URL, resolution and file format.')
parser.add_argument('-a', '--audio', action="store_true", help='Show audio streams only.')
parser.add_argument('-v', '--video', action="store_true", help='Show video streams only if -a is not specified.')
parser.add_argument('-f', '--first', action="store_true", help='Download the first one in the stream list.')
parser.add_argument('-p', '--path', metavar='{File path}', type=str, default='temp/', help='The path of the target folder of downloads.')
parser.add_argument('URL', metavar='{URL}', type=str, help='The target video URL.')

args = parser.parse_args()
print(f'get URL: {args.URL}')
print(f'get path: {args.path}')
try:
    yt = YouTube(url=args.URL)
    yt.check_availability()
except Exception as e:
    print(e)
    print("The input URL is wrong or unavailable :C. Program exits...")
    sys.exit()


if args.audio:
    streams = yt.streams.filter(only_audio=True)
elif args.video:
    streams = yt.streams.filter(only_video=True)
else:
    streams = yt.streams

str_streams = '\n'.join(list(map(str,streams)))
print(f"""
=======================================Download informations=======================================
Video Title: {yt.title}
Video Length: {str(datetime.timedelta(seconds=yt.length))}
=========================================Available streams=========================================
{str_streams}
===================================================================================================""")
if args.first: 
    try:
        ys = streams.first()
        print("Downloading...")
        ys.download(args.path)
        print("Download completed!!")
        sys.exit()
    except Exception as e:
        print(e)
        sys.exit()
    
while True:
    try:
        itag = input("Enter the corresponding itag to download: ")
        ys = yt.streams.get_by_itag(itag)
        print("Downloading...")
        ys.download(args.path)
        print("Download completed!!")
        break
    except:
        print("Error: This itag is not available.")
        itag = input(f"Enter the corresponding itag to download: ")
        continue

