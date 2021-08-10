import folium
from folium.plugins import HeatMap
import json
import webbrowser
import os

point_data = json.loads(open('./0721_22/data/point.json', mode='r', encoding='utf-8').read())

m2 = folium.Map(location=[36.505354, 127.704334], zoom_start=7, tiles='Cartodb Positron')
HeatMap(point_data).add_to(m2)

m2.save('./0721_22/heatmap.html')

chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'    # 라즈비안에선 필요없음
print(os.getcwd())
webbrowser.get(chrome_path).open(os.getcwd() + '/0721_22/heatmap.html')
#webbrowser.open(os.getcwd() + '/data/heatmap.html')                        # 라즈비안에서 실행시