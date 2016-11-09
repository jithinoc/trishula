
import tensorflow as tf
from trishula.models import Sequential
from trishula.layers import DenseLayer, SoftmaxLayer, Convolution2DLayer, MaxPooling2DLayer, FlattenLayer

from trishula.utils import error_functions
from trishula.utils import activation_functions
from trishula.datasets import mnist

mnist_data = mnist.load_data('../data/')

cross_entropy = error_functions.cross_entropy
relu = activation_functions.relu

n_kerns= [32, 64]
batch_size=50

model = Sequential()

model.add(
	Convolution2DLayer(
		filter_shape=(5,5,1,n_kerns[0]),
		input_shape=(batch_size,28,28,1),
		strides=1,
		activ_fn=relu
		)
	)

model.add(
	MaxPooling2DLayer(
		shape=2,
		strides=2
		)
	)

model.add(
	Convolution2DLayer(
		filter_shape=(5,5,n_kerns[0],n_kerns[1]),
		input_shape=(batch_size,14,14,n_kerns[0]),
		strides=1,
		activ_fn=relu
		)
	)

model.add(
	MaxPooling2DLayer(
		shape=2,
		strides=2
		)
	)

model.add(FlattenLayer())

model.add(
	DenseLayer(
		shape=(7*7*64,1024), 
		activ_fn=relu
		)
	)

model.add(
	DenseLayer(
		shape=(1024, 10), 
		activ_fn=relu
		)
	)

model.add(SoftmaxLayer())

model.optimize(
	dataset=mnist_data,
	error=cross_entropy,
	learning_rate=0.5
	)