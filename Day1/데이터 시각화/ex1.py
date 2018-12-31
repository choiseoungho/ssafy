from elice_utils import EliceUtils

elice_utils = EliceUtils()
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = 2
    y = 3
    
    plt.plot(x, y)
    plt.xlabel('x_chuck')
    plt.ylabel('y_chuck')
    plt.title('sample_chart')
    
    plt.savefig("image.svg", formate="svg")
    elice_utils.send_image("image.svg")


if __name__ == "__main__":
    main()
