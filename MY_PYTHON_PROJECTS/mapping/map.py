import folium
import pandas

data = pandas.read_csv("in.csv")

# extracting the data in separate lists
latitude = list(data["lat"])
longitude = list(data["lng"])
City = list(data["city"])
Population = list(data["population_proper"])


#function to change cirlce marker color depending upon population of the City in popup
def icon_color(population):
    if population < 100000:
        return 'blue'
    elif population > 100000 and population < 1000000:
        return 'orange'
    else:
        return 'red'

#including link with each popup for the corresponding city
myhtml = """
City:<br><a href="https://www.google.com/search?q=%s" target="_blank">%s</a><br>
<hr>
Population: %s """


map = folium.Map(location=[12.9716, 77.5946],zoom_start=6, tiles = "Stamen Terrain")

#adding a child using FeatureGroup, where Marker and GeoJson are feature.
fgp = folium.FeatureGroup(name="Population")

#GeoJson layer for Population based country separation
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'red' if x['properties']['POP2005'] < 10000000
else 'blue' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'dark green'}))

fgc = folium.FeatureGroup(name="City")

# City based Markers layer
for Lt, Ln, Ct,Pop in zip(latitude,longitude,City, Population):
    iframe = folium.IFrame(html=myhtml %(Ct, Ct, Pop), width=170, height=100)
    fgc.add_child(folium.CircleMarker(location=[Lt,Ln], popup=folium.Popup(iframe), radius=5,
    fill_color=icon_color(Pop), color='white', fill_opacity=0.6))


map.add_child(fgp)
map.add_child(fgc)
map.add_child(folium.LayerControl())
map.save("map1.html")
