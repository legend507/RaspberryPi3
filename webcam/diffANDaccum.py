import cv2
import numpy as np

ESC_KEY = 27     
INTERVAL= 33     
FRAME_RATE = 30

WINDOW_ORG = "org"
WINDOW_BACK = "back"
WINDOW_DIFF = "diff"

FILE_ORG = "org_768x576.avi"


cv2.namedWindow(WINDOW_ORG)
cv2.namedWindow(WINDOW_BACK)
cv2.namedWindow(WINDOW_DIFF)


mov_org = cv2.VideoCapture(0)

has_next, i_frame = mov_org.read()


back_frame = np.zeros_like(i_frame, np.float32)


while has_next == True:
    f_frame = i_frame.astype(np.float32)

    diff_frame = cv2.absdiff(f_frame, back_frame)

    cv2.accumulateWeighted(f_frame, back_frame, 0.025)

    cv2.imshow(WINDOW_ORG, i_frame)
    cv2.imshow(WINDOW_BACK, back_frame.astype(np.uint8))
    cv2.imshow(WINDOW_DIFF, diff_frame.astype(np.uint8))

    key = cv2.waitKey(INTERVAL)
    if key == ESC_KEY:
        break

    has_next, i_frame = mov_org.read()

cv2.destroyAllWindows()
mov_org.release()
