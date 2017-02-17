import sys

import numpy as np
import random
from INeuronet import GetModel
from PrepImg import Prepare
from keras.optimizers import SGD

seed = 7
np.random.seed(seed)
random.seed(seed)

model = GetModel.getmodel()
currentbath = 0

testsx, testsy = Prepare.get()

#model.load_weights('Weights.hd5')

print(model.predict(testsx[0].reshape(1, 28, 28, 1)))



history = model.fit(
     x=testsx,
     y=testsy,
     nb_epoch=20,
     verbose=1,     
     validation_split=0.01,
     batch_size=64,
     shuffle=True,
     
 )
 
 
model.layers[0].trainable = False

csgd = SGD(lr=1e-4, momentum=0.9)

model.compile(loss='categorical_crossentropy',optimizer=csgd, metrics=['accuracy'])

history = model.fit(
     x=testsx,
     y=testsy,
     nb_epoch=40,
     verbose=1,     
     validation_split=0.01,
     batch_size=32,
     shuffle=True,
     
 )



 
print(model.predict(testsx[0].reshape(1, 28, 28, 1)))

model.save_weights('Weights.hd5')

ev = model.evaluate(testsx, testsy)

print('Score:', ev[0])
print('Acc:  ', ev[1])



