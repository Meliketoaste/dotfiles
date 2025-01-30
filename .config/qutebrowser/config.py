# pylint: disable=C0111
c = c  # noqa: F821 pylint: disable=E0602,C0103
config = config  # noqa: F821 pylint: disable=E0602,C0103
# base16-qutebrowser (https://github.com/theova/base16-qutebrowser)
# Base16 qutebrowser template by theova
# Gruvbox dark, hard scheme by Dawid Kurek (dawikur@gmail.com), morhetz (https://github.com/morhetz/gruvbox)

# base16-qutebrowser (https://github.com/theova/base16-qutebrowser)
# Scheme name: Tomorrow Night
# Scheme author: Chris Kempson (http://chriskempson.com)
# Template author: theova
# Commentary: Tinted Theming: (https://github.com/tinted-theming)
base00 = "#101010"
base01 = "#232323"
base02 = "#303032"
base03 = "#333333"
base04 = "#999999"
base05 = "#b7b7b7"
base06 = "#c1c1c1"
base07 = "#d5d5d5"
base08 = "#de6e6e"
base09 = "#dab083"
base0A = "#ffc799"
base0B = "#5f8787"
base0C = "#60a592"
base0D = "#8eaaaa"
base0E = "#d69094"
base0F = "#876c4f"

  # base00: "#101010"
  # base01: "#232323"
  # base02: "#222222"
  # base03: "#333333"
  # base04: "#999999"
  # base05: "#b7b7b7"
  # base06: "#c1c1c1"
  # base07: "#d5d5d5"
  # base08: "#de6e6e"
  # base09: "#dab083"
  # base0A: "#ffc799"
  # base0B: "#5f8787"
  # base0C: "#60a592"
  # base0D: "#8eaaaa"
  # base0E: "#d69094"
  # base0F: "#876c4f"

# Aliases for commands. The keys of the given dictionary are the
# aliases, while the values are the commands they map to.
# Type: Dict
c.aliases = {
    "q": "quit",
    "w": "session-save",
    "wq": "quit --save",
}


c.fonts.default_family = "JetBrainsMono Nerd Font"
c.fonts.default_size = "9pt"
# set qutebrowser colors
# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.

# set qutebrowser colors

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
c.colors.completion.fg = base05

# Background color of the completion widget for odd rows.
c.colors.completion.odd.bg = base01

# Background color of the completion widget for even rows.
c.colors.completion.even.bg = base00

# Foreground color of completion widget category headers.
c.colors.completion.category.fg = base0A

# Background color of the completion widget category headers.
c.colors.completion.category.bg = base00

# Top border color of the completion widget category headers.
c.colors.completion.category.border.top = base00

# Bottom border color of the completion widget category headers.
c.colors.completion.category.border.bottom = base00

# Foreground color of the selected completion item.
c.colors.completion.item.selected.fg = base05

# Background color of the selected completion item.
c.colors.completion.item.selected.bg = base02

# Top border color of the selected completion item.
c.colors.completion.item.selected.border.top = base02

# Bottom border color of the selected completion item.
c.colors.completion.item.selected.border.bottom = base02

# Foreground color of the matched text in the selected completion item.
c.colors.completion.item.selected.match.fg = base0B

# Foreground color of the matched text in the completion.
c.colors.completion.match.fg = base0B

# Color of the scrollbar handle in the completion view.
c.colors.completion.scrollbar.fg = base05

# Color of the scrollbar in the completion view.
c.colors.completion.scrollbar.bg = base00

# Background color of disabled items in the context menu.
c.colors.contextmenu.disabled.bg = base01

# Foreground color of disabled items in the context menu.
c.colors.contextmenu.disabled.fg = base04

# Background color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.bg = base00

# Foreground color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.fg = base05

# Background color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.bg = base02

# Foreground color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.fg = base05

# Background color for the download bar.
c.colors.downloads.bar.bg = base00

# Color gradient start for download text.
c.colors.downloads.start.fg = base00

