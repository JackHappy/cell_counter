import darkflow.execute_local_model # My module, located: cell_counter/data_curation
# Available modules 
import argparse

# take in flags
def get_args():
        
    parser = argparse.ArgumentParser()

    parser.add_argument('-C', '--Camera_ID', default=0, help='--Camera_ID The ID of the camera. Default 0. Format: x ')
    parser.add_argument('-M', '--Model', default='cfg/yolo.cfg' ,help='Location of config file relative to cell_counter/darkflow')
    parser.add_argument('-W', '--Weights', default='bin/yolo.weights' ,help='Location of weights relative to cell_counter/darkflow')
    parser.add_argument('-T', '--Threshold', default=0.4 ,help='Percentage confidence, above which to display box for')
    parser.add_argument('-G', '--GPU', default=1.0 ,help='GPU proportion')

    args = parser.parse_args()

    print(" \tDevice_ID: {} \t\nModel: {} \t\nWeights: {} \t\nThreshold: {} \t\nGPU: {}".format(
        args.Camera_ID,
        args.Model,
        args.Weights,
        args.Threshold,
        args.GPU,))



    
    return args.Camera_ID, args.Device_ID, args.Model, args.Weights, args.Threshold, args.GPU


def set_options(model,weights,threshold,gpu):
    config_options = {
        'model': model,
        'load': weights,
        'threshold': threshold,
        'gpu': 1.0
    }
    return set_options





if __name__ == '__main__':
    # Get device ID, usually 0, unless webcam present, then 1 or 2... etc.
    device,model,weights,threshold,gpu = get_args()

    # Call the function to open webcam and start classification
    options = set_options(model,weights,threshold,gpu)

    # execute the model from within cell_counter/darkflow
    darkflow.execute_local_model.execute_model(options,device)

    capture_video(device)



