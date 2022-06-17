import tkinter as tk                # python 3
from tkinter import StringVar, font  as tkfont # python 3
from tkinter import messagebox


#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.backcolor = "#c6dad6" ## 색
        self.buttoncolor = "#469bbb"

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

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.configure(bg=controller.backcolor, borderwidth=10) ## 배경색
        SearchPhoto = tk.PhotoImage(file="Team Project/SearchPhoto.png")
        HistoryPhoto = tk.PhotoImage(file="Team Project/HistoryPhoto.png")
        ClosePhoto = tk.PhotoImage(file="Team Project/ClosePhoto.png")
        TitlePhoto = tk.PhotoImage(file="Team Project/TitlePhoto.png")

        label = tk.Label(self, text="start page", font=controller.title_font, background=controller.backcolor) ## 포인트 쓰려면 부모 클래스 controller. ㅁㅁ
        teamlabel = tk.Label(self, text= "예스파일!", font=controller.title_font, background=controller.backcolor)
        Title = tk.Label(self, image = TitlePhoto, background=controller.backcolor)
        Searchbutton = tk.Button(self, image = SearchPhoto, command = lambda: controller.show_frame("PageOne"), background=controller.backcolor)
        Historybutton = tk.Button(self, image = HistoryPhoto, command = lambda: controller.show_frame("PageTwo"), background=controller.backcolor) ## 기록 버튼
        closebutton = tk.Button(self, image = ClosePhoto, command = quit, background=controller.backcolor)
        
        
        ## 파이썬의 가비지 컬렉터가 사진을 지워버리기 때문에 수동으로 참고 횟수를 늘려주어야 이미지 유지가 가능함
        closebutton.image = ClosePhoto
        Searchbutton.image = SearchPhoto
        Historybutton.image = HistoryPhoto
        Title.image = TitlePhoto

        label.place(x=0,y=0)
        Title.place(x=230,y=50)
        Searchbutton.place(x=240,y=310)
        Historybutton.place(x=240,y=375)
        closebutton.place(x=240,y=440)
        teamlabel.place(x=680,y=550)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def click():
            messagebox.showinfo("검색", "만드는중 입니다.  ")
            tk.txt_label.configure(text=input_text.get())
            
            

        input_text= StringVar() ##string 변수 선언

        self.configure(bg=controller.backcolor, borderwidth=10) ## 배경색 
        edit1 = tk.Entry(self,font=('Arial', 20), textvariable= input_text)
        edit2 = tk.Entry(self,font=('Arial', 100))
        label = tk.Label(self, text="page 1", font=controller.title_font, background=controller.backcolor)
        label1 = tk.Label(self, text="검색", font=('Arial', 50), background=controller.backcolor)
        label2 = tk.Label(self, text="이름",font=('Arial', 30), background=controller.backcolor)
        label3 = tk.Label(self, text="종류",font=('Arial', 30), background=controller.backcolor)
        txt_label = tk.Label(self, text=""  )
        Backbutton = tk.Button(self, text="뒤로 가기",font=("System", 30), command=lambda: controller.show_frame("StartPage"),background=controller.buttoncolor, activebackground=controller.buttoncolor) ## 배경색과 동일하게 
        Searchbutton = tk.Button(self, text="검색",font=("System", 30), command=click, background=controller.buttoncolor, activebackground=controller.buttoncolor)

        var_ra_1 = tk.IntVar()
        radio1 = tk.Radiobutton(self, text="영화", value=0, variable=var_ra_1, font=('Arial', 20), background=controller.backcolor, activebackground=controller.backcolor)
        radio3 = tk.Radiobutton(self, text="어플", value=1, variable=var_ra_1, font=('Arial', 20), background=controller.backcolor, activebackground=controller.backcolor)
        radio4 = tk.Radiobutton(self, text="책", value=2, variable=var_ra_1, font=('Arial', 20), background=controller.backcolor, activebackground=controller.backcolor)
        radio5 = tk.Radiobutton(self, text="영화", value=3, variable=var_ra_1, font=('Arial', 20), background=controller.backcolor, activebackground=controller.backcolor)
        radio2 = tk.Radiobutton(self, text="애니메이션", value=4, variable=var_ra_1, font=('Arial', 20), background=controller.backcolor, activebackground=controller.backcolor)


        Backbutton.place(x=480,y=500)
        Searchbutton.place(x=380,y=500)
        txt_label.place(x=30,y=30)
        label.place(x=0,y=0)
        label1.place(x=350,y=30)
        label2.place(x=150,y=150)
        label3.place(x=150,y=300)
        edit1.place(x=300,y=160)
        edit2.place(x=500,y=180)
        radio1.place(x=300,y=300)
        radio2.place(x=300,y=340)
        radio3.place(x=300,y=380)
        radio4.place(x=300,y=420)
        radio5.place(x=300,y=460)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.configure(bg=controller.backcolor, borderwidth=10) ## 배경색 
        label = tk.Label(self, text="page 2", font=controller.title_font, background=controller.backcolor)
        
        Backbutton = tk.Button(self, text="Go to the start page",font=("System", 30),command=lambda: controller.show_frame("StartPage"),background=controller.buttoncolor, activebackground=controller.buttoncolor)

        label.place(x=0,y=0)
        Backbutton.place(x=250,y=100)


if __name__ == "__main__":
    
    app = SampleApp()
    app.geometry("800x600")
    app.title("팀프로젝트")
    app.resizable(width= tk.FALSE, height= tk.FALSE)

    app.mainloop()