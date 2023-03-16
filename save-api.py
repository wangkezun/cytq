# coding=utf-8
import sys
import csv
from ualfred import Workflow3, notify

log = None


def main(wf):
	# Get args from Workflow, already in normalized Unicode
	args = wf.args

	wf.save_password('apiKey', args[0])


if __name__ == '__main__':
	# Create a global `Workflow` object
	wf = Workflow3()
	# Call your entry function via `Workflow.run()` to enable its helper
	# functions, like exception catching, ARGV normalization, magic
	# arguments etc.
	log = wf.logger

	sys.exit(wf.run(main))
