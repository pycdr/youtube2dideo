import sys
import requests

def CheckUrl(url):
    try:
        respons = requests.get(url)
        if respons.ok:
            print("No errors")
            return True
        raise Exception("Not ok resopns")
    except:
        print("Link is broken.")
        return False

args = sys.argv
control_args = {'--check':CheckUrl}

if len(args) == 2 or len(args) == 3:
    video_code = args[1].split('?v=')[1]
    video_url = "https://www.dideo.ir/v/yt/{}/".format(video_code)
    print(video_url)
    
    if len(args) > 2:
        if control_args.get(args[2],False):
            print("Checking for possible errors ...")
            control_args[args[2]](video_url)

elif len(args) > 3:
    print("Too much args!")
else:
    print("Missing args!")
