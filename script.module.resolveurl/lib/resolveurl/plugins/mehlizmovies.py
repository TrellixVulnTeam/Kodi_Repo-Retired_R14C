"""
    resolveurl XBMC Addon
    Copyright (C) 2017 jsergio

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import re
from lib import helpers
from resolveurl import common
from resolveurl.resolver import ResolveUrl, ResolverError

class MehlizMoviesResolver(ResolveUrl):
    name = "mehlizmovies"
    domains = ["mehlizmovies.com", "mehlizmovies.is", "mehlizmovieshd.com"]
    pattern = '(?://|\.)(mehlizmovies(?:hd)?\.(?:com|is))/player/embed\.php\?([^\s\"\']+)'
    
    def __init__(self):
        self.net = common.Net()

    def get_media_url(self, host, media_id):
        web_url = self.get_url(host, media_id)
        headers = {'User-Agent': common.RAND_UA, 'Referer': 'https://www.mehlizmovieshd.com/'}
        html = self.net.http_GET(web_url, headers=headers).content
        
        if html:
            sources = helpers.parse_sources_list(html)
            if sources:
                if len(sources) > 1:
                    try: sources.sort(key=lambda x: int(re.sub("\D", "", x[0])), reverse=True)
                    except: common.logger.log_debug('Scrape sources sort failed |int(re.sub("\D", "", x[0])|')
                    
                return helpers.pick_source(sources) + helpers.append_headers(headers)
            
        raise ResolverError('Video not found')
    
    def get_url(self, host, media_id):
        return self._default_get_url(host, media_id, template='https://www.mehlizmovieshd.com/player/embed.php?{media_id}')
