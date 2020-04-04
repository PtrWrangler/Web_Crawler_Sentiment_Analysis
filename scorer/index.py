#!/usr/bin/env python
#http://jaganadhg.freeflux.net/blog/archive/2010/09/01/pylucene-in-action-part-i.html

import os,sys,glob
import lucene
from lucene import SimpleFSDirectory, System, File, Document, Field, StandardAnalyzer, IndexWriter, Version

class luceneIndexer:
	indir = ''
	init = True # Does that index have to be created or overwritten

	def __init__(self, indir):
		lucene.initVM()
		self.indir = indir

	# Index document. Create index on first run.
	def index(self, doc, title, url):
		indexdir = SimpleFSDirectory(File(self.indir))
		analyzer = StandardAnalyzer(Version.LUCENE_30)
		index_writer = IndexWriter(indexdir, analyzer, self.init, IndexWriter.MaxFieldLength(512))
		self.init = False

		# Initialize document and index it
		document = Document()
		document.add(Field("title", title, Field.Store.YES, Field.Index.ANALYZED))
		document.add(Field("url", url, Field.Store.YES, Field.Index.ANALYZED))
		document.add(Field("text", doc, Field.Store.YES, Field.Index.ANALYZED))
		index_writer.addDocument(document)

		index_writer.optimize()
		index_writer.close()

		
#l = luceneIndexer('Index-d')
#l.index('restaurant yay!', 'restaurant', '/this/is/a/path.htm')
#l.index('This is utterly excellent! this is a good test. this is a bad text. This is utterly terrible restaurant! really cool restaurant!', 'test', '/path/title.html')