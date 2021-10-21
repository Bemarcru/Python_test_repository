
import numpy as np
import cv2
import pandas as pd
from sys import argv

def load_image(image):
    im = cv2.imread(image)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    return gray

def contours(image):
    contours,_ = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    #print(f"THIS IS contours : {contours}")
    # Initialize empty list
    lst_intensities = []

    # For each list of contour points...
    for i in range(len(contours)):
        # Create a mask image that contains the contour filled in
        cimg = np.zeros_like(image)
        cv2.drawContours(cimg, contours, i, color=255, thickness=1)
       # Access the image pixels and create a 1D numpy array then add to list
        pts = np.where(cimg)
        #print(f"THIS IS pts : {pts}")
        lst_intensities.append(image[pts[0], pts[1]])
        #roi_avg_intensity = np.mean(tight)
    return lst_intensities

def main():
    
  my_image = argv[1] 

  # Read image

  im = load_image(my_image)
  r = cv2.selectROI("Select Rois",im)
  ##We can also try to infer where exactly is the ROI located:
  #print(f"r is: {r}")
  #r = (418, 353, 69, 66)

 # Crop image
  imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
  # Close contour, applying close function
  kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (6,6))
  blurred = cv2.GaussianBlur(imCrop, (5, 5), 0)
  tight = cv2.Canny(blurred, 240, 250)
  close = cv2.morphologyEx(tight, cv2.MORPH_CLOSE, kernel, iterations=1)
  
  # Show the image with close function that will be used as a mask later on
  cv2.imshow("Closed", close)

  # Create mask where white is what we want, black otherwise
  contours, hierarchy = cv2.findContours(close.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  idx = 0
  mask = np.zeros_like(close) 
  cv2.drawContours(mask, contours, idx, 255, -1) # Draw filled contour in mask
  result_image = cv2.bitwise_and(imCrop,imCrop,mask=close)# Extract out the mask and place into output image
  
  # Show the output image (original image with the mask)
  cv2.imshow('Output', result_image)  
  

  # Show intermediate images used:
  cv2.imshow("masked image",mask)
  cv2.imshow("crop", imCrop)
  cv2.imshow("filtered", blurred)
  cv2.imshow("thresholded", tight)
  cv2.waitKey(0)

  #Calculate mean intensity in our masked result image:

  roi_avg_intensity = np.mean(result_image)
  roi_avg_intensity2 = np.mean(mask) #as a comparison we can see that the mask has mean intensity close to 0
  roi_avg_intensity3 = np.mean(close) #as a positive control, we can se that our white mask has maximum mean intensity 6
  print(roi_avg_intensity)
  print(roi_avg_intensity2) 
  print(roi_avg_intensity3)


  # Getting a list of intensities according to location:
  #intensity_list = contours(tight)  
  #print(intensity_list)

  #Finally save the ROI output image with the mask applied
  cv2.imwrite('./Synapses_ROI.jpg', result_image)
  
  
  #And create an excel file with the results:
  
  data = [roi_avg_intensity]
  
  df = pd.DataFrame(data, columns=['Average Intensity'])
  print(df)

  # Creating an excel file with the results:
  file_name = 'Averageint.xlsx'
  df.to_excel(file_name)
  print('DataFrame is written to Excel File successfully.')






  
  



## USAGE:   
# python image_cv2mask.py ../A2-MaxIP_XY01_RGB_Cy5.tif
# python image_cv2mask.py ../A2-MaxIP_XY06_RGB_Cy5.tif





if __name__ == '__main__' :
    main()