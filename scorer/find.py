#!/usr/bin/env python
#http://jaganadhg.freeflux.net/blog/archive/2010/09/01/pylucene-in-action-part-i.html

import sys
import lucene
from lucene import SimpleFSDirectory, System, File, Document, Field,\
StandardAnalyzer, IndexSearcher, Version, QueryParser

class luceneRetriver:
	def find(self, query, indir):
		lucene.initVM()
		INDEXDIR = indir

		indir = SimpleFSDirectory(File(INDEXDIR))
		lucene_analyzer = StandardAnalyzer(Version.LUCENE_30)
		lucene_searcher = IndexSearcher(indir)
		my_query = QueryParser(Version.LUCENE_30,"<default field>",\
		lucene_analyzer).parse("text:" + query + " OR title:" + query)
		MAX = 1000
		total_hits = lucene_searcher.search(my_query,MAX)
		print "\nHits: ",total_hits.totalHits, "\n"

		for hit in total_hits.scoreDocs:
			print "Hit Score:", "%.4f" % hit.score, "Title:",lucene_searcher.doc(hit.doc).get("title").encode("utf-8")
			print lucene_searcher.doc(hit.doc).get("url").encode("utf-8"),'\n'
			#doc = lucene_searcher.doc(hit.doc)
			#print doc.get("text").encode("utf-8")

l = luceneRetriver()
l.find("restaurant", "Index-d")
