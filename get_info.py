import requests


def get_picture_url(school_name):
    r = requests.get('https://zh.wikipedia.org/wiki/'+school_name).text
    start_pos = r.find('https://upload.wikimedia')
    if start_pos == -1:
        r = requests.get('https://zh.wikipedia.org/wiki/'+school_name).text
        start_pos = r.find('https://upload.wikimedia')
        if start_pos == -1:
            return -1
    r = r.replace(r[:start_pos], '')
    end_pos = r.find('"')
    r = r.replace(r[end_pos:], '')
    return r


def download_picture(school_name, url):
    with open(f'./logo/{school_name}.jpg    ', 'wb') as handle:
        response = requests.get(url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)

