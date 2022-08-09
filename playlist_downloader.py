from pytube import Playlist

link = input("Entrez l'URL de la playlist: ")

def on_download_progress(stream,chunk, bytes_remainding):
    print(int(( stream.filesize - bytes_remainding) * 100 / stream.filesize),"%")

yt_playlist = Playlist(link)

for video in yt_playlist.videos:
    video.register_on_progress_callback(on_download_progress)
    video.streams.get_highest_resolution().download("C:/Users/user/Desktop/Charbel/Compose courses")
    print("Video Downloaded: ", video.title)
print("\nFINIS!!!!")
