import random
class Playlist:
    def __init__(self):
        self.songs= []
        self.current_song_index=0

    def add_song(self,song):
        self.songs.append(song)

    def remove_song(self,song):
        if song in self.songs:
            self.songs.remove(song)
        else:
            print(f"The song {song} is not in the playlist.")

    def play_song(self,song):
        if song in self.songs:
            print(f"Playing: {song}")
        else:
            print(f"The song {song} ia not in the playlist.")

    def next_song(self):
        if self.songs:
            self.current_song_index=(self.current_song_index+1)%len(self.songs)
            print(f"Next song: {self.songs[self.current_song_index]}")
        else:
            print("The playlist is empty.")

    def previous_song(self):
        if self.songs:
            self.current_song_index=(self.current_song_index-1)%len(self.songs)
            print(f"previous song: {self.songs[self.current_song_index]}")
        else:
            print("The playlist is empty.")

    def shuffle(self):
        if self.songs:
            random.shuffle(self.songs)
            print("Playlist shuffled.")
        else:
            print("Playlist is empty.")

playlist=Playlist()
playlist.add_song("song 1")
playlist.add_song("song 2")
playlist.add_song("song 3")

playlist.play_song("song 2")
playlist.next_song()
playlist.previous_song()
playlist.shuffle()