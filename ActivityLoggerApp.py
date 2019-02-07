from tkinter import *
from mongoengine import *

class ActivityLoggerApp(Tk):
    def __init__(self):
        super().__init__()

        main = Frame(self, width=1000)
        main.pack()

        ## activity frame
        activity_label_frame = LabelFrame(main, text='Activity')
        activity_label_frame.pack(side=TOP, fill=BOTH)
        label = Label(activity_label_frame, text='Activity:')
        label.pack(side=LEFT)
        activity_name = Entry(activity_label_frame, width=30)
        activity_name.pack(side=LEFT)
        add_button = Button(activity_label_frame, text='Add', width=13, command = self.add_activity)
        add_button.pack(side=LEFT)

        ## timer frame
        timer_label_frame = LabelFrame(main, text='Timer')
        timer_label_frame.pack(fill=BOTH)
        time_label = Label(timer_label_frame, text='0 s', width=30)
        time_label.pack(side=LEFT)
        start_stop_button = Button(timer_label_frame, text='START', width=13, command=self.start_activity)
        start_stop_button.pack()

        ## statistics frame
        statistics_label_frame = LabelFrame(main, text='Statistics')
        statistics_label_frame.pack(side=BOTTOM, fill=BOTH)
        statistics_button = Button(statistics_label_frame, text='Generate statistics', command=self.generate_stats)
        statistics_button.pack()

    def generate_stats(self):
        pass

    def start_activity(self):
        pass

    def add_activity(self):
        pass


if __name__ == '__main__':
    connect('ActivityLoggerAppDB', host='localhost', port=27017)
    app = ActivityLoggerApp()
    app.mainloop()