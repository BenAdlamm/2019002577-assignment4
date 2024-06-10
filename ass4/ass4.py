from tkinter import *

# define class App
class App(Tk): # constructor for app
    def __init__(self): # inherets functions from itsself (class)
        super().__init__()
        # creating pop-up window
        self.title("Assessment 4") 
        self.geometry("500x500")

        ass4_frame = Ass4_Frame(self) # identifying the frame (frame of the window(background))
        ass4_frame.show_frame()
# PARENT CLASS ^        


class Ass4_Frame(Frame):
    def __init__(self, parent): # constructor for frame
        super().__init__(parent)
        
    def show_frame(self): # method to create buttons and textboxes
        self.pack(pady=20)
        
        # buttons
        self.print_all = Button(self, text="Print All", font="Arial", command=print_all)
        self.pos_growth = Button(self, text="Positive Growth", font="Arial", command=pos_growth)
        self.filt_date = Button(self, text="By Date", font="Arial", command=filt_date)
        self.filt_range = Button(self, text="Date Range", font="Arial", command=filt_range)
        
        # create textbox labels
        self.label_date = Label(self, text="Filter Date").grid(row=4, column=0, pady=10, padx=10)
        self.label_range = Label(self, text="Filter Range").grid(row=5, column=0, pady=10, padx=10)
        
        # create textboxes
        self.text_date = Entry(self).grid(row=4, column=1, pady=10, padx=10)
        self.text_startdate = Entry(self).grid(row=5, column=1, pady=10, padx=10)
        self.text_enddate = Entry(self).grid(row=5, column=2, pady=10, padx=10)
        
        # lay the buttons within the frame
        self.print_all.grid(row=0, column= 0, pady=10, padx= 10)
        self.pos_growth.grid(row=0, column= 1, pady=10, padx= 10)
        self.filt_date.grid(row=1, column= 0, pady=10, padx= 10)     
        self.filt_range.grid(row=1, column= 1, pady=10, padx= 10)
        
        def print_all(self):
            # prints all records

        def pos_growth(self):
            # prints all positive growth records

        def filt_date(self):
            # prints all records by date

        def filt_range(self):
            # prints all records within a range of dates
        
        

app = App()
app.mainloop()