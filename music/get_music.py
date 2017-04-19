# -*- coding: utf-8 -*-
import urllib2
import json


def get_music_url(name):
    name = name.encode('utf-8')
    html = urllib2.urlopen('http://s.music.163.com/search/get/?type=1&s=%s&limit=1' % urllib2.quote(name)).read()
    text = json.loads(html)
    if len(text['result']['songs']) == 0:
        return
    mp3url = text['result']['songs'][0]['audio']
    mp3img = text['result']['songs'][0]['album']['picUrl']
    return mp3url, mp3img


if __name__ == '__main__':
    print get_music_url('喜欢你')