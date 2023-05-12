import os
from PIL import Image, ImageEnhance,ImageOps


folder_path = "./ColorChanger"
Endfolder_path = "./ColorChangerOutPut"


def changeAllColor(color):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        outputpath = os.path.join(Endfolder_path, filename)
        img = Image.open(file_path)
        new_img = Image.new("RGBA", img.size, (0, 0, 0, 0))
        for x in range(img.width):
            for y in range(img.height):
                pixel = img.getpixel((x, y))
                new_img.putpixel((x, y), (color[0], color[1], color[2], pixel[3]))
        
        new_img.save(outputpath)

   
def changeAllColorByname(name):
    print(name)
    if(name == "Navy"):
        changeAllColor([0,74,161])
    elif(name == "Air"):
        changeAllColor([138, 35, 37])
    elif(name == "Army"):
        changeAllColor([ 84 , 143, 0 ])

