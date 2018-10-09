import json
from mapbox import Datasets
access_token = '<api key with read, write, and list access for Datasets>'

# Remove any datasets with the name "demo". This can be removed for wider use
[datasets.delete_dataset(d['id']) for d in datasets.list().json() if d['name'] == 'demo']

# Create a new, empty dataset and get info about it
datasets = Datasets(access_token = access_token)
create_resp = datasets.create(name = 'demo', description = 'Demo dataset for Datasets and Uploads APIs')
dataset_info = create_resp.json()
print(dataset_info)

# Add data to new dataset
# Make sure there is no "id" key-value pair outside the "properties" object. Mapbox has pretty strict standards for GeoJSON.
data = json.load(open(r'demo_pts.geojson'))
for count, feature in enumerate(data['features']):
    print('{}, {}'.format(count, feature))
    resp = datasets.update_feature(dataset_info['id'], count, feature)
    print(resp)