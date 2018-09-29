# -*- coding: utf-8 -*-
"""

"""
import vlc

URL = {
        'dorognoe':'http://dorognoe.hostingradio.ru:8000/radio',
        'shanson_barnaul':'http://stream.fmprod.ru:8000/chanson',
        'shanson_kiev':'http://media.brg.ua:8000/m3u/shanson'
      }

player = vlc.MediaPlayer(URL['shanson_kiev'])
player.play()
