# coding=utf-8
import sys
from ualfred import Workflow3, notify

log = None


def main(wf):
	import pickle
	from workflow import web

	args = wf.args
	query = pickle.loads(str(args[0]))
	log.debug('test')
	url = 'https://api.caiyunapp.com/v2/' + wf.get_password('apiKey') + '/' + query[4] + ',' + query[5] + '/'
	if query[6] == 1:
		log.debug(url)
		url += 'realtime.json'
		r = web.get(url)
		data = r.json()
		log.debug(data)
		wf.add_item(data['status'])

	wf.send_feedback()


if __name__ == '__main__':
	# Create a global `Workflow` object
	wf = Workflow3()
	# Call your entry function via `Workflow.run()` to enable its helper
	# functions, like exception catching, ARGV normalization, magic
	# arguments etc.
	log = wf.logger

	sys.exit(wf.run(main))
