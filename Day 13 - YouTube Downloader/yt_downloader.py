from pytube import YouTube


def download_yt_video():

    # get youtube video url
    vdo_link = input("Enter video URL: ")

    # get format
    format = input("Enter the format(Video/Audio) in which you want to download: ")

    # make request to youtube
    youtube = YouTube(vdo_link)

    # download audio
    if format.lower() == "audio":

        print("Audio is downloading...")
        youtube.streams.get_audio_only().download()
        print("Audio is downloaded.")

    # download video
    elif format.lower() == "video":

        print("Video is downloading...")

        # filter mp4 format
        youtube = youtube.streams.filter(progressive=True, file_extension="mp4")

        # order by resolution and choose first resolution
        youtube = youtube.order_by("resolution").desc().first()
        # download video
        youtube = youtube.download()

        print("Video is downloaded.")

    else:
        print("Please enter either video or audio as format")
        return False

    return True


if __name__ == "__main__":
    download_yt_video()
