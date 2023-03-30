# Bachelor Thesis Project: Conveyor Belt System for Detecting and Separating Rotten Fruits

This repository contains my Bachelor Thesis Project that is a conveyor belt system which detects and separates rotten fruits. The project combines machine learning and mechanical engineering to achieve the goal of reducing food waste in the food industry.

![ayırma_GIF](https://user-images.githubusercontent.com/30235603/226176543-379bc867-427a-4c6b-b0a1-29a4d3cd4589.gif)

---


## Project Overview

The conveyor belt system has been designed using SolidWorks, the 3D CAD file can be found in this repository (note: some parts may have been changed during assembly). 

![diagram2](https://user-images.githubusercontent.com/30235603/223701071-6989c414-ae76-4957-a02b-4e06693871e4.png)

![kod_sema](https://user-images.githubusercontent.com/30235603/224944748-073f1a72-653a-43da-9a02-7a37ad2fa11f.png)

The system uses a camera to stream real-time video of fruits passing along the conveyor belt, and the images are processed using PIL and OpenCV to predict the freshness of each fruit. 

![video1](https://user-images.githubusercontent.com/30235603/228786136-eb9a64d3-3fa2-4a53-9be3-8b00e11aa2a2.png)

The prediction model is based on the transfer learning model Xception, which has been trained using Keras. The model has achieved a validation loss of 0.00265. 

![080223_training](https://user-images.githubusercontent.com/30235603/223701159-20f56e72-95e7-40e7-ae83-e2f418dc7a78.png)

If a fruit is detected as rotten, the real-time database on Firebase is updated. A Raspberry Pi continuously receives the data from Firebase, and if the value of **run** is **True**, a DC motor is activated to separate the rotten fruit from the fresh ones. The numbers of rotten and fresh fruits are updated in the database.

![ayırıcı_calisma2_GIF](https://user-images.githubusercontent.com/30235603/226176967-bdaad217-e239-4430-9b2c-6deebef02e65.gif)

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
##### References for Images

- https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.hepsiburada.com%2Flogitech-c270-hd-webcam-siyah-yurt-disindan-pm-HB00000ZLWW6&psig=AOvVaw3RqI_vVYIZtqtnjdY2f21f&ust=1678360442074000&source=images&cd=vfe&ved=0CA0QjRxqFwoTCOivp4OazP0CFQAAAAAdAAAAABAD


- https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.hepsiburada.com%2Fraspberry-pi-3-model-a-plus-pm-HB00000JOQS2&psig=AOvVaw16oEavhjv1xmmSdUxghypp&ust=1678360397440000&source=images&cd=vfe&ved=0CA0QjRxqFwoTCOj2--2ZzP0CFQAAAAAdAAAAABAD


- https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.hepsiburada.com%2Farduino-l298n-motor-surucu-shield-dc-motor-surucu-raspberry-pm-HB000004VA3M&psig=AOvVaw2stJIWVqzC-hdsLLb0AJXn&ust=1678360480255000&source=images&cd=vfe&ved=0CA0QjRxqFwoTCIjgkpaazP0CFQAAAAAdAAAAABAD

- https://www.voltreduktor.com.tr/images/series/e-serisi/e-serisi-1.jpg

- https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.robotzade.com%2F12V-L-Reduktorlu-300-Rpm-DC-Motor%2CPR-1717.html&psig=AOvVaw3BLPaeFv2XdZ4-SIPNnBox&ust=1678360587833000&source=images&cd=vfe&ved=0CA0QjRxqFwoTCMC24siazP0CFQAAAAAdAAAAABAD

- https://www.cnc-marketi.com/Images/Urun/484cqh5v3af4d0.jpeg

- https://www.cnc-marketi.com/Images/Urun/14092020161638.png

- https://www.cnc-marketi.com/Images/Urun/14082020142829.jpeg

- https://www.cnc-marketi.com/Images/Urun/020ie5400ambag.jpeg
- https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.n11.com%2Furun%2F6203-2rs-sabit-rulman-17x40x12-528179233-30764673%3Fmagaza%3Dhasrulmanmakina&psig=AOvVaw2mOrH_MOwLdXYl8yk7oeo5&ust=1679160883162000&source=images&cd=vfe&ved=0CA0QjRxqFwoTCKj8p_K_4_0CFQAAAAAdAAAAABAD