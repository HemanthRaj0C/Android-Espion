import customtkinter
from tkinter import filedialog,ttk
import threading
import subprocess
from tkinter import StringVar
import os
import random

class ConnectApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.backgrounds = [

"""
 █████╗ ███╗   ██╗██████╗ ██████╗  ██████╗ ██╗██████╗     ███████╗███████╗██████╗ ██╗ ██████╗ ███╗   ██╗
██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔═══██╗██║██╔══██╗    ██╔════╝██╔════╝██╔══██╗██║██╔═══██╗████╗  ██║
███████║██╔██╗ ██║██║  ██║██████╔╝██║   ██║██║██║  ██║    █████╗  ███████╗██████╔╝██║██║   ██║██╔██╗ ██║
██╔══██║██║╚██╗██║██║  ██║██╔══██╗██║   ██║██║██║  ██║    ██╔══╝  ╚════██║██╔═══╝ ██║██║   ██║██║╚██╗██║
██║  ██║██║ ╚████║██████╔╝██║  ██║╚██████╔╝██║██████╔╝    ███████╗███████║██║     ██║╚██████╔╝██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═════╝     ╚══════╝╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                                                        
""",
"""
 $$$$$$\                  $$\                     $$\       $$\       $$$$$$$$\                     $$\                     
$$  __$$\                 $$ |                    \__|      $$ |      $$  _____|                    \__|                    
$$ /  $$ |$$$$$$$\   $$$$$$$ | $$$$$$\   $$$$$$\  $$\  $$$$$$$ |      $$ |       $$$$$$$\  $$$$$$\  $$\  $$$$$$\  $$$$$$$\  
$$$$$$$$ |$$  __$$\ $$  __$$ |$$  __$$\ $$  __$$\ $$ |$$  __$$ |      $$$$$\    $$  _____|$$  __$$\ $$ |$$  __$$\ $$  __$$\ 
$$  __$$ |$$ |  $$ |$$ /  $$ |$$ |  \__|$$ /  $$ |$$ |$$ /  $$ |      $$  __|   \$$$$$$\  $$ /  $$ |$$ |$$ /  $$ |$$ |  $$ |
$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |$$ |$$ |  $$ |      $$ |       \____$$\ $$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |
$$ |  $$ |$$ |  $$ |\$$$$$$$ |$$ |      \$$$$$$  |$$ |\$$$$$$$ |      $$$$$$$$\ $$$$$$$  |$$$$$$$  |$$ |\$$$$$$  |$$ |  $$ |
\__|  \__|\__|  \__| \_______|\__|       \______/ \__| \_______|      \________|\_______/ $$  ____/ \__| \______/ \__|  \__|
                                                                                          $$ |                              
                                                                                          $$ |                              
                                                                                          \__|                              
"""
            # Add other ASCII backgrounds if needed
        ]

        self.title("Android Espion")
        self.geometry("1280x720")

        customtkinter.set_default_color_theme("dark-blue")
        self.configure(fg_color="black")

        # Adjust font size for better visibility
        self.background_label = customtkinter.CTkLabel(self, text="", font=("Courier", 16), anchor="center")
        self.background_label.place(relx=0.5, rely=0.2, anchor="center")  # Place at the top

        self.set_random_background()

        self.main_frame = customtkinter.CTkFrame(self, fg_color="black")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")  # Center for main content

        self.status_bar = customtkinter.CTkFrame(self, height=30, fg_color="black")
        self.status_bar.place(relx=0, rely=0.95, relwidth=1, relheight=0.05)

        self.status_var = StringVar()
        self.status_var.set("Welcome to Android Espion")

        self.glow_label = customtkinter.CTkLabel(
            self.status_bar, 
            textvariable=self.status_var,
            text_color="#33FF33",
            font=("Tahoma", 20, "normal")
        )
        self.glow_label.place(relx=0.5, rely=0.5, anchor="center", x=1, y=1)

        self.status_label = customtkinter.CTkLabel(
            self.status_bar, 
            textvariable=self.status_var,
            text_color="#00FF00",
            font=("Tahoma", 20, "normal")
        )
        self.status_label.place(relx=0.5, rely=0.5, anchor="center")

        self.disconnect_button = customtkinter.CTkButton(
            self,
            text="Disconnect",
            command=self.disconnect,
            width=200,
            fg_color="red",
            hover_color="dark red"
        )
        self.disconnect_button.place(relx=0.5, rely=0.9, anchor="center")

        self.show_connect_page()

    def set_random_background(self):
        # Ensure that the choice is being made every time this method is called
        background_text = random.choice(self.backgrounds)
        self.background_label.configure(text=background_text)
        
        # Generate a random light color
        r = random.randint(150, 255)
        g = random.randint(150, 255)
        b = random.randint(150, 255)
        color = f"#{r:02x}{g:02x}{b:02x}"
        
        self.background_label.configure(text_color=color)

    def show_connect_page(self):
        # Clear existing widgets
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create a content frame with no padding and centered
        content_frame = customtkinter.CTkFrame(self.main_frame, fg_color="transparent", bg_color="transparent", corner_radius=15)
        content_frame.pack(expand=True, fill="both")

        # Center the title label in the content frame
        title_label = customtkinter.CTkLabel(content_frame, text="Connect to Device", font=("Helvetica", 24), bg_color="transparent", fg_color="transparent")
        title_label.pack(pady=(0, 50), anchor="center")

        # Center the input entry in the content frame
        self.input_entry = customtkinter.CTkEntry(content_frame, placeholder_text="Enter IP", width=300, corner_radius=10)
        self.input_entry.pack(pady=(0, 50), anchor="center")

        # Bind Enter key to connect action
        self.input_entry.bind("<Return>", lambda event: self.on_connect())

        # Center the connect button in the content frame
        self.connect_button = customtkinter.CTkButton(
            content_frame, 
            text="Connect", 
            command=self.on_connect, 
            width=200,
            fg_color="#1E90FF",  # Dodger Blue
            hover_color="#4169E1",  # Royal Blue
            text_color="white",
            text_color_disabled="gray",
            corner_radius=10
        )
        self.connect_button.pack(pady=(0, 10), anchor="center")

        # Center the status label in the content frame
        self.status_label = customtkinter.CTkLabel(content_frame, text="")
        self.status_label.pack(pady=10, anchor="center")

    def on_connect(self):

        #ACTUAL CONNECTION
        ip = self.input_entry.get()
        threading.Thread(target=self.connect, args=(ip,)).start()

        #TESTING PURPOSE
        #self.show_function_page()

    def connect(self, ip):
        self.status_label.configure(text="Connecting...")
        try:
            subprocess.run(["adb", "tcpip", "5555"], check=True, capture_output=True, text=True)
            if ip.count(".") == 3:
                subprocess.run(["adb", "kill-server"], check=True, capture_output=True, text=True)
                subprocess.run(["adb", "start-server"], check=True, capture_output=True, text=True)
                result = subprocess.run(["adb", "connect", f"{ip}:5555"], capture_output=True, text=True)
                if result.returncode == 0:
                    self.status_label.configure(text="Connected successfully")
                    self.after(2000, self.show_function_page)
                else:
                    self.status_label.configure(text=f"Connection failed: {result.stderr.strip()}")
            else:
                self.status_label.configure(text="Invalid IP")
        except subprocess.CalledProcessError as e:
            self.status_label.configure(text=f"Error: {e.stderr.strip()}")


    def show_function_page(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        button_frame = customtkinter.CTkFrame(self.main_frame, fg_color="transparent")
        button_frame.pack(padx=20, pady=20)

        title_label = customtkinter.CTkLabel(button_frame, text="Function Selection", font=("Helvetica", 24))
        title_label.grid(row=0, column=0, columnspan=4, pady=(0, 20))

        functions = ["List of Connected Devices","Device information", "Taking Screenshot", "Open App", "Uninstall App",
                    "Screen Mirror", "Push Image in Phone", "Select and Pull File", "Listen Audio","Open link"]
        
        for i, func_name in enumerate(functions):
            button = customtkinter.CTkButton(
                button_frame, 
                text=func_name, 
                command=lambda x=i: self.custom_function(x+2),
                width=200, 
                height=50,
                fg_color="#1E90FF",  # Dodger Blue
                hover_color="#4169E1",  # Royal Blue
                text_color="white",
                text_color_disabled="gray",
                corner_radius=10
            )
            if(i==8):
                button.grid(row=(i//4+1),column=1,padx=10,pady=10)
            elif i==9:
                button.grid(row=(i//4+1),column=2,padx=10,pady=10)
            else:
                button.grid(row=(i//4)+1, column=i%4, padx=10, pady=10)

        back_button = customtkinter.CTkButton(
            button_frame, 
            text="Back", 
            command=self.show_connect_page, 
            width=200,
            fg_color="#808080",  # Gray
            hover_color="#A9A9A9",  # Dark Gray
            text_color="white",
            text_color_disabled="gray"
        )
        back_button.grid(row=4, column=1, columnspan=2, pady=(20, 0))

        self.update()

    def custom_function(self, function_number):
        if function_number == 2:
            self.list_devices()
        elif function_number == 3:
            self.device_info()
        elif function_number == 4:
            self.screenShot()
        elif function_number == 5:
            self.open_app()
        elif function_number == 6:
            self.uninstall_app()
        elif function_number == 7:
            self.screen_copy()
        elif function_number == 8:
            self.open_image_on_phone()
        elif function_number == 9:
            self.pull_file()
        elif function_number == 10:
            self.listen_audio()
        elif function_number == 11:
            self.open_link()
        else:
            print(f"Function {function_number} called")

    def open_app(self):
        app_window = customtkinter.CTkToplevel(self)
        app_window.title("Open App")
        app_window.geometry("400x300")
        app_window.grab_set()
        app_window.focus_set()

        mode_var = customtkinter.StringVar(value="1")
        
        customtkinter.CTkRadioButton(app_window, text="Select app from list", variable=mode_var, value="1").pack(pady=10)
        customtkinter.CTkRadioButton(app_window, text="Enter Package name", variable=mode_var, value="2").pack(pady=10)

        package_entry = customtkinter.CTkEntry(app_window, placeholder_text="Enter Package name")
        package_entry.pack(pady=10)

        app_option_menu = customtkinter.CTkOptionMenu(app_window, values=[], dynamic_resizing=False)
        app_option_menu.set("Select an App")  # Set initial text
        app_option_menu.pack(pady=10)

        def load_apps():
            if mode_var.get() == "1":
                package_entry.pack_forget()
                app_option_menu.pack(pady=10)
                apps = subprocess.check_output(["adb", "shell", "pm", "list", "packages", "-3"]).decode().strip().split("\n")
                app_list = [app.replace("package:", "") for app in apps]
                app_option_menu.configure(values=app_list)
                app_option_menu.set("Select an App")  # Reset to default text after loading
            else:
                app_option_menu.pack_forget()
                package_entry.pack(pady=10)

        customtkinter.CTkButton(app_window, text="Load Apps", command=load_apps).pack(pady=10)

        def open_selected_app():
            if mode_var.get() == "1":
                app = app_option_menu.get().strip()
            else:
                app = package_entry.get()
            
            if app:
                result = subprocess.run(["adb", "shell", "monkey", "-p", app, "1"], capture_output=True, text=True)
                if result.returncode == 0:
                    self.update_status(f"Opened app: {app}")
                else:
                    self.update_status(f"Failed to open app: {result.stderr.strip()}")
            else:
                self.update_status("No app selected")
            app_window.destroy()

        customtkinter.CTkButton(app_window, text="Open App", command=open_selected_app).pack(pady=10)

        app_window.lift()
        app_window.attributes('-topmost', True)
        app_window.after_idle(app_window.attributes, '-topmost', False)

    def uninstall_app(self):
        app_window = customtkinter.CTkToplevel(self)
        app_window.title("Uninstall App")
        app_window.geometry("400x300")
        app_window.grab_set()
        app_window.focus_set()

        mode_var = customtkinter.StringVar(value="1")
        
        customtkinter.CTkRadioButton(app_window, text="Select app from list", variable=mode_var, value="1").pack(pady=10)
        customtkinter.CTkRadioButton(app_window, text="Enter Package name", variable=mode_var, value="2").pack(pady=10)

        package_entry = customtkinter.CTkEntry(app_window, placeholder_text="Enter Package name")
        package_entry.pack(pady=10)

        app_option_menu = customtkinter.CTkOptionMenu(app_window, values=[], dynamic_resizing=False)
        app_option_menu.set("Select an App")  # Set initial text
        app_option_menu.pack(pady=10)

        def load_apps():
            if mode_var.get() == "1":
                package_entry.pack_forget()
                app_option_menu.pack(pady=10)
                apps = subprocess.check_output(["adb", "shell", "pm", "list", "packages", "-3"]).decode().strip().split("\n")
                app_list = [app.replace("package:", "") for app in apps]
                app_option_menu.configure(values=app_list)
                app_option_menu.set("Select an App")  # Reset to default text after loading
            else:
                app_option_menu.pack_forget()
                package_entry.pack(pady=10)

        customtkinter.CTkButton(app_window, text="Load Apps", command=load_apps).pack(pady=10)

        def uninstall_selected_app():
            if mode_var.get() == "1":
                app = app_option_menu.get().strip()
            else:
                app = package_entry.get()
            
            if app and app != "Select an App":
                result = subprocess.run(["adb", "uninstall", app], capture_output=True, text=True)
                if result.returncode == 0:
                    self.update_status(f"Uninstalled app: {app}")
                else:
                    self.update_status(f"Failed to uninstall app: {result.stderr.strip()}")
            else:
                self.update_status("No app selected")
            app_window.destroy()

        customtkinter.CTkButton(app_window, text="Uninstall App", command=uninstall_selected_app).pack(pady=10)

        app_window.lift()
        app_window.attributes('-topmost', True)
        app_window.after_idle(app_window.attributes, '-topmost', False)

    def disconnect(self):
        try:
            result = subprocess.run(["adb", "disconnect"], capture_output=True, text=True)
            if result.returncode == 0:
                self.update_status("Disconnected successfully")
                self.show_connect_page()  # Go back to the connect page after disconnecting
            else:
                self.update_status(f"Disconnect failed: {result.stderr.strip()}")
        except subprocess.CalledProcessError as e:
            self.update_status(f"Error during disconnect: {e.stderr.strip()}")
    
    def list_devices(self):
        try:
            result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
            if result.returncode == 0:
                devices = result.stdout.strip().split('\n')[1:]
                if devices:
                    device_list = ", ".join(devices)
                    self.update_status(f"Connected devices: {device_list}")
                else:
                    self.update_status("No devices connected")
            else:
                self.update_status(f"Failed to list devices: {result.stderr.strip()}")
        except subprocess.CalledProcessError as e:
            self.update_status(f"Error listing devices: {e.stderr.strip()}")

    def screenShot(self):
        try:
            # Check if the directory exists, if not, create it
            if not os.path.exists('files'):
                os.makedirs('files')
            
            # Run adb commands to take screenshot and pull it to the local machine
            screencap_command = ["adb", "shell", "screencap", "-p", "/sdcard/screen.png"]
            pull_command = ["adb", "pull", "/sdcard/screen.png", "files/screen.png"]
            
            # Execute screencap command
            result = subprocess.run(screencap_command, capture_output=True, text=True)
            if result.returncode != 0:
                raise Exception(f"Failed to capture screenshot on device: {result.stderr}")
            
            # Execute pull command
            result = subprocess.run(pull_command, capture_output=True, text=True)
            if result.returncode != 0:
                raise Exception(f"Failed to pull screenshot: {result.stderr}")
            
            # Open the screenshot
            os.system("start files/screen.png")
            self.update_status("Screenshot taken and opened")
        except Exception as e:
            self.update_status(f"Error taking screenshot: {str(e)}")

    def update_status(self, message):
        self.status_var.set(message)
        self.update_idletasks()

    def screen_copy(self):
        screen_copy_window = customtkinter.CTkToplevel(self)
        screen_copy_window.title("Screen Copy Options")
        screen_copy_window.geometry("400x300")
        screen_copy_window.grab_set()
        screen_copy_window.focus_set()

        option_var = customtkinter.StringVar(value="1")
        
        customtkinter.CTkRadioButton(screen_copy_window, text="Normal screen mirror", variable=option_var, value="1").pack(pady=10)
        customtkinter.CTkRadioButton(screen_copy_window, text="Low resolution mirror", variable=option_var, value="2").pack(pady=10)

        def execute_screen_copy():
            option = option_var.get()
            if option == "1":
                command = "scrcpy"
            elif option == "2":
                command = "scrcpy -m 1024 -b 1M"
            
            try:
                subprocess.Popen(command, shell=True)
                self.update_status(f"Executing screen copy with option {option}")
            except Exception as e:
                self.update_status(f"Error executing screen copy: {str(e)}")
            
            screen_copy_window.destroy()

        customtkinter.CTkButton(screen_copy_window, text="Start Screen Copy", command=execute_screen_copy).pack(pady=20)

        screen_copy_window.lift()
        screen_copy_window.attributes('-topmost', True)
        screen_copy_window.after_idle(screen_copy_window.attributes, '-topmost', False)
    
    def open_image_on_phone(self):
        screen_photo_window = customtkinter.CTkToplevel(self)
        screen_photo_window.title("Open Photo on Device")
        screen_photo_window.geometry("400x250")
        screen_photo_window.configure(fg_color="black")
        screen_photo_window.grab_set()
        screen_photo_window.focus_set()

        title_label = customtkinter.CTkLabel(screen_photo_window, text="Select Photo to Open on Device", 
                                             font=("Helvetica", 18, "bold"), text_color="#00FF00")
        title_label.pack(pady=(20, 30))

        self.file_path_var = customtkinter.StringVar()
        file_path_entry = customtkinter.CTkEntry(screen_photo_window, textvariable=self.file_path_var, width=300)
        file_path_entry.pack(pady=10)

        def browse_file():
            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
            if file_path:
                self.file_path_var.set(file_path)

        browse_button = customtkinter.CTkButton(
            screen_photo_window,
            text="Browse",
            command=browse_file,
            fg_color="#1E90FF",
            hover_color="#4169E1",
            text_color="white",
            corner_radius=10
        )
        browse_button.pack(pady=10)

        def push_and_open_photo():
            location = self.file_path_var.get().strip()
            if not location:
                self.update_status("No file selected")
                return

            if not os.path.isfile(location):
                self.update_status("Selected file does not exist")
                return

            try:
                # Push file to device
                result = subprocess.run(["adb", "push", location, "/sdcard/"], capture_output=True, text=True)
                if result.returncode != 0:
                    raise Exception(f"Failed to push file: {result.stderr}")

                # Get filename
                file_name = os.path.basename(location)

                # Open file on device
                result = subprocess.run([
                    "adb", "shell", "am", "start", 
                    "-a", "android.intent.action.VIEW", 
                    "-d", f"file:///sdcard/{file_name}", 
                    "-t", "image/*"
                ], capture_output=True, text=True)
                
                if result.returncode != 0:
                    raise Exception(f"Failed to open file: {result.stderr}")

                self.update_status(f"Opened photo: {file_name}")
                screen_photo_window.destroy()
            
            except Exception as e:
                self.update_status(f"Error: {str(e)}")

        open_button = customtkinter.CTkButton(
            screen_photo_window,
            text="Open on Device",
            command=push_and_open_photo,
            fg_color="#1E90FF",
            hover_color="#4169E1",
            text_color="white",
            corner_radius=10
        )
        open_button.pack(pady=20)
    
    def pull_file(self):

        if not os.path.exists('files'):
                os.makedirs('files')

        self.selected_path = None
        self.current_directory = "/sdcard/"

        sdcard_window = customtkinter.CTkToplevel(self)
        sdcard_window.title("SD Card Contents")
        sdcard_window.geometry("800x600")
        sdcard_window.configure(fg_color="black")
        sdcard_window.grab_set()
        sdcard_window.focus_set()

        title_label = customtkinter.CTkLabel(sdcard_window, text="Select File or Folder from /sdcard/", 
                                            font=("Helvetica", 18, "bold"), text_color="#00FF00")
        title_label.pack(pady=(20, 10))

        # Create a frame for the treeview
        tree_frame = customtkinter.CTkFrame(sdcard_window, fg_color="black")
        tree_frame.pack(pady=10, padx=10, fill="both", expand=True)

        # Create Treeview
        self.tree = ttk.Treeview(tree_frame, show="tree")
        self.tree.pack(side="left", fill="both", expand=True)

        # Create scrollbar
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")

        self.tree.configure(yscrollcommand=scrollbar.set)

        # Configure treeview colors
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", 
                        background="black", 
                        foreground="white", 
                        fieldbackground="black")
        style.map('Treeview', background=[('selected', '#1E90FF')])

        def refresh_contents(path=None):
            if path is None:
                path = self.current_directory
            else:
                self.current_directory = path
            self.tree.delete(*self.tree.get_children())
            try:
                result = subprocess.run(["adb", "shell", "find", path, "-maxdepth", "1"], 
                                        capture_output=True, text=True, check=True)
                paths = result.stdout.strip().split('\n')
                for item_path in paths:
                    if item_path != path:
                        item_name = os.path.basename(item_path)
                        is_dir = subprocess.run(["adb", "shell", "test", "-d", item_path], capture_output=True).returncode == 0
                        parent = self.tree.insert("", "end", text=item_name, values=(item_path, "directory" if is_dir else "file"))
                        if is_dir:
                            # Add a dummy child to show the expand button
                            self.tree.insert(parent, "end")
            except subprocess.CalledProcessError as e:
                self.tree.insert("", "end", text=f"Error: {e.stderr}")

        def on_tree_expand(event):
            item = self.tree.focus()
            if self.tree.item(item, "values")[1] == "directory":
                children = self.tree.get_children(item)
                if len(children) == 1 and self.tree.item(children[0], "text") == "":
                    # Remove the dummy child
                    self.tree.delete(children[0])
                    # Populate the actual contents
                    path = self.tree.item(item, "values")[0]
                    try:
                        result = subprocess.run(["adb", "shell", "find", path, "-maxdepth", "1"], 
                                                capture_output=True, text=True, check=True)
                        subpaths = result.stdout.strip().split('\n')
                        for subpath in subpaths:
                            if subpath != path:
                                item_name = os.path.basename(subpath)
                                is_dir = subprocess.run(["adb", "shell", "test", "-d", subpath], capture_output=True).returncode == 0
                                child = self.tree.insert(item, "end", text=item_name, values=(subpath, "directory" if is_dir else "file"))
                                if is_dir:
                                    # Add a dummy child to show the expand button
                                    self.tree.insert(child, "end")
                    except subprocess.CalledProcessError as e:
                        self.tree.insert(item, "end", text=f"Error: {e.stderr}")

        def on_tree_double_click(event):
            item = self.tree.focus()
            if self.tree.item(item, "values")[1] == "directory":
                path = self.tree.item(item, "values")[0]
                refresh_contents(path)

        def select_item():
            try:
                selected_items = self.tree.selection()
                if selected_items:
                    selected_item = selected_items[0]
                    self.selected_path = self.tree.item(selected_item, "values")[0]
                    self.update_status(f"Selected path: {self.selected_path}")

                    pull_location = "files/"
                    pull_command = ["adb", "pull", self.selected_path, pull_location]

                    result = subprocess.run(pull_command,capture_output=True,text=True)
                    if result.returncode != 0:
                        raise Exception(f"Failed to Pull file from {self.selected_path}")
                    
                    sdcard_window.destroy()
                else:
                    self.update_status("No item selected")
            except Exception as e:
                self.update_status(f"Error taking screenshot: {str(e)}")

        refresh_button = customtkinter.CTkButton(
            sdcard_window,
            text="Refresh",
            command=lambda: refresh_contents(),
            fg_color="#1E90FF",
            hover_color="#4169E1",
            text_color="white",
            corner_radius=10
        )
        refresh_button.pack(side="left", padx=(5, 10), pady=10)

        select_button = customtkinter.CTkButton(
            sdcard_window,
            text="Select",
            command=select_item,
            fg_color="#1E90FF",
            hover_color="#4169E1",
            text_color="white",
            corner_radius=10
        )
        select_button.pack(side="left", padx=(5, 10), pady=10)

        # Bind events
        self.tree.bind("<<TreeviewOpen>>", on_tree_expand)
        self.tree.bind("<Double-1>", on_tree_double_click)

        # Initial content load
        refresh_contents()
    def listen_audio(self):
        self.audio_process = None
        audio_window = customtkinter.CTkToplevel(self)
        audio_window.title("Listen Audio")
        audio_window.geometry("400x350")
        audio_window.grab_set()
        audio_window.focus_set()

        title_label = customtkinter.CTkLabel(audio_window, text="Listen Audio", 
                                            font=("Helvetica", 18, "bold"), text_color="#00FF00")
        title_label.pack(pady=(20, 30))

        mode_var = customtkinter.StringVar(value="mic")

        mic_radio = customtkinter.CTkRadioButton(audio_window, text="Microphone Audio", 
                                                variable=mode_var, value="mic")
        mic_radio.pack(pady=10)

        device_radio = customtkinter.CTkRadioButton(audio_window, text="Device Audio", 
                                                    variable=mode_var, value="device")
        device_radio.pack(pady=10)

        status_label = customtkinter.CTkLabel(audio_window, text="", text_color="#FF0000")
        status_label.pack(pady=10)

        def start_audio_stream():
            mode = mode_var.get()
            try:
                result = subprocess.run(["adb", "shell", "getprop", "ro.build.version.release"], 
                                        capture_output=True, text=True, check=True)
                android_version = result.stdout.strip()
                android_os = int(android_version.split(".")[0])
                status_label.configure(text=f"Detected Android Version: {android_version}", text_color="#00FF00")

                if android_os < 11:
                    status_label.configure(text="This feature is only available for Android 11 or higher.", 
                                        text_color="#FF0000")
                    return

                command = ["scrcpy", "--no-video", "--no-window"]
                if mode == "mic":
                    command.append("--audio-source=mic")

                # Start the audio streaming
                self.audio_process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                status_label.configure(text=f"Streaming {mode} audio.", text_color="#00FF00")
                start_button.configure(state="disabled")
                stop_button.configure(state="normal")

            except subprocess.CalledProcessError as e:
                status_label.configure(text=f"Error: {e.stderr.strip()}", text_color="#FF0000")
            except ValueError:
                status_label.configure(text="No connected device found", text_color="#FF0000")

        def stop_audio_stream():
            if self.audio_process:
                self.audio_process.terminate()
                self.audio_process.wait()
                self.audio_process = None
            audio_window.destroy()  # Close the widget after stopping the stream

        start_button = customtkinter.CTkButton(
            audio_window,
            text="Start Audio Stream",
            command=start_audio_stream,
            fg_color="#1E90FF",
            hover_color="#4169E1",
            text_color="white",
            corner_radius=10
        )
        start_button.pack(pady=10)

        stop_button = customtkinter.CTkButton(
            audio_window,
            text="Stop Stream and Close",
            command=stop_audio_stream,
            fg_color="#FF4500",  # OrangeRed
            hover_color="#FF6347",  # Tomato
            text_color="white",
            corner_radius=10,
            state="disabled"  # Initially disabled
        )
        stop_button.pack(pady=10)

        def on_close():
            stop_audio_stream()

        audio_window.protocol("WM_DELETE_WINDOW", on_close) 
    
    def device_info(self):
        info_window = customtkinter.CTkToplevel(self)
        info_window.title("Device Information")
        info_window.geometry("500x600")
        info_window.minsize(500, 600)
        info_window.grab_set()
        info_window.focus_set()

        title_label = customtkinter.CTkLabel(info_window, text="Device Information", 
                                            font=("Helvetica", 18, "bold"), text_color="#00FF00")
        title_label.pack(pady=(20, 30))

        info_frame = customtkinter.CTkFrame(info_window)
        info_frame.pack(padx=20, pady=20, fill="both", expand=True)

        def get_prop(prop):
            result = subprocess.run(["adb", "shell", "getprop", prop], capture_output=True, text=True)
            return result.stdout.strip()

        info_data = [
            ("Model", "ro.product.model"),
            ("Manufacturer", "ro.product.manufacturer"),
            ("Chipset", "ro.product.board"),
            ("Android Version", "ro.build.version.release"),
            ("Security Patch", "ro.build.version.security_patch"),
            ("Device", "ro.product.vendor.device"),
            ("SIM", "gsm.sim.operator.alpha"),
            ("Encryption State", "ro.crypto.state"),
            ("Build Date", "ro.build.date"),
            ("SDK Version", "ro.build.version.sdk"),
        ]

        for i, (label, prop) in enumerate(info_data):
            label_widget = customtkinter.CTkLabel(info_frame, text=f"{label}:", anchor="w")
            label_widget.grid(row=i, column=0, sticky="w", padx=10, pady=5)
            
            value_widget = customtkinter.CTkLabel(info_frame, text=get_prop(prop), anchor="w")
            value_widget.grid(row=i, column=1, sticky="w", padx=10, pady=5)

        def refresh_info():
            for i, (_, prop) in enumerate(info_data):
                info_frame.grid_slaves(row=i, column=1)[0].configure(text=get_prop(prop))

        refresh_button = customtkinter.CTkButton(
            info_window,
            text="Refresh",
            command=refresh_info,
            fg_color="#1E90FF",
            hover_color="#4169E1",
            text_color="white",
            corner_radius=10
        )
        refresh_button.pack(pady=20)

        info_window.update_idletasks()
        info_window.geometry(f"{info_window.winfo_width()}x{info_window.winfo_height()}")

    def open_link(self):
        link_window = customtkinter.CTkToplevel(self)
        link_window.title("Open Link on Device")
        link_window.geometry("400x250")
        link_window.grab_set()
        link_window.focus_set()

        title_label = customtkinter.CTkLabel(link_window, text="Open Link on Device", 
                                            font=("Helvetica", 18, "bold"), text_color="#00FF00")
        title_label.pack(pady=(20, 30))

        url_entry = customtkinter.CTkEntry(link_window, width=300, placeholder_text="Enter URL (e.g., https://github.com)")
        url_entry.pack(pady=10)

        status_label = customtkinter.CTkLabel(link_window, text="", text_color="#FF0000")
        status_label.pack(pady=10)

        def open_url():
            url = url_entry.get().strip()
            if not url:
                status_label.configure(text="Error: URL cannot be empty", text_color="#FF0000")
                return
            
            try:
                result = subprocess.run([
                    "adb", "shell", "am", "start", 
                    "-a", "android.intent.action.VIEW", 
                    "-d", url
                ], capture_output=True, text=True, check=True)
                
                status_label.configure(text=f"Opened '{url}' on device", text_color="#00FF00")
                link_window.after(2000, link_window.destroy)  # Close window after 2 seconds
            except subprocess.CalledProcessError as e:
                status_label.configure(text=f"Error: {e.stderr.strip()}", text_color="#FF0000")

        open_button = customtkinter.CTkButton(
            link_window,
            text="Open Link",
            command=open_url,
            fg_color="#1E90FF",
            hover_color="#4169E1",
            text_color="white",
            corner_radius=10
        )
        open_button.pack(pady=20)

        # Bind Enter key to open_url function
        url_entry.bind("<Return>", lambda event: open_url())


if __name__ == "__main__":
    app = ConnectApp()
    app.mainloop()