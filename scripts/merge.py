import json
import requests
import os
import time


for year in range(2000,2020):
  for dirpath, dirnames, filenames in os.walk('/Users/dannyhuang/Desktop/NFL_QB_JSON_Conversions/{}'.format(year)): 
    master_reg = []
    master_pst = []
    for filename in filenames:
      if not filename.endswith('.json'):
        continue

      with open(os.path.join(dirpath, filename)) as f:
        data = json.load(f)
        # print(data)
        if filename.startswith('PST'):
            # master_pst[data["name"]] = { "season": data["season"]}
            # master_pst[data["name"]] = {}
            # master_pst[data["name"]]["players"] = {}
            # print(dirpath, filename))
            if len(data["players"]) == 0:
              continue
            for player in data["players"]: 
              if "position" in player and player["position"] == "QB":
                player["team"] = data["name"]
                player["year"] = data["season"]["year"]
                player["type"] = data["season"]["type"]
                master_pst.append(player)
        else:
          if len(data["players"]) == 0:
              continue
          for player in data["players"]: 
            if "position" in player and player["position"] == "QB":
              player["team"] = data["name"]
              player["year"] = data["season"]["year"]
              player["type"] = data["season"]["type"]
              master_reg.append(player)
    # print(master_pst)
    with open(os.path.join(dirpath, 'Draft_PST.json'), 'w') as f: 
      f.write(json.dumps(master_pst))
    with open(os.path.join(dirpath, 'Draft_REG.json'), 'w') as f: 
      f.write(json.dumps(master_reg))
  # print(dirpath, dirnames, filenames)
# fdata = {}
# f1data = f2data = "" 
# # loop through years. for each year
# #   combine base dir path with year to get full dir path. Go through all files with os.walk
# #   collect all json into one big json
# #   when done walking, write to one big json file
# with open('/Users/dannyhuang/Desktop/NFL QB JSON Coversions/2002/PST_49ers.json') as f1: 
#   f1data = f1.read() 
# with open('/Users/dannyhuang/Desktop/NFL QB JSON Coversions/2002/PST_Bears.json') as f2: 
#   f2data = f2.read() 
 
# f1data += "\n"
# f1data += f2data
# write_path = '/Users/dannyhuang/Desktop/NFL QB JSON Coversions/Master/'
# with open(os.path.join(write_path, "PST_MASTER" + ".json"), 'w') as f3:
#   f3.write(f1data)