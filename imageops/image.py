import numpy as np
from PIL import Image as PILImage


class Image():
    """
    Container for an image. Goal is to have the data represented in a form that 
    is ready to do operations on, such as a numpy array.

    For color:
    Enforce 3rd dimension in array ordered like: R, G, B, alpha (optional)
    """
    def __init__(self):
        self.num_channels = 0
        self.data = np.array([])

    def read(self, path: str):
        img = PILImage.open(path)
        self.data = np.array(img)
        self.num_channels = self.data.shape[2]

    def to_grayscale(self) -> np.ndarray:
        return (0.2126 * self.data[:,:,0]) + (0.7152 * self.data[:,:,1]) + (0.722 * self.data[:,:,2])

