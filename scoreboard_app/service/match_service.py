import db.match_crud as mcrud
from model.tennismatch import TennisMatch
from db import db

def get_player_matches(player_id):
    conn = db.connect()
    player_matches = mcrud.get_data(conn, f"owner_id = {player_id}")
    conn.close()
    match_array = []
    for match_query in player_matches:
        match_obj=TennisMatch.from_json(match_query['match_info'])
        match_obj.match_id = match_query['id']
        match_array.append(match_obj)
    return match_array

def get_player_matches_id(player_id):
    conn = db.connect()
    player_matches = mcrud.get_data(conn, f"owner_id = {player_id}")
    conn.close()
    match_array = []
    for match_query in player_matches:
        match_array.append(match_query['id'])
    return match_array


def add_match(owner_id, match: TennisMatch):
    print("adding match")
    match_info = match.to_json()
    conn = db.connect()
    mcrud.create_match(conn, owner_id, match_info)
    conn.close()

def get_match(match_id):
    conn = db.connect()
    match = mcrud.get_data(conn, f"id = {match_id}")
    conn.close()
    match = TennisMatch.from_json(match[0]['match_info'])
    match.match_id = match_id
    return match

def update_match(match_id, match: TennisMatch):
    conn = db.connect()
    match_info = match.to_json()
    mcrud.update_match(conn, match_id, match_info)
    conn.close()

def delete_match(match_id):
    conn = db.connect()
    mcrud.delete_match(conn, match_id)
    conn.close()