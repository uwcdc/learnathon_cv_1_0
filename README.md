# Learnathon: Computer Vision 1.0 + OpenCV

## Topics
### Loading, displaying, and saving images
### Image Basics
### Image Processing

# Installation Guide

I'm going to assume that we all have XCode and Homebrew installed. So, we will start Step 6 of the installation process.

Step 6: Compiling OpenCV from source is needed to use the latest OpenCV code or and to activate certain features (such as patented algorithms). Using pip, brew, or apt to install OpenCV is not recommended.

```
cd ~
$ wget -O opencv.zip https://github.com/opencv/opencv/archive/4.5.1.zip
$ wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.5.1.zip
```

Then unpack the archives:

```
$ unzip opencv.zip
$ unzip opencv_contrib.zip
```

I also like to rename the directories and I highly recommend you do so:

```
$ mv opencv-4.5.1 opencv
$ mv opencv_contrib-4.5.1 opencv_contrib
```

Followed by configuring the build with CMake (it is very important that you copy the CMake command exactly as it appears here, taking care to copy and past the entire command.

```
$ cd ~/opencv
$ mkdir build
$ cd build
$ workon gurus
$ cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
    -D PYTHON3_LIBRARY=`python -c 'import subprocess ; import sys ; s = subprocess.check_output("python-config --configdir", shell=True).decode("utf-8").strip() ; (M, m) = sys.version_info[:2] ; print("{}/libpython{}.{}.dylib".format(s, M, m))'` \
    -D PYTHON3_INCLUDE_DIR=`python -c 'import distutils.sysconfig as s; print(s.get_python_inc())'` \
    -D PYTHON3_EXECUTABLE=$VIRTUAL_ENV/bin/python \
    -D BUILD_opencv_python2=OFF \
    -D BUILD_opencv_python3=ON \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D INSTALL_C_EXAMPLES=OFF \
    -D OPENCV_ENABLE_NONFREE=ON \
    -D BUILD_EXAMPLES=ON ..
```

Then we’re ready to perform the compilation of OpenCV:

```
$ make -j8
```

*Note:* The number ‘8’ above specifies that we have 8 cores/processors for compiling. If you have a different number of processors you can update the -j  switch. For only one core/processor simply just use the make  command (from the build directory enter make clean  prior to retrying if your build failed or got stuck).

From there you can install OpenCV:

```
$ sudo make install
```

