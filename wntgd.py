import sys
from keras.models import Sequential
from keras.layers import Dense, Activation, normalization
import numpy as np

sys.stdin = open('conv.txt', 'r')

testsx = []
testsy = []

current = True
while True:
    try:
        inp = input()
    except EOFError:
        break
    if inp == "":
        break
    if current:
        testsy.append((int(inp)+0.5)*0.1)
    else:
        testsx.append(list(map(int,inp)))
    current = not current


model = Sequential()

model.add(Dense(output_dim=512, input_dim=1024))
model.add(Activation("tanh"))
model.add(normalization.BatchNormalization(mode=1))


model.add(Dense(output_dim=512))
model.add(Activation("tanh"))
model.add(Dense(output_dim=256))
model.add(Activation("tanh"))
model.add(Dense(output_dim=128))
model.add(Activation("tanh"))
model.add(Dense(output_dim=64))
model.add(Activation("tanh"))
model.add(Dense(output_dim=32))
model.add(Activation("tanh"))

model.add(Dense(output_dim=1))
model.add(Activation("tanh"))

model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['accuracy'])

history = model.fit(
    x=testsx,
    y=testsy,
    nb_epoch=50,
    verbose=1,
    validation_split=0.1,
)
print('-'*50)

for i, elem in enumerate(model.predict(testsx)):
    print(elem, testsy[i])

#wfile = open('weights.txt', 'w')

#np.set_printoptions(threshold=np.nan)

print(model.get_weights(), file=wfile)
