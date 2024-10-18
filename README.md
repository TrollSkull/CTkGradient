<h3 align="center">
    <img width="500" height="150" alt="ctkgradient logo" src=".assets/logo.png">
</h3>

<h3 align="center">Create a gradient frame for your customtkinter applications.</h3>

<h3 align="center">
    <img src=".assets/gradient_screenshot.png" alt="Screenshot" width="800" height="370">
</h3>

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
