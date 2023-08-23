import cv2
import mediapipe as mp

# Initialize Mediapipe's Hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Initialize video capture
cap = cv2.VideoCapture(0)

finger_tip_ids = [4, 8, 12, 16, 20]  # Finger landmark IDs for the finger tips

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convert the frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame to find hands
    results = hands.process(frame_rgb)
    
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            finger_count = 0
            
            # Check each finger's position relative to the hand landmarks
            for finger_id in range(5):
                tip_id = finger_tip_ids[finger_id]
                tip_landmark = landmarks.landmark[tip_id]
                y_tip = tip_landmark.y
                y_base = landmarks.landmark[tip_id - 2].y
                
                if y_tip < y_base:
                    finger_count += 1
            
            # Draw landmarks and finger count on the frame
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)
            cv2.putText(frame, f"Finger Count: {finger_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Display the frame
    cv2.imshow("Finger Counter", frame)
    
    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
c2.imshow("FINGER COUNTER", frame)