# Color gradient start for download backgrounds.
c.colors.downloads.start.bg = base0D

# Color gradient end for download text.
c.colors.downloads.stop.fg = base00

# Color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = base0C

# Foreground color for downloads with errors.
c.colors.downloads.error.fg = base08

# Font color for hints.
c.colors.hints.fg = base00

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
c.colors.hints.bg = base0A

# Font color for the matched part of hints.
c.colors.hints.match.fg = base03

# Text color for the keyhint widget.
c.colors.keyhint.fg = base05

# Highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = base05

# Background color of the keyhint widget.
c.colors.keyhint.bg = base00

# Foreground color of an error message.
c.colors.messages.error.fg = base00

# Background color of an error message.
c.colors.messages.error.bg = base08

# Border color of an error message.
c.colors.messages.error.border = base08

# Foreground color of a warning message.
c.colors.messages.warning.fg = base00

# Background color of a warning message.
c.colors.messages.warning.bg = base0E

# Border color of a warning message.
c.colors.messages.warning.border = base0E

# Foreground color of an info message.
c.colors.messages.info.fg = base05

# Background color of an info message.
c.colors.messages.info.bg = base00

# Border color of an info message.
c.colors.messages.info.border = base00

# Foreground color for prompts.
c.colors.prompts.fg = base05

# Border used around UI elements in prompts.
c.colors.prompts.border = base00

# Background color for prompts.
c.colors.prompts.bg = base00

# Background color for the selected item in filename prompts.
c.colors.prompts.selected.bg = base02

# Foreground color for the selected item in filename prompts.
c.colors.prompts.selected.fg = base05

# Foreground color of the statusbar.
c.colors.statusbar.normal.fg = base0B

# Background color of the statusbar.
c.colors.statusbar.normal.bg = base00

# Foreground color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = base0D

# Background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = base00

# Foreground color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.fg = base0C

# Background color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.bg = base00

# Foreground color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = base05

# Background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = base01

# Foreground color of the statusbar in command mode.
c.colors.statusbar.command.fg = base05

# Background color of the statusbar in command mode.
c.colors.statusbar.command.bg = base00

# Foreground color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = base00

# Background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = base05

# Foreground color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = base0E

# Background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = base00

# Foreground color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = base0D

# Background color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.bg = base00

# Background color of the progress bar.
c.colors.statusbar.progress.bg = base0D

# Default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = base05

# Foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = base08

# Foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = base05

# Foreground color of the URL in the statusbar on successful load
# (http).
c.colors.statusbar.url.success.http.fg = base0C

# Foreground color of the URL in the statusbar on successful load
# (https).
c.colors.statusbar.url.success.https.fg = base0B

# Foreground color of the URL in the statusbar when there's a warning.
c.colors.statusbar.url.warn.fg = base0E

# Background color of the tab bar.
c.colors.tabs.bar.bg = base00

# Color gradient start for the tab indicator.
c.colors.tabs.indicator.start = base0D

# Color gradient end for the tab indicator.
c.colors.tabs.indicator.stop = base0C

# Color for the tab indicator on errors.
c.colors.tabs.indicator.error = base08

# Foreground color of unselected odd tabs.
c.colors.tabs.odd.fg = base05

# Background color of unselected odd tabs.
c.colors.tabs.odd.bg = base01

# Foreground color of unselected even tabs.
c.colors.tabs.even.fg = base05

# Background color of unselected even tabs.
c.colors.tabs.even.bg = base00

# Background color of pinned unselected even tabs.
c.colors.tabs.pinned.even.bg = base0C

# Foreground color of pinned unselected even tabs.
c.colors.tabs.pinned.even.fg = base07

# Background color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.bg = base0B

# Foreground color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.fg = base07

# Background color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.bg = base02

# Foreground color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.fg = base05

# Background color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.bg = base02

# Foreground color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.fg = base05

# Foreground color of selected odd tabs.
c.colors.tabs.selected.odd.fg = base05

