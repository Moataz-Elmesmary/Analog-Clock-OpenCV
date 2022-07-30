import cv2
import numpy as np 
import datetime
import math


radius = 200
center = (250,250)

def get_ticks():
    hours_init = []
    hours_dest = []

    for i in range(0,360,6):
        x_coordinate = int(center[0] + radius * math.cos(i * math.pi / 180))
        y_coordinate = int(center[1] + radius * math.sin(i * math.pi / 180))

        hours_init.append((x_coordinate,y_coordinate))

    for i in range(0,360,6):
        x_coordinate = int(center[0] + (radius-20) * math.cos(i * math.pi / 180))
        y_coordinate = int(center[1] + (radius-20) * math.sin(i * math.pi / 180))

        hours_dest.append((x_coordinate,y_coordinate))

    return hours_init, hours_dest



def get_date():
    dt = datetime.datetime.now()
    day = dt.strftime('%A')
    date = dt.strftime('%b %d, %Y')
    return day, date

def draw_time(image):
    time_now = datetime.datetime.now().time()
    hour = math.fmod(time_now.hour, 12)
    minute = time_now.minute
    second = time_now.second

    second_angle = math.fmod(second * 6 + 270, 360)
    minute_angle = math.fmod(minute * 6 + 270, 360)
    hour_angle = math.fmod((hour*30) + (minute/2) + 270, 360)

    second_x = int(center[0] + (radius-25) * math.cos(second_angle * math.pi / 180))
    second_y = int(center[1] + (radius-25) * math.sin(second_angle * math.pi / 180))
    cv2.line(image, center, (second_x, second_y), (0, 255, 255), 1)

    minute_x = int(center[0] + (radius-60) * math.cos(minute_angle * math.pi / 180))
    minute_y = int(center[1] + (radius-60) * math.sin(minute_angle * math.pi / 180))
    cv2.line(image, center, (minute_x, minute_y), (0, 255, 0), 2)

    hour_x = int(center[0] + (radius-100) * math.cos(hour_angle * math.pi / 180))
    hour_y = int(center[1] + (radius-100) * math.sin(hour_angle * math.pi / 180))
    cv2.line(image, center, (hour_x, hour_y), (255, 191, 0), 4)

    cv2.circle(image, center, 5, (125, 125, 125), -1)

    return image



image = np.zeros((500,500,3), dtype=np.uint8)
image[:] = (0,0,0)
#image[:] = [255,255,255]


hours_init, hours_dest = get_ticks()
day, date = get_date()

for i in range(len(hours_init)):
    if i % 5 == 0:
        #cv2.line(image, hours_init[i], hours_dest[i], (0, 255, 255), 3)
        cv2.circle(image, hours_init[i], 4, (0, 255, 255), 2)
    else:
        cv2.circle(image, hours_init[i], 3, (0, 255, 255), 1)


cv2.circle(image, (250, 250), 203, (0, 0, 255), 2)
cv2.putText(image, date, (0,20), 1, 2, (255, 191, 0), 2, cv2.LINE_AA)

time_now = datetime.datetime.now().time()
cv2.putText(image, str(time_now), (0,46), 1, 2, (255, 191, 0), 2, cv2.LINE_AA)

while True:
    image_original = image.copy()

    clock_face = draw_time(image_original)

    cv2.imshow('clock', image_original)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()