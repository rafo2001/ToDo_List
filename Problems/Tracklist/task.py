def tracklist(**kwargs):
    for key, values in kwargs.items():
        print(key)
        for album, track in values.items():
            print(f"ALBUM: {album} TRACK: {track}")
