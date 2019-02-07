from tkinter import *
from mongoengine import *

class ActivityLoggerApp(Tk):
    def __init__(self):
        super().__init__()

        main = Frame(self, width=1000)
        main.pack()

        activity_label_frame = LabelFrame(main, text='Activity', width = 1000)
        activity_label_frame.pack(side=TOP, fill=BOTH)


if __name__ == '__main__':
    connect('ActivityLoggerAppDB', host='localhost', port=27017)
    app = ActivityLoggerApp()
    app.mainloop()