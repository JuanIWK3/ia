import cv2
import serial
import time

# Initialize the serial connection
ser = serial.Serial('COM5', 9600, timeout=1)
time.sleep(2)  # Allow time for the connection to establish

# Initialize the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to HSV for color detection
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the color range for detecting the red ball
    lower_red1 = (0, 120, 70)
    upper_red1 = (10, 255, 255)
    lower_red2 = (170, 120, 70)
    upper_red2 = (180, 255, 255)

    # Create two masks for the red color and combine them
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.add(mask1, mask2)

    # Find contours of the detected object
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Assume the largest contour is the ball
        ball_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(ball_contour)
        center_x = x + w // 2

        # Draw a rectangle around the ball
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Determine if the ball is on the left or right
        frame_center = frame.shape[1] // 2

        if center_x < frame_center - 50:
            print("Ball is on the left")
            ser.write(b'L')
        elif center_x > frame_center + 50:
            print("Ball is on the right")
            ser.write(b'R')
        else:
            print("Ball is centered")
            ser.write(b'S')
    else:
        # If no ball is detected, stop the robot
        print("Cannot see the ball")
        ser.write(b'S')

    # Display the frame with the detected ball
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
ser.close()
