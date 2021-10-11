import cv2
import mediapipe as mp
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np
import pyautogui


def main(number, command):
    mpHands = mp.solutions.hands
    mpLandmarks = mp.solutions.hands.HandLandmark
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils
    mpStyles = mp.solutions.drawing_styles

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volRange = volume.GetVolumeRange()
    minVol = volRange[0]
    maxVol = volRange[1]

    def coordinates(number):
        normalizedLandmark = handslms.landmark[number]
        pixelCoordinatesLandmark = mpDraw._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y,
                                                                           wCam, hCam)
        return pixelCoordinatesLandmark

    def count(coordinates1, coordinates2):
        if coordinates2 == 4:
            if coordinates(coordinates1)[0] > coordinates(coordinates2)[0]:
                numberCount = 1
            else:
                numberCount = 0
        else:
            if coordinates(coordinates1)[1] > coordinates(coordinates2)[1]:
                numberCount = 1
            else:
                numberCount = 0
        return numberCount

    def counting():
        countNumber = 0
        countingcoordinates = [[3, 4], [6, 8], [10, 12], [14, 16], [18, 20]]
        for i in countingcoordinates:
            countNumber += count(i[0], i[1])
        cv2.putText(image, str(countNumber), (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2)

    def findDistance():
        punt1 = coordinates(4)
        punt2 = coordinates(8)
        lengthHand = punt2[0] - punt1[0]
        if lengthHand < 0:
            lengthHand = lengthHand * -1

        return lengthHand

    def setVolume():
        print("Hello world")
        length = findDistance()
        vol = np.interp(length, [0, 120], [minVol, maxVol])
        print(int(length), vol)
        volume.SetMasterVolumeLevel(vol, None)
        return

    def moveMouse():
        start_point = (170, 140)
        end_point = (470, 340)
        start_pointButton = (20, 20)
        end_pointButton = (40, 40)
        color = (255, 0, 0)
        thickness = 2
        cv2.rectangle(image, start_point, end_point, color, thickness)
        cv2.rectangle(image, start_pointButton, end_pointButton, color, thickness)
        coordinate = coordinates(12)
        coordinateBreedte = (coordinate[0] - 170) * 6.4
        coordinateHoogte = (coordinate[1] - 140) * 5.4 * -1 + 1080
        if coordinateBreedte < 0:
            coordinateBreedte = 0
        if coordinateBreedte > 1920:
            coordinateBreedte = 1920
        if coordinateHoogte < 0:
            coordinateHoogte = 0
        if coordinateHoogte > 1080:
            coordinateBreedte = 1080
        eindCoordinate = (coordinateBreedte, coordinateHoogte)
        pyautogui.moveTo(eindCoordinate[0], eindCoordinate[1], 0.05)
        if coordinates(4)[0] > coordinates(2)[0]:
            pyautogui.mouseDown(coordinateBreedte, coordinateHoogte)
        else:
            pyautogui.mouseUp()

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    wCam, hCam = 640, 480
    cap.set(3, wCam)
    cap.set(4, hCam)

    with mpHands.Hands(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5,
            max_num_hands=number) as hands:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                continue

            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = hands.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.multi_hand_landmarks:
                for handslms in results.multi_hand_landmarks:
                    for lm in handslms.landmark:
                        landmarks = []
                        mpDraw.draw_landmarks(
                            image,
                            handslms,
                            mpHands.HAND_CONNECTIONS,
                            mpStyles.get_default_hand_landmarks_style(),
                            mpStyles.get_default_hand_connections_style())
                        lmx = int(lm.x * wCam)
                        lmy = int(lm.y * hCam)
                        landmarks.append([lmx, lmy])
                        mpDraw.draw_landmarks(image, handslms,
                                              mpHands.HAND_CONNECTIONS)
                    # back()
                    if command == "mouse":
                        moveMouse()
                    elif command == "sound":
                        setVolume()
                    elif command == "count":
                        counting()
            cv2.imshow('MediaPipe Hands', image)
            if cv2.waitKey(1) == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
