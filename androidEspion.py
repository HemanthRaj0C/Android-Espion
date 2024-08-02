import customtkinter
import cv2
from PIL import Image
from customtkinter import CTkImage
import threading
import subprocess
from tkinter import StringVar

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
            text_color="#33FF33",  # Lighter green for the glow
            font=("Tahoma", 20, "normal")
        )
        self.glow_label.place(relx=0.5, rely=0.5, anchor="center", x=1, y=1)

        self.status_label = customtkinter.CTkLabel(
            self.status_bar, 
            textvariable=self.status_var,
            text_color="#00FF00",  # Bright green
            font=("Tahoma", 20, "normal")
        )
        self.status_label.place(relx=0.5, rely=0.5, anchor="center")

        self.video_path = "bgvid.mp4"  # Replace with your video file path
        self.play_video()

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

        self.connect_button = customtkinter.CTkButton(content_frame, text="Connect", command=self.on_connect, width=200)
        self.connect_button.pack(pady=10)

        self.status_label = customtkinter.CTkLabel(content_frame, text="")
        self.status_label.pack(pady=10)

    def on_connect(self):
        ip = self.input_entry.get()
        threading.Thread(target=self.connect, args=(ip,)).start()

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

        functions = ["Disconnect","Function 2", "Function 3", "Function 4",
                     "Function 5", "Function 6", "Function 7", "Function 8"]

        for i, func_name in enumerate(functions):
            button = customtkinter.CTkButton(button_frame, text=func_name, 
                                             command=lambda x=i: self.custom_function(x+1),
                                             width=200, height=50)
            button.grid(row=(i//4)+1, column=i%4, padx=10, pady=10)

        back_button = customtkinter.CTkButton(button_frame, text="Back", command=self.show_connect_page, width=200)
        back_button.grid(row=3, column=1, columnspan=2, pady=(20, 0))

    def custom_function(self, function_number):
        if function_number == 1:
            self.disconnect()
            self.status_label.configure(text="Disconnected")
        elif function_number == 2:
            self.list_devices()
        else:
            print(f"Function {function_number} called")

    def disconnect(self):
        try:
            result = subprocess.run(["adb", "disconnect"], capture_output=True, text=True)
            if result.returncode == 0:
                self.update_status("Disconnected successfully")
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

    def update_status(self, message):
        self.status_var.set(message)
        self.update_idletasks()
            
    

if __name__ == "__main__":
    app = ConnectApp()
    app.mainloop()