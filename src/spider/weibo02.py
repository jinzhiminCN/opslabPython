import json
import requests
from lxml import etree

url = 'https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100505&page={}&pagebar={}&id=1005056274518158&pre_page={}'
# 配置请求头
headers = {
    'Host': 'weibo.com',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'https://weibo.com/u/6274518158?is_all=1',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cookie': 'SINAGLOBAL=8212814080343.729.1559355475260; wb_cmtLike_5204661479=1; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFiUqwsZXz.1KWr1PmBU0Ui5JpX5KMhUgL.Fo-EehBcSo2XS0.2dJLoIXnLxK-LBKBLBK.LxK-L1-eLBo5LxKBLBonL12BLxK-L1h-L1h2LxKMLBK-L1--LxK.LB-BL1KBLxKBLBonL12BLxKnLB--LBont; wb_view_log_5204661479=1680*10501; ALF=1592922164; SSOLoginState=1561386165; SCF=AveC-MnO06SGd_HeoHET-rkKnRPJoAhjjV7dzbMHVfMpK7sWc-cqV-g3d0cu3K55o_9Pvif9sV4L88Nanlu0Bzs.; SUB=_2A25wFKzmDeRhGeNM61YX9i_IzDWIHXVTY5kurDV8PUNbmtBeLVL4kW9NTlwY-wkVR4htxP3WmLWFFCkJpgtBFdKq; SUHB=0y0J80dPo-iYrF; YF-V5-G0=7e17aef9f70cd5c32099644f32a261c4; _s_tentry=login.sina.com.cn; UOR=,,login.sina.com.cn; Apache=1168818027494.0364.1561386155491; ULV=1561386155536:19:19:4:1168818027494.0364.1561386155491:1561383665719; Ugrow-G0=140ad66ad7317901fc818d7fd7743564; YF-Page-G0=f1e19cba80f4eeaeea445d7b50e14ebb|1561390518|1561390282; webim_unReadCount=%7B%22time%22%3A1561390503584%2C%22dm_pub_total%22%3A0%2C%22chat_group_pc%22%3A0%2C%22allcountNum%22%3A0%2C%22msgbox%22%3A0%7D'
}


def parse_response(response, fp):
    html = etree.HTML(response)
    mids = html.xpath('//div/@mid')
    weibos = html.xpath('//div[@mid]/div/div[@class="WB_detail"]/div[@class="WB_text W_f14"]/text()')
    times = html.xpath('//div[@mid]/div/div[@class="WB_detail"]/div[@class="WB_from S_txt2"]/a[1]/text()')

    for mid, weibo, time in zip(mids, weibos, times):
        fp.write(mid+'-' + time +"-"+ str(weibo).replace(' ', '') + '\n\n')


def main():
    # 从文件中随机获取useragents
    fp = open('c:/weibo.txt', 'a+', encoding='utf8')
    global url
    # 页码循环
    for page in range(10):
        # 每一页又分为两部分加载
        for pagebar in range(0, 2):
            url = url.format(page, pagebar, page)
            response = requests.get(url=url, headers=headers)
            text = response.text.replace("\\t", "").replace("\\n", "").replace("\\r", "") \
                .replace("\\/", "/").replace("\\\\'", "'")
            #print(text)
            json_data = json.loads(text)
            print(json_data['code'], "===>", url)
            # 获取网页代码
            parse_response(json_data['data'].replace("\\\"", "\""), fp)

    fp.close()


if __name__ == '__main__':
    main()
