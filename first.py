from PIL import Image
import numpy as np
import glob
def main():
    dire = glob.glob('photos/*.jpg')
    file = len(dire)
    array = np.zeros([file, 200, 200, 3])
    a = [20, 200, 200, 3]
    s = 200, 200, 3
    for i in dire:
        image = Image.open(i)
        image.thumbnail(s)
        a.append(np.asarray(image))
    array = np.array(a)
    return array
if __name__ == "__main__":
    main()