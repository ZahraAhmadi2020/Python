import cv2
import mss
import numpy as np

# Set the screen size
monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20.0,
                      (monitor["width"], monitor["height"]))

with mss.mss() as sct:
    while True:
        frame = sct.grab(monitor)
        img = np.array(frame)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

        out.write(img)
        cv2.imshow("Screen Recorder", img)

        # Stop recording with 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

out.release()
cv2.destroyAllWindows()
