import keras
from PIL import Image, ImageOps
import numpy as np
from glob import glob

model_path = "keras_model.h5"
labels_path = "labels.txt"
img_list = glob('검증용사진\*.jpg')
img_list.extend(glob('검증용사진\*.png'))

model = keras.models.load_model(model_path)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

for img_path in img_list:
    image = Image.open(img_path)
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array

    prediction = model.predict(data)
    print(prediction)

    with open(labels_path, 'rt', encoding='UTF8') as f : 
        readLines = f.readlines()
        
    if prediction[0,0] > prediction[0,1] :
        print(img_path,readLines[0])
    else:
        print(img_path,readLines[1])