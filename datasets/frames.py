
import cv2

def grabar():
    cap = cv2.VideoCapture('D:\\AI\\Stairs\\datasets\\images\\escalera.mp4')
    i = 0
    count=0
    # a variable to set how many frames you want to skip
    frame_skip = 10
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if i > frame_skip - 1:
            cv2.imwrite('frame_{}.jpg'.format(count), frame)
            count=count+1
            print('Done frame '+str(count))
            i = 0
            continue
        i += 1

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    grabar()