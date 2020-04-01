"""
Author: Sylvain Verdy
contact email: verdy@et.esiea.fr
"""

import numpy as np
import pandas as pd
import cv2
import torch
from PIL import Image
import os
import glob

class PrepareData:
    def __init__(self, path, df):
        self.df = df
        self.path = path
    
    def read_img(self, path):
        images = [cv2.imread(file) for file in glob.glob(path +'*.jpg')]
        print([cv2.imread(file).shape for file in glob.glob(path +'*.jpg')])
        return images
        """for filename in os.listdir(path):
            print(filename)"""

    