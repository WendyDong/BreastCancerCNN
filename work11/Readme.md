## addition: work11

   We selected a small portion of the pictures on the BreakHis-400X dataset. 
 We used them to reproduce the article "Breast Cancer Histopathology Image Classification through Assembling Multiple Compact CNNs". 
 However, in this process, we faced some problems, the network can not fit the training set very well,
 so our accuracy of the dataset is very low, and can not achieve the effect in the article. 
 Of course, this may also be caused by the data set we selected which is too small. We put the code here and everyone can check it out.
 
### txt
The pictures we picked from BreakHis-400X dataset to train the network.

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

### Results

Results: Our method in testing samples

| Scheme | Image level |	Patient level|	Kappa|	PPV |
| ----- | --------- | ----------- | ------- |------- |
| Hybrid CNN with bagging (sum) | 93.7	|94.6	|0.875	|95.5 |
| Hybrid CNN with bagging (max)  | 91.1	|91.9	|0.756	|92.0     |

Results: "Breast Cancer Histopathology Image Classification through Assembling Multiple Compact CNNs" results (initialization method: gaussian; activation: ReLU) (RS: random sampling; SW: sliding window)

|Strategy	|RS 32X32	|RS 64X64	|SW 32X32	|SW 64X64	|Max Fusion|
| ----- | --------- | ----------- | ------- |------- |------- |
|Train Loss |	0.62 |	0.65	 |0.60 |	0.58	 |N/A |
 |Validation Acc. |	69.8 |	70.2 |	69.8	 |70.2 |	N/A |
 |Acc. In Testing |	63.8 |	63.8	 |63.8	 |63.8	 |63.8 |
 
 It is weird that the article method only achieves 63.8 image level accuracy with Max fusion, and we find that almost all the testing samples are recognized as cancer type. We then tried the other initialization methods, activation functions and the different learning rate strategies, however, similar results are obtained, as shown in the following table: 
 
 |Strategy	|Xavier/ReLU	|msra/ReLU	|Xavier/PReLU	|gaussian/PReLU	|msra/PReLU |
 | ----- | --------- | ----------- | ------- |------- |------- |
|RS 32X32|	0.62/69.8	|0.62/69.8|	0.60/69.8|	0.59/69.8|	0.44/69.8|
|RS 64X64|	0.65/70.2	|0.65/70.2|	0.62/70.2|	0.54/70.2|	0.46/70.2|
|SW 32X32|	0.60/69.8	|0.60/69.8|	0.58/69.8|	0.54/69.8|	0.43/69.8|
|SW 64X64|	0.58/70.2	|0.58/70.2|	0.53/70.2|	0.48/70.2|	0.45/70.2|
|Max Fusion|	63.8	|63.8|	63.8|	63.8|	63.8|
 
The article method results is very weird so we put the code here and everyone can check it out.
