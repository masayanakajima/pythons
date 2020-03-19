import pytube
import subprocess
import os
import sys

while(True):
	input_text=input("URL or EXIT:")

	if(input_text=="exit"):
	    sys.exit()
	else:
		yt = pytube.YouTube(input_text)
		if(yt==None):
			print("invalid URL")
		else:
			vids= yt.streams.all()
			parent_dir = r""
			vids[0].download(parent_dir)
			default_filename = vids[0].default_filename 
			new_filename = default_filename+".mp3"

			subprocess.call(['ffmpeg', '-i', 
			    os.path.join(parent_dir, default_filename),
			    os.path.join(parent_dir, new_filename)
			])

			print('done')
