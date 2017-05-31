# coding=utf-8
import sys
from workflow import Workflow3, notify

log = None


def main(wf):
	import cPickle
	from data import Data
	from workflow import web

	city = wf.stored_data(u'cy-city')
	api_key = wf.get_password(u'apiKey')

	if city is None:
		wf.add_item(u'请通过cy-opt 设置所在城市')
		wf.send_feedback()
		return
	if api_key is None:
		api_key = u'TAkhjf8d1nlSlspN'

	city_name = city[1]

	url = u'https://api.caiyunapp.com/v2/' + api_key + u'/' + city[5] + u',' + city[4] + u'/forecast.json'
	log.debug(url)
	r = web.get(url)
	data = r.json()
	log.debug(data)
	if u'ok' == data[u'status']:
		result = data[u'result']
		wf.add_item(subtitle=city_name + u'未来24小时天气预报', title=result[u'hourly'][u'description'])
		wf.add_item(title=result[u'minutely'][u'description'])
		daily = result[u'daily']
		for i in range(1, 5):
			skycon = daily[u'skycon'][i]
			temp = daily[u'temperature'][i]
			wind = daily[u'wind'][i]
			ultraviolet = daily[u'ultraviolet'][i]
			aqi = daily[u'aqi'][i]
			subtitle = city_name + skycon[u'date'] + u'天气预报'
			item = Data.weather_dict.get(skycon[u'value'])
			# add first
			title = item.get(u'name')
			# add temperature
			title += u'\t温度:' + str(temp[u'max']) + u'°~' + str(temp[u'min']) + u'° \t'
			# add wind
			title += Data.get_wind_direction(wind[u'avg'][u'direction']) + Data.get_wind_speed(wind[u'avg'][u'speed'])
			# add ultraviolet
			title += u'\t紫外线:' + ultraviolet[u'desc']
			# add aqi
			title += u'\tAQI:' + str(aqi['min']) + u'~' + str(aqi['max'])

			wf.add_item(subtitle=subtitle, title=title, icon=item.get(u'icon'), copytext=subtitle + u':' + title)

	wf.send_feedback()


if __name__ == '__main__':
	# Create a global `Workflow` object
	wf = Workflow3()
	# Call your entry function via `Workflow.run()` to enable its helper
	# functions, like exception catching, ARGV normalization, magic
	# arguments etc.
	log = wf.logger

	sys.exit(wf.run(main))
