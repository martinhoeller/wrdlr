#!/usr/bin/python

import sys, getopt, os.path
import fnmatch

# SEQUENCE MATCHING
# All words containing 'clo': "clo"
# All words starting with 'clo': "clo*""
# All words ending with 'clo': "*clo"
# All words starting with 'clo' and ending with 'rm': "clo*rm"
# All words starting with 'clo', followed by any character and ending with 'h': "clo?h"

def load_dictionary(file):
	file = open(file, "r")
	lines = file.readlines()
	return [line.strip() for line in lines]

def matching_words(words, pattern, min_len = -1, max_len = -1, match_case = False):
	if (match_case == True):
		matches = [word for word in words if fnmatch.fnmatchcase(word, pattern)]
	else:
		lower_pattern = pattern.lower()
		matches = [word for word in words if fnmatch.fnmatch(word.lower(), lower_pattern)]

	if (max_len > -1):
		matches = [word for word in matches if len(word) <= max_len]

	if (min_len > -1):
		matches = [word for word in matches if len(word) >= min_len]	

	return matches

def print_words(words):
	for word in words:
		print word

def test():
	words = load_dictionary("dict_en.txt")
	print len(words), "words"
	print
	print "STARTING TESTS"
	print

	print "Words containing 'clor'"
	print_words(matching_words(words, "*clor*"))

	print "Words starting with 'clor'"
	print_words(matching_words(words, "clor*"))

	print "Words ending with 'clo'"
	print_words(matching_words(words, "*clo"))

	print "Words starting with 'clo' and ending with 'ing'"
	print_words(matching_words(words, "clo*ing"))

	print "All words starting with 'clo', followed by any character and ending with 'h'"
	print_words(matching_words(words, "clo?h"))

	print "All words with exactly 20 characters"
	print_words(matching_words(words, "*", 20, 20))

	print "All words starting with 'u' and at least 20 characters"
	print_words(matching_words(words, "u*", 20))

	print "All words ending with 'alt' and max 5 characters"
	print_words(matching_words(words, "*alt", -1, 5))


def print_help():
	print "Usage:"
	print "  wrdlr.py --dict <dictfile> --pattern <pattern> [--minlen <minlen>] [--maxlen <maxlen>] [--matchcase]"
	print
	print "Example:"
	print "  ./wrdlr.py --dict /usr/share/dict/words --pattern col* --minlen 5 --maxlen 7"


################
# Main Program # 
################

ERROR_WRONG_ARGUMENTS = 1
ERROR_DICTIONARY_FILE = 2

def main(argv):
	dictfile = ""
	pattern = ""
	minlen = -1
	maxlen = -1
	matchcase = False

	try:
		opts, args = getopt.getopt(argv,"",["dict=","pattern=", "minlen=", "maxlen=", "matchcase"])
	except getopt.GetoptError:
		print_help()
		sys.exit(ERROR_WRONG_ARGUMENTS)

	for opt, arg in opts:
		if opt in ("--dict"):
			dictfile = arg
		elif opt in ("--pattern"):
		   pattern = arg
		elif opt in ("--minlen"):
			minlen = int(arg)
		elif opt in ("--maxlen"):
			maxlen = int(arg)
		elif opt in ("--matchcase"):
			matchcase = True

	if len(dictfile) == 0 or len(pattern) == 0:
		print_help()
		sys.exit(ERROR_WRONG_ARGUMENTS)

	if not os.path.isfile(dictfile):
		print "ERROR: invalid dictionary file"
		sys.exit(ERROR_DICTIONARY_FILE)

	words = load_dictionary(dictfile)
	matches = matching_words(words, pattern, minlen, maxlen, matchcase)
	print_words(matches)
	sys.exit(0)


if __name__ == "__main__":
	main(sys.argv[1:])

#test()

