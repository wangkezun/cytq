# coding=utf-8
import sys
from ualfred import Workflow3, notify

log = None


def main(wf):
	import pickle
	from data import Data
	from ualfred import web

	city = wf.stored_data('cy-city')
	api_key = wf.get_password('apiKey')

	if city is None:
		wf.add_item('请通过cy-opt 设置所在城市')
		wf.send_feedback()
		return
	if api_key is None:
		api_key = 'TAkhjf8d1nlSlspN'

	city_name = city[1]

	url = 'https://api.caiyunapp.com/v2/' + api_key + '/' + city[5] + ',' + city[4] + '/realtime.json'
	log.debug(url)
	r = web.get(url)
	data = r.json()
	log.debug(data)
	if 'ok' == data['status']:
		result = data['result']
		item = Data.weather_dict.get(result['skycon'])
		wf.add_item(subtitle=city_name + '天气', title=item.get('name'), icon=item.get('icon'))
		wf.add_item(subtitle='相对湿度' + str(result['humidity'] * 100) + '%',
					title='温度' + str(result['temperature']) + '°',
					icon='assets/thermometer.png')
		wd = result['wind']['direction']
		ws = result['wind']['speed']
		set_wind_item(wd, ws)
		wf.add_item('空气质量指数' + str(result['aqi']), subtitle='PM2.5 ' + str(result['pm25']), icon='icon.png')
	wf.send_feedback()


def set_wind_item(wd, ws):
	from data import Data
	if ws <= 2:
		wf.add_item(icon='assets/wind-sign.png', title='无风')
	else:
		wf.add_item(icon='assets/wind-sign-1.png', title=Data.get_wind_direction(wd),
					subtitle=Data.get_wind_speed(ws) + '\t' + str(ws) + '公里/小时')


if __name__ == '__main__':
	# Create a global `Workflow` object
	wf = Workflow3()
	# Call your entry function via `Workflow.run()` to enable its helper
	# functions, like exception catching, ARGV normalization, magic
	# arguments etc.
	log = wf.logger

	sys.exit(wf.run(main))
