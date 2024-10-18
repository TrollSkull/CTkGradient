```python
from CTkGradient import CTkGradient as ctkg
import customtkinter as ctk

# Initialize CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()

# Create a GradientFrame with custom colors and direction
gradient_frame = ctkg.GradientFrame(
    master = root,
    width = 800,
    colors = ("#ec0075", "#ffd366"),
    height = 600,
    direction = ctkg.TOP_TO_BOTTOM)

gradient_frame.pack(fill = "both")

root.mainloop()
```
