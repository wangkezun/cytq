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

	url = 'https://api.caiyunapp.com/v2/' + api_key + '/' + city[2] + ',' + city[3] + '/forecast.json'
	log.debug(url)
	r = web.get(url)
	data = r.json()
	log.debug(data)
	if 'ok' == data['status']:
		result = data['result']
		wf.add_item(subtitle=city_name + '未来24小时天气预报', title=result['hourly']['description'])
		wf.add_item(title=result['minutely']['description'])
		daily = result['daily']
		for i in range(1, 5):
			skycon = daily['skycon'][i]
			temp = daily['temperature'][i]
			wind = daily['wind'][i]
			ultraviolet = daily['ultraviolet'][i]
			aqi = daily['aqi'][i]
			subtitle = city_name + skycon['date'] + '天气预报'
			item = Data.weather_dict.get(skycon['value'])
			# add first
			title = item.get('name')
			# add temperature
			title += '\t温度:' + str(temp['max']) + '°~' + str(temp['min']) + '° \t'
			# add wind
			title += Data.get_wind_direction(wind['avg']['direction']) + Data.get_wind_speed(wind['avg']['speed'])
			# add ultraviolet
			title += '\t紫外线:' + ultraviolet['desc']
			# add aqi
			title += '\tAQI:' + str(aqi['min']) + '~' + str(aqi['max'])

			wf.add_item(subtitle=subtitle, title=title, icon=item.get('icon'), copytext=subtitle + ':' + title)

	wf.send_feedback()


if __name__ == '__main__':
	# Create a global `Workflow` object
	wf = Workflow3()
	# Call your entry function via `Workflow.run()` to enable its helper
	# functions, like exception catching, ARGV normalization, magic
	# arguments etc.
	log = wf.logger

	sys.exit(wf.run(main))
