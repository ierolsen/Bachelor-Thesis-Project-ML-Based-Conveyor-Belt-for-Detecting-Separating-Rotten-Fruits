# Bachelor Thesis Project: Conveyor Belt System for Detecting and Separating Rotten Fruits

This repository contains my Bachelor Thesis Project that is a conveyor belt system which detects and separates rotten fruits. The project combines machine learning and mechanical engineering to achieve the goal of reducing food waste in the food industry.

![ayırma_GIF](https://user-images.githubusercontent.com/30235603/230324853-10c931fd-fa8d-4c3e-98fc-b0f8dcdc5053.gif)

---

## Youtube Video
By clicking the thumbnail below, you can watch the video on Youtube.


[![The Youtube Video](https://img.youtube.com/vi/ZrDW6tI3WWE/0.jpg)](https://www.youtube.com/watch?v=ZrDW6tI3WWE)


---


## Project Overview

The conveyor belt system has been designed using SolidWorks, the 3D CAD file can be found in this repository (note: some parts may have been changed during assembly). 

![diagram2](https://user-images.githubusercontent.com/30235603/228852685-ad6abfbf-e3f9-428e-a17f-191f734ae409.png)

![kod_sema](https://user-images.githubusercontent.com/30235603/224944748-073f1a72-653a-43da-9a02-7a37ad2fa11f.png)

The system uses a camera to stream real-time video of fruits passing along the conveyor belt, and the images are processed using PIL and OpenCV to predict the freshness of each fruit. 

![VIDEO_SCREEN_JPG](https://user-images.githubusercontent.com/30235603/229136131-212ed596-150b-465e-aed1-7e59a1a9490f.jpg)

The prediction model is based on the transfer learning model Xception, which has been trained using Keras. The model has achieved a validation loss of 0.00265. 

![080223_training](https://user-images.githubusercontent.com/30235603/223701159-20f56e72-95e7-40e7-ae83-e2f418dc7a78.png)

If a fruit is detected as rotten, the real-time database on Firebase is updated. A Raspberry Pi continuously receives the data from Firebase, and if the value of **run** is **True**, a DC motor is activated to separate the rotten fruit. The numbers of rotten and fresh fruits are updated in the database.

![motor_gif1](https://user-images.githubusercontent.com/30235603/229095354-ad442872-c121-404d-99ce-18c689bc62ff.gif)
![motor_gif2](https://user-images.githubusercontent.com/30235603/229095319-bd354e5b-b572-4b22-a6d2-02bb492aa5e3.gif)

Using Qt Designer, a GUI has been designed to display the numbers of fresh and rotten fruits, which continuously receives data from the Firebase database.

![GUI_](https://user-images.githubusercontent.com/30235603/228782598-69f1de6f-c0bf-4ec4-965e-3bd232ece34b.png)

---
## Dataset

The dataset used for this project can be found on Kaggle: 
https://www.kaggle.com/datasets/sriramr/fruits-fresh-and-rotten-for-classification

The dataset contains six classes: "rotten apple", "rotten banana", "rotten orange", "fresh apple", "fresh banana", and "fresh orange". Although the dataset only contains these specific fruits, the model is able to recognize other types of fruits, such as quince, outside of the dataset after combining all classes together as **rotten** and **fresh**.

---
## Requirements

The required libraries for this project are listed in the requirements.txt file. Please note that the file is only intended for Windows OS. 

For Raspberry Pi, the following libraries are required:

- rpi.gpio
- Pyrebase

>> **Please note** that Pyrebase only works on Python 3.6. It does not work on newer versions of Python.

## Installation

To install the required libraries for Windows OS, run the following command:

```sh
conda create -n env_name python=3.6
```

```sh
activate env_name
```

```sh
pip install -r requirements.txt
```


**NOTE**: 
In order to create the Database on Firabase, first create a python file named **firebase_secrets** inside of the **motor** folder. This created python file must contain the configuration keys that you can get on Firebase. Then the code will be ready to create a Database on Firebase.


## Running the Codes

Be sure that you have already installed the requirements into the environment that existed.

#### GUI:

```python
python app.py
```

#### Main Code:

```python
python run.py
```

#### Raspberry Pi

Be sure that you have already installed necessary libraries into Raspberry Pi too.

```python
python motor-run.py
```

---
## Materials Used

### Mechanical Parts

In the frame of the conveyor belt, I have chosen **Sigma Profile** for easy assembling.

- 5 Meters 30x30 Sigma Profile Slot:8 
- 2 Meters 30x60 Sigma Profile Slot:8
- 50 pieces Hidden Corner Bracket 30x30 Slot:8
- 35 pieces T Slot Nut M8 30x30 Slot:8
- 15 pieces T Slot Nut M6 30x30 Slot:8
- 4 pieces 6203 Bearing
- 2 Meters Belt

![mechanical parts](https://user-images.githubusercontent.com/30235603/225976599-8e1ccba0-856b-4e6b-bb6c-8f59dc454b23.png)

### Electrical Parts

- Logitech C270 HD WebCam
- DC-Motor
- Gear Motor (1405 rpm, 0,18kW)
- Raspberry Pi Model 3 A+
- L298N DC Motor Driver


![electrical  parts](https://user-images.githubusercontent.com/30235603/225976611-a2a22c86-7d11-4d70-8d59-859f07cc77e8.png)


---
## Conclusion

This project showcases my skills in machine learning, mechanical engineering, and GUI design, and has the potential to make a positive impact in the food industry by helping to reduce food waste.


---