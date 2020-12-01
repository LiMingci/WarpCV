import sys
sys.path.append("./build_wsl")
sys.path.append("../build_wsl")
import numpy as np
import nld
import cv2
from cv2.ximgproc import anisotropicDiffusion
import time

def test_nld():
    img_path = './test/2018-03-28T00_00_00Z.tif'
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    # img = cv2.imread(img_path)
    t0 = time.time()
    adf = nld.nld_CcADF(nld.nld_CcADFConfig(ttime=1.5))
    img_filted = adf.AnisotropicDiffusionFilter(img)
    t1 = time.time()
    print('my nld: %.3f' % (t1 - t0))
    # cv2.imwrite('./my_modis_filted.png', img_filted[1])
    # t2 = time.time()
    # dst_img = np.zeros(img.shape, dtype=img.dtype)
    # anisotropicDiffusion(img, 1.0, 0.02, 10, dst_img)
    # t3 = time.time()
    # print('cv nld: %.3f' % (t3 - t2))
    # cv2.imwrite('./cv_modis_filted.png', dst_img)


if __name__ == '__main__':
    test_nld()