# Install apt updates
sudo apt-get update -y

# Install necessary image I/O packages
sudo apt-get install -y libjpeg-dev libpng-dev libtiff-dev

# Install GTK development library
sudo apt-get install -y libgtk-3-dev

# Install necessary video I/O packages
sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev
sudo apt-get install -y libxvidcore-dev libx264-dev

# Install necessary optimization packages
sudo apt-get install -y libatlas-base-dev gfortran

# Install OpenCV and Python bindings
sudo apt-get install -y libopencv-dev python3-opencv

# Verify OpenCV installation
python -c "import cv2; print(cv2.__version__)"

# Print to the terminal
echo "OpenCV is now installed with Python bindings."
echo "Note that the OpenCV library installed from the Ubuntu repositories is not optimized."
echo "Building the OpenCV library from the source allows you to have the latest available version." 
echo "It will be optimized for your particular system, and you will have complete control over the build options."
echo "So, building from source is the recommended way of installing OpenCV."