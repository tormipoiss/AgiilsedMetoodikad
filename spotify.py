allMuusika = [
{"title": "Bohemian Rhapsody", "artist": "Queen"},
{"title": "Billie Jean", "artist": "Michael Jackson"},
{"title": "Imagine", "artist": "John Lennon"},
{"title": "Shape of You", "artist": "Ed Sheeran"},
{"title": "Rolling in the Deep", "artist": "Adele"},
{"title": "Smells Like Teen Spirit", "artist": "Nirvana"},
{"title": "Hotel California", "artist": "Eagles"},
{"title": "Sweet Child O' Mine", "artist": "Guns N' Roses"},
{"title": "Stairway to Heaven", "artist": "Led Zeppelin"},
{"title": "Thriller", "artist": "Michael Jackson"},
{"title": "Someone Like You", "artist": "Adele"},
{"title": "Nothing Else Matters", "artist": "Metallica"},
{"title": "Yesterday", "artist": "The Beatles"},
{"title": "Bad Guy", "artist": "Billie Eilish"},
{"title": "Wonderwall", "artist": "Oasis"},
{"title": "Viva la Vida", "artist": "Coldplay"},
{"title": "Blinding Lights", "artist": "The Weeknd"},
{"title": "Dance Monkey", "artist": "Tones and I"},
{"title": "Shallow", "artist": "Lady Gaga & Bradley Cooper"},
{"title": "Lose Yourself", "artist": "Eminem"}
]

def otsi_muusikat(item):
    if not item:
        print("Sisend on tühi.")
    
    tulemused = []
    for laul in allMuusika:
        if item in laul["title"] or item in laul["artist"]:
            tulemused.append(laul)

    if tulemused:
        print("Leitud laulud otsinguga: " + item)
        for i in tulemused:
            print(f"{i['title']} - {i['artist']}")
    else:
        print("Laulu ei leitud")

otsi_muusikat("Billie")

def filtreeri_muusikat(artist):
    if not artist:
        print("Sisend on tühi.")
    
    tulemused = []
    for laul in allMuusika:
        if artist in laul["artist"]:
            tulemused.append(laul)

    if tulemused:
        print("Leitud laulud artistiga: " + artist)
        for i in tulemused:
            print(f"{i['title']} - {i['artist']}")
    else:
        print("Laulu ei leitud")

filtreeri_muusikat("Adele")