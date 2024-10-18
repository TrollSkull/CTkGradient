from typing import Literal
import customtkinter as ctk

from .gradient import Gradient, LEFT_TO_RIGHT, TOP_TO_BOTTOM

class GradientFrame(ctk.CTkFrame):
    """
    A custom frame with a gradient background.

    Inherits from CTkFrame and provides a gradient background 
    defined by the specified colors and direction.

    Parameters:
        master (ctk.Widget): The parent widget of the frame.
        width (int): The width of the frame.
        height (int): The height of the frame.
        direction (str): The direction of the gradient (e.g., 'horizontal', 'vertical').
        colors (list): A list of colors to be used in the gradient.
        corner_radius (int, optional): The radius of the corners of the frame. Defaults to 0.

    Example:
        ```python
        gradient_frame = GradientFrame(
            master = root,
            width = 300,
            height = 200, 
            direction = 'horizontal',
            colors = ('#FF0000', '#0000FF')
        )
        ```
    """

    def __init__(self, master, width, height, direction: Literal["horizontal", "vertical"], colors, corner_radius = 0):
        # Call the constructor of the parent class
        super().__init__(master, width=width, height=height, corner_radius=corner_radius)

        if direction == "horizontal":
            direction = LEFT_TO_RIGHT

        if direction == "vertical":
            direction = TOP_TO_BOTTOM

        # Create the gradient canvas
        self.gradient = Gradient(master=self, width=width, height=height, direction=direction, colors = colors)
        self.gradient.pack(padx=0, pady=0, fill="both", expand = True)
