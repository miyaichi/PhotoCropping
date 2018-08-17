import cv2

face_retio = 0.6  # 顔の高さの割合
top_ratio = 0.1  # 顔の上のスペースの割合
classifier = 'Script\haarcascade_frontalface_alt.xml' # 分類器

def expand(rect, scale):
    (x, y, w, h) = rect
    y = y - int(h * scale / 100)
    h = h + int(h * scale / 100)
    return (x, y, w, h)


def facedetect(gray):
    cascade = cv2.CascadeClassifier(classifier)
    rects = cascade.detectMultiScale(gray, 1.11, 5)
    if len(rects) > 0:
        return rects[0]
    return None


def crop(before, after, width = 180, height = 255, scale=20):
    """
    Recognize face, crop image and resize.

    Args:
        before (str): Image file name to be processed.
        after (str): Image file name after processing.
        width (int): Width of the processed image (pixels).
        height (int): Height of the processed image (pixels).
        scale (int): Hair and face ratio (percentage)

    Returns:
        bool: True if the pcocess succeeds.
    """
    image = cv2.imread(before)

    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)

    # 顔認識
    face = facedetect(gray)
    if face is None:
        # Can not detect face.
        return False

    # 髪の毛の部分をscaleパラメータを使って拡張
    (fx, fy, fw, fh) = expand(face, scale)

    # 位置決め
    h = int(fh / face_retio)
    y = fy - int(h * top_ratio)
    w = int(h / height * width)
    x = fx + int(fw / 2) - int(w / 2)

    # トリミング
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    photo = rgb[y:y + h, x:x + w]
    photo = cv2.resize(photo, (width, height))

    # 切り抜いた画像の書き出し
    photo = cv2.cvtColor(photo, cv2.COLOR_RGB2BGR)
    cv2.imwrite(after, photo)

    return True
