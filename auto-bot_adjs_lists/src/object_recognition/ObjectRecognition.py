import numpy as np
import cv2
from imutils import resize
from pyautogui import screenshot, Window
from src.utils.other import getPercent


def take_screenshot(window: Window):
    filename = "src/img/screenshots/wholeScreen.png"
    screenshot(filename, region=(window.topleft[0] + getPercent(10, window.size[0]),
                                 window.topleft[1] + getPercent(3, window.size[1]),
                                 window.bottomright[0] - getPercent(20, window.size[0]),
                                 window.bottomright[1] - getPercent(15, window.size[1]),
                                 ))
    return filename


def recognize(window: Window):
    template = cv2.imread('src/img/ble.png')
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    template = cv2.Canny(template, 50, 200)
    (tH, tW) = template.shape[:2]

    window_screen = cv2.imread(take_screenshot(window=window))
    gray = cv2.cvtColor(window_screen, cv2.COLOR_BGR2GRAY)
    found = None

    for scale in np.linspace(0.2, 1.0, 20)[::-1]:
        resized = resize(gray, width=int(gray.shape[1] * scale))
        r = gray.shape[1] / float(resized.shape[1])

        if resized.shape[0] < tH or resized.shape[1] < tW:
            break

        edged = cv2.Canny(resized, 50, 200)
        result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF)
        (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

        if found is None or maxVal > found[0]:
            found = (maxVal, maxLoc, r)

    (maxVal, maxLoc, r) = found
    print('maxval=', maxVal)
    if maxVal < 5000000:
        return None
    (startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
    (endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))

    return startX + (endX - startX) / 2.5 + window.topleft[0] + getPercent(10, window.size[0]), startY + (endY - startY) / 2.5 + window.topleft[1] + getPercent(3, window.size[1])
    # cv2.rectangle(window, (startX, startY), (endX, endY), (0, 0, 255), 2)
    # cv2.imshow("Image", window)
    # cv2.waitKey(0)
    # 390 543 446 600