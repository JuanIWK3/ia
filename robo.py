import cv2
import numpy as np
import serial
import time

# Initialize the serial connection
ser = serial.Serial("COM5", 9600, timeout=1)
time.sleep(2)  # Allow time for the connection to establish

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Step 1: Convert to HSV (you'll process the image matrix manually)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Step 2: Create a binary mask for the red color
    lower_red1 = (0, 120, 70)
    upper_red1 = (10, 255, 255)
    lower_red2 = (170, 120, 70)
    upper_red2 = (180, 255, 255)

    mask1 = np.zeros(hsv.shape[:2], dtype=np.uint8)
    mask2 = np.zeros(hsv.shape[:2], dtype=np.uint8)

    # Manually apply the threshold to each pixel
    for i in range(hsv.shape[0]):
        for j in range(hsv.shape[1]):
            pixel = hsv[i, j]
            if (
                lower_red1[0] <= pixel[0] <= upper_red1[0]
                and lower_red1[1] <= pixel[1] <= upper_red1[1]
                and lower_red1[2] <= pixel[2] <= upper_red1[2]
            ) or (
                lower_red2[0] <= pixel[0] <= upper_red2[0]
                and lower_red2[1] <= pixel[1] <= upper_red2[1]
                and lower_red2[2] <= pixel[2] <= upper_red2[2]
            ):
                mask1[i, j] = 255

    # Combine the two masks
    mask = mask1

    # Step 3: Clean the image using dilation and erosion
    kernel = np.ones((5, 5), np.uint8)
    mask_cleaned = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    frame_center = frame.shape[1] // 2

    # Step 4: Find the centroid of the detected object
    M = cv2.moments(mask_cleaned)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        if cX < frame_center - 50:
            print("Ball is on the left")
            ser.write(b"L")
        elif cX > frame_center + 50:
            print("Ball is on the right")
            ser.write(b"R")
        else:
            print("Ball is centered")
            ser.write(b"S")

        # Draw the centroid on the frame
        cv2.circle(frame, (cX, cY), 5, (255, 0, 0), -1)
    else:
        print("Cannot see the ball")

    # Display the result
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask_cleaned)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
