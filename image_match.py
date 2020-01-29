import cv2
import numpy as np
import urllib


def url_to_image(url):
	resp = urllib.request.urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	return image


def doesmatch(url):
    mainimage = url_to_image(url)
    #img_rgb = cv2.imread('mainimage.jpg')
    img_gray = cv2.cvtColor(mainimage, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('template.jpg',0)

    w,h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

    threshold = 0.8

    loc = np.where(res>=threshold)


    if loc[0].size == 0:
        return False
    else:
        return True




#else:
#    for pt in zip (*loc[::-1]):
#        cv2.rectangle(img_rgb,pt,(pt[0]+w,pt[1]+h), (0,255,255),2)





#cv2.imshow('Detected',img_rgb)
#cv2.waitKey(0)
