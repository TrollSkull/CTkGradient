## Screenshots
Vertical gradient:
<img src=".assets/vertical_gradient_screenshot.png" alt="Screenshot" width="500" height="375">

Horizontal gradient:
<img src=".assets/horizontal_gradient_screenshot.png" alt="Screenshot" width="500" height="375">

## How to use it?
```python
# Import customtkinter and CTkGradient
import customtkinter as ctk
import CTkGradient as ctkg

# Initialize CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()

# Create a GradientFrame with custom colors and direction
gradient_frame = ctkg.GradientFrame(
    master = root,
    colors = ("#ec0075", "#ffd366"),
    direction = "vertical",
    height = 600,
    width = 800
)

gradient_frame.pack(fill = "both")

root.mainloop()
```
