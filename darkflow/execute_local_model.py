import cv2
from darkflow.net.build import TFNet
import numpy as np
import time



def execute_model(options,device_id):
    print(options) 
    tfnet = TFNet(options)

    start_image_capture(device_id,tfnet)

def start_image_capture(device,network):
    capture = cv2.VideoCapture(device)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    colors = [tuple(255 * np.random.rand(3)) for _ in range(10)] 

    while True:
        stime = time.time()
        ret, frame = capture.read()
        if ret:
            results = network.return_predict(frame)
            for color, result in zip(colors, results):
                tl = (result['topleft']['x'], result['topleft']['y'])
                br = (result['bottomright']['x'], result['bottomright']['y'])
                
                label = result['label']
                confidence = result['confidence']

                text = '{}: {:.0f}%'.format(label, confidence * 100)

                frame = cv2.rectangle(frame, tl, br, color, 5)
                frame = cv2.putText(frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 2)
            cv2.imshow('frame', frame)
            print('FPS {:.1f}'.format(1 / (time.time() - stime)))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()
    
def darkflow_test_function():
    # from the darkflow readme: 


    options = {"model": "cfg/yolo.cfg", "load": "bin/yolo.weights", "threshold": 0.01}

    tfnet = TFNet(options)

    imgcv = cv2.imread("./sample_img/sample_dog.jpg")
    result = tfnet.return_predict(imgcv)
    print(result)



if __name__ == '__main__':
    # temporary test:
    #darkflow_test_function()

    # temporary test for camera:
    options = {"model": "cfg/yolo.cfg", "load": "bin/yolo.weights", "threshold": 0.1}
    execute_model(options,0)

    print('nothing defaulted to run when execute_loval_model.py (this file) is run from commaned line')