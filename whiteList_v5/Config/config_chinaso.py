# 中国搜索
TASK_NAME = 'chinaso'

# 起始URL
START_URL = 'http://www.chinaso.com/'

# 控制域，必须为list格式
DOMAIN = ['chinaso.com']
# 请求头
HEADERS = {
    'Host': 'www.chinaso.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0'
}


# xpath规则
XPATHER_HREF = ".//*/@href"
# 字段模版
# {
#     "title": "",
#     "publish_time": "",
#     "source": "",
#     "author": "",
#     "belong": "",
#     "content": "",
#     "editor": "",
# },
XPATHER_NEWS_LIST = [
    {
        "title": ".//*[@class='detail-title']/text()",
        "publish_time": "substring-before(.//*[@class='detail-time'],'|')",
        "source": "substring-after(.//*[@class='detail-time'],'|')",
        "author": "",
        "belong": "string(.//*[@class='report_crumb5'])",
        "content": ".//*[@class='detail-content']//*[@class='detail-main']/descendant::text()",
        "editor": "substring-after(.//*[@class='editor'],'编辑：')",
    }
]

# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d+[_]*\d*.[s]*htm[l]*'



