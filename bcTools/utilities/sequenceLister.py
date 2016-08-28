""" Tool to list sequence inside a folder or given list of files
"""
import argparse
import sys


def _getParser(args):
	"""	Function take arguments and create a argparse parser object
		out of it.

		Args:
			args (list): List string arguments(Mostly system arguments)

		Returns:
			(argparse.Namespace) Parser object contains all the arguments
	"""
	usage = "Tool to list the sequence(s) in a directory or list of files."
	parser = argparse.ArgumentParser(description=usage)
	return parser.parse_args(args)


def sequenceLister():
	""" Initialize function for sequenceLister tool.
	"""
	parser = _getParser(sys.argv[1:])
