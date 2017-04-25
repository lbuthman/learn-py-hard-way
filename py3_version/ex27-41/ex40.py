class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

danger_zone = Song(["Right into the danger zone.",
                    "Not sure of the other lyrics, danger zone.",
                    "It's a really dangerous danger in the danger zone."])

coconuts = Song(["I've got a lovely bunch of coconuts",
                 "Twiddle-lee-dee",
                 "Here they are standing in a row",
                 "Big one, small ones some as big as your head ..."])

danger_zone.sing_me_a_song()

coconuts.sing_me_a_song()
