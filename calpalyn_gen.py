from collections import defaultdict
import Tkinter as tk
import wckToolTips

class Example(tk.Frame):
    def __init__(self, root):

        tk.Frame.__init__(self, root)
        root.attributes('-fullscreen', True)
        self.canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw", 
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.lines = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","20A","21","22","23","24","25","26","26A","27","28","29","30"] 
        self.repeating_lines = ["20","26","27","30"]
        self.ignore_lines = ["02","15","28","29"]
        self.layout = []
        self.entries = []
        self.line_numbers = 0
        self.create_lines()
        self.render_lines()
        self.set_tooltip_entries()

    def create_entries(self, line_id):
        if line_id == "01":
            self.layout.append( (tk.Label(self.frame, text = "File Type: ", width = 7),(self.line_numbers, 2),line_id+"!file_type") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
        
            self.layout.append( (tk.Label(self.frame, text = "Factor: ", width = 7),(self.line_numbers, 4),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=4)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 5),line_id+":B") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=5)

            self.layout.append( (tk.Label(self.frame, text = "Number: ", width = 7),(self.line_numbers, 6),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=6)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 7),line_id+":C") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=7)
            
        elif line_id == "03":
            self.layout.append( (tk.Label(self.frame, text = "Total: ", width = 7),(self.line_numbers, 2),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
        
            self.layout.append( (tk.Label(self.frame, text = "Subtotals: ", width = 9),(self.line_numbers, 4),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=4)
            self.layout.append( (tk.Entry(self.frame, width = 10),(self.line_numbers, 5),line_id+":B") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=5)
            self.layout.append( (tk.Entry(self.frame, width = 10),(self.line_numbers, 6),line_id+":C") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=6)
            self.layout.append( (tk.Entry(self.frame, width = 10),(self.line_numbers, 7),line_id+":D") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=7)
            self.layout.append( (tk.Entry(self.frame, width = 10),(self.line_numbers, 8),line_id+":E") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=8)
            self.layout.append( (tk.Entry(self.frame, width = 10),(self.line_numbers, 9),line_id+":F") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=9)
            self.layout.append( (tk.Entry(self.frame, width = 10),(self.line_numbers, 10),line_id+":G") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=10)
            self.layout.append( (tk.Entry(self.frame, width = 10),(self.line_numbers, 11),line_id+":H") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=11)

    
            self.layout.append( (tk.Label(self.frame, text = "Final Subtotal: ", width = 12),(self.line_numbers, 12),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=12)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 13),line_id+":I") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=13)
            
        elif line_id in ["04","05","06","07","08","09","10","11","12"]:
            self.layout.append( (tk.Label(self.frame, text = "Total: ", width = 7),(self.line_numbers, 2),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":B") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
            
        elif line_id == "13":
            self.layout.append( (tk.Label(self.frame, text = "Names File: ", width = 10),(self.line_numbers, 2),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
            
        elif line_id == "14":
            self.layout.append( (tk.Label(self.frame, text = "Raw Data: ", width = 10),(self.line_numbers, 2),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)

            self.layout.append( (tk.Label(self.frame, text = "Normalizations: ", width = 12),(self.line_numbers, 4),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=4)
            self.layout.append( (tk.Entry(self.frame, width = 10),(self.line_numbers, 5),line_id+":B") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=5)
            self.layout.append( (tk.Entry(self.frame, width = 10),(self.line_numbers, 6),line_id+":C") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=6)
            self.layout.append( (tk.Entry(self.frame, width = 10),(self.line_numbers, 7),line_id+":D") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=7)
            self.layout.append( (tk.Entry(self.frame, width = 10),(self.line_numbers, 8),line_id+":E") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=8)

        elif line_id == "16":
            self.layout.append( (tk.Label(self.frame, text = "Plot: ", width = 10),(self.line_numbers, 2),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)

        elif line_id in ["17","18","19"]:
            self.layout.append( (tk.Label(self.frame, text = "Normalization: ", width = 12),(self.line_numbers, 2),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
        
            self.layout.append( (tk.Label(self.frame, text = "Taxon: ", width = 5),(self.line_numbers, 4),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=4)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 5),line_id+":B") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=5)

            self.layout.append( (tk.Label(self.frame, text = "Extra Taxa: ", width = 10),(self.line_numbers, 6),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=6)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 7),line_id+":C") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=7)

        elif line_id == "20":
            self.layout.append( (tk.Label(self.frame, text = "Taxon: ", width = 6),(self.line_numbers, 2),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":B") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
        
            self.layout.append( (tk.Label(self.frame, text = "Norm. Type: ", width = 9),(self.line_numbers, 4),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=4)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 5),line_id+":C") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=5)

            self.layout.append( (tk.Label(self.frame, text = "Taxon Norm.: ", width = 11),(self.line_numbers, 6),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=6)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 7),line_id+":D") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=7)

            self.layout.append( (tk.Label(self.frame, text = "Supplementary: ", width = 12),(self.line_numbers, 8),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=8)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 9),line_id+":F") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=9)

            self.layout.append( (tk.Label(self.frame, text = "H Scale: ", width = 7),(self.line_numbers, 10),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=10)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 11),line_id+":I") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=11)

            self.layout.append( (tk.Label(self.frame, text = "Graph Label: ", width = 11),(self.line_numbers, 12),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=12)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 13),line_id+":J") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=13)


        elif line_id == "20A":
            self.layout.append( (tk.Label(self.frame, text = "New Group: ", width = 9),(self.line_numbers, 2),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
        
            self.layout.append( (tk.Label(self.frame, text = "Taxon Group: ", width = 11),(self.line_numbers, 4),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=4)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 5),line_id+":B") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=5)

            self.layout.append( (tk.Label(self.frame, text = "Shading: ", width = 8),(self.line_numbers, 6),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=6)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 7),line_id+":C") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=7)

            self.layout.append( (tk.Label(self.frame, text = "Angle: ", width = 12),(self.line_numbers, 8),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=8)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 9),line_id+":D") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=9)

            self.layout.append( (tk.Label(self.frame, text = "Density: ", width = 7),(self.line_numbers, 10),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=10)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 11),line_id+":E") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=11)

            self.layout.append( (tk.Label(self.frame, text = "Plot Type: ", width = 11),(self.line_numbers, 12),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=12)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 13),line_id+":F") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=13)

            self.layout.append( (tk.Label(self.frame, text = "Label: ", width = 7),(self.line_numbers, 14),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=14)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 15),line_id+":G") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=15)

            self.layout.append( (tk.Label(self.frame, text = "Label cont.: ", width = 11),(self.line_numbers, 16),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=16)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 17),line_id+":H") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=17)

        elif line_id == "21":
            self.layout.append( (tk.Label(self.frame, text = "Lines: ", width = 6),(self.line_numbers, 2),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
        
            self.layout.append( (tk.Label(self.frame, text = "Strat. Column: ", width = 12),(self.line_numbers, 4),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=4)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 5),line_id+":B") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=5)

            self.layout.append( (tk.Label(self.frame, text = "Chron. Column: ", width = 12),(self.line_numbers, 6),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=6)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 7),line_id+":C") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=7)

            self.layout.append( (tk.Label(self.frame, text = "Font: ", width = 5),(self.line_numbers, 8),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=8)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 9),line_id+":D") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=9)
            
        elif line_id == "22":
            self.layout.append( (tk.Label(self.frame, text = "Height: ", width = 9),(self.line_numbers, 2),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
        
            self.layout.append( (tk.Label(self.frame, text = "Width: ", width = 11),(self.line_numbers, 4),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=4)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 5),line_id+":B") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=5)

            self.layout.append( (tk.Label(self.frame, text = "Depth Interval: ", width = 12),(self.line_numbers, 6),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=6)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 7),line_id+":C") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=7)

            self.layout.append( (tk.Label(self.frame, text = "Chron. Interval: ", width = 12),(self.line_numbers, 8),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=8)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 9),line_id+":D") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=9)

            self.layout.append( (tk.Label(self.frame, text = "H Scale Interval: ", width = 12),(self.line_numbers, 10),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=10)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 11),line_id+":E") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=11)

        elif line_id == "23":
            self.layout.append( (tk.Label(self.frame, text = "Zonation: ", width = 9),(self.line_numbers, 2),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)

        elif line_id == "24":
            self.layout.append( (tk.Label(self.frame, text = "Vert. Label: ", width = 9),(self.line_numbers, 2),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)

        elif line_id == "25":
            self.layout.append( (tk.Label(self.frame, text = "Plot Title: ", width = 9),(self.line_numbers, 2),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)

        elif line_id == "26":
            self.layout.append( (tk.Label(self.frame, text = "Midpoint Depth: ", width = 13),(self.line_numbers, 2),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":B") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
        
            self.layout.append( (tk.Label(self.frame, text = "Vert. Thickness: ", width = 13),(self.line_numbers, 4),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=4)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 5),line_id+":C") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=5)

            self.layout.append( (tk.Label(self.frame, text = "Sample Date: ", width = 10),(self.line_numbers, 6),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=6)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 7),line_id+":D") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=7)

            self.layout.append( (tk.Label(self.frame, text = "Yrs. Uncertainty: ", width = 13),(self.line_numbers, 8),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=8)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 9),line_id+":E") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=9)

            self.layout.append( (tk.Label(self.frame, text = "Label: ", width = 7),(self.line_numbers, 10),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=10)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 11),line_id+":F") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=11)
            
        elif line_id == "26A":
            self.layout.append( (tk.Label(self.frame, text = "Chron. Label: ", width = 11),(self.line_numbers, 2),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)

        elif line_id == "27":
            self.layout.append( (tk.Label(self.frame, text = "Upper Bound: ", width = 11),(self.line_numbers, 2),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":B") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
        
            self.layout.append( (tk.Label(self.frame, text = "Boundary Type: ", width = 12),(self.line_numbers, 4),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=4)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 5),line_id+":C") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=5)

            self.layout.append( (tk.Label(self.frame, text = "Shading: ", width = 7),(self.line_numbers, 6),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=6)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 7),line_id+":D") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=7)

            self.layout.append( (tk.Label(self.frame, text = "Strat. Label: ", width = 9),(self.line_numbers, 8),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=8)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 9),line_id+":E") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=9)

        elif line_id == "30":
            self.layout.append( (tk.Label(self.frame, text = "Zone Position: ", width = 11),(self.line_numbers, 2),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":B") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
        
            self.layout.append( (tk.Label(self.frame, text = "Boundary Type: ", width = 12),(self.line_numbers, 4),line_id) )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=4)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 5),line_id+":C") )
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

    def get_entries(self):
        self.entries = defaultdict(list)
        for widget in self.layout:
            if widget[2][-2] == ":":
                    self.entries[widget[2][:2]].append(widget[0])

        self.write_lines()

    def set_tooltip_entries(self):
        for widget in self.layout:
            if widget[2][-2] == "!":
                wckToolTips.register(widget[0], "This entry is used for x.")

    def write_lines(self):
        
        with open('file.instrs', 'wb+') as f:
            
            for line in self.lines:
                entries_number = len(self.entries[line])
                data = iter(self.entries[line])

                # WRITE EACH LINE TO CALPALYN READABLE FILE
                if line == "01":
                        f.write(data.next().get()[:1] + ' ' + data.next().get()[:1] + ' ' + data.next().get()[:9])
                        f.write('\n')

                elif line == "30":
                    for i in range(entries_number/2):
                        if (i+1) != (entries_number/2):
                            f.write('0' + ' ' + data.next().get()[:7] + ' ' + data.next().get()[:1])
                        else:
                            f.write('1' + ' ' + data.next().get()[:7] + ' ' + data.next().get()[:1])
                        f.write('\n')

            
        
    def create_lines(self):
        self.line_numbers += 1
        tk.Button(self.frame, text="Generate File", command= self.get_entries, width = 10).grid(row=1,column=1)
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
