import json

following = open("following.json", "r")
followers = open("followers.json", "r")

following_json = json.load(following)
followers_json = json.load(followers)

def parse_json(json_file, str_):
    curr_set = set()
    for user in json_file[str_]:
        curr_set.add(user['string_list_data'][0]['value'])
    return curr_set

not_following = parse_json(following_json, 'relationships_following') - parse_json(followers_json, 'relationships_followers')

for users_not_following in not_following:
    print(users_not_following)