# Background color of selected odd tabs.
c.colors.tabs.selected.odd.bg = base02

# Foreground color of selected even tabs.
c.colors.tabs.selected.even.fg = base05

# Background color of selected even tabs.
c.colors.tabs.selected.even.bg = base02

## Background color for webpages if unset (or empty to use the theme's
## color).
# c.colors.webpage.bg = base03

# Dark mode
c.colors.webpage.darkmode.enabled = True
c.colors.webpage.darkmode.policy.images = "never"

c.completion.open_categories = ["bookmarks", "history", "filesystem"]

# Directory to save downloads to. If unset, a sensible OS-specific
# default is used.
# Type: Directory

# Default font families to use. Whenever "default_family" is used in a
# font setting, it's replaced with the fonts listed here. If set to an
# empty value, a system-specific monospace default is used.
# Type: List of Font, or Font

# Default font size to use. Whenever "default_size" is used in a font
# setting, it's replaced with the size listed here. Valid values are
# either a float value with a "pt" suffix, or an integer value with a
# "px" suffix.
# Type: String

# Position of the tab bar.
# Type: Position
# Valid values:
#   - top
#   - bottom
#   - left
#   - right
c.tabs.position = "left"

# When to show the tab bar.
# Type: String
# Valid values:
#   - always: Always show the tab bar.
#   - never: Always hide the tab bar.
#   - multiple: Hide the tab bar if only one tab is open.
#   - switching: Show the tab bar when switching tabs.
c.tabs.show = "switching"


c.url.searchengines = {
    "DEFAULT": "https://duckduckgo.com/?q={}",
    "!": "https://duckduckgo.com/?q={}",
    "!i": "https://duckduckgo.com/?q={}&ia=images&iax=images",
    "!discogs": "https://www.discogs.com/search/?q={}",
    "!c": "https://github.com/search?q={}&type=code",
    "!github": "https://github.com/{}",
    "!gi": "https://www.google.com/search?tbm=isch&source=hp&q={}",
    "!gmaps": "https://www.google.com/maps/search/{}",
    "!greasyfork": "https://greasyfork.org/en/scripts?q={}",
    "!libgenfic": "http://libgen.rs/fiction/?q={}",
    "!libgen": "http://libgen.rs/search.php?req={}",
    "!lobsters": "https://lobste.rs/search?q={}&what=stories&order=relevance",
    "!openuserjs": "https://openuserjs.org/?q={}",
    "!osm": "https://www.openstreetmap.org/search?query={}",
    "!redartist": "https://redacted.ch/artist.php?artistname={}",
    "!redforums": "https://redacted.ch/forums.php?action=search&search={}",
    "!red": "https://redacted.ch/torrents.php?searchstr={}",
    "!redlog": "https://redacted.ch/log.php?search={}",
    "!redrequests": "https://redacted.ch/requests.php?search={}",
    "!redusers": "https://redacted.ch/user.php?action=search&search={}",
    "!tss": "https://jira.appstate.edu/issues/?jql={}",
    "!twitter": "https://twitter.com/search?q={}",
    "!whosampled": "https://www.whosampled.com/search/?q={}",
    "!wiki": "https://www.wikipedia.org/search-redirect.php?family=wikipedia&language=en&language=en&go=Go&search={}",
    "!wikt": "https://www.wiktionary.org/search-redirect.php?family=wiktionary&language=en&go=Go&search={}",
}


# c.bindings.commands["normal"] = {
#     "!": "cmd-set-text :open !",
# }

# Change the argument to True to still load settings configured via autoconfig.yml
config.load_autoconfig(True)

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
config.set("content.cookies.accept", "all", "*")


# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value. With QtWebEngine
# between 5.12 and 5.14 (inclusive), changing the value exposed to
# JavaScript requires a restart.
# Type: FormatString
# config.set('content.headers.user_agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0', 'https://*.google.com/*')
#
# config.set('content.headers.user_agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0', 'https://*.slack.com/*')

