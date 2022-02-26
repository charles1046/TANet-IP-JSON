# from bs4 import BeautifulSoup

# import requests
#
# html_doc = requests.get('https://zh.wikipedia.org/wiki/TANet')
# with open('./raw.txt', 'w', encoding='UTF8') as raw:
#     raw.write(html_doc.text)

# soup = BeautifulSoup(html_doc.text, 'html.parser')


#############################################################
# import get_info
# import json
#
# with open('./raw.txt', 'r', encoding='UTF8') as raw:
#     r = raw.read()
#
# result = {}
# ranged = {}
# name_error = {}
# no_url = {}
#
# print('start')
# while '<li>' in r:
#     start_pos = r.find('<li>')
#     end_pos = r.find('</li>')+4
#     name_start_pos = r.find('title')+7
#     name_end_pos = r.find('">')
#     name = r[name_start_pos:name_end_pos]
#
#     ip_start_pos = r.find('</a>')+4
#     ip_end_pos = r.find('</li>')
#     ip = r[ip_start_pos:ip_end_pos]
#     ip = ip.replace('<b>', '').replace('</b>', '').replace('—', '')
#     # print(name+':'+ip+'='+get_info.get_picture_url(name))
#     url = get_info.get_picture_url(name)
#     if url == -1:
#         no_url[ip] = name
#         print('[NO_URL]'+name)
#
#     elif 'x' in ip or '~' in ip or ',' in ip:
#         ranged[ip] = url
#         print('[RANGED]'+name)
#
#     else:
#         result[ip] = url
#         get_info.download_picture(name, url)
#
#     r = r.replace(r[start_pos:end_pos], '')
#
# with open('./TANet.json', 'w', encoding='UTF8') as t:
#     json.dump(result, t, indent=4, ensure_ascii=False)
#
# with open('./TANet_ranged.json', 'w', encoding='UTF8') as t:
#     json.dump(ranged, t, indent=4, ensure_ascii=False)
#
# with open('./TANet_no_url.json', 'w', encoding='UTF8') as t:
#     json.dump(no_url, t, indent=4, ensure_ascii=False)
#
# with open('./TANet_name_error.json', 'w', encoding='UTF8') as t:
#     json.dump(name_error, t, indent=4, ensure_ascii=False)
#
# print('end')
################################################################

# soup = BeautifulSoup(r, 'html.parser')
# li_tags = soup.findAll('li')
# for tag in li_tags:
#     a_tag = tag.find_all('a')
#     result += a_tag.get('title')
#     print(str(tag.string).strip())


# pos = 0
# while 'title=' in r:
#     r = r.replace(r[pos:r.find('title=')+6], '')
#     pos = r.find('</b>')
#
# with open('./name_ip_raw.txt', 'w', encoding='UTF8') as name_ip_raw:
#     name_ip_raw = name_ip_raw.write(r)
# import get_info
#
# get_info.get_picture_url('')
import json

school = input()
if school != -1:
    with open('./TANet_140112_140125.json', 'r', encoding='UTF8') as f:
        file = json.load(f)
        print(file[school]['name']+'='+file[school]['url'])
    school = input()
