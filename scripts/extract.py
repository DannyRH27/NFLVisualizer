import json
import requests
import os
import time

# with open('/Users/dannyhuang/Desktop/NFL_QB_JSON_Conversions/League Hierarchy.json') as f:
# 	league = json.load(f)

# # team_name_and_ids= []
# # for conference in league['conferences']:
# # 	for division in conference['divisions']:
# # 		for team in division['teams']:
# # 			team_name_and_ids.append((team['name'], team['id']))

YEARS = range(2000, 2016)
SEASONS = [ 'REG', 'PST']

write_path = '/Users/dannyhuang/Desktop/NFL_QB_JSON_Conversions/'
for year in YEARS:
  for season in SEASONS:
    request_url = 'http://api.sportradar.us/nfl/official/trial/v5/en/seasons/{}/{}/teams/39f349de-6463-4803-ad70-f1e0f144f5ed/statistics.json?api_key=7pvd482f2nqjqek5qes5rhjb'.format(year, season)
    r = requests.get(request_url)
    print('processing', year, season, r)
    with open(os.path.join(write_path, str(year), season + "_" + 'Rams'+ ".json"), 'w') as f:
      f.write(r.text)
    print('done writing')
    time.sleep(5)