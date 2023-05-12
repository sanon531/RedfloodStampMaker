import tkinter as tk 
from tkinter import *
from ColorChanger import changeAllColorByname
from ImageStyleChanger import changeAllContrast

# 윈도우 생성

currentSelectedColor ="Army"
def NavyChanger():
    currentSelectedColor ="Navy"
    label.config(text=currentSelectedColor)
    changeAllColorByname("Navy")

def ArmyChanger():
    currentSelectedColor ="Army"
    label.config(text=currentSelectedColor)
    changeAllColorByname("Army")
    

def AirChanger():
    currentSelectedColor ="Air"
    label.config(text=currentSelectedColor)
    changeAllColorByname("Air")
   


def CallProcess():
    changeAllContrast(ContrastSlider.get(), 
                      BrightnessSlider.get(),
                      alphaSlider.get(),
                      angleSlider.get())


if __name__ == "__main__":
    global saved_Contrast
    global saved_Brightness
    window = tk.Tk()
    window.title("Select Panel")


    window.geometry("500x500")
    # 윈도우 생성
    # 버튼 생성


    contrast_value = tk.DoubleVar(value=3.0)
    ContrastSlider = tk.Scale(window, from_=0.0, to=10.0,resolution=0.1, variable=contrast_value,orient=HORIZONTAL)
    ContrastLabel = tk.Label(window, text="contrast =")
    ContrastLabel.pack()
    ContrastSlider.pack()

    brightness_value = tk.DoubleVar(value=3.0)

    BrightnessSlider = tk.Scale(window, from_=0.0, to=10.0,resolution=0.1, variable=brightness_value,orient=HORIZONTAL)
    BrightnessLabel = tk.Label(window, text="brightness =")
    BrightnessLabel.pack()
    BrightnessSlider.pack()

    alpha_value = tk.DoubleVar(value=50)

    alphaSlider = tk.Scale(window, from_=0.0, to=255,resolution=1, variable=alpha_value,orient=HORIZONTAL)
    alphaLabel = tk.Label(window, text="alpha =")
    alphaLabel.pack()
    alphaSlider.pack()

    angle_value = tk.DoubleVar(value=45)

    angleSlider = tk.Scale(window, from_=0.0, to=180,resolution=1, variable=angle_value,orient=HORIZONTAL)
    angleLabel = tk.Label(window, text="stripe angle =")
    angleLabel.pack()
    angleSlider.pack()

    btn0 = tk.Button(window, text="Start Generate", command= lambda:CallProcess())
    btn0.pack(anchor="center")

    label = tk.Label(window, text=currentSelectedColor)
    btn1 = tk.Button(window, text="Navy", command = lambda: NavyChanger())
    btn2 = tk.Button(window, text="Army", command= lambda:ArmyChanger())
    btn3 = tk.Button(window, text="Air", command= lambda:AirChanger())

    btn1.pack(anchor="center")
    btn2.pack(anchor="center")
    btn3.pack(anchor="center")
    label.pack()


    # 윈도우 실행
    window.mainloop()