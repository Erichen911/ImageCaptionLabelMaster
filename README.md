# Military Object detective system

![AppVeyor](https://img.shields.io/static/v1?label=version&message=0.3&color=brightgreen)
![AppVeyor](https://img.shields.io/static/v1?label=Developer&message=Erichen&color=orange)


This project includes annotation tools for **Image Caption** on mobile and PC. Developer **Erichen**, affiliated to **Pattern Recognition Laboratory, Tianjin University**.

## Introduction

With the development of remote sensing technology, people can observe our living environment more clearly from high altitude and space. Therefore, a series of research and exploration can be carried out using the acquired remote sensing images. Image Cation of remote sensing images is novel research.

Image Caption is a hot research direction in deep learning in recent years. The relationships between the image and the image description is mapping through training the neural network through marked data.

The process of obtaining the labels requires manual operation. The software in this project was developed to simplify the marking process.



* **Remote sensing data collection**: [Google Earth](https://www.google.com/earth/)
* **Development Language**: 
  
  1、PC application: PyQt5 

  2、Moblie application: Java(**front**), flask(**end**)
     
---

## PC application
The PC side marking tool interface is divided into three parts, the left side shows the picture, the middle is the marked place for the image, and the right side is the working directory

<img src="https://raw.githubusercontent.com/Erichen911/ImageCaptionLabelMaster/master/source/Windowswidget.png" />

**FEATURE**: The *suggestion.txt* file in the same level directory stores common grammars, and the software has a quick completion function.

---

## Android application
The marking tool on Android

<img src="https://raw.githubusercontent.com/Erichen911/ImageCaptionLabelMaster/master/source/Androidwidget.png" />

