import numpy as np
import cv2


def update(val=0):
    stereo.setBlockSize(cv2.getTrackbarPos('window_size', 'disparity'))
    stereo.setUniquenessRatio(
        cv2.getTrackbarPos('uniquenessRatio', 'disparity'))
    stereo.setSpeckleWindowSize(
        cv2.getTrackbarPos('speckleWindowSize', 'disparity'))
    stereo.setSpeckleRange(cv2.getTrackbarPos('speckleRange', 'disparity'))
    stereo.setDisp12MaxDiff(cv2.getTrackbarPos('disp12MaxDiff', 'disparity'))

    print('computing disparity...')
    disp = stereo.compute(imgL, imgR).astype(np.float32) / 16.0

    # cv2.imshow('left', imgL)
    cv2.imshow('disparity', (disp-min_disp)/num_disp)
    print("Image Updated")
    print()


if __name__ == "__main__":
    window_size = 2
    min_disp = 16
    num_disp = 192-min_disp*5
    blockSize = window_size
    uniquenessRatio = 1
    speckleRange = 50
    speckleWindowSize = 200
    disp12MaxDiff = 200
    P1 = 600
    P2 = 2400
    imgL = cv2.imread('../data/raw_data/left.png')
    imgR = cv2.imread('../data/raw_data/right.png')
    cv2.namedWindow('disparity')
    cv2.createTrackbar('speckleRange', 'disparity', speckleRange, 100, update)
    cv2.createTrackbar('window_size', 'disparity', window_size, 21, update)
    cv2.createTrackbar('speckleWindowSize', 'disparity',
                       speckleWindowSize, 200, update)
    cv2.createTrackbar('uniquenessRatio', 'disparity',
                       uniquenessRatio, 50, update)
    cv2.createTrackbar('disp12MaxDiff', 'disparity',
                       disp12MaxDiff, 250, update)
    cv2.createTrackbar('P1', 'disparity', P1, 5000, update)
    cv2.createTrackbar('P2', 'disparity', P2, 5000, update)
    stereo = cv2.StereoSGBM_create(
        minDisparity=min_disp,
        numDisparities=num_disp,
        blockSize=window_size,
        uniquenessRatio=uniquenessRatio,
        speckleRange=speckleRange,
        speckleWindowSize=speckleWindowSize,
        disp12MaxDiff=disp12MaxDiff,
        P1=P1,
        P2=P2
    )
    update()
    cv2.waitKey()
