import cv2
import numpy
from skimage.metrics import structural_similarity as ssim

def main():
    capture = cv2.VideoCapture('person.mp4')
    (status, fFrame) = capture.read()
    cv2.imshow('image', fFrame)
    while True:
        if capture.isOpened():
            # Read frame
            (status, frame) = capture.read()
            if status:
                if ssim(fFrame, frame, multichannel=True) <= 0.95:
                    cv2.imshow('image', frame)
                else:
                    for i in range(1,30):
                        capture.grab()
                
                key = cv2.waitKey(2)
                
                # Close program with keyboard 'q'
                if key == ord('q'):
                    cv2.destroyAllWindows()
                    exit(1)
            else:
                break
        else:
            pass

if __name__ == '__main__':
    main()    