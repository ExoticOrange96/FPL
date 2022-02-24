import requests
import pandas as pd
import numpy as np

url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
r = requests.get(url)
#transforms into a json object
json = r.json()

json.keys()
#dict_keys(['events', 'game_settings', 'phases', 'teams', 'total_players', 'elements', 'element_stats', 'element_types'])

#build a dataframe
elements_df = pd.DataFrame(json['elements']) #stores literally everything
elements_types_df = pd.DataFrame(json['element_types']) #stores the positions
teams_df = pd.DataFrame(json['teams']) #stores the team names

#smaller dataframe with relevant details
slim_elements_df = elements_df[['second_name','team','element_type','selected_by_percent','now_cost','minutes','transfers_in','value_season','total_points']]

slim_elements_df['positions'] = slim_elements_df.element_type.map(elements_types_df.set_index('id').singular_name)
slim_elements_df['club'] = slim_elements_df.team.map(teams_df.set_index('id').name)

slim_elements_df['value'] = slim_elements_df.value_season.astype(float) #VALUE = POINTS/COST

slim_elements_df.sort_values('value',ascending=False)
df = slim_elements_df.drop(['team'], axis = 1)
df = df.drop(['element_type'], axis = 1)
df = df.drop(['value_season'], axis = 1)
df = df.rename(columns={"second_name":"Name" , "selected_by_percent":"Selected %" , "now_cost":"Current cost" , "minutes":"Minutes Played", "transfers_in":"Transfered in", "total_points":"Total Points"})

print("What are you searching for?")
print("press 1 for Position")
print("press 2 for Club ")
print("press 3 for specific player " )
ans1 = int(input())

if(ans1 == 1):
  ans = input("Which position are you searching for? ")
  if(ans == "Defenders"):
    print(df.loc[df['positions'] == 'Defender'])
  elif(ans == "Forwards"):
    print(df.loc[df['positions'] == 'Forward'])
  elif(ans == "Midfielders"):
    print(df.loc[df['positions'] == 'Midfielder'])
  elif(ans == "Goalkeepers"):
    print(df.loc[df['positions'] == 'Goalkeeper'])


elif(ans1 == 2):
  ans3 = input("Which club are you searching for? ")
  ans2 = input("Are you looking for a specific postion in this club? y/n ")
  if(ans2 == 'y'):
      txt = input("Which position are you searching for? ")
      ans4 = txt.capitalize()
      if(ans4 == "Defenders" or ans4 == "Defender"):
        print(df.loc[(df['positions'] == 'Defender') & (df['club'] == ans3)])
      elif(ans4 == 'Forwards' or ans4 == "forward"):
        print(df.loc[(df['positions'] == 'Forward') & (df['club'] == ans3)])
      elif(ans4 == "Midfielders" or ans4 == "Midfielder"):
        print(df.loc[(df['positions'] == 'Midfielder') & (df['club'] == ans3)])
      elif(ans4 == "Goalkeepers" or ans4 == "Goalkeeper" ):
        print(df.loc[(df['positions'] == 'Goalkeeper') & (df['club'] == ans3)])
  else:
    print(df.loc[df['club'] == ans3])
else:
  ans5 = input("Enter the player's second name ")
  print(df.loc[df['Name'] == ans5])