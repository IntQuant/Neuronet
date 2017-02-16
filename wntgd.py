import sys

import numpy as np
import random
from INeuronet import GetModel
from PrepImg import Prepare

seed = 7
np.random.seed(seed)
random.seed(seed)

model = GetModel.getmodel()
currentbath = 0

testsx, testsy = Prepare.get()

model.load_weights('Weights.hd5')

print(model.predict(testsx[0].reshape(1, 28, 28, 1)))

history = model.fit(
     x=testsx,
     y=testsy,
     initial_epoch=90,
     nb_epoch=100,
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



