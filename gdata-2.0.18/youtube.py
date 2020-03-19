# -*- coding: utf-8 -*-

from gdata import *
import gdata.youtube
import gdata.youtube.service

search_word='undertale'
client=gdata.youtube.service.YouTubeService()
query=gdata.youtube.service.YouTubeVideoQuery()
query.vq=search_word
query.start_index=1
query.max_results=10
query.racy='exclude'
query.orderby='relevance'

feed=client.YouTubeQuery(query)
for entry in feed.entry:
 link = LinkFinder.GetHtmlLink(entry)
 print link

 ♪₍₍(ง・。・)ว⁾⁾♪♪₍₍ ᕕ(・。・ )ᕗ⁾⁾♪
 ♪⁽⁽◝(・。・)◜⁾⁾≡₍₍◞(・。・)◟₎₎♪

 
  