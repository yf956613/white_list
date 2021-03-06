# 瞭望东方
TASK_NAME = 'cac_gov'

# 起始URL
START_URL = 'http://www.cac.gov.cn/'

# 控制域，必须为list格式
DOMAIN = ['cac.gov.cn']
# 请求头
HEADERS = {
    'Host': 'www.cac.gov.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0',
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
        "title": ".//*[@id='title']/descendant::text()",
        "publish_time": ".//*[@id='pubtime']/text()",
        "soruce": "substring-after(.//*[@id='source'],'来源：')",
        "author": "",
        "belong": "string(.//*[@id='bread'])",
        "content": ".//*[@id='content']/descendant::text()",
        "editor": "",
    }
]


# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{4}-\d{2}/\d+/\w+_\d*\.[s]*htm[l]*'

