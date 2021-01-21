# YouTube video downloader
### Enjoy download video from YouTube :D
# How to install requirement package:
## Unix/macOS
```
python3 -m pip install -r requirements.txt
```
## Windows
```
py -m pip install -r requirements.txt
```
### If you keep getting "regex_search: could not find match for (?:v=|\/)([0-9A-Za-z_-]{11}).*" exception, reinstall pytube and install the latest pytube directly from github
The following command should fix the issue.
```
pip install git+https://github.com/nficano/pytube.git
```
See <a>https://github.com/pytube/pytube/issues/333</a> for the details.
# Usage
```
downloader.py [-h] [-a] [-v] {URL} {File path}

Download youtube videos according to URL, resolution and file format.

positional arguments:
{URL}        The target video URL.
{File path}  The path of the target folder of downloads.

optional arguments:
-h, --help   show this help message and exit
-a, --audio  Show audio streams only.
-v, --video  Show video streams only if -a is not specified.
```