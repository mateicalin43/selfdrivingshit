#region of interest


def region_of_interest(image):
    height = image.shape[0]
    polygons = np.array([
    [(200, height ), (1100, height), (550, 250)]
    ])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image
