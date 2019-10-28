#Mike Kmiec
#CSE163 HW 7

import cse163_utils
import matplotlib.pyplot as plt
import numpy as np
import imageio




def invert_colors(image):
    """
    Given a color image(3-d numpy array).
    
    Return a new inverted color image.
    """
    x, y, z = image.shape
    img = np.zeros((x, y, z))
    img[:, :, 0] = 255 - image[:, :, 0]
    img[:, :, 1] = 255 - image[:, :, 1]
    img[:, :, 2] = 255 - image[:, :, 2]
    return img

def blur(gray_image, patch_size):
    """
    Given a gray image and a patch size.
    
    Return a new image blurred with the given patch size.
    """
    kernel = np.ones((patch_size, patch_size)) * (1/(patch_size**2))
    height, width = gray_image.shape
    result = np.zeros((height - (patch_size - 1), width - (patch_size - 1)))
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            curr = gray_image[i:i+patch_size, j:j+patch_size]
            result[i, j] = np.sum(curr * kernel)
    return result.astype(np.uint8)


def template_match(image, template):
    """
    Given an image and template.
    
    Return a 2-d numpy array of the similarity between
    the template(2-d numpy array) at each point in the gray
    image(2-d numpy array).
    """
    height, width = image.shape
    x, y = template.shape
    avg = np.sum(template)/(x*y)
    template = template - avg
    result = np.zeros((height - (x - 1), width - (y - 1)))
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            curr = image[i:i+x, j:j+y]
            curr_avg = np.sum(curr)/(x*y)
            curr = curr - curr_avg
            result[i, j] = np.sum(curr * template)
    return result


def find_xy(result):
    """
    Given the result of template_match, finds the position (x, y) with
    the highest similarity.
    """
    ij = np.unravel_index(np.argmax(result), result.shape)
    return ij[::-1]


def plot_result(image, template, result):
    """
    Given an image, a template, and the result of
    template_match(image, template), makes a plot showing the result
    of the match.
    """
    x, y = find_xy(result)

    plt.figure(figsize=(8, 3))
    ax1 = plt.subplot(1, 3, 1)
    ax2 = plt.subplot(1, 3, 2)
    ax3 = plt.subplot(1, 3, 3, sharex=ax2, sharey=ax2)

    ax1.imshow(template, cmap=plt.cm.gray)
    ax1.set_axis_off()
    ax1.set_title('template')

    ax2.imshow(image, cmap=plt.cm.gray)
    ax2.set_axis_off()
    ax2.set_title('image')
    # highlight matched region
    template_height,  template_width = template.shape
    rect = plt.Rectangle((x, y), template_width, template_height,
                         edgecolor='r', facecolor='none')
    ax2.add_patch(rect)

    ax3.imshow(result)
    ax3.set_axis_off()
    ax3.set_title('`match_template`\nresult')
    # highlight matched region
    ax3.autoscale(False)
    ax3.plot(x, y, 'o', markeredgecolor='r', markerfacecolor='none',
             markersize=10)
    plt.show()


def main():
#    Test Problem 0 Invert Colors
    img = imageio.imread('images/puppy.png')[:, :, :3]
    fig = plt.figure(figsize=(10, 5))
    a = fig.add_subplot(1, 2, 1)
    imgplot = plt.imshow(img)

    a = fig.add_subplot(1, 2, 2)
    img = invert_colors(img)
    imgplot = plt.imshow(img)

    
#    Test Problem 1 Blur
    img = imageio.imread('image/coins.png')
    fig = plt.figure(figsize=(15, 15))
    a = fig.add_subplot(1, 2, 1)
    imgplot = plt.imshow(img, cmap=plt.cm.gray)
    a = fig.add_subplot(1, 2, 2)
    img = blur(img, 30)
    imgplot = plt.imshow(img, cmap=plt.cm.gray)
    
#    Test Problem 2 Template Match
    img = imageio.imread('images/coins.png')
    template = img[170:220, 75:130]
    result = template_match(img, template)
    plot_result(img, template, result)

if __name__ == '__main__':
    main()

