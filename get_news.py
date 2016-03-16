#!/usr/bin/env python

import feedparser

from apcontent import alarmpi_content

class news(alarmpi_content):
  def build(self):
    try:
      rss_url = 'http://' + self.sconfig['host'] + self.sconfig['path']
      rss = feedparser.parse(rss_url)

      #for entry in rss.entries[:4]:
      #    print entry['title']
      #    print entry['description']
      #    
      #print rss.entries[0]['title']
      #print rss.entries[0]['description']
      #print rss.entries[1]['title']
      #print rss.entries[1]['description']
      #print rss.entries[2]['title']
      #print rss.entries[2]['description']
      #print rss.entries[3]['title']
      #print rss.entries[3]['description']

      newsfeed = rss.entries[0]['title'] + '.  ' + rss.entries[0]['description'] + '.  ' + rss.entries[1]['title'] + '.  ' + rss.entries[1]['description'] + '.  ' + rss.entries[2]['title'] + '.  ' + rss.entries[2]['description'] + '.  ' + rss.entries[3]['title'] + '.  ' + rss.entries[3]['description'] + '.  ' 

      # print newsfeed
      newsfeed = newsfeed.encode('utf-8')

      # Today's news from BBC
      news = 'Y ahora, Las ultimas noticias de la seccion internacional de BBC news' + newsfeed
        

    except rss.bozo:
      news = 'Fallo conexion a BBC. '

    if self.debug:
      print news

    self.content = news
