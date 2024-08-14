import db.match_crud as mcrud
from model.tennismatch import TennisMatch
from model.user import User
import json
from service import user_service

def get_player_matches(user: User):
    player_matches = mcrud.get_user_matches(user.access_token)
    match_array = []
    for match_query in player_matches:
        match_obj=TennisMatch.from_json(match_query)
        #match_obj.relatorio()
        match_array.append(match_obj)
        print(match_query)
    
   
    return match_array

def get_player_matches_id(user: User):
    player_matches = mcrud.get_user_matches(user.access_token)
    #print('=')
    #print(player_matches)
    #print('=')
    match_array = []
    for match_query in player_matches:
        match_query = json.loads(match_query)
        match_array.append(match_query['idMatch'])
    return match_array


def add_match(match: TennisMatch):
    
    access_token,refresh_token = user_service.load_tokens()
    match_info = match.to_json() 
    mcrud.create_match(match_info, access_token, refresh_token)


def get_match(match_id):
    match = mcrud.get_match_by_id(match_id)
    #print(match)
    match = TennisMatch.from_dict(match)
    match.match_id = match_id
    return match

def update_match(match: TennisMatch):
    access_token,refresh_token = user_service.load_tokens()
    match_info = match.to_json()
    mcrud.update_match(match_info, access_token, refresh_token)

def delete_match(match_id, token):

    mcrud.delete_match(match_id, token)