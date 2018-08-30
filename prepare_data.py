import data_curation # My module, located: cell_counter/data_curation
# Available modules 
import argparse

# take in flags
def get_args():
        
    parser = argparse.ArgumentParser()

    parser.add_argument('-R','--rename_images',help='Rename images to a uniform filesystem name_0001.jpg, name_0002.jpg, ...' )
    parser.add_argument('-D', '--draw_boxes', nargs='*', help='The names of objects you want to classify, format: pos_tumour neg_tumour non_tumour')
    parser.add_argument('-C', '--generate_config', help='takes n number of object classes as input, generates .cfg, format: n')

    args = parser.parse_args()

    print(" \tRename: {} \n\tDraw: {} \n\tConfig: {}".format(
        args.rename_images,
        args.draw_boxes,
        args.generate_config))


# For args.rename_images, module: data_curation.rename_images

# For Draw boxes, modules: data_curation.manual_bounding_boxes, data_curation.generate_xml

# for Generate config, module: data_curation.generate_config_file


if __name__ == '__main__':
    get_args()


