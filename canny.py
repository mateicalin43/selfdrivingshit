# canny wheeeeee

def canny(image):
    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
    #reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    #canny
    canny = cv2.Canny(blur, 50, 150)
    return canny
