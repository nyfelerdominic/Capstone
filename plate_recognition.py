import cv2
import pytesseract
import numpy as np

test_images = [
               'test_img_02.jpg'
               ]
text_border = "===================="
setconfig = r'''-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
                -l eng
                --psm 6
                --oem 3'''

for image_string in test_images:
    print("Output for " + image_string + ":\n")
    img_cv = cv2.imread(image_string) 

    img_cv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    img_cv = cv2.threshold(img_cv, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    
    kernel_in = np.ones((5,5), np.float32)/25
    img_cv = cv2.filter2D(img_cv,-1,kernel_in)


    predicted_result = pytesseract.image_to_string(img_cv, config=setconfig)

    cv2.imshow('img_cv', img_cv)
    cv2.waitKey(0)

    print(predicted_result + "\n" + text_border)

print("\rEND OF TESTS")