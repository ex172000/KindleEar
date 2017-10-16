#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: insert0003 <https://github.com/insert0003>
from .cartoonmadbase import CartoonMadBaseBook

def getBook():
    return Shiji

class Shiji(CartoonMadBaseBook):
    title               = u'食戟之靈'
    description         = u'由《少年疾驅》的作者附田老師跟里漫畫界的名畫師佐伯俊(也就是tosh老師)合作的jump next主打短篇!'
    language            = 'zh-tw'
    feed_encoding       = 'big5'
    page_encoding       = 'big5'
    mastheadfile        = 'mh_comic.gif'
    coverfile           = 'cv_shiji.jpg'
    feeds               = [(u'食戟之靈', 'http://www.cartoonmad.com/comic/1698.html')]
