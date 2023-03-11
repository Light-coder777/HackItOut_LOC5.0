# !mkdir pan_card_tampering
# !mkdir pan_card_tampering\image
# Using the SSIM algorithm
import numpy as np
from skimage.metrics import structural_similarity
import cv2


def ssim_tampering(original,tampered):
    o_np = np.array(original)
    t_np = np.array(tampered)
    new_o = cv2.resize(o_np,(250, 160))
    new_t = cv2.resize(t_np,(250, 160))
    # if (original.size == tampered.size):
    
    # Convert the images to grayscale
    original_gray = cv2.cvtColor(new_o, cv2.COLOR_BGR2GRAY)
    tampered_gray = cv2.cvtColor(new_t, cv2.COLOR_BGR2GRAY)
    (score, diff) = structural_similarity(original_gray, tampered_gray, full=True)
    diff = (diff * 255).astype("uint8")
    print("SSIM Score is : {}".format(score*100))
    if score >= 80:
        return "The given pan card is original"
    else:
        return "The given pan card is tampered"
    

original = cv2.imread('pan_card_tampering/image/original.png')
tampered = cv2.imread('pan_card_tampering/image/tampered.png')
ssim_tampering(original=original,tampered=tampered)