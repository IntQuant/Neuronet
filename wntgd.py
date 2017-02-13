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

print(model.predict(testsx[0].reshape(1, 4, 32, 32)))

history = model.fit(
     x=testsx,
     y=testsy,
     nb_epoch=20,
     verbose=1,     
     validation_split=0.01,
     batch_size=10
 )
 
print(model.predict(testsx[0].reshape(1, 4, 32, 32)))

model.save_weights('Weights.hd5')




