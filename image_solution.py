# This
'''
Good cells- circle detection, cv2.HoughCircles
Bad cells- Employ general image detect

Change image to Grey scale
Edge detection- blurring ?

Deployment of algorithm

Limitations: Overlabing cells



'''
import cv2 as cv


def read_process_image(fp):
    """
    Reading in of image and converting to grayscale

    :param fp: file path for input image
    :return: grayscale image
    """
    # Read image
    img = cv.imread(fp)
    # Convert from BGR to gray scale
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return img_gray


def detect_circles(img, dp):
    """
    Detection of circles within image based on provided dp

    :param img: gray-scale image
    :param dp: ratio of ...
    :return: Number of circles detected
    """
    # Utilize HoughCircles for circle detection
    circles = cv.HoughCircles(image=img, method=cv.HOUGH_GRADIENT, dp=dp, minDist=10, maxRadius=150)
    return len(circles[0])


def image_solution(fp):
    """
    Main function performing sickle-cell percentage calculation

    :param fp: file path of image
    :return: percentage of sickle cells in image
    """
    # Read, process image
    img = read_process_image(fp)
    # Detect total number of 'good' cells in image
    num_good_cells = detect_circles(img, dp=2)
    # Detect total number of cells in image
    num_all_cells = detect_circles(img, dp=4)
    return (num_all_cells - num_good_cells) / num_all_cells



if __name__ == '__main__':
    percent_sickle = image_solution('testSCD.png')
    print(percent_sickle)
