#!/usr/bin/python
# -*- coding: utf-8 -*-

# freeseer - vga/presentation capture software
#
#  Copyright (C) 2011  Free and Open Source Software Learning Centre
#  http://fosslc.org
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

# For support, questions, suggestions or any other inquiries, visit:
# http://wiki.github.com/fosslc/freeseer/


import datetime
import os

from freeseer.framework.config import Config
from freeseer.framework.logger import Logger
from freeseer.framework.presentation import *

from rss_parser import *
from talkeditor_db_connector import *

__version__=u'1.9.7'

class TalkEditorCore:
    '''
    Talk Editor core logic code.
    '''
    def __init__(self, ui):
        self.ui = ui
        
        # Read in config information
        configdir = os.path.abspath(os.path.expanduser('~/.freeseer/'))
        self.logger = Logger(configdir)
        self.db = TalkEditor_DB_Connector(configdir)

        self.logger.log.info(u"Core initialized")   
	
    ##
    ## Database Functions
    ##
    def get_talk_titles(self):
        return self.db.get_talk_titles()
        
    def get_presentation(self, presentation_id):
	return self.db.get_presentation(presentation_id)

    def add_talks_from_rss(self, rss):
        entry = str(rss)
        feedparser = FeedParser(entry)

        if len(feedparser.build_data_dictionary()) == 0:
            self.logger.log.info("RSS: No data found.")

        else:
            for presentation in feedparser.build_data_dictionary():
                talk = Presentation(presentation["Title"],
                                    presentation["Speaker"],
                                    "",
                                    presentation["Level"],
                                    presentation["Event"],
                                    presentation["Time"],
                                    presentation["Room"])
                                    
                if not self.db.db_contains(talk):
                    self.add_talk(talk)

    def add_talk(self, presentation):
        self.db.add_talk(presentation)
        self.logger.log.debug('Talk added: %s - %s', presentation.speaker, presentation.title)
        
    def update_talk(self, talk_id, speaker, title, room, event, dateTime):
        self.db.update_talk(talk_id, speaker, title, room, event, dateTime)
        self.logger.log.debug('Talk updated: %s - %s', speaker, title)
        
    def delete_talk(self, talk_id):
        self.db.delete_talk(talk_id)
        self.logger.log.debug('Talk deleted: %s', talk_id)

    def clear_database(self):
        self.db.clear_database()
        self.logger.log.debug('Database cleared!')

