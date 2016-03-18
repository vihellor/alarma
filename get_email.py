#!/usr/bin/env python

from imapclient import IMAPClient
import time


DEBUG = True

HOSTNAME = 'imap.gmail.com'
USERNAME = 'your username here'
PASSWORD = 'your password here'
MAILBOX = 'Inbox'

def loop():
    server = IMAPClient(HOSTNAME, use_uid=True, ssl=True)
    server.login(USERNAME, PASSWORD)

    if DEBUG:
        print('Logging in as ' + USERNAME)
        select_info = server.select_folder(MAILBOX)
        print('%d messages in INBOX' % select_info['EXISTS'])

    folder_status = server.folder_status(MAILBOX, 'UNSEEN')
    newmails = int(folder_status['UNSEEN'])

    if DEBUG:
        print "tienes ", newmails, " correos nuevos en tu bandeja"
