from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import pygame
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk
root=Tk()

root.title("MP3 player")
root.geometry("650x400")
pygame.mixer.init()

def play_time():
    if stopped:
        return

    current_time=pygame.mixer.music.get_pos()/1000
    converted_current_time=time.strftime('%M:%S',time.gmtime(current_time))
    song=play_box.get(ACTIVE)
    song_mut=MP3(song)
    global song_length
    song_length=song_mut.info.length
    converted_song_length=time.strftime('%M:%S',time.gmtime(song_length))
    
    if int(song_slider.get())==int(song_length):
        stop()

    elif paused:
        pass
    else:
        next_time=int(song_slider.get())+1
        song_slider.config(to=song_length,value=next_time)
        converted_current_time=time.strftime('%M:%S',time.gmtime(int(song_slider.get())))
        status_bar.config(text=f'Time Elapsed: {converted_current_time} of {converted_song_length}')

    if current_time>=1:
        status_bar.config(text=f'Time Elapsed: {converted_current_time} of {converted_song_length}')
    status_bar.after(1000,play_time)




def songs():
    songs=filedialog.askopenfilenames(initialdir="audio/",filetypes=(("mp3 Files","*.mp3"),))
    for song in songs:
        #strip out directory
        #song=song.replace("/home/admin2/Desktop/MP3-player/audio/","")
        my_label.config(text=song)
        play_box.insert(END, song)

def delete_song():
    play_box.delete(ANCHOR)

def delete_songs():
    play_box.delete(0,END)

def play():
    global stopped
    stopped=False
    song=play_box.get(ACTIVE)
    #song=f'/home/admin2/Desktop/MP3-player/audio/{song}'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    play_time()


global stopped
stopped=False
def stop():
    pygame.mixer.music.stop()
    play_box.selection_clear(ACTIVE)
    status_bar.config(text=f'')
    song_slider.config(value=0)
    global stopped
    stopped=True

#pause variable
global paused
paused=False

def pause(paused_1):
    global paused
    paused=paused_1
    if paused:
        pygame.mixer.music.unpause()
        paused=False
    else:
        pygame.mixer.music.pause()
        paused=True

def next_song():
    status_bar.config(text='')
    song_slider.config(value=0)
    next_one=play_box.curselection()
    next_one=next_one[0]+1
    song=play_box.get(next_one)
    song=f'{song}'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    play_box.selection_clear(0,END)
    play_box.activate(next_one)
    play_box.selection_set(next_one,last=None)

def previous_song():
    status_bar.config(text='')
    song_slider.config(value=0)
    next_one=play_box.curselection()
    next_one=next_one[0]-1
    song=play_box.get(next_one)
    song=f'{song}'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    play_box.selection_clear(0,END)
    play_box.activate(next_one)
    play_box.selection_set(next_one,last=None)

def volume(x):
    pygame.mixer.music.set_volume(volume_slider.get())

def seek(x):
    song=play_box.get(ACTIVE)
    #song=f'/home/admin2/Desktop/MP3-player/audio/{song}'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0,start=song_slider.get())


#main frame
main_frame=Frame(root)
main_frame.pack(pady=20)

#play_list box
play_box=Listbox(main_frame,bg="black",fg="green",width=60,selectbackground="blue")
play_box.grid(row=0,column=0)

#volume slider frame
volume_frame=LabelFrame(main_frame,text="volume")
volume_frame.grid(row=0,column=1)
#volume slider
volume_slider=ttk.Scale(volume_frame,from_=1,to=0,orient=VERTICAL,length=125,value=1,command=volume)
volume_slider.pack(pady=10)

#song slider
song_slider=ttk.Scale(main_frame,from_=0,to=100,orient=HORIZONTAL,length=550,value=0,command=seek)
song_slider.grid(row=2,column=0,pady=20,padx=10)

#button images
back_img=PhotoImage(file="icons/output-fast-backward.png")
forward_img=PhotoImage(file="icons/output-fast-forward.png")
play_img=PhotoImage(file="icons/output-play.png")
pause_img=PhotoImage(file="icons/output-pause.png")
stop_img=PhotoImage(file="icons/output-stop.png")

#buttons frame
control_frame=Frame(main_frame)
control_frame.grid(row=1,column=0,pady=20)

#buttons
back_btn=Button(control_frame,image=back_img,borderwidth=0,command=previous_song)
forward_btn=Button(control_frame,image=forward_img,borderwidth=0,command=next_song)
play_btn=Button(control_frame,image=play_img,borderwidth=0,command=play)
pause_btn=Button(control_frame,image=pause_img,borderwidth=0,command=lambda:pause(paused))
stop_btn=Button(control_frame,image=stop_img,borderwidth=0,command=stop)

back_btn.grid(row=0,column=0,padx=10)
forward_btn.grid(row=0,column=1,padx=10)
play_btn.grid(row=0,column=2,padx=10)
pause_btn.grid(row=0,column=3,padx=10)
stop_btn.grid(row=0,column=4,padx=10)

#menu creation
m_menu=Menu(root)
root.config(menu=m_menu)

#add song menu dropdown
add_song_menu=Menu(m_menu,tearoff=0)
m_menu.add_command(label="Add songs",command=songs)
#adding many songs
#m_menu.add_command(label="add more songs",command=songs)

#remove songs
remove_song_menu=Menu(m_menu,tearoff=0)
m_menu.add_cascade(label="Remove songs",menu=remove_song_menu)
remove_song_menu.add_command(label="Delete a song",command=delete_song)
remove_song_menu.add_command(label="Delete all songs",command=delete_songs)

#status bar
status_bar=Label(root,text='nothing',bd=1,relief=GROOVE,anchor=E)
status_bar.pack(fill=X,side=BOTTOM,ipady=2)


#temporary label
my_label=Label(root,text="")
my_label.pack(pady=20)


root.mainloop()
