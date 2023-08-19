from spider import spider
spider=spider.spider()


def main():

    print("\033[0;32;40m欢迎使用元气壁纸下载器命令行版本，gui版本正在制作中\033[0m")
    print("\033[0;32;40m目前支持两种模式，模式1输入壁纸链接  模式2输入搜索关键词和页数\033[0m")
    print("\033[0;32;40m获取壁纸链接请前往https://bizhi.cheetahfun.com/\033[0m")
    print("\033[0;32;40m保存路径请以/结尾  例如./test/  而不是./test\033[0m")
    print("\033[0;32;40m使用模式2时若闪退请减少页数或更换关键词\033[0m")
    while 1:
        f=input("请输入1或者2 输入exit退出: ")
        if f=='1':
            link=input("请输入壁纸链接: ")
            path=input("请输入保存路径：")
            spider.DownloadLinkVideo(url=link,path=path)
        elif f=='2':
            keyword=input("请输入关键词: ")
            page=input("请输入下载页数(必填): ")
            path=input("请输入保存路径")
            spider.DownloadSearchVideo(keyword,path,page)
        elif f=='exit':
            break
        else:
            print("输入错误")
            continue
if __name__=='__main__':
    main()