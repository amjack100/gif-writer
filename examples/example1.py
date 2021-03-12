import numpy as np
from PIL import Image
from tqdm import tqdm

from gif_writer import GifWriter

img = Image.open("./frog-small.jpg")

ar = np.array(img)
ar = np.einsum("abc->cab", ar)[0]
# print(ar.shape)


def conv(img, kernel):

    kh = kernel.shape[0]
    kw = kernel.shape[1]

    img = np.pad(
        img,
        pad_width=((kh // 2, kh // 2), (kw // 2, kw // 2)),
        mode="constant",
        constant_values=0,
    ).astype(np.float32)

    h = kh // 2
    w = kw // 2

    image_conv = np.zeros(img.shape)

    with GifWriter("./out2.gif", fps=60) as gw:
        for i in tqdm(range(h, img.shape[0] - h)):
            # print(i)
            for j in range(w, img.shape[1] - w):
                # sum = 0
                x = img[i - h : i - h + kh, j - w : j - w + kw]
                x = x.flatten() * kernel.flatten()
                # print(x)
                image_conv[i][j] = x.sum()
            gw.record(image_conv)

        # print(kernel.flatten())
    h_end = -h
    w_end = -w

    if h == 0:
        return image_conv[h:, w:w_end]
    if w == 0:
        return image_conv[h:h_end, w:]

    return image_conv[h:h_end, w:w_end]


sigma = 3
filter_size = 2 * int(4 * sigma + 0.5) + 1
gaussian_filter = np.zeros((filter_size, filter_size), np.float32)

m = filter_size // 2
n = filter_size // 2
with GifWriter("./out1.gif", fps=60) as gw:
    for i, x in enumerate(range(-m, m + 1)):
        for j, y in enumerate(range(-n, n + 1)):
            x1 = 2 * np.math.pi * (sigma ** 2)
            x2 = np.math.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2))
            # print(f"{x + m} - {y + n}")
            gaussian_filter[x + m, y + n] = (1 / x1) * x2
            gw.record(gaussian_filter)

out_img = conv(ar, gaussian_filter)
