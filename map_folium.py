import folium
import pandas

def h_color(elev):
    minimum_h = int(min(df['ELEV']))
    step = int((max(df['ELEV']-min(df['ELEV'])))/3)
    if elev in range(minimum_h,minimum_h+step):
        col = 'green'
    elif elev in range(minimum_h+step,minimum_h+step*2):
        col = 'red'
    else:
        col = 'blue'
    return col

df = pandas.read_csv('Volcano.txt')

map1 = folium.Map(location=[45.372,-121.697],zoom_start=6,tiles='Stamen Terrain')
for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    folium.Marker([lat,lon],popup=name,
                  icon=folium.Icon(color=h_color(elev))).add_to(map1)

map1.save('map.html')
