#!/usr/bin/python
import os, re, time

def WrdLineCount(txt):
	line_count = 0
	wrd_count = 0
	for line in txt:
		if len(line) > 1 :
			line_count += 1
			wrd_count += len( line.split(" ") )
	return (wrd_count, line_count)


testDir = "TestCorpus/"
workDir = raw_input("Corpus Dir (default: %s):"%testDir)

if len(workDir) >0 and os.path.exists(workDir):
	print ("using dir: %s"%workDir)
else:	
	workDir = testDir
	print ("using dir: %s"%testDir)
	

ob = ""
stat = {}
for fn in os.listdir(workDir):
	wfn = workDir+fn
	cnt = open(wfn, "r").readlines()

	(wrd_count, line_count) = WrdLineCount(cnt)
	stat[fn] = (wrd_count, line_count)
	ob += "file: %s, lines: %s, words, %s, ratio, %4.2f\n"%(wfn, line_count, wrd_count, wrd_count/float(line_count) )

print (ob)
isExport = raw_input("Export Statistic Data (y/N):")
if re.match("[y|Y]", isExport) :
	expFn = raw_input("Input Export File Name (only .csv):")

	if not len(expFn) >0:
		expFn = time.strftime( 'WordLineCount_%H%m%S', time.localtime( time.time() ) ) + ".csv"
		print ("Not input any export filename, using default file name. Export file name: %s"%expFn)

	stat_ob = "file name, line count, word count, words/lines\n"
	for fn in stat.keys():
		(wrd, line) = stat[fn]
		stat_ob += "%s, %s, %s, %4.2f\n"%(fn, wrd, line, wrd/float(line))

	open(expFn, "w").write(stat_ob)
