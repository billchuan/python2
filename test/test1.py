import time
import urllib
from urllib import request

# 构造请求头信息
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64)\
AppleWebKit/537.36 (KHTML, like Gecko)\
Chrome/63.0.3239.132 Safari/537.36"
}


def loadpage(fullurl, filename):
    print("正在下载：", filename)
    req = request.Request(fullurl, headers=header)
    resp = request.urlopen(req).read()
    return resp


def writepage(html, filename):
    print("正在保存：", filename)

    with open(filename, "wb") as f:
        f.write(html)

    print("---------------------------")


# 构造url
def tiebaSpider(url, begin, end):
    for page in range(begin, end + 1):
        pn = (page - 1) * 50
        fullurl = url + "&pn=" + str(pn)  # 每次请求的完整url
        filename = "D:/学习/Python/第" + str(page) + "页.html"  # 每次请求后保存的文件名

        html = loadpage(fullurl, filename)  # 调用爬虫，爬取网页
        writepage(html, filename)  # 把获取到的网页信息写入本地


if __name__ == '__main__':
    kw = input("请输入贴吧名：")
    begin = int(input("请输入起始页："))
    end = int(input("请输入结束页："))

    url = "http://tieba.baidu.com/f?"

    key = urllib.parse.urlencode({"kw": kw})

    url = url + key

    tiebaSpider(url, begin, end)

    time.sleep(10)
