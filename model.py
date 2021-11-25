from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Conv2D
from tensorflow.keras.applications import ResNet50

model = Sequential()
model.add(Input())
model.add(Conv2D(kernel_size=(3,3)))