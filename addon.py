# -*- coding: utf-8 -*-

"""
    PyLearner Add-on
    Author: Twilight

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

import os, sys, urlparse, urllib
import xbmc, xbmcaddon, xbmcgui, xbmcplugin

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

params = urlparse.parse_qs(sys.argv[2][1:])
action = params.get('action', None)


def action_url(query):
    return addon_url + '?' + urllib.urlencode(query)


items = [
        {
         'title': 'Python Programming Tutorials',
         'icon': 'https://i.ytimg.com/vi/DkW5CSZ_VII/mqdefault.jpg',
         'index': 'plugin://plugin.video.youtube/channel/UCJbPGzawDH1njbqV-D5HqKw/playlist/PLEA1FEF17E1E5C0DA/',
         'auto':  'plugin://plugin.video.youtube/?path=/root/video&action=play_all&playlist=$PLEA1FEF17E1E5C0DA'
        },
        {
         'title': 'Python 3.4 Programming Tutorials',
         'icon': 'https://i.ytimg.com/vi/HBxCHonP6Ro/mqdefault.jpg',
         'index': 'plugin://plugin.video.youtube/channel/UCJbPGzawDH1njbqV-D5HqKw/playlist/PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_/',
         'auto':  'plugin://plugin.video.youtube/?path=/root/video&action=play_all&playlist=$PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_'
        },
        {
         'title': 'Pygame (Python Game Development) Playlist',
         'icon': 'https://i.ytimg.com/vi/K5F-aGDIYaM/mqdefault.jpg',
         'index': 'plugin://plugin.video.youtube/channel/UCJbPGzawDH1njbqV-D5HqKw/playlist/PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq/',
         'auto':  'plugin://plugin.video.youtube/?path=/root/video&action=play_all&playlist=$PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq'
        },
        {
         'title': 'Python GUI Development with GTK+ 3',
         'icon': 'https://i.ytimg.com/vi/0O11oEp7QYw/mqdefault.jpg',
         'index': 'plugin://plugin.video.youtube/channel/UCJbPGzawDH1njbqV-D5HqKw/playlist/PL6gx4Cwl9DGBBnHFDEANbv9q8T4CONGZE/',
         'auto':  'plugin://plugin.video.youtube/?path=/root/video&action=play_all&playlist=$PL6gx4Cwl9DGBBnHFDEANbv9q8T4CONGZE'
        },
        {
         'title': 'Python GUI with Tkinter Playlist',
         'icon': 'https://i.ytimg.com/vi/RJB1Ek2Ko_Y/mqdefault.jpg',
         'index': 'plugin://plugin.video.youtube/channel/UCJbPGzawDH1njbqV-D5HqKw/playlist/PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d/',
         'auto':  'plugin://plugin.video.youtube/?path=/root/video&action=play_all&playlist=$PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d'
        },
        {
         'title': 'Python Basic Tutorials',
         'icon': 'https://i.ytimg.com/vi/mk4625XRkwU/mqdefault.jpg',
         'index': 'plugin://plugin.video.youtube/channel/UCfzlCWGWYyIQ0aLC5w48gBQ/playlist/PLQVvvaa0QuDdFqJtqsyeEewqVm_7VRrlD/',
         'auto':  'plugin://plugin.video.youtube/?path=/root/video&action=play_all&playlist=$PLQVvvaa0QuDdFqJtqsyeEewqVm_7VRrlD'
        },
        {
         'title': 'Intermediate Python Tutorials',
         'icon': 'https://i.ytimg.com/vi/8PzDfykGg_g/mqdefault.jpg',
         'index': 'plugin://plugin.video.youtube/channel/UCfzlCWGWYyIQ0aLC5w48gBQ/playlist/PLQVvvaa0QuDfhTF3Zfyzc_yD-Mq9iTp4G/',
         'auto':  'plugin://plugin.video.youtube/?path=/root/video&action=play_all&playlist=$PLQVvvaa0QuDfhTF3Zfyzc_yD-Mq9iTp4G'
        },
        {
         'title': 'Python 3 Basics Tutorial Series ',
         'icon': 'https://i.ytimg.com/vi/IX6mc9l6tY4/mqdefault.jpg',
         'index': 'plugin://plugin.video.youtube/channel/UCfzlCWGWYyIQ0aLC5w48gBQ/playlist/PLQVvvaa0QuDe8XSftW-RAxdo6OmaeL85M/',
         'auto':  'plugin://plugin.video.youtube/?path=/root/video&action=play_all&playlist=$PLQVvvaa0QuDe8XSftW-RAxdo6OmaeL85M'
        },
        {
         'title': 'Pygame - Making Games with Python',
         'icon': 'https://i.ytimg.com/vi/Y7joZ67mC6o/mqdefault.jpg',
         'index': 'plugin://plugin.video.youtube/channel/UCfzlCWGWYyIQ0aLC5w48gBQ/playlist/PLQVvvaa0QuDcxG_Cajz1JyTH6eAvka93C/',
         'auto':  'plugin://plugin.video.youtube/?path=/root/video&action=play_all&playlist=$PLQVvvaa0QuDcxG_Cajz1JyTH6eAvka93C'
        },
        {
         'title': 'wxPython: Making Windows / GUIs for user-friendliness',
         'icon': 'https://i.ytimg.com/vi/NMjV_HGLAQE/mqdefault.jpg',
         'index': 'plugin://plugin.video.youtube/channel/UCEpe5DhhS0HYFBaCVsU2Iwg/playlist/PLQVvvaa0QuDc4SQhfpm6XHO0l-1Ybtur2/',
         'auto':  'plugin://plugin.video.youtube/?path=/root/video&action=play_all&playlist=$PLQVvvaa0QuDc4SQhfpm6XHO0l-1Ybtur2'
        },
        {
         'title': 'PyQT Python GUI Application Development with Python',
         'icon': 'https://i.ytimg.com/vi/JBME1ZyHiP8/mqdefault.jpg',
         'index': 'plugin://plugin.video.youtube/channel/UCEpe5DhhS0HYFBaCVsU2Iwg/playlist/PLQVvvaa0QuDdVpDFNq4FwY9APZPGSUyR4/',
         'auto':  'plugin://plugin.video.youtube/?path=/root/video&action=play_all&playlist=$PLQVvvaa0QuDdVpDFNq4FwY9APZPGSUyR4'
        },
        {
         'title': 'Python Tutorials',
         'icon': 'https://i.ytimg.com/vi/FsAPt_9Bf3U/mqdefault.jpg',
         'index': 'plugin://plugin.video.youtube/channel/UCCezIgC97PvUuR4_gbFUs5g/playlist/PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU/',
         'auto':  'plugin://plugin.video.youtube/?path=/root/video&action=play_all&playlist=$PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU'
        },
        {
         'title': 'Python OOP Tutorials - Working with Classes',
         'icon': 'https://i.ytimg.com/vi/ZDa-Z5JzLYM/mqdefault.jpg',
         'index': 'plugin://plugin.video.youtube/channel/UCCezIgC97PvUuR4_gbFUs5g/playlist/PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc/',
         'auto':  'plugin://plugin.video.youtube/?path=/root/video&action=play_all&playlist=$PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc'
        },
        {
         'title': 'Python - Setting up a Python Environment',
         'icon': 'https://i.ytimg.com/vi/YJC6ldI3hWk/mqdefault.jpg',
         'index': 'plugin://plugin.video.youtube/channel/UCCezIgC97PvUuR4_gbFUs5g/playlist/PL-osiE80TeTt66h8cVpmbayBKlMTuS55y/',
         'auto':  'plugin://plugin.video.youtube/?path=/root/video&action=play_all&playlist=$PL-osiE80TeTt66h8cVpmbayBKlMTuS55y'
        },
        {
         'title': 'Python Tutorial for Beginners (For Absolute Beginners)',
         'icon': 'https://i.ytimg.com/vi/41qgdwd3zAg/mqdefault.jpg',
         'index': 'plugin://plugin.video.youtube/channel/UCs6nmQViDpUw0nuIx9c_WvA/playlist/PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n/',
         'auto':  'plugin://plugin.video.youtube/?path=/root/video&action=play_all&playlist=$PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n'
        },
        {
         'title': 'Python Tutorials',
         'icon': 'https://i.ytimg.com/vi/P74JAYCD45A/mqdefault.jpg',
         'index': 'plugin://plugin.video.youtube/channel/UCbhm6TbMBTWn_GxrIbPFapA/playlist/PLGzru6ACxEALhcvY18A-iox-mEoieHMVG/',
         'auto':  'plugin://plugin.video.youtube/?path=/root/video&action=play_all&playlist=$PLGzru6ACxEALhcvY18A-iox-mEoieHMVG'
        },
        {
         'title': 'Pro Python Programming Course',
         'icon': 'https://i.ytimg.com/vi/fKO32pt6CpE/mqdefault.jpg',
         'index': 'plugin://plugin.video.youtube/channel/UCbhm6TbMBTWn_GxrIbPFapA/playlist/PLGzru6ACxEAKorNc8bMhv2vTa0qGbjBcD/',
         'auto':  'plugin://plugin.video.youtube/?path=/root/video&action=play_all&playlist=$PLGzru6ACxEAKorNc8bMhv2vTa0qGbjBcD'
        },
        {
         'title': 'Python Glossary',
         'icon': 'https://i.ytimg.com/vi/5aS8oIm2CoA/mqdefault.jpg',
         'index': 'plugin://plugin.video.youtube/channel/UCbhm6TbMBTWn_GxrIbPFapA/playlist/PLGzru6ACxEAI40_BjeVIboIzlmgRv4RuL/',
         'auto':  'plugin://plugin.video.youtube/?path=/root/video&action=play_all&playlist=$PLGzru6ACxEAI40_BjeVIboIzlmgRv4RuL'
        },
        {
         'title': 'Learn Python 3 By Example',
         'icon': 'https://i.ytimg.com/vi/Ov125thke0s/mqdefault.jpg',
         'index': 'plugin://plugin.video.youtube/channel/UCbhm6TbMBTWn_GxrIbPFapA/playlist/PLGzru6ACxEAISepi3SZ-doH9MJ8XNYLTQ/',
         'auto':  'plugin://plugin.video.youtube/?path=/root/video&action=play_all&playlist=$PLGzru6ACxEAISepi3SZ-doH9MJ8XNYLTQ'
        },
        {
         'title': 'Python GUI',
         'icon': 'https://i.ytimg.com/vi/hKvphf5L5L4/mqdefault.jpg',
         'index': 'plugin://plugin.video.youtube/channel/UCbhm6TbMBTWn_GxrIbPFapA/playlist/PLGzru6ACxEAJu4Aa3HnOqrBfCIs_ftmeQ/',
         'auto':  'plugin://plugin.video.youtube/?path=/root/video&action=play_all&playlist=$PLGzru6ACxEAJu4Aa3HnOqrBfCIs_ftmeQ'
        },
        {
         'title': 'Zero to Hero with Python Tutorial FULL - Easy Learning python 3.4 from begin to advance',
         'icon': 'https://yt3.ggpht.com/-gOuki6sqKD8/AAAAAAAAAAI/AAAAAAAAAAA/bPPb2wYyOdM/s256-c-k-no-mo-rj-c0xffffff/photo.jpg',
         'url': 'plugin://plugin.video.youtube/play/?video_id=pTV6bILLP_s'
        },
        {
         'title': 'Python Programming Tutorial | Learn Python programming | Python language',
         'icon': 'https://yt3.ggpht.com/-doHjtyH8IV4/AAAAAAAAAAI/AAAAAAAAAAA/iVDcOtCdcrw/s256-c-k-no-mo-rj-c0xffffff/photo.jpg',
         'url': 'plugin://plugin.video.youtube/play/?video_id=BTzav965P7w',
        }
        ]


# Build Root Menu:
def main_menu():

    xbmc.executebuiltin('Container.SetViewMode(50)')

    bucky_playlists = []
    sentex_playlists = []
    coreyschafer_playlists = []
    mastercodeonline_playlists = []
    z2h_videos = []

    ####################################################################################################################
    _list_item = xbmcgui.ListItem(label='[COLOR red]Bucky - "The new Boston" playlists:[/COLOR]')
    _list_item.setInfo('video', {'title': '[COLOR red]Bucky - "The new Boston" playlists:[/COLOR]'})
    _list_item.setArt({'icon': 'https://yt3.ggpht.com/-XkSKloPzgjg/AAAAAAAAAAI/AAAAAAAAAAA/zXjJK7mxrHw/s256-c-k-no-mo-rj-c0xffffff/photo.jpg', 'fanart': addonfanart})

    addDirItem(handle=addon_handle, url=None, listitem=_list_item, isFolder=False)

    for item in items[:5]:
        _list_item = xbmcgui.ListItem(label=item['title'])
        _list_item.setInfo('video', {'title': item['title']})
        _list_item.setArt({'icon': item['icon'], 'fanart': addonfanart})
        _url = item['index']
        _isFolder = True
        bucky_playlists.append((_url, _list_item, _isFolder))

    addDirItems(addon_handle, bucky_playlists)

    ####################################################################################################################
    _list_item = xbmcgui.ListItem(label='[COLOR red]Sentdex\'s Playlists:[/COLOR]')
    _list_item.setInfo('video', {'title': '[COLOR red]Sentdex\'s Playlists:[/COLOR]'})
    _list_item.setArt({'icon': 'https://yt3.ggpht.com/-kHTbb6oDqmY/AAAAAAAAAAI/AAAAAAAAAAA/BHWd_jlJmJU/s256-c-k-no-mo-rj-c0xffffff/photo.jpg', 'fanart': addonfanart})

    addDirItem(handle=addon_handle, url=None, listitem=_list_item, isFolder=False)

    for item in items[5:11]:
        _list_item = xbmcgui.ListItem(label=item['title'])
        _list_item.setInfo('video', {'title': item['title']})
        _list_item.setArt({'icon': item['icon'], 'fanart': addonfanart})
        _url = item['index']
        _isFolder = True
        sentex_playlists.append((_url, _list_item, _isFolder))

    addDirItems(addon_handle, sentex_playlists)

    ####################################################################################################################
    _list_item = xbmcgui.ListItem(label='[COLOR red]Corey Schafer\'s Playlists:[/COLOR]')
    _list_item.setInfo('video', {'title': '[COLOR red]Corey Schafer\'s Playlists:[/COLOR]'})
    _list_item.setArt({'icon': 'https://yt3.ggpht.com/-s6PgRDss0XQ/AAAAAAAAAAI/AAAAAAAAAAA/fb7pMinwZh8/s256-c-k-no-mo-rj-c0xffffff/photo.jpg', 'fanart': addonfanart})

    addDirItem(handle=addon_handle, url=None, listitem=_list_item, isFolder=False)

    for item in items[11:14]:
        _list_item = xbmcgui.ListItem(label=item['title'])
        _list_item.setInfo('video', {'title': item['title']})
        _list_item.setArt({'icon': item['icon'], 'fanart': addonfanart})
        _url = item['index']
        _isFolder = True
        coreyschafer_playlists.append((_url, _list_item, _isFolder))

    addDirItems(addon_handle, coreyschafer_playlists)

    ####################################################################################################################
    _list_item = xbmcgui.ListItem(label='[COLOR red]ProgrammingKnowledge\'s Playlists:[/COLOR]')
    _list_item.setInfo('video', {'title': '[COLOR red]ProgrammingKnowledge\'s Playlists:[/COLOR]'})
    _list_item.setArt({'icon': 'https://yt3.ggpht.com/-doHjtyH8IV4/AAAAAAAAAAI/AAAAAAAAAAA/iVDcOtCdcrw/s256-c-k-no-mo-rj-c0xffffff/photo.jpg', 'fanart': addonfanart})

    addDirItem(handle=addon_handle, url=None, listitem=_list_item, isFolder=False)

    _list_item = xbmcgui.ListItem(label=items[14]['title'])
    _list_item.setInfo('video', {'title': items[14]['title']})
    _list_item.setArt({'icon': items[14]['icon'], 'fanart': addonfanart})
    _url = items[14]['index']
    addDirItem(handle=addon_handle, url=_url, listitem=_list_item, isFolder=True)

    ####################################################################################################################
    _list_item = xbmcgui.ListItem(label='[COLOR red]Master Code Online\'s Playlists:[/COLOR]')
    _list_item.setInfo('video', {'title': '[COLOR red]Master Code Online\'s Playlists:[/COLOR]'})
    _list_item.setArt({'icon': 'https://yt3.ggpht.com/-eVR4D5YRYdI/AAAAAAAAAAI/AAAAAAAAAAA/Pvvsnj87qXw/s256-c-k-no-mo-rj-c0xffffff/photo.jpg', 'fanart': addonfanart})

    addDirItem(handle=addon_handle, url=None, listitem=_list_item, isFolder=False)

    for item in items[15:20]:
        _list_item = xbmcgui.ListItem(label=item['title'])
        _list_item.setInfo('video', {'title': item['title']})
        _list_item.setArt({'icon': item['icon'], 'fanart': addonfanart})
        _url = item['index']
        _isFolder = True
        mastercodeonline_playlists.append((_url, _list_item, _isFolder))

    addDirItems(addon_handle, mastercodeonline_playlists)

    ####################################################################################################################
    _list_item = xbmcgui.ListItem(label='[COLOR red]Zero-to-Hero one-time long videos:[/COLOR]')
    _list_item.setInfo('video', {'title': '[COLOR red]Zero-to-Hero one-time long videos:[/COLOR]'})
    _list_item.setArt({'icon': addonicon, 'fanart': addonfanart})

    addDirItem(handle=addon_handle, url=None, listitem=_list_item, isFolder=False)

    for item in items[20:]:
        _list_item = xbmcgui.ListItem(label=item['title'])
        _list_item.setInfo('video', {'title': item['title']})
        _list_item.setArt({'icon': item['icon'], 'fanart': addonfanart})
        _url = action_url({'action': 'play', 'item': item['url']})
        _isFolder = False
        z2h_videos.append((_url, _list_item, _isFolder))

    addDirItems(addon_handle, z2h_videos)

    ####################################################################################################################
    endDir(addon_handle)


if action is None:
    main_menu()

elif action[0] == 'play':

    url = params['item'][0]

    if url == items[20]['url']:
        execute('Playmedia("plugin://plugin.video.youtube/play/?video_id=pTV6bILLP_s")')

    elif url == items[21]['url']:
        execute('Playmedia("plugin://plugin.video.youtube/play/?video_id=BTzav965P7w")')

