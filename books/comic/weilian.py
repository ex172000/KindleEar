#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: insert0003 <https://github.com/insert0003>
from .cartoonmadbase import CartoonMadBaseBook

def getBook():
    return Weilian

class Weilian(CartoonMadBaseBook):
    title               = u'偽戀'
    description         = u'你拿著鎖我拿著鑰匙將其珍視之物 時刻不離帶在身邊等到有一天我們長大再會的時候用這把鑰匙將其中的東西取出來那時候… 我們就結婚吧'
    language            = 'zh-tw'
    feed_encoding       = 'big5'
    page_encoding       = 'big5'
    mastheadfile        = 'mh_comic.gif'
    coverfile           = 'cv_weilian.jpg'
    feeds               = [(u'偽戀', 'http://www.cartoonmad.com/comic/1412.html')]
