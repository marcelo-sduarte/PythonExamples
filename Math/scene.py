import tkinter as tk


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    tree_center = scene_left + 500
    tree_top = scene_top + 100
    tree_height = 150
   
    draw_sky(canvas, tree_center, tree_top, tree_height)
    draw_land(canvas, tree_center, tree_top, tree_height)
    draw_cloud(canvas, tree_center, tree_top, tree_height)
    draw_sun(canvas, tree_center, tree_top, tree_height)
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)
    

# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.


def draw_sky(canvas, sky_x, sky_y, height):
    top_left_x = 0
    top_letf_y = 0
    bottom_right_x = 1400
    bottom_right_y = 400

    canvas.create_rectangle(top_left_x, top_letf_y,bottom_right_x, bottom_right_y,
     fill="#ACFFFB", outline="#ACFFFB")

def draw_land(canvas, land_x, land_y, height):
    top_left_x = 1400
    top_letf_y = 1400
    bottom_right_x = 0
    bottom_right_y = 400

    canvas.create_rectangle(top_left_x, top_letf_y,bottom_right_x, bottom_right_y,
     fill="#AA7B1C", outline="#AA7B1C")

def draw_cloud(canvas, cloud_x, cloud_y, height):     
    top_left_x = 150
    top_letf_y = 100
    bottom_right_x = 100
    bottom_right_y = 50
    for i in range(1,5):        
        canvas.create_oval(top_left_x*i, top_letf_y,bottom_right_x*i, bottom_right_y,
        fill="#FFFFFF", outline="#FFFFFF", )

def draw_sun(canvas, cloud_x, cloud_y, height):
    height = 2
    top_left_x = 50*height
    top_letf_y = 0*height
    bottom_right_x = 0*height
    bottom_right_y = 50*height       
    canvas.create_oval(top_left_x, top_letf_y,bottom_right_x, bottom_right_y,
        fill="#ffff00", outline="#ffff00",)

def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    height = 300
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")


# Call the main function so that
# this program will start executing.
main()