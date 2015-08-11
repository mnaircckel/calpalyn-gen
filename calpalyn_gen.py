from collections import defaultdict
import Tkinter as tk
import math
import wckToolTips

# Author: Marcel Champagne
# This program is written in Tkinter, using a library wckToolTips in order to have tool tip functionality
# The basic frame is made so there can be a vertical scroll bar, this way the user may create as many lines as possible

# Base tk Frame class
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

        # Variables keep track of which lines exist in the calpalyn program, lines 20, 26, 27, and 30 may repeat
        self.lines = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","20A","21","22","23","24","25","26","26A","27","28","29","30"] 
        self.repeating_lines = ["20","26","27","30"]

        # Lines 02 15 28 and 29 are ignored in this front end version of calpalyn --
        # they are automatically written to the file in the specified format but don't take user input
        self.ignore_lines = ["02","15","28","29"]

        # Layout stores all the widgets in a list with a line identifer
        self.layout = []

        # Entries contains all the widgets that are entries (not labels and buttons)
        self.entries = []

        # Keep track off the number of line numbers
        self.line_numbers = 0

        # Create the intial lines and render them as a form
        self.create_lines()
        self.render_lines()

    def create_entries(self, line_id):
        if line_id == "01":
            self.layout.append( (tk.Label(self.frame, text = "File Type * : ", width = 9),(self.line_numbers, 2),line_id+"!file_type") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for File Type.")
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
            self.layout[len(self.layout)-1][0].insert(0,0)
        
            self.layout.append( (tk.Label(self.frame, text = "Factor * : ", width = 9),(self.line_numbers, 4),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Factor.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=4)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 5),line_id+":B") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=5)
            self.layout[len(self.layout)-1][0].insert(0,0)

            self.layout.append( (tk.Label(self.frame, text = "Number * : ", width = 9),(self.line_numbers, 6),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Number.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=6)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 7),line_id+":C") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=7)
            self.layout[len(self.layout)-1][0].insert(0,-1.0)
            
        elif line_id == "03":
            self.layout.append( (tk.Label(self.frame, text = "Total: ", width = 7),(self.line_numbers, 2),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Total.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
        
            self.layout.append( (tk.Label(self.frame, text = "Subtotals: ", width = 9),(self.line_numbers, 4),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Subtotals.")
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
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Final Subtotal.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=12)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 13),line_id+":I") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=13)
            
        elif line_id in ["04","05","06","07","08","09","10","11","12"]:
            self.layout.append( (tk.Label(self.frame, text = "Subtotal: ", width = 7),(self.line_numbers, 2),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Subtotal.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":B") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
            
        elif line_id == "13":
            self.layout.append( (tk.Label(self.frame, text = "Names File * : ", width = 11),(self.line_numbers, 2),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Names File.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
            self.layout[len(self.layout)-1][0].insert(0,1)
            
        elif line_id == "14":
            self.layout.append( (tk.Label(self.frame, text = "Raw Data * : ", width = 10),(self.line_numbers, 2),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Raw Data.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
            self.layout[len(self.layout)-1][0].insert(0,1)

            self.layout.append( (tk.Label(self.frame, text = "Normalizations * : ", width = 14),(self.line_numbers, 4),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Normalizations.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=4)
            self.layout.append( (tk.Entry(self.frame, width = 10),(self.line_numbers, 5),line_id+":B") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=5)
            self.layout[len(self.layout)-1][0].insert(0,0)
            self.layout.append( (tk.Entry(self.frame, width = 10),(self.line_numbers, 6),line_id+":C") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=6)
            self.layout[len(self.layout)-1][0].insert(0,0)
            self.layout.append( (tk.Entry(self.frame, width = 10),(self.line_numbers, 7),line_id+":D") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=7)
            self.layout[len(self.layout)-1][0].insert(0,0)
            self.layout.append( (tk.Entry(self.frame, width = 10),(self.line_numbers, 8),line_id+":E") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=8)
            self.layout[len(self.layout)-1][0].insert(0,1)

        elif line_id == "16":
            self.layout.append( (tk.Label(self.frame, text = "Plot * : ", width = 10),(self.line_numbers, 2),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Plot.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
            self.layout[len(self.layout)-1][0].insert(0,1)

        elif line_id in ["17","18","19"]:
            self.layout.append( (tk.Label(self.frame, text = "Normalization: ", width = 12),(self.line_numbers, 2),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Normalization.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
        
            self.layout.append( (tk.Label(self.frame, text = "Taxon: ", width = 5),(self.line_numbers, 4),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Taxon.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=4)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 5),line_id+":B") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=5)

        elif line_id == "20":
            self.layout.append( (tk.Label(self.frame, text = "Taxon: ", width = 6),(self.line_numbers, 2),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Taxon.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":B") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
        
            self.layout.append( (tk.Label(self.frame, text = "Norm. Type: ", width = 9),(self.line_numbers, 4),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Norm. Type:")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=4)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 5),line_id+":C") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=5)

            self.layout.append( (tk.Label(self.frame, text = "Taxon Norm.: ", width = 11),(self.line_numbers, 6),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Taxon Norm.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=6)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 7),line_id+":D") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=7)

            self.layout.append( (tk.Label(self.frame, text = "5 Times Curve: ", width = 12),(self.line_numbers, 8),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for 5 Times Curve.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=8)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 9),line_id+":F") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=9)

            self.layout.append( (tk.Label(self.frame, text = "H Scale: ", width = 7),(self.line_numbers, 10),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for H Scale.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=10)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 11),line_id+":I") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=11)

            self.layout.append( (tk.Label(self.frame, text = "Graph Label: ", width = 11),(self.line_numbers, 12),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Graph Label.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=12)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 13),line_id+":J") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=13)


        elif line_id == "20A":
            self.layout.append( (tk.Label(self.frame, text = "New Group: ", width = 9),(self.line_numbers, 2),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for New Group.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
        
            self.layout.append( (tk.Label(self.frame, text = "Taxon Group: ", width = 11),(self.line_numbers, 4),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Taxon Group.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=4)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 5),line_id+":B") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=5)

            self.layout.append( (tk.Label(self.frame, text = "Shading: ", width = 8),(self.line_numbers, 6),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Shading.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=6)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 7),line_id+":C") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=7)

            self.layout.append( (tk.Label(self.frame, text = "Angle: ", width = 12),(self.line_numbers, 8),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Angle.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=8)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 9),line_id+":D") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=9)

            self.layout.append( (tk.Label(self.frame, text = "Density: ", width = 7),(self.line_numbers, 10),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Density.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=10)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 11),line_id+":E") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=11)

            self.layout.append( (tk.Label(self.frame, text = "Plot Type: ", width = 11),(self.line_numbers, 12),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Plot Type.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=12)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 13),line_id+":F") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=13)

            self.layout.append( (tk.Label(self.frame, text = "Label: ", width = 7),(self.line_numbers, 14),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Label.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=14)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 15),line_id+":G") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=15)

            self.layout.append( (tk.Label(self.frame, text = "Label cont.: ", width = 11),(self.line_numbers, 16),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Label cont.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=16)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 17),line_id+":H") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=17)

        elif line_id == "21":
            self.layout.append( (tk.Label(self.frame, text = "Lines: ", width = 6),(self.line_numbers, 2),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Lines.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
        
            self.layout.append( (tk.Label(self.frame, text = "Strat. Column: ", width = 12),(self.line_numbers, 4),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Strat. Column.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=4)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 5),line_id+":B") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=5)

            self.layout.append( (tk.Label(self.frame, text = "Chron. Column: ", width = 12),(self.line_numbers, 6),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Chron. Column.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=6)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 7),line_id+":C") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=7)

            self.layout.append( (tk.Label(self.frame, text = "Font: ", width = 5),(self.line_numbers, 8),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Font.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=8)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 9),line_id+":D") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=9)
            
        elif line_id == "22":
            self.layout.append( (tk.Label(self.frame, text = "Height: ", width = 9),(self.line_numbers, 2),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Height.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
        
            self.layout.append( (tk.Label(self.frame, text = "Width: ", width = 11),(self.line_numbers, 4),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Width.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=4)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 5),line_id+":B") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=5)

            self.layout.append( (tk.Label(self.frame, text = "Depth Interval: ", width = 12),(self.line_numbers, 6),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Depth.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=6)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 7),line_id+":C") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=7)

            self.layout.append( (tk.Label(self.frame, text = "Chron. Interval: ", width = 12),(self.line_numbers, 8),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Chron. Interval.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=8)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 9),line_id+":D") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=9)

            self.layout.append( (tk.Label(self.frame, text = "H Scale Interval: ", width = 12),(self.line_numbers, 10),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for H Scale Interval.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=10)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 11),line_id+":E") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=11)

        elif line_id == "23":
            self.layout.append( (tk.Label(self.frame, text = "Zonation: ", width = 9),(self.line_numbers, 2),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Zonation.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)

        elif line_id == "24":
            self.layout.append( (tk.Label(self.frame, text = "Vert. Label: ", width = 9),(self.line_numbers, 2),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Vert. Label.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)

        elif line_id == "25":
            self.layout.append( (tk.Label(self.frame, text = "Plot Title: ", width = 9),(self.line_numbers, 2),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Plot Title.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)

        elif line_id == "26":
            self.layout.append( (tk.Label(self.frame, text = "Midpoint Depth: ", width = 13),(self.line_numbers, 2),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Midpoint Depth.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":B") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
        
            self.layout.append( (tk.Label(self.frame, text = "Vert. Thickness: ", width = 13),(self.line_numbers, 4),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for File Type.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=4)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 5),line_id+":C") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=5)

            self.layout.append( (tk.Label(self.frame, text = "Sample Date: ", width = 10),(self.line_numbers, 6),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Sample Date.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=6)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 7),line_id+":D") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=7)

            self.layout.append( (tk.Label(self.frame, text = "Yrs. Uncertainty: ", width = 13),(self.line_numbers, 8),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Yrs. Uncertainty")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=8)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 9),line_id+":E") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=9)

            self.layout.append( (tk.Label(self.frame, text = "Label: ", width = 7),(self.line_numbers, 10),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Label.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=10)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 11),line_id+":F") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=11)
            
        elif line_id == "26A":
            self.layout.append( (tk.Label(self.frame, text = "Chron. Label: ", width = 11),(self.line_numbers, 2),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Chron. Label")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)

        elif line_id == "27":
            self.layout.append( (tk.Label(self.frame, text = "Upper Bound: ", width = 11),(self.line_numbers, 2),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Upper Bound.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":B") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
        
            self.layout.append( (tk.Label(self.frame, text = "Boundary Type: ", width = 12),(self.line_numbers, 4),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Boundary Type.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=4)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 5),line_id+":C") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=5)

            self.layout.append( (tk.Label(self.frame, text = "Shading: ", width = 7),(self.line_numbers, 6),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Shading.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=6)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 7),line_id+":D") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=7)

            self.layout.append( (tk.Label(self.frame, text = "Strat. Label: ", width = 9),(self.line_numbers, 8),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Strat. Label.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=8)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 9),line_id+":E") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=9)

        elif line_id == "30":
            self.layout.append( (tk.Label(self.frame, text = "Zone Position: ", width = 11),(self.line_numbers, 2),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Zone Position.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":B") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
        
            self.layout.append( (tk.Label(self.frame, text = "Boundary Type: ", width = 12),(self.line_numbers, 4),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Boundary Type.")
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
                    if widget[2][:3] == "26A":
                        self.entries[widget[2][:3]].append(widget[0])
                    else:
                        self.entries[widget[2][:2]].append(widget[0])

        self.write_lines()

    def write_lines(self):
        
        with open('file.instrs', 'wb+') as f:
            
            for line in self.lines:
                entries_number = len(self.entries[line])
                data = iter(self.entries[line])

                # WRITE EACH LINE TO CALPALYN READABLE FILE
                if line == "01":
                        f.write(data.next().get()[:1] + ' ' + data.next().get()[:1] + ' ' + data.next().get()[:9])
                        f.write(" "*81+"// Line 1")
                        f.write('\n')

                elif line == "02":
                    f.write('1\n')

                elif line == "03":
                        f.write(data.next().get()[:1] + ' ' + data.next().get()[:1] + ' ' + data.next().get()[:1] + ' ' + data.next().get()[:1] + ' ' + data.next().get()[:1] + ' ' + data.next().get()[:1] + ' ' + data.next().get()[:1] + ' ' + data.next().get()[:1] + ' ' + data.next().get()[:1])
                        f.write('\n')

                elif line in ["04","05","06","07","08","09","10","11","12"]:
                        f.write('1' + ' ' + data.next().get()[:75])
                        f.write('\n')

                elif line == "13":
                        f.write(data.next().get()[:1])
                        f.write('\n')
                        
                elif line == "15":
                    f.write('1\n')

                elif line == "14":
                        f.write(data.next().get()[:1] + ' ' + data.next().get()[:1] + ' ' + data.next().get()[:1] + ' ' + data.next().get()[:1] + ' ' + data.next().get()[:1])
                        f.write('\n')

                elif line == "16":
                        f.write(data.next().get()[:1])
                        f.write('\n')
                        
                elif line in ["17", "18", "19"]:
                        f.write(data.next().get()[:1] + ' ' + data.next().get()[:5])
                        f.write('\n')

                
                # Line 20 handles lines 20 and 20A
                elif line == "20":
                    for i in range(entries_number/14):

                        # Line 20 entries
                        dataB = data.next().get()[:5]
                        dataC = data.next().get()[:1]
                        dataD = data.next().get()[:5]
                        dataF = data.next().get()[:1]
                        dataI = data.next().get()[:6]
                        dataJ = data.next().get()[:30]

                        # Line 20A entries
                        data1A = data.next().get()[:1]
                        data1B = data.next().get()[:1]
                        data1C = data.next().get()[:1]
                        data1D = data.next().get()[:7]
                        data1E = data.next().get()[:2]
                        data1F = data.next().get()[:1]
                        data1G = data.next().get()[:30]
                        data1H = data.next().get()[:30]

                        # Line 20                                                  
                        if (i+1) != (entries_number/14):
                            
                            f.write('0' + ' ' + dataB + ' '*(5-len(dataB)) + ' ' + dataC + ' ' + dataD + ' '*(5-len(dataD)) + ' '*22 + dataF + '      ' + dataI + ' '*(6-len(dataI)) + ' ' + dataJ )
                        else:
                            f.write('1' + ' ' + dataB + ' '*(5-len(dataB)) + ' ' + dataC + ' ' + dataD + ' '*(5-len(dataD)) + ' '*22 + dataF + '      ' + dataI + ' '*(6-len(dataI)) + ' ' + dataJ )
                            
                        f.write('\n')
                        # Line 20A
                        f.write(data1A + ' ' + data1B + ' ' + data1C + ' ' + data1D + ' '*(7-len(data1D)) + ' ' + data1E + ' '*(2-len(data1E)) + ' ' + data1F + ' ' + data1G + ' '*(30-len(data1G)) + ' ' + data1G + ' '*(30-len(data1H)) )
                        f.write('\n')
                        

                elif line == "21":
                        f.write(data.next().get()[:1] + ' ' + data.next().get()[:1] + ' ' + data.next().get()[:1] + ' ' + data.next().get()[:1])
                        f.write('\n')

                elif line  == "22":
                        dataA = data.next().get()[:6]
                        dataB = data.next().get()[:6]
                        dataC = data.next().get()[:6]
                        dataD = data.next().get()[:6]
                        dataE = data.next().get()[:6]
                        f.write(' ' + dataA + ' '*(6-len(dataA)) + ' ' + dataB + ' '*(6-len(dataB)) + ' ' + dataC + ' '*(6-len(dataC)) + ' ' + dataD + ' '*(6-len(dataD)) + ' ' + dataE)
                        f.write('\n')

                elif line == "23":
                        f.write(data.next().get()[:2])
                        f.write('\n')                   

                elif line == "24":
                        f.write(data.next().get()[:40])
                        f.write('\n')

                elif line == "25":
                        f.write(data.next().get()[:80])
                        f.write('\n')

                elif line == "26":
                    for i in range(entries_number/5):
                                            
                        dataB = data.next().get()[:7]
                        dataC = data.next().get()[:7]
                        dataD = data.next().get()[:7]
                        dataE = data.next().get()[:7]
                        dataF = data.next().get()[:8]
                        
                        if (i+1) != (entries_number/5):
                            f.write('0' + ' ' + dataB + ' '*(7-len(dataB)) + ' ' + dataC + ' '*(7-len(dataC)) + ' ' + dataD + ' '*(7-len(dataD)) + ' ' + dataE + ' '*(7-len(dataE)) + ' ' + dataF)
                        else:
                            f.write('1' + ' ' + dataB + ' '*(7-len(dataB)) + ' ' + dataC + ' '*(7-len(dataC)) + ' ' + dataD + ' '*(7-len(dataD)) + ' ' + dataE + ' '*(7-len(dataE)) + ' ' + dataF)
                        f.write('\n')

                elif line == "26A":
                        f.write(data.next().get()[:30])
                        f.write('\n')

                elif line == "27":
                    for i in range(entries_number/4):
                        dataB = data.next().get()[:7]
                        dataC = data.next().get()[:1]
                        dataD = data.next().get()[:7]
                        dataE = data.next().get()
                        num_dataE = int(math.ceil(len(dataE)/12))

                        if (i+1) != (entries_number/4):
                            f.write('0' + ' ' + dataB + ' '*(7-len(dataB)) + ' ' + dataC + ' ' + dataD + ' '*(7-len(dataD)) + ' '*16)
                        else:
                            f.write('1' + ' ' + dataB + ' '*(7-len(dataB)) + ' ' + dataC + ' ' + dataD + ' '*(7-len(dataD)) + ' '*16)
                        for i in range(num_dataE):
                            f.write(dataE[0+i*12:12+i*12] + ' ')
                        f.write('\n')

                elif line == "28":
                    f.write('0\n')

                elif line == "29":
                    f.write('1\n')

                elif line == "30":
                    for i in range(entries_number/2):
                        dataB = data.next().get()[:7]
                        dataC = data.next().get()[:1]

                        if (i+1) != (entries_number/2):
                            f.write('0' + ' ' + dataB + ' '*(7-len(dataB)) + ' ' + dataC)
                        else:
                            f.write('1' + ' ' + dataB + ' '*(7-len(dataB)) + ' ' + dataC)
                        
                        f.write('\n')
            
                    

            
        
    def create_lines(self):
        self.line_numbers += 1
        tk.Button(self.frame, text="Generate File", command= self.get_entries, width = 10).grid(row=0,column=1)
        tk.Label(self.frame, text="* Indicates Required", width = 15).grid(row=1,column=1)
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
