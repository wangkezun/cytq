# coding=utf-8
import sys
import csv
import json
from ualfred import Workflow3, notify

log = None

def main(wf):

	# Get args from Workflow, already in normalized Unicode
	args = wf.args

	with open('cityidloc.csv', newline='', encoding='utf-8') as csvfile:
		csv_reader = csv.reader(csvfile, delimiter=',')
		for rows in csv_reader:
			if args[0] in rows[1]:
				log.debug(rows)
				wf.add_item(rows[1], arg=json.dumps(rows), uid=csv_reader.line_num, valid=True)

	# Add an item to Alfred feedback

	wf.send_feedback()


if __name__ == '__main__':
	# Create a global `Workflow` object
	wf = Workflow3()
	# Call your entry function via `Workflow.run()` to enable its helper
	# functions, like exception catching, ARGV normalization, magic
	# arguments etc.
	log = wf.logger

	sys.exit(wf.run(main))
