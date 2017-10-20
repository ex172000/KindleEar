#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: insert0003 <https://github.com/insert0003>
from .cartoonmadbase import CartoonMadBaseBook

def getBook():
    return Shiji

class Shiji(CartoonMadBaseBook):
    title               = u'亚人'
    description         = u'People don't die.'
    language            = 'zh-tw'
    feed_encoding       = 'big5'
    page_encoding       = 'big5'
    mastheadfile        = 'mh_comic.gif'
    coverfile           = 'cv_yaren.jpg'
    feeds               = [(u'亞人', 'http://www.cartoonmad.com/comic/3572.html')]
