# coding=utf-8
import sys


# init datas
class Data:
	def __init__(self):
		pass

	weather_dict = {u'CLEAR_DAY': {u'name': u'晴天', u'icon': u'assets/sun-3.png'},
					u'CLEAR_NIGHT': {u'name': u'晴夜', u'icon': u'assets/moon-1.png'},
					u'PARTLY_CLOUDY_DAY': {u'name': u'多云', u'icon': u'assets/cloudy.png'},
					u'PARTLY_CLOUDY_NIGHT': {u'name': u'多云', u'icon': u'assets/cloudy-night.png'},
					u'CLOUDY': {u'name': u'阴', u'icon': u'assets/cloud.png'},
					u'RAIN': {u'name': u'雨', u'icon': u'assets/rain-1.png'},
					u'SNOW': {u'name': u'雪', u'icon': u'assets/snow.png'},
					u'WIND': {u'name': u'风', u'icon': u'assets/windy.png'},
					u'FOG': {u'name': u'雾', u'icon': u'assets/fogg.png'}, u'HAZE': {u'name': u'霾'},
					u'SLEET': {u'name': u'冻雨'}}

	@staticmethod
	def get_wind_direction(wd):
		if wd <= 22.5 or wd > 337.5:
			return u'北风'
		elif 22.5 < wd <= 67.5:
			return u'东北风'
		elif 67.5 < wd <= 112.5:
			return u'东风'
		elif 112.5 < wd <= 157.5:
			return u'东南风'
		elif 157.5 < wd <= 202.5:
			return u'南风'
		elif 202.5 < wd <= 247.5:
			return u'西南风'
		elif 247.5 < wd <= 292.5:
			return u'西风'
		elif 292.5 < wd <= 337.5:
			return u'西北风'

	@staticmethod
	def get_wind_speed(ws):
		if ws <= 2:
			return u'无风'
		if 2 < ws <= 6:
			return u'软风'
		elif 6 < ws <= 12:
			return u'轻风'
		elif 12 < ws <= 19:
			return u'缓风'
		elif 19 < ws <= 30:
			return u'和风'
		elif 30 < ws <= 40:
			return u'清风'
		elif 40 < ws <= 51:
			return u'强风'
		elif 51 < ws <= 62:
			return u'疾风'
		elif 62 < ws <= 75:
			return u'烈风'
		elif 75 < ws <= 87:
			return u'增强烈风'
		elif 87 < ws <= 103:
			return u'暴风'
		elif 103 < ws <= 149:
			return u'台风'
		elif 149 < ws <= 183:
			return u'强台飓风'
		elif 183 < ws <= 220:
			return u'超强台飓风'
		else:
			return u'极强台飓风'
