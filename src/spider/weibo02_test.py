from lxml import etree

if __name__ == '__main__':
    with open("C:/Users/Administrator/Desktop/11.html",encoding="UTF-8") as ff:
        html = etree.HTML(ff.read())
        mids = html.xpath('//div/@mid')
        weibos = html.xpath('//div[@mid]/div/div[@class="WB_detail"]/div[@class="WB_text W_f14"]/text()')
        times = html.xpath('//div[@mid]/div/div[@class="WB_detail"]/div[@class="WB_from S_txt2"]/a[1]/text()')

        for mid, weibo, time in zip(mids, weibos, times):
            print(time,mid,str(weibo).replace(' ',''))