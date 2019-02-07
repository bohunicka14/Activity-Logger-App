from tkinter import *
from mongoengine import *
from Activity import *

class ActivityLoggerApp(Tk):
    def __init__(self):
        super().__init__()

        main = Frame(self, width=1000)
        main.pack()

        self.duration = 0 # in seconds
        self.activity_is_stopped = True

        self.fields1 = ['name', 'duration']
        self.fields2 = ['from', 'to']
        self.db = []

        ## activity frame
        activity_label_frame = LabelFrame(main, text='Activity')
        activity_label_frame.pack(side=TOP, fill=BOTH)
        label = Label(activity_label_frame, text='Activity:')
        label.pack(side=LEFT)

        self.content = StringVar()
        activity_name_entry = Entry(activity_label_frame, width=30, textvariable=self.content)
        activity_name_entry.pack(side=LEFT)
        add_button = Button(activity_label_frame, text='Add', width=13, command = self.add_activity)
        add_button.pack(side=LEFT)

        ## timer frame
        timer_label_frame = LabelFrame(main, text='Timer')
        timer_label_frame.pack(fill=BOTH)
        self.time_label = Label(timer_label_frame, text='0 h 0 m {} s'.format(self.duration), width=30)
        self.time_label.pack(side=LEFT)
        self.start_stop_button = Button(timer_label_frame, text='START', width=13, command=self.start_activity)
        self.start_stop_button.pack()

        ## statistics frame
        statistics_label_frame = LabelFrame(main, text='Statistics')
        statistics_label_frame.pack(side=BOTTOM, fill=BOTH)
        statistics_button = Button(statistics_label_frame, text='Generate statistics', command=self.generate_stats)
        statistics_button.pack(side=LEFT)
        finish_button = Button(statistics_label_frame, text='Finish Activity', command=self.finish)
        finish_button.pack(side=LEFT)

        self.timer()

    def finish(self):
        pass

    def generate_stats(self):
        pass

    def start_activity(self):
        if self.activity_is_stopped:
            self.activity_is_stopped = False
            self.start_stop_button.config(text='STOP')

        else:
            self.start_stop_button.config(text='START')
            self.activity_is_stopped = True

    def add_activity(self):
        self.activity_name = self.content.get()
        activity = Activity(name = self.activity_name)
        activity.save()
        for i in Activity.objects:
            print(i.name)

    def timer(self):
        if not self.activity_is_stopped:
            formated_result = self.format_seconds(self.duration)
            self.time_label.config(text='{} h {} m {} s'.format(formated_result.get('h'), formated_result.get('m'),
                                                                formated_result.get('s')))
            self.duration += 1
        self.after(1000, self.timer)

    def format_seconds(self, s):
        hours = s // 3600
        s = s % 3600
        minutes = s // 60
        s = s % 60

        return {'h': hours, 'm': minutes, 's': s}


if __name__ == '__main__':
    connect('ActivityLoggerAppDB', host='mongodb://localhost/ActivityLoggerAppDB', port=27017)
    app = ActivityLoggerApp()
    app.mainloop()