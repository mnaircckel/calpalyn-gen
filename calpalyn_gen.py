import Tkinter as tk

class Example(tk.Frame):
    def __init__(self, root):

        tk.Frame.__init__(self, root)
        self.canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw", 
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.lines = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","20A","21","22","23","24","25","26","26A","27","28","29","30"] 
        self.repeating_lines = ["20","26","27","30"]
        self.ignore_lines = ["2","15","28","29"]
        self.layout = []
        self.line_numbers = 0
        self.create_lines()
        self.render_lines()

    def create_entries(self, line_id):
        self.layout.append( (tk.Label(self.frame, text = "Name A: ", width = 7),(self.line_numbers, 2),line_id) )
        self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
        self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id) )
        self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
        
        self.layout.append( (tk.Label(self.frame, text = "Name B: ", width = 7),(self.line_numbers, 4),line_id) )
        self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=4)
        self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 5),line_id) )
        self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=5)
        
    def new_line20(self):
        self.line_numbers += 1
        self.create_entries("20")
        self.layout.append( (tk.Label(self.frame, relief="groove", text="Line 20", width = 8),(self.line_numbers, 1),"20") )
        self.layout[len(self.layout)-1][0].grid(row=self.line_numbers,column=1)
        self.line_numbers += 1
        self.create_entries("20A")
        self.layout.append( (tk.Label(self.frame, relief="groove", text="Line 20A", width = 8),(self.line_numbers, 1),"20A") )
        self.layout[len(self.layout)-1][0].grid(row=self.line_numbers,column=1)

    def new_line26(self):
        self.line_numbers += 1
        self.create_entries("26")
        self.layout.append( (tk.Label(self.frame, relief="groove", text="Line 26", width = 8),(self.line_numbers, 1),"26") )
        self.layout[len(self.layout)-1][0].grid(row=self.line_numbers,column=1)
        
    def new_line27(self):
        self.line_numbers += 1
        self.create_entries("27")
        self.layout.append( (tk.Label(self.frame, relief="groove", text="Line 27", width = 8),(self.line_numbers, 1),"27") )
        self.layout[len(self.layout)-1][0].grid(row=self.line_numbers,column=1)
        
    def new_line30(self):
        self.line_numbers += 1
        self.create_entries("30")
        self.layout.append( (tk.Label(self.frame, relief="groove", text="Line 30", width = 8),(self.line_numbers, 1),"20") )
        self.layout[len(self.layout)-1][0].grid(row=self.line_numbers,column=1)
        
    def create_lines(self):
        self.line_numbers += 1
        self.layout.append( (tk.Button(self.frame, text="Generate File", command= None, width = 10),(1,1), "button") )
        for line in self.lines:
            self.line_numbers += 1
            if line not in self.ignore_lines:
                self.create_entries(line)
            self.layout.append( (tk.Label(self.frame, relief="groove", text="Line " + line, width = 8),(self.line_numbers, 1),line) )
            if line in self.repeating_lines:
                if line == "20":
                    self.layout.append( (tk.Button(self.frame, text="+", command= self.new_line20, width = 8),(self.line_numbers, 999),line) )
                elif line == "26":
                    self.layout.append( (tk.Button(self.frame, text="+", command= self.new_line26, width = 8),(self.line_numbers, 999),line) )
                elif line == "27":
                    self.layout.append( (tk.Button(self.frame, text="+", command= self.new_line27, width = 8),(self.line_numbers, 999),line) )
                elif line == "30":
                    self.layout.append( (tk.Button(self.frame, text="+", command= self.new_line30, width = 8),(self.line_numbers, 999),line) )
                
    def render_lines(self):
        for widget in self.layout:
            widget[0].grid(row=widget[1][0],column=widget[1][1])

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    root=tk.Tk()
    Example(root).pack(side="top", fill="both", expand=True)
    root.title("Calpalyn File Generator")
    root.mainloop()
