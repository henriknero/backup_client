import tkinter
from backup_client.filehandler import observer

observer = observer.FileObserver()
observer.add_dir('.')
observer.start()


def do_stuff_pls():
    observer.add_file('.\\fuckme.txt')


top = tkinter.Tk()
button = tkinter.Button(top, text='Pls press me', command=do_stuff_pls)
button.pack()
top.mainloop()
