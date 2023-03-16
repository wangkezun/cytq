# coding=utf-8
import sys
from ualfred import Workflow3,notify

log = None


def main(wf):
	import json
	# Get args from Workflow, already in normalized Unicode
	args = wf.args
	result = json.loads(str(args[0]))

	wf.store_data('cy-city', result)

	# Add an item to Alfred feedback
	log.debug(result[3])

	print(result)

if __name__ == '__main__':
	# Create a global `Workflow` object
	wf = Workflow3()
	# Call your entry function via `Workflow.run()` to enable its helper
	# functions, like exception catching, ARGV normalization, magic
	# arguments etc.
	log = wf.logger

	sys.exit(wf.run(main))
