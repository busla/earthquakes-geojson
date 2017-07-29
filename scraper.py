import requests
import geojson

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_geojson():
    res = requests.get('http://apis.is/earthquake/is')

    geo_data = []
    for item in res.json()['results']:
        point = geojson.Point((item['longitude'], item['latitude']))
        feature = geojson.Feature(geometry=point, properties=item)
        geo_data.append(feature)

    feature_collection = geojson.FeatureCollection(geo_data)
    return jsonify(feature_collection)