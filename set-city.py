# coding=utf-8
import sys
import csv
from workflow import Workflow3, notify

log = None


def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
	csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
	for row in csv_reader:
		yield [unicode(cell, 'utf-8') for cell in row]


def main(wf):

	import cPickle

	# Get args from Workflow, already in normalized Unicode
	args = wf.args

	reader = unicode_csv_reader(open('cityidloc.csv'))
	for i, rows in enumerate(reader):
		if rows[1] == args[0] or rows[2] == args[0] or rows[3] == \
				args[0]:
			log.debug(rows[1])
			wf.add_item(rows[1] + ',' + rows[2] + ',' + rows[3],
						str(rows[4]) + ' ' + str(rows[5]), arg=cPickle.dumps(rows), uid=i, valid=True)

	wf.store_data(u'cy-city', args[0])

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
