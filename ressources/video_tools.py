#!usr/bin/python3


def webcam():
    from cv2 import VideoCapture,imshow,waitKey,destroyAllWindows,cvtColor,COLOR_BGR2GRAY,imencode,flip,VideoWriter,VideoWriter_fourcc

    camera = VideoCapture(0)

    while camera.isOpened():
        ret, frame = camera.read()
        if not ret:
            break
        imshow('frame', frame)

        if waitKey(1) == ord('0'):
            break