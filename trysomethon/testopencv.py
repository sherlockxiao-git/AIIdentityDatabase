import  cv2

# colored Image

Img = cv2.imread("E:\AIChangingFace\\trysomethon\\2.png", 1)

# Black and White (gray scale)

Img_1 = cv2.imread("E:\AIChangingFace\trysomethon", 0)

# Img = cv2.imread("E:\AIChangingFace\trysomethon", 1)

cv2.imshow("xiao",Img)

cv2.waitKey(0)

cv2.waitKey(2000)

cv2.destroyAllWindows()

