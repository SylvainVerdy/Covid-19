import numpy
import pandas as pd

import sys
import subprocess
import requests
import io

class Download:
    def __init__(self, url):
        
        self.url = url
        self.df = pd.DataFrame()
    
    def getDataFrame(self, url):
        df=pd.read_csv(url)
        print(df.head(5))
        return df
    
    def save(self, df):
        df.to_pickle("./data/data.csv")
    
    def getFolderData(self, url):
        """
        getFolderData :  download from git a repository or a folder, with git clone + url 
        """
        folder_url = "https://github.com/ieee8023/covid-chestxray-dataset.git"
        subprocess.call(['git', 'clone', folder_url])
  