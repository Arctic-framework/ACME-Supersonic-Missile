import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk
import colorama
print( colorama.Fore.RED + """:@:                                                                                              .@-
.#@+.                                                                                          .+@#.
 :@@@.                                                                                        .%@@: 
 .*@@@=.                                                                                    .-@@@*. 
  .@@@@%.                                                                                  .#@@@@:  
  .+@@@@@-                                                                                :@@@@@*.  
   .@@@@@@%.                                                                            .#@@@@@@.   
   .=@@@@@@@.                                                                          .@@@@@@@=.   
    .@@@@@@@@+.                                                                      .=@@@@@@@@.    
    .-@@@@@@@@@.                                                                    .%@@@@@@@@=.    
     .#@@@@@@@@@-.                                                                 :@@@@@@@@@%.     
      :@@@@@@@@@@@.                                                              .#@@@@@@@@@@:      
      .*@@@@@@@@@@@:.                                                           .@@@@@@@@@@@#.      
       .@@@@@@@@@@@@*.                                                        .=@@@@@@@@@@@@:       
       .-@@@@@@@@@@@@@.  .. .. .:=+*#%@@@@@@#+-.     .+#%@@@@@%#*+=-.... ..  .@@@@@@@@@@@@@+.       
        .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.   +@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.        
         :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-.       .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-.        
         .*@@@@ROBOTICS@@@@@@@@@@@@@@@@@@%..            ..*@@@@@@@@@@@@@@@@VEX@@@@@@@@@@@%.         
          .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.                  .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@.          
          .-@@@@@@@@@@@@@@@@@@@@@@@@@@%.                     *@@@@@@@@@@@@@@@@@@@@@@@@@@=.          
           .@@@@@@@@@@@@@@@@@@@@.......                       ......#@@@@@@@@@@@@@@@@@@@.           
            .@@@@@@@@@@@@@@@@@@@=                                  :@@@@@@@@@@@@@@@@@@@:.           
            .=@@@@@@@@@@@@@@@@@@@                                 .#@@@@@@@@@@@@@@@@@@+.            
             .@@@@@@@@@@@@@@@@@@@*.                               =@@@@@@@@@@@@@@@@@@@.             
              .@@@@@@@@@@@@@@@@@@@.                               @@@@@@@@@@@@@@@@@@@:.             
              .:@@@@@@@@@@@@@@@@@@#.                             +@@@@@@@@@@@@@@@@@@=.              
               .*@@@@@ARCTIX@@@@@@@=                            .@@@@@@@@2023@@@@@@%.               
                .@@@@@@@@@@@@@@@@@@@.                          .*@@@@@@@@@@@@@@@@@@.                
                 .@@@@@@@@@@@@@@@@@@+                          :@@@@@@@@@@@@@@@@@@.                 
                  .%@@@@@@@@@@@@@@@@*.                         +@@@@@@@@@@@@@@@@@.                  
                   -@@@@@@@@@@@@@@@@@.                        .*@@@@@@@@@@@@@@@@*                   
                   .@@@@@@@@@@@@@@@@@.                        .%@@@@@@@@@@@@@@@@-                   
                   .@@@@@@@@@@@@@@@@@=                        .@@@@@@@@@@@@@@@@@.                   
                   .@@@@@@@@@@@@@@@@@*.                       +@@@@@@@@@@@@@@@@@.                   
                   .%@@@@@@MIT@@@@@@@@                       .*@@@@@@@LICENSE@@@.                   
                    -@@@@@@@@@@@@@@@@@-                       @@@@@@@@@@@@@@@@@#                    
                    .@@@@@@@@@@@@@@@@@#.                     +@@@@@@@@@@@@@@@@@:                    
                    .%@@@@@@@@@@@@@@@@@                     .#@@@@@@@@@@@@@@@@@.                    
                    .#@@@@@@@@@@@@@@@@@*                    .@@@@@@@@@@@@@@@@@%.                    
                     :@@@@@@@@@@@@@@@@@%.                   *@@@@@@@@@@@@@@@@@-                     
                     .@@@@@@@@@@@@@@@@@@-                   @@@@@@@@@@@@@@@@@@.                     
                     .*@@@@@@@@@@@@@@@@@%.                 *@@@@@@@@@@@@@@@@@%.                     
                      .%@@@@@@@@@@@@@@@@@:                .@@@@@@@@@@@@@@@@@@.                      
                       .%@@@@@@@FTC@@@@@@#.               *@@@@@@@@@@@@@@@@@.                       
                        .#@@@@@@@@@@@@@@@@.              .@@@@PYTHON@@@@@@%.                        
                          -@@@@@@@@@@@@@@@%.             *@@@@@@@@@@@@@@@*                          
                           .#@@@@@@@@@@@@@@:            .@@@@@@@@@@@@@@@.                           
                             :@@@@@@@@@@@@@%.           *@@@@@@@@@@@@@=                             
                              .-@@@@@@@@@@@@=          .@@@@@@@@@@@@*.                              
                                .+@@@@@@@@@@@.         %@@@@@@@@@@#.                                
                                  .*@@@@@@@@@#        .@@@@@@@@@%.                                  
                                    .*@@@@@@@@.      .%@@@@@@@@..                                   
                                      .#@@@@@@@.     -@@@@@@%:                                      
                                        .%@@@@@.    .@@@@@@:                                        
                                         ..@@@@@.   #@@@@-.                                         
                                           ..@@@*   BMK+.                                           
                                             .=@@ .@@@.                                             
                                               .@@.@-.    """)
