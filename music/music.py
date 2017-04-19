# -*- coding: utf-8 -*-
import web
from get_music import get_music_url

urls = (
    '/', 'Index',
    '/s', 'Search',
)

app = web.application(urls, globals())
render = web.template.render('templates')


class Index:
    def GET(self):
        return render.index()


class Search:
    def GET(self):
        i = web.input()
        name = i.get('name')
        mp3url, mp3pic = get_music_url(name)
        return render.index(mp3url=mp3url, bgimg=mp3pic)

if __name__ == '__main__':
    app.run()