# Allow websites to show notifications.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
# config.set('content.notifications.enabled', True, 'https://calendar.google.com')
# config.set('content.notifications.enabled', True, 'https://meet.google.com')
# config.set('content.notifications.enabled', True, 'https://app.slack.com')

# Load images automatically in web pages.
# Type: Bool
# config.set('content.images', True, '*')

# Enable JavaScript.
# Type: Bool
# config.set('content.javascript.enabled', True, '*')

# Bindings
config.bind(";", "set-cmd-text :", mode="normal")
config.bind(
    "<F2>",
    "config-cycle statusbar.show always never;; config-cycle tabs.show always never",
)
config.bind(
    "gcc",
    "config-cycle statusbar.show always never;; config-cycle tabs.show always never",
)

config.bind("b", "tab-focus last", mode="normal")
config.bind("gf", "hint", mode="normal")
config.bind("t", "open -t", mode="normal")
config.bind("x", "tab-close", mode="normal")
config.bind("yv", "hint links spawn mpv {hint-url}", mode="normal")
config.bind("<Ctrl-!>", "cmd-set-text :open ! ", mode="normal")
config.bind('<Ctrl-N>',         'completion-item-focus next',           mode='command')
config.bind('<Ctrl-P>',         'completion-item-focus prev',           mode='command')
config.bind('<Ctrl-y>', 'command-accept', mode='command')
config.bind('<Shift-!>', 'cmd-set-text :open ! ' )




