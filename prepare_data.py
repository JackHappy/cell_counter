import data_curation # My module, located: cell_counter/data_curation
import argparse

# take in flags
parser = argparse.ArgumentParser()

parser.add_argument('-dir','--image_directory', help='Location of images to train model with, format: media/data/x' )
parser.add_argument('-rename', '--rename_images', help='relabel images, format: name (gives: name_0001.jpg, name_0002.jpg, ...)')
parser.add_argument('-categories', '--object_categories', help='The names of objects you want to classify, format: (pos_tumour,neg_tumour,non_tumour)')
parser.add_argument('-boxes', '--draw_boxes', help='Draw bounding boxes on n un-annotated images without annotations, format: n')
parser.add_argument('-config', '--generate_config', help='takes n number of object classes as input, generates .cfg, format: n')

args = parser.parse_args()

print(" \tDirectory: {} \n\tFilenames: {} \n\tCategories: {} \n\tImages to annotate: {}".format(
    args.image_directory,
    args.rename_images,
    args.object_categories,
    args.draw_boxes,
    args.generate_config))