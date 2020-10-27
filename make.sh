build_dir="build_wsl"
python gen2.py pycv ${build_dir} headers.txt && \
g++ -shared -rdynamic -g -O3 -Wall -fPIC -fopenmp \
cv.cpp  src/*.cpp src/*.cc src/*.c  \
-DMODULE_STR=cv_opti -DMODULE_PREFIX=pycv -DBUILD_DIR=${build_dir} \
-DNDEBUG -DPY_MAJOR_VERSION=3.8 \
`pkg-config --cflags --libs opencv`  \
`python3-config --includes --ldflags` \
-I . -I./include -I/home/limc/miniconda3/envs/py3sid/lib/python3.8/site-packages/numpy/core/include \
-o ${build_dir}/cv_opti.so 
