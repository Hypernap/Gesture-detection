import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
def rhs():
  for hand_landmarks in results.multi_hand_landmarks:
      for point in mp_hands.HandLandmark:
        nl0 = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
        nl4 = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        if nl4.x<nl0.x :
            return True
def indexISclose():
  for hand_landmarks in results.multi_hand_landmarks:
      for point in mp_hands.HandLandmark:
        nl8 = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        nl7 = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP]
        nl6 = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP]
        if nl7.y > nl6.y and nl8.y>nl6.y:
          return True

def thumbISclose():
  for hand_landmarks in results.multi_hand_landmarks:
      for point in mp_hands.HandLandmark:
        nl4 = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
        nl3 = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
        nl2 = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP]
        if nl3.x > nl2.x and nl4.x>nl2.x:
          return True

def middleISclose():
  for hand_landmarks in results.multi_hand_landmarks:
      for point in mp_hands.HandLandmark:
        nl12 = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
        nl11 = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP]
        nl10 = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP]
        if nl12.y > nl10.y and nl11.y>nl10.y:
          return True

def ringISclose():
  for hand_landmarks in results.multi_hand_landmarks:
      for point in mp_hands.HandLandmark:
        nl16 = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
        nl15 = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP]
        nl14 = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP]
        if nl16.y > nl14.y and nl15.y>nl14.y:
          return True

def pinkyISclose():
  for hand_landmarks in results.multi_hand_landmarks:
      for point in mp_hands.HandLandmark:
        nl20 = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
        nl19 = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP]
        nl18 = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP]
        if nl20.y > nl18.y and nl19.y>nl18.y:
          return True

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(max_num_hands=1,
    min_detection_confidence=0.55,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    image = cv2.flip(image,0)
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
          if rhs():#For only Right hands
            mp_drawing.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            for point in mp_hands.HandLandmark:
                if thumbISclose() and indexISclose() and middleISclose() and ringISclose() and pinkyISclose():
                  for hand_landmarks in results.multi_hand_landmarks:
                    for point in mp_hands.HandLandmark:
                      nl0 = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
                      print("Hand closed")



    cv2.imshow('MediaPipe Hands', image)#FOR DISPLAY
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
