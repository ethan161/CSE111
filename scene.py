import tkinter as tk
import random

def main():
    width = 800
    height = 500

    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()

def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    height = 500
    width = 800
    draw_sky(canvas, height)
    draw_ground(canvas, height)
    draw_cloud(canvas)
    grass_side_left = 0
    grass_side_right = 10
    grass_height = 500
    while grass_side_right != width:
        draw_grass(canvas, grass_side_left, grass_side_right, grass_height)
        grass_side_right += 10
        grass_side_left += 10    

def draw_sky(canvas, height):
    sky_height = height / .8
    sky_top = 0
    sky_side_left= 0
    sky_side_right = 800
    canvas.create_rectangle(sky_side_left, sky_top, 
            sky_side_right, sky_height,
            outline="DeepSkyBlue2", width=1, fill="DeepSkyBlue2")

def draw_ground(canvas, height):
    ground_height = height / .8
    ground_bottom = height
    ground_side_left= 0
    ground_side_right = 800
    canvas.create_rectangle(ground_side_left, ground_height, 
            ground_side_right, ground_bottom,
            outline="green4", width=1, fill="green4")

def draw_cloud(canvas):
    upper_side = 25
    upper_height = 25
    lower_side = 125
    lower_height = 75
    canvas.create_oval(upper_side, upper_height, 
            lower_side, lower_height, 
            outline="snow", width=1, fill="snow")
    upper_side += 75
    upper_height = 10
    lower_side += 75
    lower_height = 80
    canvas.create_oval(upper_side, upper_height, 
            lower_side, lower_height, 
            outline="snow", width=1, fill="snow")
    upper_side += 75
    upper_height = 25
    lower_side += 75
    lower_height = 75
    canvas.create_oval(upper_side, upper_height, 
            lower_side, lower_height, 
            outline="snow", width=1, fill="snow")

def draw_grass(canvas, grass_side_left, grass_side_right, grass_height):
        grass_top = random.randint(475, 495)
        canvas.create_rectangle(grass_side_left, grass_top, 
                grass_side_right, grass_height,
                outline="green4", width=1, fill="green4")

main()