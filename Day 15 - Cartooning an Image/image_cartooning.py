import cv2
import matplotlib.pyplot as plt

# read image
img = cv2.imread('Elon_Musk.jpg')

# Preprocess the Image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9
)

# Apply the Cartoon Effect
color = cv2.bilateralFilter(img, 9, 300, 300)
cartoon = cv2.stylization(color, sigma_s=150, sigma_r=0.25)

# save and show image
cv2.imwrite('Elon_Musk_Toon.jpg', cartoon)
plt.imshow(cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB))
plt.title('Cartoon Image')
plt.show()
