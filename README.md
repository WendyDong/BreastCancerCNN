# BreastCancerCNN
Our experiment was carried out with caffe.

###  network profile

 deploy_SE_bn4.prototxt is the network profile of hybrid model in our paper "Breast Cancer Histopathology Image Classification through Assembling Multiple
Compact CNNs"

 deploy_64.prototxt and deploy_32.prototxt is the network profile of the method in "Breast Cancer Histopathological Image Classification using Convolutional Neural Networks"

###  data prepare

 Filefold global and patch contains the image filelist. Download the BACH dataset first and modify the path in the txt file with your own path.

###  pretrained models

 You can get the pretrained models here. [model](https://drive.google.com/file/d/14fjGKqL8CfJlrVdTdsal5fy3v5aV4CvI/view?usp=sharing)， [model-patch](https://drive.google.com/file/d/1zPzQTLSIGvBNwzUK0lO4xAIagnNxV-mM/view?usp=sharing).

###  vote.ipynb

 In this file you can extract the result of the global and patch images. After that, you can compute various indicators in the following vote.ipynb content.


