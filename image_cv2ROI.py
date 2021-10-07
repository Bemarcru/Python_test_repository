
import cv2
import numpy as np
from sys import argv

def load_image(image):
      #im = cv2.imread(my_image,cv2.IMREAD_GRAYSCALE)
    im = cv2.imread(image)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    return gray

def contours(image):
    contours,_ = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    # Initialize empty list
    lst_intensities = []

    # For each list of contour points...
    for i in range(len(contours)):
        # Create a mask image that contains the contour filled in
        cimg = np.zeros_like(image)
        cv2.drawContours(cimg, contours, i, color=255, thickness=-1)
     # Access the image pixels and create a 1D numpy array then add to list
        pts = np.where(cimg == 255)
        lst_intensities.append(image[pts[0], pts[1]])
        #roi_avg_intensity = np.mean(tight)
        
    return lst_intensities

def main():
    
    my_image = argv[1] 

    # Read image

    im = load_image(my_image)
    

    # Select ROI
    #import pdb; pdb.set_trace()
    r = cv2.selectROI("Select Rois",im)


    # Crop image
    imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    blurred = cv2.GaussianBlur(imCrop, (5, 5), 0)

 
    # compute a "wide", "mid-range", and "tight" threshold for the edges
    # using the Canny edge detector
   # wide = cv2.Canny(blurred, 10, 200)
    #mid = cv2.Canny(blurred, 30, 150)
    tight = cv2.Canny(blurred, 240, 250)
    # mask roi
    

    # show the output Canny edge maps
    #cv2.imshow("Wide Edge Map", wide)
    #cv2.imshow("Mid Edge Map", mid)
    cv2.imshow("Tight Edge Map", tight)
    
    print(imageDest)

    #masked_roi = cv2.bitwise_and(imCrop,imCrop,mask=tight)
    #cv2.imshow("maskedroi",tight)
    
    cv2.waitKey(0)

    # Create new image for result storage
    # Mat imageDest = cvCreateMat(480, 640, CV_8UC3);
    # Cut out ROI and store it in imageDest
    #image->copyTo(imageDest, mask);    
    
   

   ###  Try doing an intensity list within the tight thresholded selection
   ### look for the select ROI code and modify it for converting the thresholded into a ROI in which we will 
   # extract the list of intensities and make an average
   ## WHy 255 in contours??
   
    intensity_list = contours(tight)
    print(intensity_list)
  

    # Display cropped image

    #cv2.imshow('img', imCrop)
    #cv2.waitKey(0)

     #python image_cv2ROI.py ../A2-MaxIP_XY01_RGB_Cy5.tif



if __name__ == '__main__' :
    main()
    

