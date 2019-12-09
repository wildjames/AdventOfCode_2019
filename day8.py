import numpy as np

def decode_image(img, x_size, y_size):
    'Take img as a string'
    layers = []
    img = np.array([int(n) for n in img])
    n_layers = len(img) // (x_size*y_size)
    layers = img.reshape((n_layers, y_size, x_size))

    return layers

# Part one
with open('day8.txt', 'r') as image_file:
    img = image_file.read().strip()
image = decode_image(img, 25, 6)

N_zeros = 25*6
target_layer = np.array([])
for layer in image:
    if np.sum(layer==0) < N_zeros:
        N_zeros = np.sum(layer==0)
        target_layer = layer
print("Part 1 answer: {}".format(np.sum(target_layer==1)*np.sum(target_layer==2)))

# Part 2
# 0: Black
# 1: White
# 2: Transparent
# Image is rendered by stacking directly on top of each other.

import matplotlib.pyplot as plt
def render_image(image):
    image = image[::-1]
    render = image[0]
    for i, layer in enumerate(image[1:]):
        locs = np.where(layer != 2)
        render[locs] = layer[locs]

    return render

render = render_image(image)
plt.imshow(render)
plt.show()
