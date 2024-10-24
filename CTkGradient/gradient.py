import customtkinter as ctk

TOP_TO_BOTTOM = 1
LEFT_TO_RIGHT = 2
RADIAL = 3  # Nueva constante para gradiente radial

class Gradient(ctk.CTkCanvas):

    gradient_tag = "GradientFrame"
    hex_format = "#%04x%04x%04x"

    def __init__(self, master, colors=("#ec0075", "#ffd366"), direction=LEFT_TO_RIGHT, **kwargs):
        # Set default width and height if not provided
        kwargs["height"] = kwargs.get("height", 200)
        kwargs["width"] = kwargs.get("width", 200)
        kwargs["bg"] = kwargs.get("bg", colors[1])
        kwargs["highlightthickness"] = 0  # Eliminate any internal highlight border

        # Initialize the CTkCanvas
        super().__init__(master, **kwargs)

        # Store geometry and gradient settings
        self.geometry = [kwargs["width"], kwargs["height"]]
        self.colors = colors
        self.direction = direction

        # Draw the initial gradient
        self.draw_gradient()

        # Bind resize event
        self.bind("<Configure>", self.on_resize)

    def draw_gradient(self):
        """
        Draws a gradient on the canvas based on the specified colors and direction.
        """
        # Clear the current canvas content
        self.delete(self.gradient_tag)

        if self.direction == RADIAL:
            self._draw_radial_gradient()

        else:
            self._draw_linear_gradient()

    def _draw_linear_gradient(self):
        """
        Draws a linear gradient based on the specified direction (left-to-right or top-to-bottom).
        """
        limit = self.geometry[0] if self.direction == LEFT_TO_RIGHT else self.geometry[1]

        # Get RGB values from hex colors
        red1, green1, blue1 = self.winfo_rgb(self.colors[0])
        red2, green2, blue2 = self.winfo_rgb(self.colors[1])

        # Calculate the color change ratios
        red_ratio = (red2 - red1) / limit
        green_ratio = (green2 - green1) / limit
        blue_ratio = (blue2 - blue1) / limit

        # Draw the gradient line by line
        for pixel in range(limit):
            red = int(red1 + (red_ratio * pixel))
            green = int(green1 + (green_ratio * pixel))
            blue = int(blue1 + (blue_ratio * pixel))

            color = self.hex_format % (red, green, blue)

            # Determine the start and end points based on the direction
            if self.direction == LEFT_TO_RIGHT:
                x1 = pixel
                y1 = 0
                x2 = pixel
                y2 = self.geometry[1]
            else:
                x1 = 0
                y1 = pixel
                x2 = self.geometry[0]
                y2 = pixel

            # Draw the line with the calculated color
            self.create_line(x1, y1, x2, y2, tag=self.gradient_tag, fill=color)

        # Ensure the gradient is at the bottom layer of the canvas
        self.tag_lower(self.gradient_tag)

    def _draw_radial_gradient(self):
        """
        Draws a radial gradient from the center of the canvas, covering the entire frame.
        """

        # Calculate the center point and maximum radius to cover the entire frame
        center_x = self.geometry[0] // 2
        center_y = self.geometry[1] // 2

        # Maximum radius should cover the farthest corner (diagonal distance from the center)
        max_radius = int(((center_x**2 + center_y**2)**0.5) - 110)

        # Get RGB values from hex colors
        red1, green1, blue1 = self.winfo_rgb(self.colors[0])
        red2, green2, blue2 = self.winfo_rgb(self.colors[1])

        # Calculate the color change ratios
        red_ratio = (red2 - red1) / max_radius
        green_ratio = (green2 - green1) / max_radius
        blue_ratio = (blue2 - blue1) / max_radius

        # Draw the gradient oval by oval, expanding outward from the center
        for radius in range(max_radius):
            red = int(red1 + (red_ratio * radius))
            green = int(green1 + (green_ratio * radius))
            blue = int(blue1 + (blue_ratio * radius))

            color = self.hex_format % (red, green, blue)

            # Draw the oval with the calculated color, adjusting to fill the frame
            self.create_oval(
                center_x - radius,  # left
                center_y - radius,  # top
                center_x + radius,  # right
                center_y + radius,  # bottom
                tag=self.gradient_tag,
                outline=color,
                width=2  # Width of the outline to avoid gaps
            )

        # Ensure the gradient is at the bottom layer of the canvas
        self.tag_lower(self.gradient_tag)

    def on_resize(self, event):
        """
        Redraw the gradient when the canvas is resized.
        """
        self.geometry = [event.width, event.height]
        self.draw_gradient()

    def config(self, cnf = None, **kwargs):
        """
        Updates the configuration of the GradientFrame widget.
        """
        # Update the colors if provided
        if "colors" in kwargs and len(kwargs["colors"]) > 1:
            self.colors = kwargs.pop("colors")

        # Update the direction if provided
        if "direction" in kwargs and kwargs["direction"] in (LEFT_TO_RIGHT, TOP_TO_BOTTOM, RADIAL):
            self.direction = kwargs.pop("direction")

        # Update the geometry if the width or height is provided
        if "height" in kwargs:
            self.geometry[1] = kwargs["height"]

        if "width" in kwargs:
            self.geometry[0] = kwargs["width"]

        # Apply the changes and redraw the gradient
        super().config(cnf, **kwargs)
        self.draw_gradient()

    def configure(self, cnf = None, **kwargs):
        # Alias for config method to match tkinter's API
        self.config(cnf, **kwargs)
