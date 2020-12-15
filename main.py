from sys import argv
from requests import get


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


control_args = {'--check': CheckUrl}

if len(argv) == 2 or len(argv) == 3:
    video_code = argv[1].split('?v=')[1]
    video_url = "https://www.dideo.ir/v/yt/{}/".format(video_code)
    print(video_url)

    if len(argv) > 2:
        if control_args.get(argv[2], False):
            print("Checking for possible errors ...")
            control_args[argv[2]](video_url)

elif len(argv) > 3:
    print("Too much args!")
else:
    print("Missing args!")
