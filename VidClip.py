
# ▌ ▐·▪   ▄▄· ▪        ▄• ▄▌.▄▄ · 
#▪█·█▌██ ▐█ ▌▪██ ▪     █▪██▌▐█ ▀. 
#▐█▐█•▐█·██ ▄▄▐█· ▄█▀▄ █▌▐█▌▄▀▀▀█▄
# ███ ▐█▌▐███▌▐█▌▐█▌.▐▌▐█▄█▌▐█▄▪▐█
#. ▀  ▀▀▀·▀▀▀ ▀▀▀ ▀█▄▀▪ ▀▀▀  ▀▀▀▀ 

# Make sure you have ffmpeg installed and setup
# on CMD (admin) run pip install PyQt5 PyQt5-tools wxPython
# run this program through CMD as administrator or you will get an error on export
# Exported clips will share the same name as the input file, with part numbers following
# Clips will be exported in the same directory as the input clip

from tkinter import *
from tkinter import filedialog
from moviepy.video.io.VideoFileClip import VideoFileClip

root = Tk()
root.title("Video Clipping Tool")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.avi *.mov")])
    file_entry.delete(0, END)
    file_entry.insert(0, file_path)

def split_video():
    file_path = file_entry.get()
    clip_length = int(clip_length_entry.get())
    video = VideoFileClip(file_path)
    duration = video.duration
    clips = []
    for i in range(0, int(duration), clip_length):
        start_time = i
        end_time = min(i + clip_length, duration)
        clip = video.subclip(start_time, end_time)
        clips.append(clip)
    for i, clip in enumerate(clips):
        clip.write_videofile("{}_part{}.mp4".format(file_path[:-4], i+1), codec='libx264')

def grab_clips():
    file_path = file_entry.get()
    start_time = int(start_time_entry.get())
    end_time = int(end_time_entry.get())
    video = VideoFileClip(file_path)
    clip = video.subclip(start_time, end_time)
    clip.write_videofile("grabbed_clip.mp4", codec='libx264')

file_label = Label(root, text="Video File:")
file_label.grid(row=0, column=0, padx=5, pady=5)

file_entry = Entry(root)
file_entry.grid(row=0, column=1, padx=5, pady=5)

browse_button = Button(root, text="Browse", command=browse_file)
browse_button.grid(row=0, column=2, padx=5, pady=5)

clip_length_label = Label(root, text="Clip Length (seconds):")
clip_length_label.grid(row=1, column=0, padx=5, pady=5)

clip_length_entry = Entry(root)
clip_length_entry.grid(row=1, column=1, padx=5, pady=5)

split_button = Button(root, text="Split Video", command=split_video)
split_button.grid(row=1, column=2, padx=5, pady=5)

start_time_label = Label(root, text="Start Time (seconds):")
start_time_label.grid(row=2, column=0, padx=5, pady=5)

start_time_entry = Entry(root)
start_time_entry.grid(row=2, column=1, padx=5, pady=5)

end_time_label = Label(root, text="End Time (seconds):")
end_time_label.grid(row=3, column=0, padx=5, pady=5)

end_time_entry = Entry(root)
end_time_entry.grid(row=3, column=1, padx=5, pady=5)

grab_button = Button(root, text="Grab Clip", command=grab_clips)
grab_button.grid(row=3, column=2, padx=5, pady=5)

root.mainloop()
