import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

infile = open('eq_data_1_day_m1.json', 'r')
outfile = open('readable_eq_data.json', 'w')

eqdata = json.load(infile)

json.dump(eqdata, outfile, indent=4)

list_of_eqs = eqdata['features']

mags, lons, lats = [], [], []

for eq in list_of_eqs:
    mag = eq['properties']['mag']
    lon = eq['geometry']['coordinates'][0]
    lat = eq['geometry']['coordinates'][1]

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:10])
print(lats[:10])


data = [Scattergeo(lon = lons, lat = lats)]

my_layout = Layout(title = 'Global Earthquakes 1 day')

fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename = 'global_eqs.html')






