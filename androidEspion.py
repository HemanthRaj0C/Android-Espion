import customtkinter
import cv2
from PIL import Image
from customtkinter import CTkImage
import threading
import subprocess
from tkinter import StringVar
import os

class GlowButton(customtkinter.CTkButton):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.configure(fg_color="#4682B4")  # Steel Blue
            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)

        def on_enter(self, e):
            self.configure(fg_color="#00BFFF")  # Deep Sky Blue (glowing effect)

        def on_leave(self, e):
            self.configure(fg_color="#4682B4")

class ConnectApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Android Espion")
        self.geometry("1920x1080")

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        self.video_label = customtkinter.CTkLabel(self, text="")
        self.video_label.place(x=0, y=0, relwidth=1, relheight=0.95)

        self.main_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.main_frame.place(relx=0.5, rely=0.45, anchor="center")

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

        self.video_path = "bgvid.mp4"  # Replace with your video file path
        self.play_video()

        self.disconnect_button = customtkinter.CTkButton(
            self,
            text="Disconnect",
            command=self.disconnect,
            width=200,
            fg_color="red",
            hover_color="dark red"
        )
        self.disconnect_button.place(relx=0.5, rely=0.9, anchor="center")

        self.disconnect_button = customtkinter.CTkButton(
            self,
            text="Disconnect",
            command=self.disconnect,
            width=200,
            fg_color="red",
            hover_color="#8B0000",  # Dark red for hover
            text_color="white",
            text_color_disabled="gray"
        )
        self.disconnect_button.place(relx=0.5, rely=0.9, anchor="center")

        self.show_connect_page()

    def play_video(self):
        def video_loop():
            cap = cv2.VideoCapture(self.video_path)
            while True:
                ret, frame = cap.read()
                if not ret:
                    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    continue
                frame = cv2.resize(frame, (1920, 1080))
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(cv2image)
                ctk_image = CTkImage(light_image=img, dark_image=img, size=(1920, 1080))
                self.video_label.configure(image=ctk_image)
                self.video_label.image = ctk_image

        threading.Thread(target=video_loop, daemon=True).start()

        threading.Thread(target=video_loop, daemon=True).start()

    def show_connect_page(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        content_frame = customtkinter.CTkFrame(self.main_frame, fg_color="transparent")
        content_frame.pack(padx=20, pady=20)

        title_label = customtkinter.CTkLabel(content_frame, text="Connect to Device", font=("Helvetica", 24))
        title_label.pack(pady=(0, 20))

        self.input_entry = customtkinter.CTkEntry(content_frame, placeholder_text="Enter IP", width=300)
        self.input_entry.pack(pady=10)

        self.input_entry.bind("<Return>", lambda event: self.on_connect())

        self.connect_button = customtkinter.CTkButton(
            content_frame, 
            text="Connect", 
            command=self.on_connect, 
            width=200,
            fg_color="#1E90FF",  # Dodger Blue
            hover_color="#4169E1",  # Royal Blue
            text_color="white",
            text_color_disabled="gray"
        )
        self.connect_button.pack(pady=10)

        self.status_label = customtkinter.CTkLabel(content_frame, text="")
        self.status_label.pack(pady=10)

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

        functions = ["Taking Screenshot", "List of Connected Devices", "Function 3", "Function 4",
                    "Function 5", "Function 6", "Function 7", "Function 8"]

        for i, func_name in enumerate(functions):
            button = GlowButton(
                button_frame, 
                text=func_name, 
                command=lambda x=i: self.custom_function(x+2),
                width=200, 
                height=50,
                text_color="white",
                text_color_disabled="gray"
            )
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
        back_button.grid(row=3, column=1, columnspan=2, pady=(20, 0))

        self.update()

    def custom_function(self, function_number):
        if function_number == 2:
            self.screenShot()
        elif function_number == 3:
            self.list_devices()
        else:
            print(f"Function {function_number} called")

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
            

if __name__ == "__main__":
    app = ConnectApp()
    app.mainloop()