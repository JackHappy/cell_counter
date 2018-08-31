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

To run any .ipynb, run ```jupyter notebook```

# Hardware configuration:

Connect any usb camera to computer, may need to modify OpenCV device ID if other cameras in use (cv2.VideoCapture(0)-->cv2.VideoCapture(1))

# Preparation of custom dataset

Place images in `media/data`

### Rename images
python prepare_data.py -R


### Annotate the images with bounding boxes
(This can be done in small batches for sanity)
`python prepare_data.py -D`

### Generate config file
`python prepare_data.py -C`


prepare_data.py flags:
    `-R --rename`

    `-D --draw`

    `-C --config`