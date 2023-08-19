import requests
from bs4 import BeautifulSoup
import config
import os
class spider:
    headers = config.config.headers
    def __init__(self):
        pass
    def GetVideo(self,url): #获取指定壁纸页面中的视频链接，返回一个元组，第一个元素为视频链接，第二个元素为视频标题
        res=requests.get(url=url,headers=self.headers).text
        soup=BeautifulSoup(res,features="html.parser")
        return (soup.find('video',attrs={'id':'myVideo'}).get('src'),soup.find('h1',attrs={"class":"pt-2 font-semibold text-gray-150 text-sm"}).text.replace('\n','').strip())
    def GetSearchVideo(self,keyword:str,page=1): #获取搜索页面特点页数的壁纸链接
            if int(page)==1:
                res = requests.get("https://bizhi.cheetahfun.com/search.html?search={}&page={}".format(keyword, page)).text
                soup=BeautifulSoup(res,features="html.parser")
                linklist = soup.find_all('a',attrs={"data-wallpaper-type":"0"})
                for link in linklist:
                    url=link.get('href')
                    yield self.GetVideo(url=url)
            elif int(page)>1:
                for i in range(page+1):
                    res = requests.get("https://bizhi.cheetahfun.com/search.html?search={}&page={}".format(keyword, page)).text
                    soup = BeautifulSoup(res, features="html.parser")
                    linklist = soup.find_all('a', attrs={"data-wallpaper-type": "0"})
                    if linklist !=True:
                        return "暂未搜索到壁纸,请更换关键词或减少页数"
                    for link in linklist:
                        url=link.get('href')
                        yield self.GetVideo(url=url)
            else:
                return 0
    def DownloadVideo(self,url:str,path,data,name): #下载视频
            if os.path.exists(path=path) !=True:
                os.mkdir(path)
            filename=path+name+'.mp4'
            with open(filename,mode='wb')as f:
                f.write(data)
    def DownloadLinkVideo(self,url,path): #下载某个壁纸
        Videolink=self.GetVideo(url=url)[0]
        data=requests.get(Videolink,headers=self.headers).content
        self.DownloadVideo(url=Videolink,path=path,data=data,name=self.GetVideo(url)[1])
        print("{}.mp4 Done!".format(self.GetVideo(url)[1]))
    def DownloadSearchVideo(self,keyword:str,path,page:int=1,):
        for i in self.GetSearchVideo(keyword,page):
            data=requests.get(i[0],headers=self.headers).content
            self.DownloadVideo(url=i[0],path=path,data=data,name=i[1])
            print("{}.mp4 Done!".format(i[1]))