import tkinter as tk
from tkinter import font  as tkfont
from PIL import Image, ImageTk
import os
from tkinter import filedialog
from tkinter import ttk

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller, master = None, *pargs):
        tk.Frame.__init__(self, parent, master, *pargs)
        self.controller = controller
        #label = tk.Label(self, text="This is the start page", font=controller.title_font)
        #label.pack(side="top", fill="x", pady=10)
        self.image = Image.open('E:/Frontend_Tkinter/ECE-block.jpg')
        self.img_copy= self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = tk.Label(self, image=self.background_image)
        self.background.pack(fill="both", expand= True)
        self.background.bind('<Configure>', self._resize_image)

        #window = tk.Tk()
        label1 = tk.Label(self,text='HUMAN ACTIVITY RECOGNITION USING DEEPLEARNING',fg='white',bg='red',relief='raised',font=('Times New Roman',40,'bold'))
        label1.place(x=17,y=8)


        button1 = tk.Button(self, text="    TRAIN    ",fg='white',bg='red',relief='ridge',font=('Times New Roman',16,'bold'),command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="     TEST     ",fg='white',bg='red',relief='ridge',font=('Times New Roman',16,'bold'),command=lambda: controller.show_frame("PageTwo"))
        button1.place(x=700,y=400)
        button2.place(x=700,y=450)

    def _resize_image(self,event):
        new_width = event.width
        new_height = event.height
        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #label = tk.Label(self, text="This is page 1", font=controller.title_font)
        #label.pack(side="top", fill="x", pady=10)
        def trainevent():
            label9 = tk.Label(self, text=' Model Trained ',fg='white',bg='green',relief='raised',font=('Times New Roman',20,'bold'))
            label9.place(x=730,y=400)

        def fileDialog():
            filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =(("mp4 files","*.mp4  *.mkv"),("all files","*.*")) )
            label6.destroy()
            label7 = tk.Label(self, text='  Uploaded  ',fg='white',bg='green',relief='raised',font=('Times New Roman',20,'bold'))
            label7.place(x=850,y=150)
            button2 = tk.Button(self,text="TRAIN",relief='raised',font=('Times New Roman',16,'bold'), command=trainevent)
            button2.place(x=730,y=350)
            print(filename)



        data1 = ""
        data2 = ""
        data3 = ""

        label5 = tk.Label(self, text="      UPLOAD:     ",fg='white',bg='BLUE',relief='raised',font=('Times New Roman',20,'bold'))
        label5.place(x=480,y=150)

        label6 = tk.Label(self, text='Not uploaded',fg='white',bg='red',relief='raised',font=('Times New Roman',20,'bold'))
        label6.place(x=850,y=150)


        button1 = tk.Button(self,text="Browse",relief='raised',font=('Times New Roman',16,'bold'), command=fileDialog)
        button1.place(x=730,y=148)

        label1 = tk.Label(self, text="Input Image Size:",fg='white',bg='BLUE',relief='raised',font=('Times New Roman',20,'bold'))
        label1.place(x=480,y=200)


        label2 = tk.Entry(self, textvariable=data1,font=('Times New Roman',20))
        label2.place(x=730,y=200)

        label3 = tk.Label(self, text="  Learning Rate:  ",fg='white',bg='BLUE',relief='raised',font=('Times New Roman',20,'bold'))
        label3.place(x=480,y=250)

        label4 = tk.Entry(self, textvariable=data2,font=('Times New Roman',20))
        label4.place(x=730,y=250)

        label8 = tk.Label(self, text="Select Optimizer: ",fg='white',bg='BLUE',relief='raised',font=('Times New Roman',20,'bold'))
        label8.place(x=480,y=300)

        optim_sel = ttk.Combobox(self, width = 27, textvariable = data3,font=(20))
        optim_sel['values'] = ('SGD','GD','Adam','Adagrad','Nesterov','Momentum','Gradient descent')
        optim_sel.current()
        optim_sel.place(x=730,y=300)

        button1 = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"))
        #button2 = tk.Button(self, text="     TEST     ",fg='white',bg='red',relief='ridge',font=('Times New Roman',16,'bold'),command=lambda: controller.show_frame("PageTwo"))
        #button2.place(x=700,y=400)
        button1.pack()

        #label7 = tk.Label(self, text="  Learning Rate:  ",fg='white',bg='BLUE',relief='raised',font=('Times New Roman',20,'bold'))
        #label7.place(x=480,y=250)





class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
