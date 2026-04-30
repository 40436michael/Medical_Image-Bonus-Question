import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# =====================================
# Create output folder
# =====================================
os.makedirs("output", exist_ok=True)

# =====================================
# Edge Detection Methods Ranking
# 1. Canny
# 2. Sobel
# 3. Laplacian
# 4. LoG
# 5. Prewitt
# 6. Roberts
# =====================================

def process_and_display(image_path, title):

    # Read grayscale image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print(f"Cannot read image: {image_path}")
        return

    img = cv2.resize(img, (512, 512))

    # Preprocessing
    blurred = cv2.GaussianBlur(img, (5,5), 0)

    # =====================================
    # 1. Canny (Rank #1)
    # =====================================
    canny = cv2.Canny(blurred, 50, 150)

    # =====================================
    # 2. Sobel (Rank #2)
    # =====================================
    sobelx = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
    sobel = cv2.magnitude(sobelx, sobely)
    sobel = cv2.normalize(sobel, None, 0, 255, cv2.NORM_MINMAX)
    sobel = np.uint8(sobel)

    # =====================================
    # 3. Laplacian (Rank #3)
    # =====================================
    laplacian = cv2.Laplacian(blurred, cv2.CV_64F)
    laplacian = np.absolute(laplacian)
    laplacian = cv2.normalize(laplacian, None, 0, 255, cv2.NORM_MINMAX)
    laplacian = np.uint8(laplacian)

    # =====================================
    # 4. LoG (Rank #4)
    # =====================================
    log_blur = cv2.GaussianBlur(img, (7,7), 1.5)
    log = cv2.Laplacian(log_blur, cv2.CV_64F)
    log = np.absolute(log)
    log = cv2.normalize(log, None, 0, 255, cv2.NORM_MINMAX)
    log = np.uint8(log)

    # =====================================
    # 5. Prewitt (Rank #5)
    # =====================================
    kernelx = np.array([[1,0,-1],
                        [1,0,-1],
                        [1,0,-1]])

    kernely = np.array([[1,1,1],
                        [0,0,0],
                        [-1,-1,-1]])

    prewittx = cv2.filter2D(blurred, -1, kernelx)
    prewitty = cv2.filter2D(blurred, -1, kernely)

    prewitt = cv2.addWeighted(prewittx, 0.5, prewitty, 0.5, 0)

    # =====================================
    # 6. Roberts (Rank #6)
    # =====================================
    kernelx = np.array([[1,0],
                        [0,-1]])

    kernely = np.array([[0,1],
                        [-1,0]])

    robertsx = cv2.filter2D(blurred, -1, kernelx)
    robertsy = cv2.filter2D(blurred, -1, kernely)

    roberts = cv2.addWeighted(robertsx, 0.5, robertsy, 0.5, 0)

    # =====================================
    # Save images
    # =====================================
    base = title.replace(" ", "_")

    cv2.imwrite(f"output/{base}_original.png", img)
    cv2.imwrite(f"output/{base}_canny.png", canny)
    cv2.imwrite(f"output/{base}_sobel.png", sobel)
    cv2.imwrite(f"output/{base}_laplacian.png", laplacian)
    cv2.imwrite(f"output/{base}_log.png", log)
    cv2.imwrite(f"output/{base}_prewitt.png", prewitt)
    cv2.imwrite(f"output/{base}_roberts.png", roberts)

    # =====================================
    # Display
    # =====================================
    plt.figure(figsize=(16,10))
    plt.suptitle(title, fontsize=18)

    images = [
        img, canny, sobel,
        laplacian, log, prewitt, roberts
    ]

    titles = [
        "Original",
        "1. Canny",
        "2. Sobel",
        "3. Laplacian",
        "4. LoG",
        "5. Prewitt",
        "6. Roberts"
    ]

    for i in range(len(images)):
        plt.subplot(3,3,i+1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.axis("off")

    plt.tight_layout()
    plt.savefig(f"output/{base}_comparison.png", dpi=300)
    plt.show()

    print(f"{title} finished and saved.")

# =====================================
# Main
# =====================================
if __name__ == "__main__":

    # Natural Image
    process_and_display("image/natural.jpg", "Natural Image")

    # Medical Image
    process_and_display("image/medical.jpg", "Medical Image")