# -*- coding: UTF-8 -*-
import requests,re,thread,time

def get_content(j,ulr,interval):
    with open(str(j)+'.jpg',"wb") as f:
        each = requests.get(url)
        f.write(each.content)
        print str(j)+ '.jpg 下载完成'
        time.sleep(interval)
    thread.exit_thread()


start_page = input('输入起始页面')
end_page = input('输入结束页面')

for page in range(start_page,end_page):
    qiushi_url = 'https://www.qiushibaike.com/imgrank/page/%d'%page
    try:
        content = requests.get(qiushi_url)
    except:
        print '读取图片失败'
    else:

        print '开始下载'
        list_pic_ulr = re.findall(r'//pic.qiushibaike.com/system/pictures/.*/medium/.*jpg', content.text)

        for i in range(len(list_pic_ulr)):
            list_pic_ulr[i] = 'http:' + list_pic_ulr[i]
        # print list_pic_ulr

        j = 0
        for url in list_pic_ulr:
            thread.start_new_thread(get_content, (j, url, 1))
            j += 1
            time.sleep(2)











