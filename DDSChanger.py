import os
import shutil
from PIL import Image

Endfolder_path = "./ProcessEnd"

DDSfolder_path = "./DDSOriginal"
DDSfolderResult_path = "./ProcessTarget"

def CallDDSToPng():
    for filename in os.listdir(DDSfolder_path):
        if filename.endswith(".dds"):
            file_path = os.path.join(DDSfolder_path, filename)
            end_path = os.path.join(DDSfolderResult_path, filename)
            with Image.open(file_path) as im:
                im.save(end_path.replace(".dds", ".png"))


def CallPngToDDS():

    for filename in os.listdir(Endfolder_path):
        if filename.endswith(".png"):
            # 파일 경로
            file_path = os.path.join(Endfolder_path, filename)
            # PIL 라이브러리를 사용하여 이미지 열기
            with Image.open(file_path) as im:
                # 이미지를 png 로 저장하고 기존 dds 파일 삭제
                im.save(file_path.replace(".png", ".dds"))
                os.remove(file_path)


if __name__ == "__main__":
    CallDDSToPng()