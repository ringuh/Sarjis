#!/usr/bin/python
# -*- coding: utf-8 -*-

import Queue
import threading
import time
from project import db, app
from bs4 import BeautifulSoup
from project.models import Sarjakuva as SK, Strippi
import datetime, urllib, os, requests, hashlib
from project.luokat import *
import sys

from project.taustaprosessit.sarjis_parseri import Looper

def runs():
	exitFlag = 0
	queueLock = threading.Lock()
	workQueue = Queue.Queue()

	class myThread (threading.Thread):
		def __init__(self, name, q):
			threading.Thread.__init__(self)
			#self.threadID = threadID
			self.name = name
			self.q = q
		def run(self):
			print "Starting " + self.name
			count = 0
			while not exitFlag or count < 10:
				queueLock.acquire()
				if not workQueue.empty():
					data = self.q.get()
					
					
					queueLock.release()
					Looper(data)
					#print "%s processing %s" % (self.name, data.nimi)
				else:
					#print "else"
					count += 1
					queueLock.release()
				time.sleep(1)
			print "Exiting " + self.name

	

	threadList = ["Thread-1", "Thread-2", "Thread-3", "Thread-4", "Thread-5", "Thread-6"]
	#nameList = ["One", "Two", "Three", "Four", "Five"]
	
	
	threads = []
	
	sarjakuvat = db.session.query(SK).order_by(SK.id).all()		

	#Create new threads
	for tName in threadList:
		thread = myThread(tName, workQueue)
		thread.start()
		threads.append(thread)
		

	# Fill the queue
	queueLock.acquire()
	for s in sarjakuvat:
		workQueue.put(s)
	queueLock.release()

	# Wait for queue to empty
	while not workQueue.empty():
		#print workQueue.qsize()
		#time.sleep(2)
		pass

	# Notify threads it's time to exit
	exitFlag = 1

	# Wait for all threads to complete
	for t in threads:
		t.join()
	print "Exiting Main Thread"

