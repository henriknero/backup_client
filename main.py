import tkinter
from backup_client.filehandler import observer
#import pdb;pdb.set_trace()
observer = observer.FileObserver()
observer.addDir('.')
observer.start()

def doStuffPls():
    observer.addFile('.\\fuckme.txt')
    

top = tkinter.Tk()
button = tkinter.Button(top,text='Pls press me', command=doStuffPls)
button.pack()
top.mainloop()