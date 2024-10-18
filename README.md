```python
import customtkinter as ctk
import CTkGradient as ctkg

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
    direction = "vertical")

gradient_frame.pack(fill = "both")

root.mainloop()
```
