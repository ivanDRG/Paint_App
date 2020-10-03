from tkinter import *
import tkinter.font

# Define class

class PaintApp:

    # Define class variables
    stroke_color = "black"

    fill_color = None

    drawing_tool = "pencil"

    left_but = "up"

    x_pos, y_pos = None, None

    x1_line_pt, y1_line_pt, x2_line_pt, y2_line_pt = None, None, None, None

    # Change stroke color
    
    def stroke_white(self, event=None):
        print("white")
        self.stroke_color = "white"

    def stroke_black(self, event=None):
        self.stroke_color = "black"
        print("black")

    def stroke_grey(self, event=None):
        self.stroke_color = "grey"
        print("grey")

    def stroke_green(self, event=None):
        self.stroke_color = "green"
        print("green")

    def stroke_yellow(self, event=None):
        self.stroke_color = "yellow"
        print("yellow")

    def stroke_magenta(self, event=None):
        self.stroke_color = "magenta"
        print("magenta")
    
    def stroke_red(self, event=None):
        self.stroke_color = "red"
        print("red")
    
    def stroke_blue(self, event=None):
        self.stroke_color = "blue"
        print("blue")

    # Change fill color

    def fill_none(self, event=None):
        print("None")
        self.fill_color = None
    
    def fill_white(self, event=None):
        print("white")
        self.fill_color = "white"

    def fill_black(self, event=None):
        self.fill_color = "black"
        print("black")

    def fill_grey(self, event=None):
        self.fill_color = "grey"
        print("grey")

    def fill_green(self, event=None):
        self.fill_color = "green"
        print("green")

    def fill_yellow(self, event=None):
        self.fill_color = "yellow"
        print("yellow")

    def fill_magenta(self, event=None):
        self.fill_color = "magenta"
        print("magenta")
    
    def fill_red(self, event=None):
        self.fill_color = "red"
        print("red")
    
    def fill_blue(self, event=None):
        self.fill_color = "blue"
        print("blue")    

    # Change paint tool

    def pencil_tool(self, event=None):
        self.drawing_tool = "pencil"

    def line_tool(self, event=None):
        self.drawing_tool = "line"
        
    def arc_tool(self, event=None):
        self.drawing_tool = "arc"
        
    def oval_tool(self, event=None):
        self.drawing_tool = "oval"
        
    def rectangle_tool(self, event=None):
        self.drawing_tool = "rectangle"
       
    def text_tool(self, event=None):
        self.drawing_tool = "text"

    # Catch mouse down
    def left_but_down(self, event=None):
        self.left_but = "down"

        self.x1_line_pt = event.x
        self.y1_line_pt = event.y

    # Catch mouse up

    def left_but_up(self, event=None):
        self.left_but = "up"

        self.x_pos = None
        self.y_pos = None

        self.x2_line_pt = event.x
        self.y2_line_pt = event.y

        if self.drawing_tool == "line":
            self.line_draw(event)
        elif self.drawing_tool == "arc":
            self.arc_draw(event)
        elif self.drawing_tool == "oval":
            self.oval_draw(event)
        elif self.drawing_tool == "rectangle":
            self.rectangle_draw(event)
        elif self.drawing_tool == "text":
            self.text_draw(event)

    # Catch mouse move

    def motion(self, event=None):

        if self.drawing_tool == "pencil":
            self.pencil_draw(event)

    # Draw pencil

    def pencil_draw(self, event=None):

        if self.left_but == "down":
            if self.x_pos is not None and self.y_pos is not None:
                event.widget.create_line(self.x_pos, self.y_pos, event.x, event.y, smooth=TRUE, fill=self.stroke_color)

            self.x_pos = event.x
            self.y_pos = event.y

    # Draw line

    def line_draw(self, event=None):

        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            event.widget.create_line(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt, smooth=TRUE, fill=self.stroke_color)

    # Draw Arc

    def arc_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            coords = self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt

            event.widget.create_arc(coords, start=0, extent=150, fill=self.stroke_color, style=ARC)

    # Draw oval

    def oval_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            coords = self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt

            event.widget.create_oval(coords, fill=self.fill_color, outline=self.stroke_color, width=2)

    # Draw rectangle

    def rectangle_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            coords = self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt

            event.widget.create_rectangle(coords, fill=self.fill_color, outline=self.stroke_color, width=2)

    # Draw text

    def text_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt):
            text_font=tkinter.font.Font(family="Helvetica", size=20, weight="bold")

            event.widget.create_text(self.x1_line_pt, self.y1_line_pt, fill=self.stroke_color, font=text_font, text="WOW")

    # Initialize

    def __init__(self, root):
        # Set Menu

        my_menu = Menu(root)
        root.config(menu=my_menu)

        # Add tools cascade

        menu_tools = Menu(my_menu)
        my_menu.add_cascade(label="Tools", menu=menu_tools)
        menu_tools.add_command(label="Pencil", command=self.pencil_tool)
        menu_tools.add_command(label="Line", command=self.line_tool)
        menu_tools.add_command(label="Arc", command=self.arc_tool)
        menu_tools.add_command(label="Oval", command=self.oval_tool)
        menu_tools.add_command(label="Rectangle", command=self.rectangle_tool)
        menu_tools.add_command(label="text", command=self.text_tool)

        # Add stroke color cascade

        menu_stroke = Menu(my_menu)
        my_menu.add_cascade(label="Stroke", menu=menu_stroke)
        menu_stroke.add_command(label="White", command=self.stroke_white)
        menu_stroke.add_command(label="Black", command=self.stroke_black)
        menu_stroke.add_command(label="Grey", command=self.stroke_grey)
        menu_stroke.add_command(label="Green", command=self.stroke_green)
        menu_stroke.add_command(label="Yellow", command=self.stroke_yellow)
        menu_stroke.add_command(label="Magenta", command=self.stroke_magenta)
        menu_stroke.add_command(label="Red", command=self.stroke_red)
        menu_stroke.add_command(label="Blue", command=self.stroke_blue)

        # Add fill color cascade

        menu_fill = Menu(my_menu)
        my_menu.add_cascade(label="Fill", menu=menu_fill)
        menu_fill.add_command(label="None", command=self.fill_none)
        menu_fill.add_separator()
        menu_fill.add_command(label="White", command=self.fill_white)
        menu_fill.add_command(label="Black", command=self.fill_black)
        menu_fill.add_command(label="Grey", command=self.fill_grey)
        menu_fill.add_command(label="Green", command=self.fill_green)
        menu_fill.add_command(label="Yellow", command=self.fill_yellow)
        menu_fill.add_command(label="Magenta", command=self.fill_magenta)
        menu_fill.add_command(label="Red", command=self.fill_red)
        menu_fill.add_command(label="Blue", command=self.fill_blue)

        drawing_area = Canvas(root)

        drawing_area.pack()

        drawing_area.bind("<Motion>", self.motion)
        drawing_area.bind("<ButtonPress-1>", self.left_but_down)
        drawing_area.bind("<ButtonRelease-1>", self.left_but_up)
    
    # Create menu item



root = Tk()
root.title("Paint")
paint_app = PaintApp(root)





root.mainloop()