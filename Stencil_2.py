from PIL import Image,ImageOps

# 이미지 파일 경로 설정

img_path = "./fra_basic_equipment.png"
# 이미지 열기
image = Image.open(img_path)

# 그레이스케일로 변환
image = image.convert("L")

# Threshold 기반으로 이미지의 Brightness 에 따라 해당 도구의 테두리 추출
image = image.point(lambda x: 255 * (x > 50))
image = image.convert("1")
image = ImageOps.invert(image)
image = image.convert("RGBA")


# 결과 이미지 저장
image.save("./result.png")