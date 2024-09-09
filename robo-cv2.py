import cv2
import numpy as np
import serial
import time

# Initialize the serial connection
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # Adjust to your correct serial port
time.sleep(2)  # Allow time for the connection to establish

# Initialize the webcam
cap = cv2.VideoCapture(1)  # Adjust the camera index if necessary

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Step 1: Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Step 2: Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(hsv, (11, 11), 0)

    # Step 3: Create a binary mask for the red color
    lower_red1 = (0, 120, 70)
    upper_red1 = (10, 255, 255)
    lower_red2 = (170, 120, 70)
    upper_red2 = (180, 255, 255)

    mask1 = cv2.inRange(blurred, lower_red1, upper_red1)
    mask2 = cv2.inRange(blurred, lower_red2, upper_red2)

    # Combine both masks
    mask = mask1 | mask2

    # Step 4: Perform morphological operations to remove small noise
    kernel = np.ones((5, 5), np.uint8)
    mask_cleaned = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Step 5: Find contours
    contours, _ = cv2.findContours(mask_cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    frame_center = frame.shape[1] // 2
    ball_detected = False

    for contour in contours:
        area = cv2.contourArea(contour)

        # Filter by size (adjust the minimum area to suit your case)
        if area > 500:
            # Check for circularity
            perimeter = cv2.arcLength(contour, True)
            if perimeter > 0:
                circularity = 4 * np.pi * (area / (perimeter ** 2))
                if 0.7 <= circularity <= 1.3:
                    # Find the centroid of the ball
                    M = cv2.moments(contour)
                    if M["m00"] != 0:
                        cX = int(M["m10"] / M["m00"])
                        cY = int(M["m01"] / M["m00"])
                        ball_detected = True

                        # Soft turning logic
                        if cX < frame_center - 50:
                            print("Ball is on the left")
                            ser.write(b"L")  # Turn left softly
                        elif cX > frame_center + 50:
                            print("Ball is on the right")
                            ser.write(b"R")  # Turn right softly
                        else:
                            print("Ball is centered")
                            ser.write(b"F")  # Move forward

                        # Draw the contour and centroid on the frame
                        cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
                        cv2.circle(frame, (cX, cY), 5, (255, 0, 0), -1)
                    break  # Process only the first large circular object

    if not ball_detected:
        print("Cannot see the ball")
        ser.write(b"N")  # "N" for no ball detected

    # Display the result
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask_cleaned)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
