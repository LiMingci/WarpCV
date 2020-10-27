import sys
sys.path.append("../build_wsl")
import nld
import cv2


def test_nld():
    img_path = './pic2.png'
    img = cv2.imread(img_path)
    adf = nld.nld_CcADF()
    img_filted = adf.AnisotropicDiffusionFilter(img)
    cv2.imwrite('./pic2_filted.png', img_filted[1])


if __name__ == '__main__':
    test_nld()