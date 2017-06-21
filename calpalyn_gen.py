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

        self.line_descriptions = {"01": "","02": "","03": "Total/Subtotals","04": "","05": "","06": "","07": "","08": "","09": "", "10": "","11": "","12": "","13": "Taxa File","14": "calpalyn.listing File","15": "","16": "Plot Graph","17": "calpalyn.listing Normalization","18": "\"","19": "\"","20": "Graph Options","20A": "Graph Format","21": "Graph Elements","22": "Graph Scaling","23": "Pollen Zonation","24": "Vertical Axis","25": "Plot Title","26": "Chronology Column","26A": "Chronology Label","27": "Stratigraphy Column","28": "","29": "","30": "Pollen Zones"}
        self.repeating_lines = ["20","26","27","30"]

        # Lines 02 15 28 and 29 are ignored in this front end version of calpalyn --
        # they are automatically written to the file in the specified format but don't take user input
        self.ignore_lines = ["02","15","28","29"]

        # Layout stores all the widgets in a list with a line identifer
        self.layout = []

        # Entries contains all the widgets that are entries (not labels and buttons)
        self.entries = defaultdict(list)

        # Keep track off the number of line numbers
        self.line_numbers = 0

        # Create the intial lines and render them as a form
        self.create_lines(self.lines)
        self.render_lines()

    def create_entries(self, line_id):
        if line_id == "01":
            self.layout.append( (tk.Label(self.frame, text = "File Type * : ", width = 17),(self.line_numbers, 2),line_id+"!file_type") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for File Type.")
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
            self.layout[len(self.layout)-1][0].insert(0,0)

            self.layout.append( (tk.Label(self.frame, text = "Level Factor * : ", width = 13),(self.line_numbers, 4),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Number.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=4)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 5),line_id+":C") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=5)
            self.layout[len(self.layout)-1][0].insert(0,-1.0)
            
        elif line_id == "03":
            self.layout.append( (tk.Label(self.frame, text = "Total: ", width = 7),(self.line_numbers, 2),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Total.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
        
            self.layout.append( (tk.Label(self.frame, text = "Subtotals (5-12):", width = 16),(self.line_numbers, 4),line_id) )
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
            self.layout.append( (tk.Entry(self.frame, width = 10),(self.line_numbers, 12),line_id+":I") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=12)


        elif line_id == "04":
            self.layout.append( (tk.Label(self.frame, text = "Excluded Taxa: ", width = 15),(self.line_numbers, 2),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Subtotal.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":B") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
            
        elif line_id in ["05","06","07","08","09","10","11","12"]:
            self.layout.append( (tk.Label(self.frame, text = "Subtotal Taxa: ", width = 15),(self.line_numbers, 2),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Subtotal.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":B") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
            
        elif line_id == "13":
            self.layout.append( (tk.Label(self.frame, text = "Taxon Names * : ", width = 15),(self.line_numbers, 2),line_id) )
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
            self.layout.append( (tk.Label(self.frame, text = "Taxon * : ", width = 8),(self.line_numbers, 2),line_id) )
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

            self.layout.append( (tk.Label(self.frame, text = "H. Interval: ", width = 10),(self.line_numbers, 10),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for H Scale.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=10)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 11),line_id+":I") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=11)

            self.layout.append( (tk.Label(self.frame, text = "H. Graph Label: ", width = 14),(self.line_numbers, 12),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Graph Label.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=12)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 13),line_id+":J") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=13)


        elif line_id == "20A":
            self.layout.append( (tk.Label(self.frame, text = "New Group * : ", width = 12),(self.line_numbers, 2),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "If you have two taxa next to each other both with 'blank' labels, you must specify both as new taxon groups.")
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

            self.layout.append( (tk.Label(self.frame, text = "Line Angle: ", width = 12),(self.line_numbers, 8),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Angle.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=8)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 9),line_id+":D") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=9)

            self.layout.append( (tk.Label(self.frame, text = "Line Density: ", width = 13),(self.line_numbers, 10),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Density.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=10)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 11),line_id+":E") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=11)

            self.layout.append( (tk.Label(self.frame, text = "Plot Type: ", width = 11),(self.line_numbers, 12),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Plot Type.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=12)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 13),line_id+":F") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=13)

        elif line_id == "21":
            self.layout.append( (tk.Label(self.frame, text = "Level Lines: ", width =12),(self.line_numbers, 2),line_id) )
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

            self.layout.append( (tk.Label(self.frame, text = "Enlarged Font: ", width = 12),(self.line_numbers, 8),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Font.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=8)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 9),line_id+":D") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=9)
            
        elif line_id == "22":
            self.layout.append( (tk.Label(self.frame, text = "Diagram Height: ", width = 13),(self.line_numbers, 2),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Height.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=2)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 3),line_id+":A") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=3)
        
            self.layout.append( (tk.Label(self.frame, text = "Diagram Width: ", width = 13),(self.line_numbers, 4),line_id) )
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

            self.layout.append( (tk.Label(self.frame, text = "H. Interval Size: ", width = 13),(self.line_numbers, 10),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for H Scale Interval.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=10)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 11),line_id+":E") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=11)

        elif line_id == "23":
            self.layout.append( (tk.Label(self.frame, text = "Pollen Zonation: ", width = 13),(self.line_numbers, 2),line_id) )
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

            self.layout.append( (tk.Label(self.frame, text = "Substance Label: ", width = 13),(self.line_numbers, 10),line_id) )
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

            self.layout.append( (tk.Label(self.frame, text = "Zone Label: ", width = 9),(self.line_numbers, 8),line_id) )
            wckToolTips.register(self.layout[len(self.layout)-1][0], "This entry is used for Zone Label.")
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=8)
            self.layout.append( (tk.Entry(self.frame, width = 6),(self.line_numbers, 9),line_id+":E") )
            self.layout[len(self.layout)-1][0].grid(row=self.line_numbers, column=9)

        elif line_id == "30":
            self.layout.append( (tk.Label(self.frame, text = "Zone Boundary: ", width = 13),(self.line_numbers, 2),line_id) )
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
        self.layout.append( (tk.Label(self.frame, anchor = "w", font = "Verdana 13 bold", relief = "raised", text="Line 20", width = 30, height = 1),(self.line_numbers, 1),"20") )
        self.layout[len(self.layout)-1][0].grid(row=self.line_numbers,column=1)
        self.line_numbers += 1
        self.create_entries("20A")
        self.layout.append( (tk.Label(self.frame, anchor = "w", font = "Verdana 13 bold", relief = "raised", text="Line 20A", width = 30, height = 1),(self.line_numbers, 1),"20A") )
        self.layout[len(self.layout)-1][0].grid(row=self.line_numbers,column=1)

    def new_line26(self):
        self.line_numbers += 1
        self.create_entries("26")
        self.layout.append( (tk.Label(self.frame, anchor = "w", font = "Verdana 13 bold", relief = "raised", text="Line 26", width = 30, height = 1),(self.line_numbers, 1),"26") )
        self.layout[len(self.layout)-1][0].grid(row=self.line_numbers,column=1)
        
    def new_line27(self):
        self.line_numbers += 1
        self.create_entries("27")
        self.layout.append( (tk.Label(self.frame, anchor = "w", font = "Verdana 13 bold", relief = "raised", text="Line 27", width = 30, height = 1),(self.line_numbers, 1),"27") )
        self.layout[len(self.layout)-1][0].grid(row=self.line_numbers,column=1)
        
    def new_line30(self):
        self.line_numbers += 1
        self.create_entries("30")
        self.layout.append( (tk.Label(self.frame, anchor = "w", font = "Verdana 13 bold", relief = "raised", text="Line 30", width = 30, height = 1),(self.line_numbers, 1),"20") )
        self.layout[len(self.layout)-1][0].grid(row=self.line_numbers,column=1)

    def get_entries(self):
        
        self.entries = defaultdict(list)
        
        for widget in self.layout:
            if widget[2][-2] == ":":
                    if widget[2][:3] == "26A":
                        self.entries[widget[2][:3]].append(widget[0])
                    else:
                        self.entries[widget[2][:2]].append(widget[0])

    def write_lines(self):

        self.get_entries()
        
        with open('file.instrs', 'wb+') as f:
            
            for line in self.lines:
                entries_number = len(self.entries[line])
                data = iter(self.entries[line])

                # Format each line and write it to instruction file for use by Calpalyn
                if line == "01":
                        dataA = data.next().get()[:1]
                        dataB = data.next().get()[:9]
                        
                        f.write(dataA + ' '*(1-len(dataA)) +  ' ' + '0' + ' ' + dataB)
                        f.write(" "*81+"//Line "+str(line))
                        f.write('\n')

                elif line == "02":
                        f.write('1')
                        f.write(" "*81+"//Line "+str(line))
                        f.write('\n')

                elif line == "03":
                        dataA = data.next().get()[:1]
                        dataB = data.next().get()[:1]
                        dataC = data.next().get()[:1]
                        dataD = data.next().get()[:1]
                        dataE = data.next().get()[:1]
                        dataF = data.next().get()[:1]
                        dataG = data.next().get()[:1]
                        dataH = data.next().get()[:1]
                        dataI = data.next().get()[:1] 
                        f.write(dataA + ' '*(1-len(dataA)) + ' ' + dataB + ' '*(1-len(dataB))  + ' ' + dataC + ' '*(1-len(dataC))  + ' ' + dataD + ' '*(1-len(dataD))  + ' ' + dataE + ' '*(1-len(dataE))  + ' ' + dataF + ' '*(1-len(dataF))  + ' ' + dataG + ' '*(1-len(dataG))  + ' ' + dataH + ' '*(1-len(dataH))  + ' ' + dataI)
                        f.write(" "*81+"//Line "+str(line))
                        f.write('\n')

                elif line in ["04","05","06","07","08","09","10","11","12"]:
                        dataA = data.next().get()[:75]
                        f.write('1' + ' ' + dataA)
                        f.write(" "*81+"//Line "+str(line))
                        f.write('\n')

                elif line == "13":
                        dataA = data.next().get()[:1]
                        f.write(dataA)
                        f.write(" "*81+"//Line "+str(line))
                        f.write('\n')
                        
                elif line == "15":
                        f.write('1')
                        f.write(" "*81+"//Line "+str(line))
                        f.write('\n')

                elif line == "14":
                        dataA = data.next().get()[:1]
                        dataB = data.next().get()[:1]
                        dataC = data.next().get()[:1]
                        dataD = data.next().get()[:1]
                        dataE = data.next().get()[:1]
                        f.write(dataA + ' '*(1-len(dataA)) + ' ' + dataB + ' '*(1-len(dataB))  + ' ' + dataC + ' '*(1-len(dataC)) +  ' ' + dataD + ' '*(1-len(dataD)) + ' ' + dataE)
                        f.write(" "*81+"//Line "+str(line))
                        f.write('\n')

                elif line == "16":
                        dataA = data.next().get()[:1]
                        f.write(dataA)
                        f.write(" "*81+"//Line "+str(line))
                        f.write('\n')
                        
                elif line in ["17", "18", "19"]:
                        dataA = data.next().get()[:1]
                        dataB = data.next().get()[:5]
                        f.write(dataA + ' '*(1-len(dataA)) + ' ' + dataB)
                        f.write(" "*81+"//Line "+str(line))
                        f.write('\n')

                
                # Line 20 handles lines 20 and 20A
                elif line == "20":
                    for i in range(entries_number/12):

                        # Line 20 entries
                        dataB = data.next().get()[:5]
                        dataC = data.next().get()[:1]
                        dataD = data.next().get()[:25]
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
                        
                        # Line 20                                                  
                        if (i+1) != (entries_number/12):
                            
                            f.write('0' + ' ' + dataB + ' '*(5-len(dataB)) + ' ' + dataC + ' '*(1-len(dataC))  + ' ' + dataD + ' '*(25-len(dataD)) + ' ' + dataF + ' '*(1-len(dataF))  + '      ' + dataI + ' '*(6-len(dataI)) + ' ' + dataJ )
                        else:
                            f.write('1' + ' ' + dataB + ' '*(5-len(dataB)) + ' ' + dataC + ' '*(1-len(dataC))  + ' ' + dataD + ' '*(25-len(dataD)) + ' ' + dataF + ' '*(1-len(dataF))  + '      ' + dataI + ' '*(6-len(dataI)) + ' ' + dataJ )
                        f.write(" "*81+"//Line "+str(20))                            
                        f.write('\n')
                        # Line 20A
                        f.write(data1A + ' '*(1-len(data1A)) + ' ' + data1B + ' '*(1-len(data1B)) + ' ' + data1C + ' '*(1-len(data1C)) + ' ' + data1D + ' '*(7-len(data1D)) + ' ' + data1E + ' '*(2-len(data1E)) + ' ' + data1F)
                        f.write(" "*81+"//Line 20A")
                        f.write('\n')
                        

                elif line == "21":
                        dataA = data.next().get()[:1]
                        dataB = data.next().get()[:1]
                        dataC = data.next().get()[:1]
                        dataD = data.next().get()[:1]
                        f.write(dataA + ' '*(1-len(dataA)) + ' ' + dataB + ' '*(1-len(dataB)) + ' ' + dataC + ' '*(1-len(dataC))  + ' ' + dataD)
                        f.write(" "*81+"//Line "+str(line))
                        f.write('\n')

                elif line  == "22":
                        dataA = data.next().get()[:6]
                        dataB = data.next().get()[:6]
                        dataC = data.next().get()[:6]
                        dataD = data.next().get()[:6]
                        dataE = data.next().get()[:6]
                        f.write(' ' + dataA + ' '*(6-len(dataA)) + ' ' + dataB + ' '*(6-len(dataB)) + ' ' + dataC + ' '*(6-len(dataC)) + ' ' + dataD + ' '*(6-len(dataD)) + ' ' + dataE)
                        f.write(" "*81+"//Line "+str(line))
                        f.write('\n')

                elif line == "23":
                        dataA = data.next().get()[:2]
                        f.write(dataA)
                        f.write(" "*81+"//Line "+str(line))
                        f.write('\n')                   

                elif line == "24":
                        dataA = data.next().get()[:40]
                        f.write(dataA)
                        f.write(" "*81+"//Line "+str(line))
                        f.write('\n')

                elif line == "25":
                        dataA = data.next().get()[:80] 
                        f.write(dataA)
                        f.write(" "*81+"//Line "+str(line))
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
                        f.write(" "*81+"//Line "+str(line))
                        f.write('\n')

                elif line == "26A":
                        dataA = data.next().get()[:30]
                        f.write(dataA)
                        f.write(" "*81+"//Line "+str(line))
                        f.write('\n')

                elif line == "27":
                    for i in range(entries_number/4):
                        dataB = data.next().get()[:7]
                        dataC = data.next().get()[:1]
                        dataD = data.next().get()[:7]
                        dataE = data.next().get()
                        num_dataE = int(math.ceil(len(dataE)/12.0))

                        if (i+1) != (entries_number/4):
                            f.write('0' + ' ' + dataB + ' '*(7-len(dataB)) + ' ' + dataC + ' '*(1-len(dataC))  + ' ' + dataD + ' '*(7-len(dataD)) + ' '*17)
                        else:
                            f.write('1' + ' ' + dataB + ' '*(7-len(dataB)) + ' ' + dataC + ' '*(1-len(dataC))  + ' ' + dataD + ' '*(7-len(dataD)) + ' '*17)
                        for i in range(num_dataE):
                            f.write(dataE[0+i*12:12+i*12] + ' ')
                        f.write(" "*81+"//Line "+str(line))
                        f.write('\n')

                elif line == "28":
                        f.write('0')
                        f.write(" "*81+"//Line "+str(line))
                        f.write('\n')

                elif line == "29":
                        f.write('1')
                        f.write(" "*81+"//Line "+str(line))
                        f.write('\n')

                elif line == "30":
                    for i in range(entries_number/2):
                        dataB = data.next().get()[:7]
                        dataC = data.next().get()[:1]

                        if (i+1) != (entries_number/2):
                            f.write('0' + ' ' + dataB + ' '*(7-len(dataB)) + ' ' + dataC)
                        else:
                            f.write('1' + ' ' + dataB + ' '*(7-len(dataB)) + ' ' + dataC)
                        
                        f.write(" "*81+"//Line "+str(line))
                        f.write('\n')

        
    def create_lines(self, these_lines):
        self.line_numbers += 1
        tk.Button(self.frame, text="Generate Instruction File", command= self.write_lines, width = 20).grid(row=0,column=1)
        tk.Button(self.frame, text="Clear All Fields", command= self.read_lines, width = 20).grid(row=1,column=1)
        tk.Label(self.frame, text="* Indicates Required", width = 15).grid(row=1,column=2)
        self.create_form(these_lines)

    def read_lines(self):
        
        for widget in self.layout:
            widget[0].destroy()
            
        self.layout = []
        self.entries = defaultdict(list)

        lines_to_create = []
        entries_read = []
        
        with open('file.instrs', 'rb+') as f:
            
            for line in f:
                line = line.split()
                try:
                    index = line.index("//Line")
                except ValueError:
                    print("Error loading line, make sure it was generated and has line names.")
                else:
                    lines_to_create.append(line[index+1])
                    for i in range(index):
                        entries_read.append(line[i])

        self.line_numbers = 0
        self.create_lines(lines_to_create)
        self.get_entries()

        self.render_lines()

    def remove_last_line(self):
        to_remove = []

        if self.line_numbers <= 33:
            return
        
        for widget in self.layout:
            print(widget[1][0],self.line_numbers)
            if widget[1][0] == self.line_numbers:
                widget[0].destroy()
                to_remove.append(widget)
                
        for widget in to_remove:
            self.layout.remove(widget)

        self.line_numbers -= 1

    def create_form(self,these_lines):
                             
        for line in these_lines:
            self.line_numbers += 1
            if line not in self.ignore_lines:
                self.create_entries(line)
            self.layout.append( (tk.Label(self.frame, anchor = "w", font = "Verdana 13 bold", relief = "raised", text="Line " + line + ": " + self.line_descriptions[line], width = 30, height = 1),(self.line_numbers, 1),line) )
            
            if line in self.repeating_lines:
                if line == "20":
                    self.layout.append( (tk.Button(self.frame, text="+", command= self.new_line20, width = 8),(self.line_numbers, 999),line) )
                elif line == "26":
                    self.layout.append( (tk.Button(self.frame, text="+", command= self.new_line26, width = 8),(self.line_numbers, 999),line) )
                elif line == "27":
                    self.layout.append( (tk.Button(self.frame, text="+", command= self.new_line27, width = 8),(self.line_numbers, 999),line) )
                elif line == "30":
                    self.layout.append( (tk.Button(self.frame, text="+", command= self.new_line30, width = 8),(self.line_numbers, 999),line) )
                    
        self.layout.append( (tk.Button(self.frame, text="Remove Last Line", command= self.remove_last_line, width = 14),(0, 2),line) )
               
                
    def render_lines(self):
        for widget in self.layout:
            widget[0].grid(row=widget[1][0],column=widget[1][1])

    def render_entries(self):
        for entry in self.layout:
            entry[0].grid(row=entry[1][0],column=entry[1][1])

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    root=tk.Tk()
    Example(root).pack(side="top", fill="both", expand=True)
    root.title("Calpalyn File Generator")
    root.mainloop()
