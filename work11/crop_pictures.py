#²Ã¼ô¶Ô±ÈµÄÍ¼Æ¬
from PIL import Image
import os
for bei in ['400X']:
    for fold in [1]:
        with open("txt_bagging/fold{}/{}/train.txt".format(str(fold+1),bei),'r') as f:
            lines=f.readlines()
            for line in lines:
                imagename=line.split(' ')[0]
                img=Image.open(imagename)
                img=img.resize((230,350))
                for mode in ["sliding_32_32","sliding_64_64"]:
                    newname=imagename.rstrip().replace("preprocess","preprocess_duibi/"+mode)           
                    newdir=newname[0:-len(newname.split("/")[-1])]
                    if not os.path.exists(newdir):
                        os.makedirs(newdir)
                    if mode =="random_32_32":       
                        heng=[random.randint(0,197) for _ in range(1000)]
                        shu=[random.randint(0,317) for _ in range(1000)]
                        for every in range(1000):
                                box = (heng[every],shu[every],heng[every]+32,shu[every]+32)                    
                                img.crop(box).save(newname[0:-4]+"_"+str(every)+".jpg")
                    elif mode =="random_64_64":  
                        heng=[random.randint(0,165) for _ in range(1000)]
                        shu=[random.randint(0,285) for _ in range(1000)]
                        for every in range(1000):
                                box = (heng[every],shu[every],heng[every]+64,shu[every]+64)                    
                                img.crop(box).save(newname[0:-4]+"_"+str(every)+".jpg")
                    elif mode =="sliding_32_32":  
                        for i in range(13):
                            for j in range(20):
                                box = (i*16,j*16,(i+2)*16,(j+2)*16)     
                                img.crop(box).save(newname[0:-4]+"_"+str(i)+"_"+str(j)+".jpg")
                    elif mode =="sliding_64_64":  
                        for i in range(6):
                            for j in range(9):
                                box = (i*32,j*32,(i+2)*32,(j+2)*32)                    
                                img.crop(box).save(newname[0:-4]+"_"+str(i)+"_"+str(j)+".jpg")