# #!/usr/bin/env python
# # Documentation: qute://help/configuring.html qute://help/settings.html
# import subprocess
# import os
# # Settings {{{1
# # pylint: disable=C0111
# c = c  # noqa: F821 pylint: disable=E0602,C0103,W0127
# config = config  # noqa: F821 pylint: disable=E0602,C0103,W0127
# TERMCMD = ['kitty', '-1']
# config.load_autoconfig(False)
# c.auto_save.session = True
# c.backend = 'webengine'
# c.completion.cmd_history_max_items = 1000
# c.completion.shrink = True
# c.completion.use_best_match = True
# c.content.cookies.accept = 'no-3rdparty'
# c.content.fullscreen.window = False
# c.downloads.prevent_mixed_content = False
# c.content.notifications.enabled = False
# c.content.pdfjs = False
# c.content.private_browsing = False
# BASEDIR = os.getenv("XDG_CONFIG_HOME", os.path.join(os.getenv('HOME'), '.config'))
# # TODO: darkmode and better-duckduckgo not working
# c.content.webrtc_ip_handling_policy = 'disable-non-proxied-udp'
# c.content.geolocation = False
# c.downloads.location.suggestion = 'both'
# c.downloads.remove_finished = 1
# c.editor.command = [*TERMCMD, 'nvim', '-c', 'norm {line}G{column0}l', '{file}']
# c.hints.border = '0'
# c.hints.chars = 'asdfjkl;ghnmxcvbziowerut'
# c.hints.padding = {"bottom": 1, "left": 1, "right": 1, "top": 1}
# c.input.insert_mode.auto_load = True
# c.scrolling.bar = 'when-searching'
# c.scrolling.smooth = True
# c.session.lazy_restore = True
# c.statusbar.padding = {"bottom": 0, "left": 0, "right": 0, "top": 0}
# c.statusbar.show = "always"
# c.tabs.mousewheel_switching = False
# c.tabs.new_position.unrelated = 'next'
# c.tabs.select_on_remove = 'last-used'
# c.tabs.show = "multiple"
# c.tabs.show_switching_delay = 400
# c.tabs.title.format = "{audio}{current_title}"
# c.url.open_base_url = True
# c.window.hide_decoration = True
# c.window.transparent = True
#
# c.fileselect.handler = "default"
# c.fileselect.single_file.command = [*TERMCMD, 'ranger', '--choosefile', '{}']
# c.fileselect.multiple_files.command = [*TERMCMD, 'ranger', '--choosefiles', '{}']
# c.fileselect.folder.command = [*TERMCMD, 'ranger', '--choosedir', '{}']
# # Fonts {{{1
# FONT_SIZE = '10pt'
# FIXED = 'Iosevka Mayukai CodePro'
# SANS_SERIF = 'Futura'
# SERIF = 'Helvetica'
# c.fonts.default_family = SANS_SERIF
# # c.fonts.default_family = [ "Futura", "Unifont" ]
# c.fonts.statusbar = f'{FONT_SIZE} {FIXED}'
# c.fonts.completion.category = f'{FONT_SIZE} {FIXED}'
# c.fonts.completion.entry = f'{FONT_SIZE} {FIXED}'
# c.fonts.hints = f'{FONT_SIZE} {FIXED}'
# # c.fonts.web.family.fixed = FIXED
# c.fonts.web.family.sans_serif = SANS_SERIF
# c.fonts.web.family.serif = SERIF
# c.fonts.web.family.standard = SANS_SERIF
# c.fonts.web.size.default = 14
# c.fonts.web.size.default_fixed = 14
# # Aliases {{{1
# c.aliases["echo"] = "message-info"
# c.aliases["sleep"] = "later"
# # Search Engines {{{1
# c.url.searchengines = {
#     # actual search engines
#     'as': 'https://astiango.com/search.php?q={}',
#     'am': 'https://www.amazon.in/s?k={}',
#     'DEFAULT': 'https://www.google.com/search?hl=en&q={}',
#     'g': 'https://www.google.com/search?hl=en&q={}',
#     'gs': 'https://scholar.google.com/scholar?hl=en&q={}',
#     'd': 'https://www.duckduckgo.com/?q={}',
#     'dh': 'https://html.duckduckgo.com/html?q={}',  # nojs version of duckduckgo
#     '4': 'https://4chan.org/{}',
#     'l': 'https://www.lainchan.org/{}',
#     'mw': 'https://www.merriam-webster.com/dictionary/{}',
#     'ly': 'https://www.lyrics.com/lyrics/{}',  # lyric finding engine
#     'r': 'https://old.reddit.com/r/{}',
#     's': 'https://open.spotify.com/search/{}',
#     'st': 'https://startpage.com/do/metasearch.pl?query={}',
#     'su': 'https://steamunlocked.net/?s={}',
#     'wiby': 'https://wiby.me/?q={}',
#     'scp': 'https://scp-wiki.wikidot.com/scp-{}',
#     'y': 'https://youtube.com/search?q={}',
#     'yt': 'https://yewtu.be/search?q={}',  # invidious
#     'yw': 'https://yewtu.be/watch?v={}',
#     'sp': 'https://www.smartprix.com/products/?q={}',
#     'gf': 'https://greasyfork.org/en/scripts?q={}',
#     'ud': 'https://www.urbandictionary.com/define.php?term={}',
#     'wl': 'https://wikiless.org/w/index.php?search={}',
#     'w': 'https://en.wikipedia.org/w/index.php?search={}',
#     'mc': 'https://minecraft.fandom.com/wiki/{}',
#     'sd': 'https://stardewvalleywiki.com/{}',
#     'f': 'https://wiki.factorio.com/{}',
#     'ug': 'https://www.ultimate-guitar.com/search.php?search_type=title&value={}',
#     # IRC channels
#     'irc': 'https://netsplit.de/channels/?chat={}',
#     # books
#     'aa': 'https://annas-archive.org/search?q={}',
#     'cb': 'https://library.cmi.ac.in/cgi-bin/koha/opac-search.pl?q={}',
#     'b': 'https://libgen.is/search.php?req={}',
#     'bf': 'https://libgen.is/fiction/?q={}',
#     'b2': 'https://1lib.in/s/{}',
#     'b3': 'https://www.pdfdrive.com/search?q={}',
#     'b4': 'https://libgen.rs/search?req={}',
#     'b5': 'https://libgen.st/search?query={}',
#     # academics
#     'o': 'http://oeis.org/search?q={}',
#     'oa': 'http://oeis.org/A{}',
#     'ob': 'http://oeis.org/b{}.txt',
#     'wi': 'https://www.wolframalpha.com/input/?i={}',
#     'wm': 'https://mathworld.wolfram.com/search/index.html?query={}',
#     'sh': 'https://sci-hub.ru/{}',
#     # linux
#     'm': 'https://melpa.org/#/?q={}',
#     'aw': 'https://wiki.archlinux.org/index.php?search={}',
#     'gw': 'https://wiki.gentoo.org/index.php?search={}',
#     'ig': 'https://wiki.installgentoo.com/index.php?search={}',
#     'm': 'https://linux.die.net/man/1/{}',  # man pages
#     'm2': 'https://man.archlinux.org/{}',  # arch man pages
#     'aur': 'https://aur.archlinux.org/packages/{}',
#     'al': 'https://archlinux.org/packages/?q={}',
#     'ala': 'https://archlinux.org/packages/core/x86_64/{}',
#     'alc': 'https://archlinux.org/packages/community/x86_64/{}',
#     'ale': 'https://archlinux.org/packages/extra/x86_64/{}',
#     # programming
#     'asm': 'https://www.felixcloutier.com/x86/{}',
#     'c': 'https://duckduckgo.com/?q=site%3Acppreference.com/w/c+{}',
#     'ho': 'https://hoogle.haskell.org/?hoogle={}',
#     'hg': 'https://hoogle.haskell.org/?scope=set%3Aincluded-with-ghc&hoogle={}',
#     'hw': 'https://wiki.haskell.org/{}',
#     'hb': 'https://en.wikibooks.org/wiki/Haskell/{}',
#     'nlab': 'https://www.google.com/search?as_q={}&as_sitesearch=https://ncatlab.org/nlab',
#     'cl': 'https://en.cppreference.com/w/c/language/{}',
#     'dd': 'https://devdocs.io/{}',
#     'gh': 'https://github.com/{}',
#     'gl': 'https://github.com/Vedant36/{}',
#     'ide': 'https://glot.io/new/{}',  # online code editor without login
#     'grep': 'https://grep.app/search?q={}',  # search for code examples
#     'py': 'https://pypi.org/search/?q={}',
#     'pg': 'https://www.pygame.org/docs/ref/{}.html',
#     'xy': 'https://learnxinyminutes.com/docs/{}',  # learning new prog.lang.
#     # films and shows
#     'an': 'https://zoro.to/search?keyword={}',  # anime
#     'mr': 'https://mangareader.to/search?keyword={}',
#     'p': 'https://thepiratebay.org/search.php?q={}',
#     'p2': 'https://tpb.one/search.php?q={}',
# }
# # Youtube/Ad Blocking {{{1
# c.content.javascript.enabled = True
# c.content.autoplay = False
# c.content.blocking.adblock.lists = [
#     "https://raw.githubusercontent.com/brave/adblock-lists/master/brave-unbreak.txt",
#     "https://easylist.to/easylist/easylist.txt",
#     "https://easylist.to/easylist/easyprivacy.txt",
#     "https://secure.fanboy.co.nz/fanboy-cookiemonster.txt",
#     "https://easylist.to/easylist/fanboy-annoyance.txt",
#     "https://secure.fanboy.co.nz/fanboy-annoyance.txt",
#     "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances.txt",
#     "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2020.txt",
#     "https://github.com/uBlockOrigin/uAssets/raw/master/filters/unbreak.txt",
#     "https://github.com/uBlockOrigin/uAssets/raw/master/filters/resource-abuse.txt",
#     "https://github.com/uBlockOrigin/uAssets/raw/master/filters/privacy.txt",
#     "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters.txt",
# ]
# c.content.blocking.enabled = True
# c.content.blocking.hosts.lists = [
#     "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts",
#     "https://blocklistproject.github.io/Lists/everything.txt",
# ]
# c.content.blocking.method = 'adblock'
#
# # Bindings {{{1
# c.bindings.commands = {}
# c.bindings.commands["normal"] = {
#     "d": "nop",
#     "!": "cmd-set-text :open !",
#     "A": "cmd-set-text :open {url:pretty}",
#     "H": "fake-key <left>",
#     "J": "back",
#     "K": "forward",
#     "L": "fake-key <right>",
#     "ZA": "quit --save",
#     "ZQ": "close",
#     "ZZ": "save;; close",
#     "<ctrl-r>": "save;; restart",
#     "ce": "config-edit",
#     "cs": "config-source",
#
#     # pass fake key to qutebrowser
#     **{f"e{i}": f"fake-key {i}"
#         for i in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM`1234567890~!@#$%^&*()"},
#     "e<space>": "fake-key <esc>",
#
#     # like gi but clears text too(on most sites)
#     "gI": "hint inputs --first;; mode-enter insert;; fake-key <ctrl-a><backspace>",
#     "gw": "open https://web.archive.org/web/*/{url:pretty}",
#     ";w": "hint links run :open https://web.archive.org/web/*/{hint-url}",
#     ";W": "hint links run :open -t https://web.archive.org/web/*/{hint-url}",
#     ";D": "hint --rapid links download",
#     "h":  "tab-prev",
#     "l":  "tab-next",
#     "ya": "yank inline '<a href={url}>{title}</a>'",
#     "yo": "yank inline '[[{url}][{title}]]'",
#     "yw": "fake-key <ctrl-a>",
#     ";j": "hint links spawn sh -c 'echo {hint-url} | tee -a ~/temp'",
#     ";n": "hint links spawn -d kitty nvim {hint-url}",
#     ";s": "hint links spawn -d surf {hint-url}",
#     "S": "spawn -d surf {url}",
#     ",f": "spawn -d firefox {url}",
#
#     # Binds to open current url in mpv/upmpv
#     ",m": "spawn -d mpv {url}",
#     ",M": "hint links spawn -d mpv {hint-url}",
#     "M":  "spawn -d umpv {url}",
#     "2M": "spawn -d umpv -p 2 {url}",
#     ";M": "hint --rapid links spawn umpv {hint-url}",
#     ";m": "hint links spawn umpv {hint-url}",
#     "2;m": "hint links spawn umpv -p 2 {hint-url}",
#
#     # config-cycle
#     ",b": "config-cycle content.blocking.enabled;; reload",
#     ",p": "config-cycle content.proxy socks://localhost:9050/ system",
#     ",s": "config-cycle -t statusbar.show never always",
#     ",t": "config-cycle -t tabs.show multiple never",
#     ",u": "config-cycle -t statusbar.show never always;; config-cycle tabs.show never multiple",
#     "\\": "config-cycle -t statusbar.show never always;; config-cycle tabs.show never multiple",
#
#     # to change playback rate on youtube
#     ",y": "cmd-set-text -s :jseval -q document.querySelector('video').playbackRate =",
#
#     # enable scroll
#     ",S": "jseval -q document.body.style.overflow = 'visible'",
# }
# c.bindings.commands["insert"] = {
#     "<Ctrl-a>": "fake-key <Home>",
#     "<Alt-b>": "fake-key <Ctrl-Left>",
#     "<Ctrl-b>": "fake-key <Left>",
#     "<Ctrl-c>": "fake-key <Ctrl-a><Backspace>",
#     "<Alt-d>": "fake-key <Ctrl-Delete>",
#     "<Ctrl-d>": "fake-key <Delete>",
#     "<Ctrl-e>": "fake-key <End>",
#     "<Alt-f>": "fake-key <Ctrl-Right>",
#     "<Ctrl-f>": "fake-key <Right>",
#     "<Ctrl-h>": "fake-key <Backspace>",
#     "<Ctrl-j>": "fake-key <Enter>",
#     "<Ctrl-k>": "fake-key <Shift-End><Delete>",
#     "<Ctrl-m>": "fake-key <Enter>",
#     "<Ctrl-n>": "fake-key <Down>",
#     "<Ctrl-p>": "fake-key <Up>",
#     "<Ctrl-u>": "fake-key <Shift-Home><Delete>",
#     "<Ctrl-w>": "fake-key <Ctrl-Backspace>",
#     "<Ctrl-x><Ctrl-e>": "edit-text",
# }
#
# # Darkmode/Colors from Xresources {{{1
# c.colors.webpage.darkmode.enabled = False
# c.colors.webpage.darkmode.policy.images = 'never'
# c.colors.webpage.preferred_color_scheme = 'dark'
# c.colors.webpage.darkmode.algorithm = 'lightness-hsl'
# c.colors.webpage.darkmode.contrast = -.022  # the lower the darker
#
#
# # taken from https://qutebrowser.org/doc/help/configuring.html
# # 0:black, 1:red, 2:green,, 3:yellow, 4:blue, 5:magenta, 6:cyan, 7:white
# # +8 are lighter variants in most color schemes
# xresources = {}
# x = subprocess.run(["xrdb", "-query"], stdout=subprocess.PIPE, check=False)
# lines = x.stdout.decode().split("\n")
# for line in filter(lambda l: l.startswith("*"), lines):
#     prop, _, value = line.partition(":\t")
#     xresources[prop] = value
#
#
# c.colors.webpage.bg = '#ccc7bb'
# c.colors.statusbar.normal.bg = BG
# c.colors.statusbar.command.bg = BG
# c.colors.statusbar.command.fg = FG
# c.colors.statusbar.normal.fg = FG
# c.colors.statusbar.url.success.https.fg = xresources["*.color2"]
# c.colors.statusbar.url.hover.fg = xresources["*.color4"]
#
# SELECTED = xresources["*.color8"]
# c.colors.tabs.even.bg = EVEN
# c.colors.tabs.odd.bg = ODD
# c.colors.tabs.even.fg = FG
# c.colors.tabs.odd.fg = FG
# c.colors.tabs.selected.even.bg = SELECTED
# c.colors.tabs.selected.odd.bg = SELECTED
# c.colors.hints.bg = FG
# c.colors.hints.fg = BG
#
# c.colors.tabs.indicator.start = xresources["*.color4"]
# c.colors.tabs.indicator.stop = xresources["*.color6"]
# c.colors.tabs.indicator.error = xresources["*.color1"]
# c.colors.completion.even.bg = EVEN
# c.colors.completion.odd.bg = ODD
# c.colors.completion.fg = FG
# c.colors.completion.category.bg = BG
# c.colors.completion.category.fg = FG
# c.colors.completion.item.selected.bg = BG
# c.colors.completion.item.selected.fg = FG
#
# # Headers and javascript exceptions {{{1
# c.content.webgl = False
# c.content.canvas_reading = False
# c.content.headers.accept_language = 'en-US,en;q=0.5'
# c.content.headers.custom = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
# c.content.headers.user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'
# config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')
# config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://accounts.google.com/*')
# config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')
# config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://docs.google.com/*')
# config.set('content.register_protocol_handler', False, 'https://mail.google.com')
# config.set('content.images', True, 'chrome-devtools://*')
# config.set('content.images', True, 'devtools://*')
# config.set('content.javascript.enabled', True, 'chrome-devtools://*')
# config.set('content.javascript.enabled', True, 'devtools://*')
# config.set('content.javascript.enabled', True, 'chrome://*/*')
# config.set('content.javascript.enabled', True, 'qute://*/*')
# config.set('content.javascript.enabled', True, 'https://www.youtube.com/*')
# config.set('content.javascript.enabled', True, 'https://duckduckgo.com/*')
# config.set('content.geolocation', False, 'https://www.google.com')
# config.set('content.geolocation', False, 'https://www.embibe.com')
# # }}}
