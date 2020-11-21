import os
import sys

if __name__ != '__main__':
    print("Currently not support importing.")
    raise KeyboardInterrupt("Force Exit")

print("Supported: ")
print("Pictures: png, jpg, jpeg, tif, tiff, bmp, gif, ico")
print("Videos: mp4, webm, mov, mkv, avi, flv(RIP), wmv")
print("Audio: mp3, ape, flac, wav, m4a")

print("Please copy this file to the folder, that has all these files.")
print("Press Enter to continue, or press 'q' and enter to exit.")
t = input("")
if t == "q":
    print("Quitting..")
    sys.exit(1)

print("Working on it...")
print("Outputting to 'vap.html'...")
print("Getting files' properties...")
fp = open("vap.html", 'w')
os.system("dir /b *.png *.jpg *.jpeg *.tif *.tiff *.bmp *.gif *.ico > pictures.vap.tmp")
os.system("dir /b *.mp4 *.webm *.mov *.mkv *.avi *.flv *.wmv > videos.vap.tmp")
os.system("dir /b *.mp3 *.ape *.flac *.wav *.m4a > audio.vap.tmp")
os.system("echo \nEOF > pictures.vap.tmp")
os.system("echo \nEOF > videos.vap.tmp")
os.system("echo \nEOF > audio.vap.tmp")
pic = open("pictures.vap.tmp")
vid = open("videos.vap.tmp")
ado = open("audio.vap.tmp")
print("Processing Pictures...")
p = ""
v = ""
a = ""
for picline in pic:
    picline = picline.strip("\n")
    if picline == "EOF":
        break
    p += '\n<img src="' + str(picline) + '" style="width:100%;"></img>'
print("Processing Videos...")
for vidline in vid:
    vidline = vidline.strip("\n")
    if vidline == "EOF":
        break
    v = '\n<video src="' + str(vidline) + '" controls></video>'
print("Processing Audio...")
for adoline in ado:
    adoline = adoline.strip("\n")
    if adoline == "EOF":
        break
    a = '\n<audio src="' + str(adoline) + '" controls="controls"></audio>'

print("Writting to file...")
fp.write("<!DOCTYPE HTML>\n<HTML>\n<HEAD><TITLE>VAP OUTPUT</TITLE>\n</HEAD>\n<BODY>\n" + str(p) + "\n" + str(v) + "\n" + str(a) + "\n</BODY>\n</HTML>")
pic.close()
vid.close()
ado.close()
fp.close()
os.remove("pictures.vap.tmp")
os.remove("videos.vap.tmp")
os.remove("audio.vap.tmp")
print("Done.")
os.system("vap.html")
