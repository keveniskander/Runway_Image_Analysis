import cv2
import numpy as np
 
# def add_brightness(image):
#     image_HLS = cv2.cvtColor(image,cv2.COLOR_RGB2HLS) # Conversion to HLS
#     image_HLS = np.array(image_HLS, dtype = np.float64)
#     random_brightness_coefficient = np.random.uniform()+0.5 # generates value between 0.5 and 1.5
#     image_HLS[:,:,1] = image_HLS[:,:,1]*random_brightness_coefficient #scale pixel values up or down for channel 1(Lightness)
#     image_HLS[:,:,1][image_HLS[:,:,1]>255] = 255 #Sets all values above 255 to 255
#     image_HLS = np.array(image_HLS, dtype = np.uint8)
#     image_RGB = cv2.cvtColor(image_HLS,cv2.COLOR_HLS2RGB) # Conversion to RGB
#
#     return image_RGB

 
def detect_snow():
 
    image = cv2.imread('snow.jpg')
    img = cv2.resize(image, (700,700))
 
    upper_range = np.array([179, 19, 255])
    lower_range = np.array([0, 0, 195])
 
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_range, upper_range)
    output = cv2.bitwise_and(img, img, mask=mask)
 
    cv2.imshow('image', img)
    cv2.imshow('output', output)
 
    #cv2.imshow('mask', mask)
 
    count_white = cv2.countNonZero(mask)
 
    print("number of white pixels ", count_white)
 
    nPixels = mask.size
    print("number of total pixels ", nPixels)
 
    count_black = nPixels-count_white
 
    print("number of black pixels ", count_black)
 
    print("percent of white pixels: {0:.2f}%".format((count_white/nPixels)*100))
    print("percent of black pixels: {0:.2f}%".format((count_black / nPixels) * 100))
 
    while True:
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
 
    cv2.destroyAllWindows()
    return
 
 
detect_snow()