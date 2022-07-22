import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
image2 = gray
zeros = np.zeros(frame.shape[:2], dtype = "uint8")
begin = 0
end = 5
changenum = 10000
# image 2 = 처음 이미지
time_count = 0

while cap.isOpened() == True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    image1 = gray
    # subtract와 비슷한 역할-인터넷 검색하기
    sframe = cv2.absdiff(image2, image1)
    # cv2.threshold(입력 파일, 기준값, 기준값이상일때 바뀌는 값, type) -> retval(기준값 출력), dst(결과 출력)
    trash, sframe2 = cv2.threshold(sframe, 50, 255, cv2.THRESH_BINARY)
    pnum = sum(sum(sframe2))
    cv2.putText(frame, str(pnum), (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    B, G, R =  cv2.split(frame)
    end = time.time()
    if pnum > changenum:
        begin = time.time()
        end = time.time()
    if 3 < end - begin:
        cv2.imshow("cctv", frame)
    else:
        cv2.imshow("cctv", cv2.merge([zeros, zeros, R]))
        end = time.time()
    image2 = image1
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.release()
cv2.destroyAllWindows()