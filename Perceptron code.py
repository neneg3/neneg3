# Enter variables 
x_input = [0.1,0.2,0.3,0.4,0.5]
w_weights = [0.4,0.5,0.6,0.7,0.8]
threshold = 0.2

# Define the activation function
def step(weighted_sum):
    if weighted_sum > threshold:
        return 1 
    else:
        return 0

  # Define Perceptron
def perceptron():
    weighted_sum = 0 
    for i,w in zip(x_input, w_weights):
        weighted_sum += i*w    
        print(weighted_sum)
    return step(weighted_sum) 

output = perceptron()
print("output: " + str(output))
