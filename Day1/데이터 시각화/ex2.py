from elice_utils import EliceUtils

elice_utils = EliceUtils()
from matplotlib import pyplot as plt
import numpy as np

def main():
    print("비교 차트 그리기")
    x=np.arange(1,10)
    y=np.arange(1,10)
    plt.xlabel("person")
    plt.ylabel("grade")
    
    # Python
    plt.plot(x,y)
    plt.xlabel("x_check")
    plt.ylabel("y_check")
    plt.title('sample_chart')
    
    plt.savefig("image.svg", format="svg")
    elice_utils.send_image("image.svg")


if __name__ == "__main__":
    main()
