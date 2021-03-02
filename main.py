# Loops forever
while True:
    import urllib.request
    import re
# Asks you to enter what u want to search
    Context = input("Enter a youtube search: ")
    Search = ""
    for space in Context:
# Making it thatevery space u make it adds a plus sign in between
        if space in " ":
            Search += "+"
        else:
            Search += space
# decodes what u typed
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + Search)
    video_id = re.findall(r"watch\?v=(\S{11})", html.read().decode())
# Sends u the video
    print("https://www.youtube.com/watch?v=" + video_id[0]
# Made by Abadjula#4856
