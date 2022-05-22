import cv2

resim = cv2.imread("C:\\Users\\Hp\\Desktop\\resim.jpg",0)
cv2.imshow("Resim", resim)

cv2.imwrite("C:\\Users\\Hp\\Desktop\\yeniresim.jpg",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
