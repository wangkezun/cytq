# coding=utf-8
import sys


# init datas
class Data:
	def __init__(self):
		pass

	weather_dict = {'CLEAR_DAY': {'name': '晴天', 'icon': 'assets/sun-3.png'},
					'CLEAR_NIGHT': {'name': '晴夜', 'icon': 'assets/moon-1.png'},
					'PARTLY_CLOUDY_DAY': {'name': '多云', 'icon': 'assets/cloudy.png'},
					'PARTLY_CLOUDY_NIGHT': {'name': '多云', 'icon': 'assets/cloudy-night.png'},
					'CLOUDY': {'name': '阴', 'icon': 'assets/cloud.png'},
					'RAIN': {'name': '雨', 'icon': 'assets/rain-1.png'},
					'SNOW': {'name': '雪', 'icon': 'assets/snow.png'},
					'WIND': {'name': '风', 'icon': 'assets/windy.png'},
					'FOG': {'name': '雾', 'icon': 'assets/fogg.png'}, 'HAZE': {'name': '霾'},
					'SLEET': {'name': '冻雨'}}

	@staticmethod
	def get_wind_direction(wd):
		if wd <= 22.5 or wd > 337.5:
			return '北风'
		elif 22.5 < wd <= 67.5:
			return '东北风'
		elif 67.5 < wd <= 112.5:
			return '东风'
		elif 112.5 < wd <= 157.5:
			return '东南风'
		elif 157.5 < wd <= 202.5:
			return '南风'
		elif 202.5 < wd <= 247.5:
			return '西南风'
		elif 247.5 < wd <= 292.5:
			return '西风'
		elif 292.5 < wd <= 337.5:
			return '西北风'

	@staticmethod
	def get_wind_speed(ws):
		if ws <= 2:
			return '无风'
		if 2 < ws <= 6:
			return '软风'
		elif 6 < ws <= 12:
			return '轻风'
		elif 12 < ws <= 19:
			return '缓风'
		elif 19 < ws <= 30:
			return '和风'
		elif 30 < ws <= 40:
			return '清风'
		elif 40 < ws <= 51:
			return '强风'
		elif 51 < ws <= 62:
			return '疾风'
		elif 62 < ws <= 75:
			return '烈风'
		elif 75 < ws <= 87:
			return '增强烈风'
		elif 87 < ws <= 103:
			return '暴风'
		elif 103 < ws <= 149:
			return '台风'
		elif 149 < ws <= 183:
			return '强台飓风'
		elif 183 < ws <= 220:
			return '超强台飓风'
		else:
			return '极强台飓风'
