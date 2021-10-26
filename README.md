# Python_test_repository

Python script generated to perform image analysis with OpenCV. We will obtain average intensity within a ROI defined by thresholded contours. Basically, the original image file is filtered with Gaussian Blur filter and then thresholded to select only the brightest points within a cropped region. A mask with those brightest regions is created and overlapped to the original image to select only those areas for the average intensity calculation. 

The data set provided is: confocal images of human neurons cocultured with hek cells expressing post-synaptic receptors (artificial synapse formation assay). Images are maximum intensity projections for the Cy5 channel. The ROI will thus select only the synaptic puncta formed over a hek cell.



## Packages used:

It requires OpenCV, numpy, pandas and openpyxl (for writing an excel file as output data).

* Open CV package:

conda install -c conda-forge opencv 

* Openpyxl:

pip install openpyxl 

## Usage

image_cv2mask.py [path to image.tif]

Examples:

python image_cv2mask.py ../A2-MaxIP_XY01_RGB_Cy5.tif


python image_cv2mask.py ../A2-MaxIP_XY06_RGB_Cy5.tif



and so on for the different image files included in Test data folder.





