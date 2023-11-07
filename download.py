from yt_dlp import YoutubeDL


def download_audio_from_url(url):
    videoinfo = YoutubeDL().extract_info(url=url, download=False)
    length = videoinfo['duration']
    filename = f"./audio/youtube/{videoinfo['id']}.mp3"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
    }
    with YoutubeDL(options) as ydl:
        ydl.download([videoinfo['webpage_url']])
    return filename, length


# Testing by running this file
if __name__ == "__main__":
    url = "https://www.youtube.com/watch?v=q_eMJiOPZMU"
    filename, length = download_audio_from_url(url)
    print(f"Audio file: {filename} with length {length} seconds")
    print("Done!")
