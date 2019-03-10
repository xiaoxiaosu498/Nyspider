import requests
import json

def get_comment():
    for i in range(1,7000):
        # 打印页码
        print(i)
        # headers头部
        headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0', 'Referer': "https://y.qq.com/n/yqq/song/0031TAKo0095np.html"}   
        # 请求的url
        url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk=2058499274&jsonpCallback\=jsoncallback06927647062927766&loginUin=2230661779&hostUin=0&format=jsonp&inCharset=utf8&outCharset=GB2312¬ice=0&platform=yqq&needNewCode=0&cid=205360772&reqtype=2&biztype=1&topid=212877900&cmd=8&needmusiccrit=0&pagenum=%s&pagesize=25&lasthotcommentid=song_212877900_3035803620_1526783365&callback=jsoncallback06927647062927766&domain=qq.com&ct=24&cv=101010' %i
        # 打印当前访问的url地址
        print(url)
        # 将请求得到的页面赋值为req
        req = requests.get(url, headers = headers, verify = False)
        # 对获取到的内容进行utf-8编码
        html = str(req.content, 'utf-8')
        # 对非正规的json进行处理，去掉头部跟尾部多余的部分
        html = html.strip("jsoncallback06927647062927766(")
        html = html.replace(")", "")
        #去掉两边的空格
        html = html.strip()
        #将处理后的json转化为python的json
        data = json.load(html)
        #获取json中评论的部分
        list = data['comment']['commentlist']
        # 每次重新定义一个列表来存储每一页的评论
        content = []
        # 遍历当前页面的评论并通过调用write()函数来保存
        for i in list:
            # 偶尔也会有一页的评论获取不到，这时候如果报错了可以直接忽略这一页，然后继续运行
            try:
                content.append(i['rootcommentcontent']).replace("[em]", "")replace("[/em]","").replace("e400",""))
            except KeyError:
                content = []
                break
        write(content)

# 将当前页面的评论传递过来
def write(content)
    # 打开一个文件，将列表的内容一行一行的存储下来
    with oepn('contents.txt', 'a', encoding = 'utf-8') as f:
        for i in range(len(content)):
            # 因为转json后\n不会自动换行，所以我们将\n进行手动换行
            string = Content[i].split("\\n")
            for i in string:
                #因为出现了很多评论被删除的情况,我们把这句给过滤掉
                i = i.replace("该评论已经被删除"，“”)
                # 打印每条评论
                print(i)
                # 将评论写入文本
                f.writelines(i)
                #给评论换行
                f.write("\n")

if __name__ == "__main__":
    get_comment()