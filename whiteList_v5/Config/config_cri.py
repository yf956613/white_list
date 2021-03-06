# 国际在线
TASK_NAME = 'cri_net'

# 起始URL
START_URL = 'http://www.cri.cn/'

# 控制域，必须为list格式
DOMAIN = ['cri.cn']
# 请求头
HEADERS = {
    'Host': 'news.cri.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://news.cri.cn/china/',
    'Connection': 'keep-alive',
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
        "title": ".//*[@class='atitle']/text()",
        "publish_time": ".//*[@class='apublishtime']/text()|.//*[@class='acreatedtime']/text()",
        "soruce": "substring-after(.//*[@class='asource'],'来源：')",
        "author": "",
        "belong": "string(.//*[@class='crumbs'])",
        "content": ".//*[@id='abody']/descendant::text()",
        "editor": "substring-after(.//*[@class='aeditor'],'编辑：')",
    },
    {
        "title": ".//*[@class='slider-top']/h3/text()",
        "publish_time": ".//*[@class='slider-tinfo-left fl']/span[1]/text()",
        "soruce": "substring-after(.//*[contains(text(),'来源')],'来源：')",
        "author": "",
        "belong": "",
        "content": ".//*[@class='abody']/descendant::p/text()",
        "editor": "substring-after(.//*[contains(text(),'编辑')],'编辑:')",

    }
]


# 正则匹配规则,此处为静态页面url的正则表达式，匹配以下的规则的网址将抓取其中新闻内容
REGEX_URL = r'/\d{8}/.*\.html'

