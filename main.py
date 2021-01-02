from requests import get
from argparse import ArgumentParser

parser = ArgumentParser(description = "This program converts youtube video links to dideo.ir")
parser.add_argument("url", help = "youtube link")
parser.add_argument("--check", action = "store_true", help = "checking for possible errors")
args = parser.parse_args()

url = args.url

def CheckUrl(url):
    try:
        respons = get(url)
        if respons.ok:
            print("No errors")
            return True
        raise Exception("Not ok resopns")
    except:
        print("Link is broken.")
        return False

video_code = url.split('?v=')[1]
video_url = "https://www.dideo.ir/v/yt/{}/".format(video_code)
print(video_url)
if args.check:
    print("Checking for possible errors ...")
    CheckUrl(video_url)
