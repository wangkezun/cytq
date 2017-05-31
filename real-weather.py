# coding=utf-8
import sys
from workflow import Workflow3, notify

log = None


def main(wf):
	import cPickle
	from data import Data
	from workflow import web

	city = wf.stored_data('cy-city')
	api_key = wf.get_password('apiKey')

	if city is None:
		wf.add_item(u'请通过cy-opt 设置所在城市')
		wf.send_feedback()
		return
	if api_key is None:
		api_key = u'TAkhjf8d1nlSlspN'

	city_name = city[1]

	url = u'https://api.caiyunapp.com/v2/' + api_key + u'/' + city[5] + u',' + city[4] + u'/realtime.json'
	log.debug(url)
	r = web.get(url)
	data = r.json()
	log.debug(data)
	if 'ok' == data['status']:
		result = data['result']
		item = Data.weather_dict.get(result['skycon'])
		wf.add_item(subtitle=city_name + u'天气', title=item.get('name'), icon=item.get('icon'))
		wf.add_item(subtitle=u'相对湿度' + str(result['humidity'] * 100) + u'%',
					title=u'温度' + str(result['temperature']) + u'°',
					icon='assets/thermometer.png')
		wd = result['wind']['direction']
		ws = result['wind']['speed']
		set_wind_item(wd, ws)
		wf.add_item(u'空气质量指数' + str(result['aqi']), subtitle=u'PM2.5 ' + str(result['pm25']), icon='icon.png')
	wf.send_feedback()


def set_wind_item(wd, ws):
	from data import Data
	if ws <= 2:
		wf.add_item(icon=u'assets/wind-sign.png', title=u'无风')
	else:
		wf.add_item(icon=u'assets/wind-sign-1.png', title=Data.get_wind_direction(wd),
					subtitle=Data.get_wind_speed(ws) + u'\t' + str(ws) + u'公里/小时')


if __name__ == '__main__':
	# Create a global `Workflow` object
	wf = Workflow3()
	# Call your entry function via `Workflow.run()` to enable its helper
	# functions, like exception catching, ARGV normalization, magic
	# arguments etc.
	log = wf.logger

	sys.exit(wf.run(main))
