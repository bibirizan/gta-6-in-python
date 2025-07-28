import tkinter as tk

# Fereastră
root = tk.Tk()
root.title("Mini GTA fără Pygame")

canvas_width = 800
canvas_height = 600
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Mașinuța (dreptunghi roșu)
car_width = 50
car_height = 30
car = canvas.create_rectangle(375, 285, 375 + car_width, 285 + car_height, fill="red")

car_speed = 10

# Funcție mișcare
def move_car(event):
    key = event.keysym
    if key == "Left":
        canvas.move(car, -car_speed, 0)
    elif key == "Right":
        canvas.move(car, car_speed, 0)
    elif key == "Up":
        canvas.move(car, 0, -car_speed)
    elif key == "Down":
        canvas.move(car, 0, car_speed)

# Legăm tastele de funcția de mișcare
root.bind("<KeyPress>", move_car)

# Loop principal
root.mainloop()
input("Apasă Enter pentru a închide...")

