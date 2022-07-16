from tkinter import *
from tkinter import filedialog
import pygame
root=Tk()

root.title("MP3 player")
root.geometry("500x400")
pygame.mixer.init()

def add_song():
    song=filedialog.askopenfilename(initialdir="audio/",filetypes=(("mp3 Files","*.mp3"),))
    #strip out directory
    song=song.replace("/home/admin2/Desktop/MP3-player/audio/","")
    my_label.config(text=song)
    play_box.insert(END, song)

def add_many_songs():
    songs=filedialog.askopenfilenames(initialdir="audio/",filetypes=(("mp3 Files","*.mp3"),))
    for song in songs:
        #strip out directory
        song=song.replace("/home/admin2/Desktop/MP3-player/audio/","")
        my_label.config(text=song)
        play_box.insert(END, song)

def delete_song():
    play_box.delete(ANCHOR)

def delete_songs():
    play_box.delete(0,END)

def play():
    song=play_box.get(ACTIVE)
    song=f'/home/admin2/Desktop/MP3-player/audio/{song}'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

#play_list box
play_box=Listbox(root,bg="black",fg="green",width=60,selectbackground="blue")
play_box.pack(pady=20)




#button images
back_img=PhotoImage(file="icons/output-fast-backward.png")
forward_img=PhotoImage(file="icons/output-fast-forward.png")
play_img=PhotoImage(file="icons/output-play.png")
pause_img=PhotoImage(file="icons/output-pause.png")
stop_img=PhotoImage(file="icons/output-stop.png")

#buttons frame
control_frame=Frame(root)
control_frame.pack(pady=20)

#buttons
back=Button(control_frame,image=back_img,borderwidth=0)
forward=Button(control_frame,image=forward_img,borderwidth=0)
play=Button(control_frame,image=play_img,borderwidth=0,command=play)
pause=Button(control_frame,image=pause_img,borderwidth=0)
stop=Button(control_frame,image=stop_img,borderwidth=0)

back.grid(row=0,column=0,padx=10)
forward.grid(row=0,column=1,padx=10)
play.grid(row=0,column=2,padx=10)
pause.grid(row=0,column=3,padx=10)
stop.grid(row=0,column=4,padx=10)

#menu creation
m_menu=Menu(root)
root.config(menu=m_menu)

#add song menu dropdown
add_song_menu=Menu(m_menu,tearoff=0)
m_menu.add_cascade(label="Add songs",menu=add_song_menu)
add_song_menu.add_command(label="add one song",command=add_song)
#adding many songs
add_song_menu.add_command(label="add more songs",command=add_many_songs)

#remove songs
remove_song_menu=Menu(m_menu,tearoff=0)
m_menu.add_cascade(label="Remove songs",menu=remove_song_menu)
remove_song_menu.add_command(label="Delete a song",command=delete_song)
remove_song_menu.add_command(label="Delete all songs",command=delete_songs)


#temporary label
my_label=Label(root,text="")
my_label.pack(pady=20)


root.mainloop()
