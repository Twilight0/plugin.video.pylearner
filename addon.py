# -*- coding: utf-8 -*-

"""
    PyLearner Add-on
    Author: Twilight0

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 2 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.

        You should have received a copy of the GNU General Public License
        along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os, sys, urlparse, urllib2
import xbmc, xbmcaddon, xbmcgui, xbmcplugin
import CommonFunctions as common
# import YDStreamExtractor

# Commands:
join = os.path.join
Addon = xbmcaddon.Addon()
language = Addon.getLocalizedString
addonname = Addon.getAddonInfo("name")
addonid = Addon.getAddonInfo("id")
addonpath = Addon.getAddonInfo("path")
addonfanart = Addon.getAddonInfo("fanart")
addonicon = join(addonpath, 'icon.png')

addDirItem = xbmcplugin.addDirectoryItem
addDirItems = xbmcplugin.addDirectoryItems
endDir = xbmcplugin.endOfDirectory
execute = xbmc.executebuiltin

# Handlers:
addon_url = sys.argv[0]
addon_handle = int(sys.argv[1])

params = dict(urlparse.parse_qsl(sys.argv[2][1:]))
action = params.get('action', None)


def opener(url):

    requester = urllib2.Request(url)
    requester.add_header('User-Agent', 'Mozilla/5.0 (msie 11.0; windows nt 6.2 ; Trident/7.0; rv:11.0) like Gecko')
    response = urllib2.urlopen(requester)
    result = response.read()
    response.close()

    return result


def txt_box(heading, announce):
    window_id = 10147
    control_id1 = 1
    control_id2 = 5
    gui_window = xbmcgui.Window(window_id)

    execute('ActivateWindow(%d)' % window_id)
    xbmc.sleep(500)

    gui_window.getControl(control_id1).setLabel(heading)

    try:
        txt = open(announce)
        text = txt.read()

    except:
        text = announce

    gui_window.getControl(control_id2).setText(str(text))

    return


def cheat_sheet(cs_link):

    raw = opener(cs_link)

    txt_box('Python Cheat Sheet', raw)


def constructor():

    main = []

    _xml_ = opener('http://thgiliwt.offshorepastebin.com/pylearner.xml')

    result = common.parseDOM(_xml_, 'item')

    for item in result:
        title = common.parseDOM(item, 'title')
        icon = common.parseDOM(item, 'icon')
        url = common.parseDOM(item, 'url')
        _type_ = common.parseDOM(item, 'type')

        item_data = ({'title': title[0], 'icon': addonicon if icon[0] == '' else icon[0], 'url': url[0].
                     replace('https://www.youtube.com/channel', 'plugin://plugin.video.youtube/channel').
                     replace('https://www.youtube.com/watch?v=', 'plugin://plugin.video.youtube/play/?video_id='),
                     "type": str(_type_).strip('[]\'u')})
        main.append(item_data)

    return main


# Build Root Menu:
def main_menu():

    xbmc.executebuiltin('Container.SetViewMode(50)')

    item_list = []

    items = constructor()

    for item in items:

        list_item = xbmcgui.ListItem(label=item['title'], iconImage=item['icon'])
        list_item.setInfo('video', {'title': item['title']})
        list_item.setArt({'thumb': item['icon'], 'fanart': addonfanart})

        if item['type'] == 'sep':
            url = addon_url
            isFolder = False

        elif item['type'] == 'video':
            # url = item['url']
            url = '{0}?action=play&url={1}'.format(addon_url, item['url'])
            isFolder = False

        elif item['type'] == 'index':
            url = item['url']
            isFolder = True

        elif item['type'] == 'pycheat':
            url = '{0}?action=pycheat&url={1}'.format(addon_url, item['url'])
            isFolder = False

        else:
            url = addon_url
            isFolder = False

        item_list.append((url, list_item, isFolder))

    addDirItems(addon_handle, item_list)
    endDir(addon_handle, cacheToDisc=False)


# def play_item(path, name, icon):
#
#     plot = """Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.
#     Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java.
#     The language provides constructs intended to enable writing clear programs on both a small and large scale.
#     Python supports multiple programming paradigms, including object-oriented, imperative and functional programming or procedural styles.
#     It features a dynamic type system and automatic memory management and has a large and comprehensive standard library.
#     Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems.
#     Using third-party tools, such as Py2exe or Pyinstaller, Python code can be packaged into stand-alone executable programs for some of the most popular operating systems, so Python-based software can be distributed to, and used on, those environments with no need to install a Python interpreter.
#     Above description was taken from wikipedia: https://en.wikipedia.org/wiki/Python_(programming_language)"""
#
#     list_item = xbmcgui.ListItem(path=path)
#     list_item.setInfo('video', {'title': name, 'plot': plot})
#     list_item.setArt({'thumb': icon})
#     xbmcplugin.setResolvedUrl(addon_handle, True, listitem=list_item)

if action is None:
    main_menu()

elif action == 'play':

    execute('PlayMedia("{0}")'.format(params['url']))

#     stream = YDStreamExtractor.getVideoInfo(params['url'])
#     url = stream.streamURL()
#     title = stream.selectedStream()['title']
#     thumb = stream.selectedStream()['thumbnail']
#     #plot = stream.selectedStream()['description']
#     play_item(url, title, thumb)

elif action == 'pycheat':

    cheat_sheet(params['url'])
