import numpy as np
import warnings
warnings.filterwarnings("ignore")
import tensorflow as tf
from tensorflow import keras
tf.compat.v1.enable_eager_execution()
import matplotlib.pyplot as plt
from model_utils import save_model

# construct TensorFlow model
model = keras.Sequential()
model.add(keras.layers.InputLayer(input_shape=(None, 1)))
model.add(keras.layers.Dense(8, activation='tanh', kernel_initializer='random_normal', bias_initializer='random_normal'))
model.add(keras.layers.Conv1D(4, 3, dilation_rate=1, activation='tanh', padding='causal', kernel_initializer='glorot_uniform', bias_initializer='random_normal'))
model.add(keras.layers.Conv1D(4, 3, dilation_rate=2, activation='tanh', padding='causal', kernel_initializer='glorot_uniform', bias_initializer='random_normal'))
model.add(keras.layers.Dense(8, activation='sigmoid', kernel_initializer=tf.keras.initializers.Orthogonal(), bias_initializer='random_normal'))
model.add(keras.layers.Dense(1, kernel_initializer='orthogonal', bias_initializer='random_normal'))

# construct signals
N = 100
x = 10 * np.sin(np.arange(N) * np.pi * 0.1)
y = model.predict((x.reshape((1, -1, 1))))
print(y.shape)
y = y.flatten()

# plot signals
plt.figure()
plt.plot(x)
plt.plot(y, '--')
plt.ylim(-0.5, 0.5)
plt.savefig('python/conv.png')

# save signals
np.savetxt('test_data/conv_x_python.csv', x, delimiter=',')
np.savetxt('test_data/conv_y_python.csv', y, delimiter=',')

save_model(model, 'models/conv.json')
