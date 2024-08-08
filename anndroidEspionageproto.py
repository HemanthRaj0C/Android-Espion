import os
import platform

def connect():
    os.system("adb tcpip 5555")
    ip = input("Enter IP: ")
    while(ip==""):
        ip = input("Enter IP: ")
    if ip.count(".")==3:
        os.system("adb kill-server > docs/hidden.txt 2>&1&&adb start-server > docs/hidden.txt 2>&1")
        os.system("adb connect " + ip + ":5555")
    else:
        print("Invalid IP")

def disconnect():
    os.system("adb disconnect")

def screen_shot():
    os.system("adb shell screencap -p /sdcard/screen.png")
    os.system("adb pull /sdcard/screen.png files")
    os.system("start files/screen.png")

def get_device_info():
    model = os.popen(f"adb shell getprop ro.product.model").read()
    manufacturer = os.popen(f"adb shell getprop ro.product.manufacturer").read()
    chipset = os.popen(f"adb shell getprop ro.product.board").read()
    android = os.popen(f"adb shell getprop ro.build.version.release").read()
    security_patch = os.popen(
        f"adb shell getprop ro.build.version.security_patch"
    ).read()
    device = os.popen(f"adb shell getprop ro.product.vendor.device").read()
    sim = os.popen(f"adb shell getprop gsm.sim.operator.alpha").read()
    encryption_state = os.popen(f"adb shell getprop ro.crypto.state").read()
    build_date = os.popen(f"adb shell getprop ro.build.date").read()
    sdk_version = os.popen(f"adb shell getprop ro.build.version.sdk").read()
    wifi_interface = os.popen(f"adb shell getprop wifi.interface").read()

    print(
        f"""
    Model :{model}\
    Manufacturer :{manufacturer}\
    Chipset :{chipset}\
    Android Version :{android}\
    Security Patch : {security_patch}\
    Device : {device}\
    SIM : {sim}\
    Encryption State : {encryption_state}\
    Build Date : {build_date}\
    SDK Version : {sdk_version}\
"""
    )

def open_app():
    #mode
    print(f"""
    1)Select app from list
    2)Enter Package name
""")
    mode = input("Enter Mode:")
    if mode=="1":
        list = os.popen("adb shell pm list packages -3").read().split("\n")
        list.remove("")
        i=1
        for app in list:
            app = app.replace("package:","")
            print(f"{i}){app}")
            i+=1
        selection = input("Enter App Number: ")
        if selection.isdigit():
            if int(selection) < len(list) and int(selection) > 0:
                app = list[int(selection)-1].replace("package:","")
                print(app)
            else:
                print("Invalid Selection")
        else:
            print("Invalid Selection")
    elif mode=="2":
        app = input("Enter Package name:")
        if app == "":
            print("Package name empty")

    os.system(f"adb shell monkey -p {app} 1")

def uninstall_app():
    #mode
    print(f"""
    1)Select app from list
    2)Enter Package name
""")
    mode = input("Enter Mode:")
    if mode=="1":
        list = os.popen("adb shell pm list packages -3").read().split("\n")
        list.remove("")
        i=1
        for app in list:
            app = app.replace("package:","")
            print(f"{i}){app}")
            i+=1
        selection = input("Enter App Number: ")
        if selection.isdigit():
            if int(selection) < len(list) and int(selection) > 0:
                app = list[int(selection)-1].replace("package:","")
                print(app)
            else:
                print("Invalid Selection")
        else:
            print("Invalid Selection")
    elif mode=="2":
        app = input("Enter Package name:")
        if app == "":
            print("Package name empty")
    os.system(f"adb uninstall {app}")

def install_app():
    file_location = input(f"Enter APK path in computer: ")

    if file_location == "":
        print(f"Null Input Going back to Main Menu")
        return
    else:
        if file_location[len(file_location) - 1] == " ":
            file_location = file_location.removesuffix(" ")
        file_location = file_location.replace("'", "")
        file_location = file_location.replace('"', "")
        if not os.path.isfile(file_location):
            print(
                f"This file does not exist"
            )
            return
        else:
            file_location = "'" + file_location + "'"
            os.system("adb install " + file_location)

def open_photo():
    location = input("Enter the path of photo in computer: ")
    if(location==""):
        print("Empty location is not valid")
        return
    else:
        location = location.strip()
        location = location.replace("'","")
        location = location.replace('"',"")
        if not os.path.isfile(location):
            print(f"This file does not exist")
            return
        else:
            location = '"' + location + '"'
            os.system("adb push " + location + " /sdcard/")
        if platform.system()=="Windows":
            location = location.split("\\")
            file_name = location[len(location)-1]
        file_name = file_name.replace("'","")
        file_name = file_name.replace('"',"")
        file_name = "'" + file_name + "'"
        print(file_name)
        os.system(f'adb shell am start -a android.intent.action.VIEW -d "file:///sdcard/{file_name}" -t image/jpeg')



def mirror():
    os.system("scrcpy")

def listen_audio(mode):
    print(f"This feature is currently available for devices running on Android 11 or higher only.")
    try:
        androidVersion = os.popen("adb shell getprop ro.build.version.release").read()
        android_os = int(androidVersion.split(".")[0])
        print(f"Detected Android Version : {androidVersion}")
    except ValueError:
        print(f"No connected device found\nGoing back to Main Menu")
        return

    if android_os < 11:
        print(f"Going back to Main Menu")
        return

    match mode:
        case "mic":
            print(
                f"\nStreaming Microphone Audio \n\nPress Ctrl+C to Stop.\n"
            )
            os.system("scrcpy --no-video --audio-source=mic")

        case "device":
            print(
                f"\nStreaming Device Audio \n\nPress Ctrl+C to Stop.\n"
            )
            os.system("scrcpy --no-video")


# connect()
# screen_shot()
# get_device_info()
# open_app()
# uninstall_app()
# install_app()
# mirror()
# open_photo()
# listen_audio("mic")
# listen_audio("device")
# disconnect()
