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

### Install this (cell_counter) repository
```git clone``` repo

install python3.6

install pipenv, navigate to the cell_counter repository folder

install dependencies ```pipenv install```

```pipenv shell```

To run any .ipynb, run ```jupyter notebook```

### Install darkflow repository within cell_counter

within  cell_counter, run `git clone https://github.com/thtrieu/darkflow.git`

Then follow the instructions outine in darkflow/README.md, but using pipenv not pip. E.g.:

    `pipenv setup.py build_ext --inplace`

    `pipenv install -e .`

As a workaround for a bug: ImportError: No module named 'darkflow.cython_utils'. Copy the  `cell_counter/darkflow/darkflow/cython_utils` and `cell_counter/darkflow/darkflow/utils` to `cell_counter/darkflow/` directory.

# Hardware configuration:

Connect any usb camera to computer, may need to modify OpenCV device ID if other cameras in use. Relevant opencv line: cv2.VideoCapture(0) vs. cv2.VideoCapture(1))

# Preparation of custom dataset

Place images in `media/data`

### (TODO) Rename images
python prepare_data.py -R


### (TODO) Annotate the images with bounding boxes

(This can be done in small batches for sanity)

`python prepare_data.py -D`

### (TODO) Generate config file

`python prepare_data.py -FLAG OPTION`

example to start annotating images that have cats and dogs:

    `python prepare_data.py -D cats dogs`

example to generate a confige file when there are 2 types of objects:

    `python prepare_data.py -C 2`

prepare_data.py FLAGS:

    `-R','--rename_images', Rename images to a uniform filesystem name_0001.jpg, name_0002.jpg, ...' )

    `-D', '--draw_boxes', nargs='*', The names of objects you want to classify, format: pos_tumour neg_tumour non_tumour

    `-C', '--generate_config', takes n number of object classes as input, generates .cfg, format: n


# Live camera feed classification

TEMPORARY SOLUTION: `python darkflow/execute_local_model.py`

FUTURE SOLUTION BELOW

`python live_feed.py -FLAG OPTION`

example: `python live_feed.py -C 1 -W bin/yolov3.weights

live_feed.py FLAGS:

    `-C', '--Camera_ID', default=0, Camera_ID The ID of the camera. Default 0. Format: x

    `-M', '--Model', default='cfg/yolo.cfg' Location of config file relative to cell_counter/darkflow

    `-W', '--Weights', default='bin/yolo.weights' Location of weights relative to cell_counter/darkflow

    `-T', '--Threshold', default=0.4 Percentage confidence, above which to display box fo

    `-G', '--GPU', default=1.0 GPU proportion    

