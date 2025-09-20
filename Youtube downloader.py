import youtube_dl

ydl = youtube_dl.YoutubeDL({'outtmpl': '%(title)s.%(ext)s'})

with ydl:
    result = ydl.extract_info(
        'https://www.youtube.com/watch?v=7CCKGbuzrUM',
        download=False # We want to download the video
    )

    if 'entries' in result:
        # Can be a playlist or a list of videos
        video = result['entries'][0]
    else:
        # Just a video
        video = result

    print(f"Downloaded video: {video['title']}")
    print(f"Video URL: {video['webpage_url']}")