print(colorama.Fore.CYAN + "Created by Arctic 2023 for FTC, at the price of a boba tea.")
print(colorama.Fore.CYAN + "Because coders will literally work for 10 hours to automate a task that takes 2 minutes..")


class WaypointApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Waypoint Mapper")
        self.root.configure(bg="white")
        self.style = ThemedStyle(root)
        self.style.set_theme("radiance")  # Choose a theme (e.g., "radiance")

        # Load field image and scale it to fit the canvas
        field_image = Image.open("CenterStage1.png")
        field_size = (800, 800)  # Set the canvas to be square
        self.field_image = ImageTk.PhotoImage(field_image.resize(field_size))

        # Initialize waypoint entry variables
        self.waypoint_label = tk.StringVar()
        self.waypoint_x = tk.DoubleVar()
        self.waypoint_y = tk.DoubleVar()
        self.waypoint_time = tk.DoubleVar()
        self.waypoint_speed = tk.DoubleVar()

        # Initialize edit waypoint variables
        self.edit_waypoint_label = tk.StringVar()
        self.edit_waypoint_x = tk.DoubleVar()
        self.edit_waypoint_y = tk.DoubleVar()
        self.edit_waypoint_time = tk.DoubleVar()
        self.edit_waypoint_speed = tk.DoubleVar()

        self.create_widgets()
        self.waypoints = []
        self.waypoint_counter = 1
        self.selected_waypoint = None
        self.canvas_markers = {}  # Dictionary to store canvas marker IDs
        self.lines = []

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding=10)
        frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        ttk.Button(self.root, text="Print JavaScript Waypoints", command=self.print_javascript_waypoints).grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        # Create a frame for the canvas
        canvas_frame = ttk.Frame(frame)
        canvas_frame.grid(row=0, column=1, rowspan=4, padx=20, pady=10, sticky="nsew")
        canvas_frame.columnconfigure(0, weight=1)
        canvas_frame.rowconfigure(0, weight=1)

        # Canvas for field image (square)
        canvas_size = 800
        self.canvas = tk.Canvas(canvas_frame, width=canvas_size, height=canvas_size, bd=0, highlightthickness=0)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.field_image)

        # Button to toggle Dark Mode
        dark_mode_button = ttk.Button(self.root, text="Toggle Dark Mode", command=self.toggle_dark_mode)
        dark_mode_button.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        # Waypoint Entry Fields
        entry_frame = ttk.Frame(frame)
        entry_frame.grid(row=0, column=0, rowspan=4, padx=10, pady=10, sticky="nsew")
        entry_frame.columnconfigure(1, weight=1)

        # Waypoint List
        list_frame = ttk.Frame(self.root)
        list_frame.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")
        list_frame.columnconfigure(0, weight=1)
        list_frame.rowconfigure(0, weight=1)

        self.waypoint_list = ttk.Treeview(list_frame, columns=("Label", "X", "Y", "Time", "Speed"), show="headings")
        self.waypoint_list.heading("Label", text="Label")
        self.waypoint_list.heading("X", text="X")
        self.waypoint_list.heading("Y", text="Y")
        self.waypoint_list.heading("Time", text="Time")
        self.waypoint_list.heading("Speed", text="Speed")
        self.waypoint_list.grid(row=0, column=0, sticky="nsew")

        # Waypoint Edit Fields
        self.edit_frame = ttk.Frame(self.root, padding=10)
        self.edit_frame.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
        self.edit_frame.columnconfigure(1, weight=1)

        ttk.Label(self.edit_frame, text="Edit Waypoint").grid(row=0, column=0, sticky="w")

        edit_labels = ["Label:", "X:", "Y:", "Time to Wait:", "Speed of Movement:"]
        edit_variables = [self.edit_waypoint_label, self.edit_waypoint_x, self.edit_waypoint_y, self.edit_waypoint_time, self.edit_waypoint_speed]

        for i, label in enumerate(edit_labels):
            ttk.Label(self.edit_frame, text=label).grid(row=i+1, column=0, sticky="w")
            edit_variables[i] = tk.DoubleVar()
            ttk.Entry(self.edit_frame, textvariable=edit_variables[i]).grid(row=i+1, column=1, sticky="ew")

        ttk.Button(self.edit_frame, text="Update Waypoint", command=self.update_waypoint).grid(row=6, column=0, columnspan=2, sticky="ew")
        ttk.Button(self.edit_frame, text="Delete Waypoint", command=self.delete_waypoint).grid(row=7, column=0, columnspan=2, sticky="ew")

        # Button to clear waypoints
        ttk.Button(self.root, text="Clear Waypoints", command=self.clear_waypoints).grid(row=4, column=0, padx=20, pady=10, sticky="ew")

        # Button to print the waypoint data
        ttk.Button(self.root, text="Print Waypoints", command=self.print_waypoints).grid(row=5, column=0, padx=20, pady=10, sticky="ew")

        # Bind the canvas click event to add waypoints
        self.canvas.bind("<Button-1>", self.canvas_click)

    def toggle_dark_mode(self):
        current_theme = self.style.theme_use()
        if current_theme == "radiance":
            self.style.set_theme("elegance")  # Choose another theme (e.g., "elegance") for dark mode
        else:
            self.style.set_theme("radiance")  # Switch back to the default theme for light mode

    def print_javascript_waypoints(self):
        javascript_code = []
        for waypoint in self.waypoints:
            label, x, y, time, speed = waypoint
            javascript_code.append(f'waypoints.add(new Waypoint({x / 100.0}, {y / 100.0}, {speed}, {time}));')

        javascript_code = '\n'.join(javascript_code)

        print(javascript_code)

    def canvas_click(self, event):
        label = "Waypoint" + str(self.waypoint_counter)
        self.waypoint_counter += 1
        x_pixel = event.x
        y_pixel = event.y
        time = self.waypoint_time.get()
        speed = self.waypoint_speed.get()

        # Add waypoint to the list
        self.waypoints.append((label, x_pixel, y_pixel, time, speed))
        self.waypoint_list.insert('', 'end', values=(label, x_pixel, y_pixel, time, speed))

        # Draw a circle (marker) on the Canvas to represent the waypoint
        radius = 5
        marker_id = self.canvas.create_oval(x_pixel - radius, y_pixel - radius, x_pixel + radius, y_pixel + radius, fill='blue')
        self.canvas_markers[label] = marker_id  # Store the marker ID for this waypoint

        # Draw lines connecting waypoints
        if len(self.waypoints) >= 2:
            self.update_lines()

        # Change the color of waypoints
        if len(self.waypoints) == 1:
            self.canvas.itemconfig(self.canvas_markers[self.waypoints[0][0]], fill="green")
        elif len(self.waypoints) > 1:
            self.canvas.itemconfig(self.canvas_markers[self.waypoints[0][0]], fill="green")
            self.canvas.itemconfig(self.canvas_markers[self.waypoints[-1][0]], fill="red")

    def update_lines(self):
        # Remove existing lines
        for line_id in self.lines:
            self.canvas.delete(line_id)

        self.lines.clear()

        # Draw lines between consecutive waypoints
        for i in range(len(self.waypoints) - 1):
            x1, y1, _, _ = self.waypoints[i][1:]
            x2, y2, _, _ = self.waypoints[i + 1][1:]
            line_id = self.canvas.create_line(x1, y1, x2, y2, fill='blue', width=2)
            self.lines.append(line_id)

    def print_waypoints(self):
        for waypoint in self.waypoints:
            print("Label:", waypoint[0])
            print("X:", waypoint[1])
            print("Y:", waypoint[2])
            print("Time to Wait:", waypoint[3])
            print("Speed of Movement:", waypoint[4])
            print()

    def select_waypoint(self, event):
        item = self.waypoint_list.selection()[0]
        self.selected_waypoint = item
        label, x, y, time, speed = self.waypoint_list.item(item, 'values')
        self.edit_waypoint_label.set(label)
        self.edit_waypoint_x.set(x)
        self.edit_waypoint_y.set(y)
        self.edit_waypoint_time.set(time)
        self.edit_waypoint_speed.set(speed)

    def update_waypoint(self):
        if self.selected_waypoint:
            label = self.edit_waypoint_label.get()
            x = self.edit_waypoint_x.get()
            y = self.edit_waypoint_y.get()
            time = self.edit_waypoint_time.get()
            speed = self.edit_waypoint_speed.get()
            self.waypoint_list.item(self.selected_waypoint, values=(label, x, y, time, speed))
            for i, item in enumerate(self.waypoints):
                if item[0] == label:
                    self.waypoints[i] = (label, x, y, time, speed)

    def delete_waypoint(self):
        selected_items = self.waypoint_list.selection()
        if selected_items:
            for item in selected_items:
                label_to_delete = self.waypoint_list.item(item, 'values')[0]

                if label_to_delete in self.canvas_markers:
                    marker_id = self.canvas_markers[label_to_delete]
                    self.canvas.delete(marker_id)
                    self.canvas_markers.pop(label_to_delete)

                new_waypoints = [waypoint for waypoint in self.waypoints if waypoint[0] != label_to_delete]
                self.waypoints = new_waypoints
                self.waypoint_list.delete(item)

    def clear_waypoints(self):
        # Remove waypoints from the list and clear the waypoint list Treeview
        self.waypoints.clear()
        self.waypoint_list.delete(*self.waypoint_list.get_children())

        # Clear the canvas markers and waypoints
        for label, marker_id in self.canvas_markers.items():
            self.canvas.delete(marker_id)
        self.canvas_markers.clear()

if __name__ == "__main__":
    root = tk.Tk()
    app = WaypointApp(root)
    root.mainloop()
