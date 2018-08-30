# Cell counter
A tool to identify and quantify cell groups using open source code (OpenCV) and cheap equipment (USB camera)


# Goal 
1. Connect the USB camera to any microscope and open a live feed
2. Have a button to capture image
3. Apply a filter to the image specific to DAB immunohistochemistry
4. Identify relevant cells
5. Of the relevant cells, count positive and negative cells
6. Estimate of the percentage of positive staining cells

# Use of code
Envisioned: Clone repo and double click .exe or .dmg based on operating system

Delivery ETA: Two Weeks &copy;


# Project setup and modifications:
```git clone``` repo

install python3.6

install pipenv, navigate to the cell_counter repository folder

install dependencies ```pipenv install```

```pipenv shell```

To run any .ipynb, in, run ```jupyter notebook```

# Hardware configuration:

Connect any usb camera to computer, may need to modify OpenCV device ID if other cameras in use (cv2.VideoCapture(0)-->cv2.VideoCapture(1))

# Preparation of custom dataset

Place images in `media/data`

Annotate the images with bounding boxes
(This can be done in small batches for sanity)

For example, annotate all the cells in 3 images, located in media/ki67_tumour folder as either pos_tumour, neg_tumour or non_tumour:
python prepare_data.py -dir media/data/ki67_tumour -categories (pos_tumour,neg_tumour,non_tumour) -boxes 3

prepare_data.py flags:
    -dir # Location of images to train model with, format: media/data/x
    -rename # relabel images, format: name (gives: name_0001.jpg, name_0002.jpg, ...))
    -categories # The names of objects you want to classify, format: (pos_tumour,neg_tumour,non_tumour))
    -boxes # Draw bounding boxes on n un-annotated images without annotations, format: n
    -config # Takes n number of object classes as input, generates .cfg, format: n