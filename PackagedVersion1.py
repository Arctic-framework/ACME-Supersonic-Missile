import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk

class WaypointApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Waypoint Mapper")
        self.root.configure(bg="white")
        self.style = ThemedStyle(root)
        self.style.set_theme("radiance")

        self.selected_waypoint = None  # Initialize selected_waypoint


        self.canvas_markers = {}  # Initialize canvas_markers dictionary
        self.lines = []  # Initialize lines list

        # Initialize edit waypoint variables in the __init__ method
        self.edit_waypoint_label = tk.StringVar()
        self.edit_waypoint_x = tk.DoubleVar()
        self.edit_waypoint_y = tk.DoubleVar()
        self.edit_waypoint_time = tk.DoubleVar()
        self.edit_waypoint_speed = tk.DoubleVar()



        field_image = Image.open("CenterStage1.png")
        field_size = (800, 800)
        self.field_image = ImageTk.PhotoImage(field_image.resize(field_size))

        self.create_widgets()
        self.waypoints = []
        self.waypoint_counter = 1

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding=10)
        frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        ttk.Button(self.root, text="Print JavaScript Waypoints", command=self.print_javascript_waypoints).grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        canvas_frame = ttk.Frame(frame)
        canvas_frame.grid(row=0, column=1, rowspan=4, padx=20, pady=10, sticky="nsew")
        canvas_frame.columnconfigure(0, weight=1)
        canvas_frame.rowconfigure(0, weight=1)

        canvas_size = 800
        self.canvas = tk.Canvas(canvas_frame, width=canvas_size, height=canvas_size, bd=0, highlightthickness=0)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.canvas.create_image(0, canvas_size, anchor=tk.SW, image=self.field_image)

        entry_frame = ttk.Frame(frame)
        entry_frame.grid(row=0, column=0, rowspan=4, padx=10, pady=10, sticky="nsew")
        entry_frame.columnconfigure(1, weight=1)

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

        # Create edit variables and Entry widgets
        self.edit_waypoint_label = tk.StringVar()
        self.edit_waypoint_x = tk.DoubleVar()
        self.edit_waypoint_y = tk.DoubleVar()
        self.edit_waypoint_time = tk.DoubleVar()
        self.edit_waypoint_speed = tk.DoubleVar()

        edit_frame = ttk.Frame(self.root, padding=10)
        edit_frame.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")
        edit_frame.columnconfigure(1, weight=1)

        ttk.Label(edit_frame, text="Edit Waypoint").grid(row=0, column=0, sticky="w")

        edit_labels = ["Label:", "X:", "Y:", "Time to Wait:", "Speed of Movement:"]
        edit_variables = [self.edit_waypoint_label, self.edit_waypoint_x, self.edit_waypoint_y, self.edit_waypoint_time, self.edit_waypoint_speed]

        for i, label in enumerate(edit_labels):
            ttk.Label(edit_frame, text=label).grid(row=i+1, column=0, sticky="w")
            ttk.Entry(edit_frame, textvariable=edit_variables[i]).grid(row=i+1, column=1, sticky="ew")

        ttk.Button(edit_frame, text="Update Waypoint", command=self.update_waypoint).grid(row=6, column=0, columnspan=2, sticky="ew")
        ttk.Button(edit_frame, text="Delete Waypoint", command=self.delete_waypoint).grid(row=7, column=0, columnspan=2, sticky="ew")

        ttk.Button(self.root, text="Clear Waypoints", command=self.clear_waypoints).grid(row=4, column=0, padx=20, pady=10, sticky="ew")
        ttk.Button(self.root, text="Print Waypoints", command=self.print_waypoints).grid(row=5, column=0, padx=20, pady=10, sticky="ew")

        self.canvas.bind("<Button-1>", self.canvas_click)
        self.waypoint_list.bind("<<TreeviewSelect>>", self.select_waypoint)

    def print_javascript_waypoints(self):
        javascript_code = []
        for waypoint in self.waypoints:
            label, x, y, time, speed = waypoint
            adjusted_x = x * 12.0 / 800.0
            adjusted_y = 12.0 - (y * 12.0 / 800.0)
            javascript_code.append(f'waypoints.add(new Waypoint({adjusted_x}, {adjusted_y}, {speed}, {time}));')

        javascript_code = '\n'.join(javascript_code)
        print(javascript_code)

    def canvas_click(self, event):
        label = "Waypoint" + str(self.waypoint_counter)
        self.waypoint_counter += 1
        x_pixel = event.x
        y_pixel = event.y
        time = self.edit_waypoint_time.get()
        speed = self.edit_waypoint_speed.get()

        adjusted_x = x_pixel * 12.0 / 800.0
        adjusted_y = 12.0 - (y_pixel * 12.0 / 800.0)

        self.waypoints.append((label, adjusted_x, adjusted_y, time, speed))
        self.waypoint_list.insert('', 'end', values=(label, adjusted_x, adjusted_y, time, speed))

        radius = 5
        marker_id = self.canvas.create_oval(x_pixel - radius, y_pixel - radius, x_pixel + radius, y_pixel + radius, fill='blue')
        self.canvas_markers[label] = marker_id

        if len(self.waypoints) >= 2:
            self.update_lines()

        if len(self.waypoints) == 1:
            self.canvas.itemconfig(self.canvas_markers[self.waypoints[0][0]], fill="green")
        elif len(self.waypoints) > 1:
            self.canvas.itemconfig(self.canvas_markers[self.waypoints[0][0]], fill="green")
            self.canvas.itemconfig(self.canvas_markers[self.waypoints[-1][0]], fill="red")

        self.canvas.update()

    def update_lines(self):
        for line_id in self.lines:
            self.canvas.delete(line_id)
        self.lines.clear()

        for i in range(len(self.waypoints) - 1):
            x1, y1, _, _ = self.waypoints[i][1:]
            x2, y2, _, _ = self.waypoints[i + 1][1:]
            line_id = self.canvas.create_line(x1 * 800.0 / 12.0, (12.0 - y1) * 800.0 / 12.0, x2 * 800.0 / 12.0, (12.0 - y2) * 800.0 / 12.0, fill='blue', width=2)
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
        selected_items = self.waypoint_list.selection()
        if selected_items:
            item = selected_items[0]
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

            for i, item in enumerate(self.waypoints):
                if item[0] == label:
                    self.waypoints[i] = (label, x, y, time, speed)

            self.update_lines()

            self.waypoint_list.item(self.selected_waypoint, values=(label, x, y, time, speed))

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
        self.waypoints.clear()
        self.waypoint_list.delete(*self.waypoint_list.get_children())

        for label, marker_id in self.canvas_markers.items():
            self.canvas.delete(marker_id)
        self.canvas_markers.clear()

if __name__ == "__main__":
    root = tk.Tk()
    app = WaypointApp(root)
    root.mainloop()
