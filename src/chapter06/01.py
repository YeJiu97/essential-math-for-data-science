import numpy as np
import matplotlib.pyplot as plt

# Defining the activation functions
def relu(x):
    return np.maximum(0, x)

def tanh(x):
    return np.tanh(x)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(x):
    e_x = np.exp(x - np.max(x))  # Stability improvement by subtracting max(x)
    return e_x / e_x.sum()

# Generating data for the plot
x = np.linspace(-10, 10, 400)
y_relu = relu(x)
y_tanh = tanh(x)
y_sigmoid = sigmoid(x)
y_softmax = softmax(x)  # Normally used for vectors, we'll visualize one output for clarity

# Plotting the functions
plt.figure(figsize=(10, 6))
plt.plot(x, y_relu, label='ReLU', color='blue')
plt.plot(x, y_tanh, label='Tanh', color='red')
plt.plot(x, y_sigmoid, label='Sigmoid', color='green')
plt.plot(x, y_softmax, label='Softmax', color='purple', linestyle='--')  # To differentiate since it's not typically used like this

plt.title('Visualization of Activation Functions')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
