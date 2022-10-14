def add_songs(*args):
    result, print_result = {}, ""
    for song_name, lyrics in args:
        result[song_name] = result.get(song_name, []) + lyrics
    for p_song_name, p_lyrics in result.items():
        print_result += f"- {p_song_name}\n" + '\n'.join(p_lyrics)
        if p_lyrics:
            print_result += "\n"
    return print_result


print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),
))


