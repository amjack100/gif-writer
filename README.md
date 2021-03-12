<h1 align="center">Gif Writer </h1>
<p>
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

Record image iterations through any loop and output a gif

## Usage

```python
from gif_writer import GifWriter
```

## Example

When you're iterating through images, maybe you'd like to have a better intuitive feel for how your code is operating.

In this example, we can examine the step-by-step output of loop that applies a basic gaussian blur.

```python
    with GifWriter("./output.gif", fps=60) as gw:
        for i in range(h, img.shape[0] - h):
            for j in range(w, img.shape[1] - w):
                x = img[i - h : i - h + kh, j - w : j - w + kw]
                x = x.flatten() * kernel.flatten()
                image_conv[i][j] = x.sum()
            gw.record(image_conv)
```

<!-- ![](./docs/out1.gif) -->

![](./docs/frog-small.jpg)
![](./docs/out2.gif)
