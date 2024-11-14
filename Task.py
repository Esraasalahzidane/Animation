import pygame
from tkinter import *
import random
import threading

class MainGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("let's go 🤘")

        pygame.mixer.init()  

        self.w = 600
        self.h = 250
        self.canvas = Canvas(self.window, width=self.w, height=self.h, bg='white')
        self.canvas.pack()

   
        self.car = PhotoImage(file="car1.gif").zoom(2)
        self.x = 0
        self.y = self.h / 2 
        self.velocity_y = -8 
        self.gravity = 0.3 
        self.dx = 5 

        self.car_id = self.canvas.create_image(self.x, self.y, image=self.car, tags="car")

        self.change_background_color()
        self.animate()

    
        threading.Thread(target=self.play_music, daemon=True).start()

        self.window.mainloop()

    def play_music(self):
        pygame.mixer.music.load("EV.mp3")
        pygame.mixer.music.play(-1) 

    def change_background_color(self):
        colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink"]
        self.canvas.config(bg=random.choice(colors))
        self.canvas.after(1000, self.change_background_color)

    def animate(self):
     
        self.velocity_y += self.gravity
        self.y += self.velocity_y 
        if self.y >= self.h * 0.75:  
            self.velocity_y = -8 
        elif self.y <= self.h * 0.25: 
            self.velocity_y = 8  
        
        self.x += self.dx
        if self.x > self.w + 65:
            self.x = 0  
        self.canvas.coords(self.car_id, self.x, self.y)

        self.canvas.after(30, self.animate)  


MainGUI()
