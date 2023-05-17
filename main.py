import ttkbootstrap as ttk
from generate import TextGenerator



class TypeInterface:
    def __init__(self):git

        self.text = None
        self.stats = False
        self.correct_words = []
        self.timer = None
        self.wpm = 0
        # self.seconds = 15

        # ------------------------------------Window------------------------------------------------------------ #
        self.window = ttk.Window(title="Typing Speed Test",
                                 themename="vapor",
                                 resizable=(False, False),
                                 size=(800, 800),)

        # ------------------------------------Entry------------------------------------------------------------ #
        self.entry = ttk.Entry(self.window,
                               font=("Arial", 20))
        self.entry.grid(column=0,
                        row=0, columnspan=3,
                        padx=20,
                        pady=35,
                        sticky="ew")
        self.entry.insert(0, "Type Here")
        self.entry.configure(state="disabled")
        self.window.columnconfigure(0, weight=1)

        # ------------------------------------RadioButtons------------------------------------------------------------ #
        self.var = ttk.IntVar()

        self.radio1 = ttk.Radiobutton(self.window, text="15s", variable=self.var, value=15)
        self.radio1.grid(row=1, column=0, )

        self.radio2 = ttk.Radiobutton(self.window, text="30s", variable=self.var, value=30)
        self.radio2.grid(row=1, column=1,)

        self.radio3 = ttk.Radiobutton(self.window, text="60s", variable=self.var, value=60)
        self.radio3.grid(row=1, column=2,)

        self.var.set(15)
        self.seconds = self.var.get()

        # ------------------------------------Button------------------------------------------------------------ #
        self.start_button = ttk.Button(text="Start",
                                       command=self.start_button_control,
                                       cursor="hand2",
                                       )
        self.start_button.grid(column=0,
                               row=2,
                               pady=30,
                               padx=50)

        self.stop_button = ttk.Button(text="Stop",
                                       command=self.stop_button_control,
                                       cursor="hand2",
                                       )
        self.stop_button.grid(column=1,
                               row=2,
                               pady=30,
                               padx=50)
        # ------------------------------------Meter------------------------------------------------------------ #
        self.clock = ttk.Meter(self.window,
                               amounttotal=self.seconds,
                               amountused=self.seconds,
                               showtext=True)
        self.clock.grid(row=2,
                        column=2,
                        pady=30,
                        padx=100)

        # ------------------------------------Label------------------------------------------------------------ #
        self.label = ttk.Label(self.window,
                               text="Press Start",
                               wraplength=600,
                               font=("Arial", 20),
                               justify="center")
        self.label.grid(row=3,
                        column=0,
                        columnspan=3)
        # ----------------------------------------------------------------------------------------------------------- #
        self.window.mainloop()
# ------------------------------------------------------------------------------------------------------------------- #
    def timer_countdown(self, count):
        '''Implements timer countdown mechanism'''
        self.clock.configure(amountused=count)
        if count >0:
            self.timer = self.window.after(1000, self.timer_countdown, count-1)
            self.start_button.configure(text="Reset")
        else:
            self.get_stats()

    def get_stats(self):
        '''Calculate and outputs Words per Minute'''
        text_list = self.text.split()
        entry_list = self.entry.get().split()
        self.entry.configure(state="disabled")
        for index in range(0,len(entry_list)):
            if entry_list[index] == text_list[index]:
                self.correct_words.append(entry_list[index])

        self.wpm = int(len(self.correct_words)//(self.seconds/60))
        self.label.configure(text=f"WPM: {self.wpm}")
        self.wpm = 0
        self.correct_words = []

    def start_button_control(self):

        if self.timer == None:
            self.configure_clock()
            self.timer_countdown(self.seconds)

        else:
            self.configure_clock()
            self.window.after_cancel(self.timer)  # Stop previous timer from implementing
            self.label.configure(text=self.text)
            self.timer_countdown(self.seconds)

    def configure_clock(self):
        '''Configure Clock based the radiobutton selected'''
        self.text = TextGenerator().text
        self.seconds = self.var.get()
        self.clock.configure(amounttotal=self.seconds)
        self.label.configure(text=self.text)
        self.entry.configure(state="enabled")
        self.entry.delete(0, "end")

    def stop_button_control(self):
        self.window.after_cancel(self.timer)
# ----------------------------------------------------------------------------------------------------------------- #


app = TypeInterface()
