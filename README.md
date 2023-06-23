# pedestrian-detection
Computer Vision Project using YOLOv8 to detect and count the number of people in the livestream from Illinois Quad Cam and Alma Mater

## Setting up Environment

### Windows (WSL2)
1) Launch your instance of WSL2
2) [Install Mamba](https://mamba.readthedocs.io/en/latest/installation.html) and depending on whether you have Anaconda installed or not, there are two different sets of instructions. We are using mamba as it's much faster than conda at installing packages.
3) `git clone https://github.com/yaswant2403/pedestrian-detection`
4) Then open your **bash** terminal in the folder you cloned your repo in and run the following set of commands one by one
```
mamba env create -f environment.yml # creates the environment according to the yml file
mamba activate pedestrian-detection # activates environment so that the packages are usable in the code
```
5) In `backend/` run `extract_images.py` to download the video and extract the images into `data/video/frames/`.

   For development environment, don't let the `duration > 120`. 
6) Split your terminal (In VSCode) or open a new terminal and run `run_inference.py` to output the number of detections that standard `yolov8n.pt` runs. In the future, we will have our own model trained on a custom dataset.

### Mac
1) [Install Mamba](https://mamba.readthedocs.io/en/latest/installation.html) and depending on whether you have Anaconda installed or not, there are two different sets of instructions. We are using mamba as it's much faster than conda at installing packages.
2) `git clone https://github.com/yaswant2403/pedestrian-detection`
3) Then open a **bash** terminal (Mac may sometimes open zsh which we DONT want) in the folder you cloned your repo in and run the following set of commands one by one
```
mamba env create -f environment.yml # creates the environment according to the yml file
mamba activate pedestrian-detection # activates environment so that the packages are usable in the code
```
4-6) Same steps as [Windows](#windows-wsl2)
