import tkinter as tk

def show_card():
    message = (
        "💖 Happy Valentine’s Day 💖\n\n"
        "You are an amazing friend!\n"
        "Thank you for all the laughs,\n"
        "support, and good vibes 🌸\n\n"
        "🍓💌 You are loved 💌🍓"
    )
    label.config(text=message)

# Create app window
app = tk.Tk()
app.title("Valentine Card 💕")
app.geometry("400x300")
app.configure(bg="#ffd6e8")

# Title
title = tk.Label(
    app,
    text="💝 Valentine Card 💝",
    font=("Comic Sans MS", 18, "bold"),
    bg="#ffd6e8",
    fg="#ff4d88"
)
title.pack(pady=15)

# Card message
label = tk.Label(
    app,
    text="Click the button for a surprise 💌",
    font=("Comic Sans MS", 12),
    bg="#ffd6e8",
    fg="#cc0066",
    wraplength=350,
    justify="center"
)
label.pack(pady=20)

# Button
button = tk.Button(
    app,
    text="Open Valentine 💖",
    font=("Comic Sans MS", 12, "bold"),
    bg="#ff99c8",
    fg="white",
    command=show_card
)
button.pack(pady=15)

# Run app
app.mainloop()