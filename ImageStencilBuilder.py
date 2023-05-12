from PIL import Image, ImageDraw, ImageFilter, ImageChops

# 이미지 파일 경로

# 이미지 파일 경로
image_path = "./LOL.dds"

# 이미지 불러오기
image = Image.open(image_path)


# 이미지 크기 맞추기
background = Image.new('RGBA', image.size, (255, 255, 255, 0))
image = Image.alpha_composite(background, image)

# 배경 추출
background = Image.new('RGBA', image.size, (255, 255, 255, 0))
diff = ImageChops.difference(image, background)
diff = ImageChops.add(diff, diff, 1.0, -10)
bbox = diff.getbbox()
cropped = image.crop(bbox)

# 스텐실 효과 적용
stencil = Image.new('RGBA', cropped.size, (0,0, 0, 0))
draw = ImageDraw.Draw(stencil)
draw.bitmap((0, 0), cropped, fill=(0, 0, 0, 255))

# 두께 조절
thickness = 1
expanded_stencil = stencil.filter(ImageFilter.MaxFilter(thickness))


# 스텐실 이미지 저장
stencil_path = "./thumbnail_12.dds"
expanded_stencil.save(stencil_path)# 스텐실 이미지 저장
