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

        item_data = ({'title': title[0], 'icon': addonicon if icon[0] == '' else icon[0], 'url': url[0], "type": str(_type_).strip('[]\'u')})
        main.append(item_data)

    return main


# Build Root Menu:
def main_menu():

    xbmc.executebuiltin('Container.SetViewMode(50)')

    item_list = []

    items = constructor()

    for item in items:

        list_item = xbmcgui.ListItem(label=item['title'])
        list_item.setInfo('video', {'title': item['title']})
        list_item.setArt({'icon': item['icon'], 'fanart': addonfanart})

        if item['type'] == 'sep':
            url = None
            isFolder = False
            list_item.setProperty('IsPlayable', 'false')
        elif item['type'] == 'video':
            url = '{0}?action=play&url={1}'.format(addon_url, item['url'])
            isFolder = False
            list_item.setProperty('IsPlayable', 'true')
        elif item['type'] == 'index':
            url = item['url']
            isFolder = True
            list_item.setProperty('IsPlayable', 'false')
        elif item['type'] == 'pycheat':
            url = '{0}?action=pycheat&url={1}'.format(addon_url, item['url'])
            isFolder = False
            list_item.setProperty('IsPlayable', 'false')
        else:
            url = None
            isFolder = False

        item_list.append((url, list_item, isFolder))

    addDirItems(addon_handle, item_list)
    endDir(addon_handle)


if action is None:
    main_menu()

elif action == 'play':

    execute('Playmedia("{0}")'.format(params['url']))

elif action == 'pycheat':

    cheat_sheet(params['url'])
