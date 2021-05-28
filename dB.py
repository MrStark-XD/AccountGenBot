#    Copyright (C) DEVSEXPO 2020-2021
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from bot import mongo_client

m_s = mongo_client['accountgenbot']
sud = m_s['users']
shd = m_s['hits']

def add_user_to_db(user, no):
    stark = sud.find_one({"user": user})
    if stark:
        no2 = stark['no'] + 1
        sud.update_one(
            {"user": user}, {"$set": {"no": no2}}
        )
    else:
        sud.insert_one({'user': user, 'no': no})
       
def get_user_limit(user):
    stark1 = sud.find_one({"user": user})
    if stark1:
        return stark1['no']
    else:
        return 0
    
def get_all_users():
    stark2 = sud.find()
    if stark2:
        return list(stark2)
    else:
        return None
    
def dl_all_users():
    stark2 = sud.delete_many()
    
def dl_one_user(user):
    stark2 = sud.delete_one({'user': user})
    
def add_hits_to_db(hit):
    stark2 = shd.find_one({"hit": hit})
    if not stark2:
        shd.insert_one({'hit': hit})
        
def rm_all_hits():
    stark2 = shd.delete_many()
    
def all_hit():
    stark2 = shd.find()
    return list(stark2)
    
def rm_hit(hit):
    stark1 = shd.delete_one({"hit": hit})
    
def hit_exists(hit):
    stark2 = shd.find_one({'hit': hit})
    if stark2:
        return True
    else:
        return False
