# Breast cancer histopathology image classification through assembling multiple compact CNNs
This is a toolbox that implements the testing of the approach described in our papers: Breast cancer histopathology image classification through assembling multiple compact CNNs.

Our experiment was carried out with caffe.

###  network profile

 deploy_SE_bn4.prototxt is the network profile of hybrid model in our paper "Breast Cancer Histopathology Image Classification through Assembling Multiple Compact CNNs"

 deploy_64.prototxt and deploy_32.prototxt is the network profile of the method in "Breast Cancer Histopathological Image Classification using Convolutional Neural Networks"

###  data prepare

 Filefold global and patch contains the image filelist. Download the BACH dataset first and modify the path in the txt file with your own path.
 
 [BreaKHis](https://ieeexplore.ieee.org/abstract/document/7312934) and [BACH Challenge Dataset](https://iciar2018-challenge.grand-challenge.org/) are utilized in our test. 

 You can also download the dataset and data splitting files in our paper for research purposes from [Dataset-Downloading-Address](https://drive.google.com/drive/folders/1fjOYHnX7n-gmBXCChq9pZM8ByskOVe3_?usp=sharing).

 Note: please follow the data usage regulations. 

###  pretrained models

 You can get the pretrained models here. [model](https://drive.google.com/file/d/14fjGKqL8CfJlrVdTdsal5fy3v5aV4CvI/view?usp=sharing)， [model-patch](https://drive.google.com/file/d/1zPzQTLSIGvBNwzUK0lO4xAIagnNxV-mM/view?usp=sharing).

###  vote.ipynb

 In this file you can extract the result of the global and patch images. After that, you can compute various indicators in the following vote.ipynb content.


### addition: work11
 We selected a small portion of the pictures on the BreakHis-400X dataset. We used them to reproduce the article "Breast Cancer Histopathology Image Classification through Assembling Multiple Compact CNNs". However, in this process, we faced some problems, the network can not fit the training set very well, so our accuracy of the dataset is very low, and can not achieve the effect in the article. Of course, this may also be caused by the data set we selected which is too small. We put the code here and everyone can check it out.

### Citation
Please kindly cite this paper in your publications if it helps your research:
```
@article{zhu2019breast,
  title={Breast cancer histopathology image classification through assembling multiple compact CNNs},
  author={Zhu, Chuang and Song, Fangzhou and Wang, Ying and Dong, Huihui and Guo, Yao and Liu, Jun},
  journal={BMC Medical Informatics and Decision Making},
  volume={19},
  number={1},
  pages={198},
  year={2019},
  publisher={Springer}
}
```
