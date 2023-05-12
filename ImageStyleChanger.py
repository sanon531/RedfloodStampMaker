import os
from PIL import Image, ImageEnhance,ImageOps,ImageDraw


folder_path = "./ProcessTarget"
end_path = "./ColorChanger"

def update_image(imagepath,outputpath,grayscale = False,
                 contrast_value = 2,
                 brightness_value =5,
                 LimitAlpha = 50,
                 Angle = 45
                 ):
    img = Image.open(imagepath)
    r_original, g_original, b_original, a_original = img.split()
    # Apply the intensity and contrast adjustments to the RGB channels
    r = ImageEnhance.Contrast(r_original).enhance(contrast_value)
    r = ImageEnhance.Brightness(r).enhance(brightness_value)
    g = ImageEnhance.Contrast(g_original).enhance(contrast_value)
    g = ImageEnhance.Brightness(g).enhance(brightness_value)
    b = ImageEnhance.Contrast(b_original).enhance(contrast_value)
    b = ImageEnhance.Brightness(b).enhance(brightness_value)

    # Merge the adjusted RGB channels with the alpha channel
    img = Image.merge('RGBA', (r, g, b, a_original))

    if grayscale:
        alpha_channel = img.getchannel('A')
        binary_mask = alpha_channel.point(lambda x: 255 if x == 255 else 0)
        # Convert the image to grayscale, using the binary mask as a transparency mask
        gray_img = ImageOps.colorize(img.convert('L'), (0, 0, 0), (255, 255, 255)).convert('RGBA')
        gray_img.putalpha(binary_mask)        #img = ImageOps.grayscale(img)
        gray_img.save(outputpath)

        new_size = tuple(2 * x for x in img.size)

        new_img = Image.new("RGBA", new_size, (0, 0, 0, 150))
        for x in range(1,new_img.width,2):
            for y in range(new_img.height):
                new_img.putpixel((x,y),(0, 0, 0, 0))
        new_img = new_img.rotate(Angle)

        top =new_img.height/4
        right = new_img.width/4

        new_img = new_img.crop(
            (top,right,top +img.width,right+img.height)
            )


        for x in range(img.width):
            for y in range(img.height):
                pixel = img.getpixel((x, y))
                if pixel[3] > LimitAlpha:
                    new_img.putpixel((x, y), (0, 0, 0, 255))
        outline_img = ImageOps.expand(new_img, border=0, fill='black')


        

        for x in range(gray_img.width):
            for y in range(gray_img.height):
                pixel = img.getpixel((x, y))
                if pixel[3] > LimitAlpha:
                    darkamount = pixel[0] +  pixel[1] + pixel[2]
                    darkamount = int(darkamount/3)
                    gray_img.putpixel((x, y), (darkamount, darkamount, darkamount, 255- darkamount))
                    outline_img.putpixel((x, y), (0,0, 0, 0))

        result = Image.alpha_composite(outline_img, gray_img)
        #Case Process
        #print(imagepath+ str(result.size))
        for x in range(result.width):
            for y in range(result.height):
                if x < 3 or x > result.width - 4 or y <3 or y > result.height - 4:
                    result.putpixel((x,y),(0, 0, 0, 255))
        for x in range(result.width):
            for y in range(result.height):
                if x < 2 or x > result.width - 3 or y <2 or y > result.height - 3:
                    result.putpixel((x,y),(0, 0, 0, 0))
        for x in range(result.width):
            for y in range(result.height):
                if x < 1 or x > result.width - 2 or y <1 or y > result.height - 2:
                    result.putpixel((x,y),(0, 0, 0, 255))
                


        result.save(outputpath)
    else : 
       # Save the result to the output file
        img.save(outputpath)



def changeAllContrast(contrast_value =2 ,brightness_value =5 , LimitAlpha = 50 ,Angle = 45 ):
    print(contrast_value)
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        endPos_path = os.path.join(end_path, filename)
        #print(endPos_path)
        update_image(file_path,endPos_path,True,
                     contrast_value,
                     brightness_value,
                     LimitAlpha,Angle)



if __name__ == "__main__":
    changeAllContrast()