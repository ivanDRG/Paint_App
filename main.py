from tkinter import *
import tkinter.font

# Define class

class PaintApp:
    pass

    # Define class variables

    drawing_tool = "text"

    left_but = "up"

    x_pos, y_pos = None, None

    x1_line_pt, y1_line_pt, x2_line_pt, y2_line_pt = None, None, None, None

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
                event.widget.create_line(self.x_pos, self.y_pos, event.x, event.y, smooth=TRUE)

            self.x_pos = event.x
            self.y_pos = event.y

    # Draw line

    def line_draw(self, event=None):

        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            event.widget.create_line(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt, smooth=TRUE, fill="green")

    # Draw Arc

    def arc_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            coords = self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt

            event.widget.create_arc(coords, start=0, extent=150, fill="red", style=ARC)

    # Draw oval

    def oval_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            coords = self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt

            event.widget.create_oval(coords, fill="midnight blue", outline="yellow", width=2)

    # Draw rectangle

    def rectangle_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt):
            coords = self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt

            event.widget.create_rectangle(coords, fill="midnight blue", outline="yellow", width=2)

    # Draw text

    def text_draw(self, event=None):
        if None not in (self.x1_line_pt, self.y1_line_pt):
            text_font=tkinter.font.Font(family="Helvetica", size=20, weight="bold")

            event.widget.create_text(self.x1_line_pt, self.y1_line_pt, fill="green", font=text_font, text="WOW")

    # Initialize

    def __init__(self, root):
        drawing_area = Canvas(root)

        drawing_area.pack()

        drawing_area.bind("<Motion>", self.motion)
        drawing_area.bind("<ButtonPress-1>", self.left_but_down)
        drawing_area.bind("<ButtonRelease-1>", self.left_but_up)

root = Tk()
paint_app = PaintApp(root)
root.mainloop()