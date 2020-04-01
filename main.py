"""
Author : Sylvain Verdy
Contact : sylvain.verdy.pro@gmail.com
"""

import pandas as pd
import download as download
from preparedata import PrepareData

class Main:

    def __init__(self):
        self.data = pd.DataFrame()
        self.dl = download.Download("https://raw.githubusercontent.com/ieee8023/covid-chestxray-dataset/master/metadata.csv")
        
    def download_data(self):
        url_repo = "https://github.com/ieee8023/covid-chestxray-dataset/tree/master/images"
        df = self.dl.getDataFrame("https://raw.githubusercontent.com/ieee8023/covid-chestxray-dataset/master/metadata.csv")
        self.dl.getFolderData(url_repo)
        print(df)
        try:
            self.dl.save(df)
        except:
            print("already saved")
        return df

    def getImages(self, path):
        images = preparedata.read_img(path)

main = Main()
path="./data/images/"
preparedata = PrepareData(path, df=pd.DataFrame())
main.getImages(path)