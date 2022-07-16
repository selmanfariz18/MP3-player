from tkinter import *

root=Tk()

root.title("MP3 player")
root.geometry("500x400")

#play_list box
play_box=Listbox(root,bg="black",fg="green",width=60)
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
play=Button(control_frame,image=play_img,borderwidth=0)
pause=Button(control_frame,image=pause_img,borderwidth=0)
stop=Button(control_frame,image=stop_img,borderwidth=0)

back.grid(row=0,column=0,padx=10)
forward.grid(row=0,column=1,padx=10)
play.grid(row=0,column=2,padx=10)
pause.grid(row=0,column=3,padx=10)
stop.grid(row=0,column=4,padx=10)
root.mainloop()
