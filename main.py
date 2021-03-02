import urllib.request
import re
Context = input("Enter a youtube search: ")
Search = ""
for space in Context:
    if space in " ":
        Search += "+"
    else:
        Search += space
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + Search)
video_id = re.findall(r"watch\?v=(\S{11})", html.read().decode())
print("https://www.youtube.com/watch?v=" + video_id[0])