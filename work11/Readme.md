## addition: work11

   We selected a small portion of the pictures on the BreakHis-400X dataset. 
 We used them to reproduce the article "Breast Cancer Histopathology Image Classification through Assembling Multiple Compact CNNs". 
 However, in this process, we faced some problems, the network can not fit the training set very well,
 so our accuracy of the dataset is very low, and can not achieve the effect in the article. 
 Of course, this may also be caused by the data set we selected which is too small. We put the code here and everyone can check it out.
 
### txt
the pictures we picked from BreakHis-400X dataset to train the network.

### preprocess.py
The script for image preprocessing.

### crop_pictures.py
The script for image crop. In the script,
we crop the pictures in the way carried out in article 
"Breast Cancer Histopathology Image Classification through Assembling Multiple Compact CNNs". 

### example
Some example images processed by the above script。

### other folds
The train script and prototxt file (random_32_32, random_64_64, sliding_32_32, sliding_64_64)
