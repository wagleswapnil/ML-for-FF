#################################################################################################
# The class Network contains the structure and methods of the neural network used in this       #
# project.                                                                                      #
#                                                                                               #
# The author of this code is:                                                                   #
# Swapnil Wagle                                                                                 #
# Max Planck Institute of Colloids and Interfaces, Potsdam, Germany                             #
# E-mail id: swapnil.wagle@mpikg.mpg.de                                                         #
#################################################################################################

import random
import numpy

# Initialization of the class
class Network(object):
    
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [numpy.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [numpy.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]    
        
        
# The feed_forward method takes input 'a' which is the input vector for any layer of the neural network
# and returns the output of the same layer by calculating the output of each of the neurons in the layer by
# function (output = weight * input + bias)  
    def feed_forward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = self.sigmoid(numpy.dot(w, a) + b)
            return a

# The SGD (Stochastic Gradient Descent) method takes the training data (training_data), number of iterations for
# training the netowk (epochs), the size of the training data in each iteration (mini_batch_size) and the 
# learning rate (eta) as the inputs and prints the progress of the network after each iteration (or epoch) of 
# training. First it devides the training data into small mini matches for training the network and then passes
# each of the mini batches to the update_mini_batch method for updating the biases and weights of each of the 
# (neurons of the) layers in the network. 
    def SGD(self, training_data, epochs, mini_batch_size, eta, test_data):
        if test_data:
            n_test = len(test_data)
        n = len(training_data)
        for j in range(epochs):                        # if range() function does not work, try xrange(). Check google for details- 
            random.shuffle(training_data)              # -as it depends on the python version
            mini_batches = [training_data[k: k + mini_batch_size] for k in range(0, n, mini_batch_size)]
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
            if test_data:
                print ("Epoch {0}: {1} / {2}". format(j, self.evaluate(test_data), n_test))
            else:
                print ("Epoch {0} complete". format(j))

# The update_mini_batch method takes the mini batch and learning rate from the SGD method for training the network.
# For updating the biases and weights, it calls the 'backprop' method for the calclation of the error in each of 
# the layers and updates them by functions:
#   updated bias = current bias - (learning rate/ size of the batch) * summation of (error in the output of the neuron * output of the neuron)
#   updated weight = current weight - (learning rate/ size of the batch) * sum (error in the output of the neuron)
    def update_mini_batch(self, mini_batch, eta):
        nabla_b = [numpy.zeros(b.shape) for b in self.biases]
        nabla_w = [numpy.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch:
            (delta_nabla_b, delta_nabla_w) = self.backprop(x, y)
            nabla_b = [nb + dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.biases = [b - (eta/len(mini_batch))*nb for b, nb in zip(self.biases, nabla_b)]
        self.weights = [w - (eta/len(mini_batch))*nw for w, nw in zip(self.weights, nabla_w)]
        
# The backprop method takes the input and output vectors (numpy arrays) from the mini batch and returns the updated errors in each of the 
# neurons by calculating the cost derivatives with respect to the biases (variables nabla_b) and weights (variables nabla_w). 
    def backprop(self, x, y):
        nabla_b = [numpy.zeros(b.shape) for b in self.biases]
        nabla_w = [numpy.zeros(w.shape) for w in self.weights]
        activation = x
        activations = [x]
        zs = []
        for b, w in zip(self.biases, self.weights):
            print (w.shape, activation.shape, b.shape)
            z = numpy.dot(w, activation) + b
            print(z.shape)
            zs.append(z)
            activation = self.sigmoid(z)
            activations.append(activation)
            temp = numpy.transpose(activation)
            temp_z = numpy.transpose(z)
        delta = self.cost_derivative(temp[-1], y) *  self.sigmoid_prime(temp_z[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = numpy.dot(delta, temp[-2].transpose())
        for l in range(2, self.num_layers-1):
            z = zs[-1]
            sp = self.sigmoid_prime(z)
            delta = numpy.dot(self.weights[-l+1].transpose(),delta) * sp
            nabla_b[-1] = delta
            nabla_w[-1] = numpy.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)

# The method 'evaluate' takes an input vector as a numpy array (variable test_data) and gets the output vector for this
# corresponding input vector by calling the 'feedforward' method. Note that the weights and biases of the network, denoted 
# by self.weights and self.biases, respectively, are being updated by each round of training iteration (epoch) and the 
# output is being monitored in the 'SGD' by the print statements.
    def evaluate(self, test_data):
        test_results = self.feedforward(test_data)
        return (test_results)
        
    def cost_derivative(self, output_activations, y):
        return (output_activations - y)
        
    def sigmoid(self, z):
        return 1.0/(1.0 + numpy.exp(-z))
        
    def sigmoid_prime(self, z):
        res_sig_prime = self.sigmoid(z)*(1-self.sigmoid(z))
        return (res_sig_prime)
    
    
        
