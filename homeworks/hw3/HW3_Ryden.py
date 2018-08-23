import sys
# Change the following for your own Dropbox path
sys.path.insert(0, '/Users/ryden/Dropbox/Coding/Secrets')

from MeetupAPI import *
import meetup.api
client = meetup.api.Client(api_key)
groups = client.GetFindGroups(zip = '63132')
# check inside the object
# groups[0].__dict__

# Q1
def MostMembers(x):
    all_members = [i.members for i in x]
    largest_group = all_members.index(max(all_members))
    return x[largest_group].name

popular_group = MostMembers(groups)
popular_group
# u'Saint Louis Volunteer Group'

# Q2
group_members = client.GetMembers(group_id = groups[largest_group].__dict__['id'])
# check inside object
# members.__dict__['results'][0].keys()

def MostPopular(x):
    member_ids = [i['id'] for i in x.results]
    member_groups = [client.GetGroups(member_id = i) for i in member_ids]
    group_counts = [i.meta['count'] for i in member_groups]
    most_groups = group_counts.index(max(group_counts))
    most_popular = x.results[most_groups]
    return {'name' : most_popular['name'], 'id' : most_popular['id'], 'groups' : member_groups[most_groups]}

popular_user = MostPopular(group_members)
popular_user['name']
# u'Alf'

# Q3
MostMembers(meetup.api.MeetupObjectList(popular_user['groups'].results))
# u'Michigan Adventurers Club'

