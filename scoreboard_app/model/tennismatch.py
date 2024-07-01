import copy
from datetime import datetime
import json
import sys,os


class TennisMatch:
    def __init__(self, player1 : str, player2 : str, match_id, max_sets=3):

        self.match_id = match_id
        self.player1 = player1
        self.player2 = player2
        self.match_moment = MatchMoment()
        self.history_undo = []
        self.history_redo = []
        self.max_sets = max_sets
        self.title = f"{player1} x {player2} : {datetime.now().strftime('%Y-%m-%d %H:%M')}"

    def to_dict(self):
        return {
            'match_id': self.match_id,
            'title': self.title,
            'player1': self.player1,
            'player2': self.player2,
            'match_moment': self.match_moment.to_dict(),  # assuming MatchMoment has a to_dict method
            'history_undo': [moment.to_dict() for moment in self.history_undo[-5:]],  # assuming MatchMoment has a to_dict method
            'history_redo': [moment.to_dict() for moment in self.history_undo[-5:]],  # assuming MatchMoment has a to_dict method
        }
        
    def to_json(self):
        return json.dumps(self.to_dict(), sort_keys=True, indent=4)
    
    @classmethod
    def from_dict(cls, data):
        match = cls(data['player1'], data['player2'], data['match_id'])
        match.match_moment = MatchMoment.from_dict(data['match_moment'])  # assuming MatchMoment has a from_dict method
        match.history_undo = [MatchMoment.from_dict(moment) for moment in data['history_undo']]  # assuming MatchMoment has a from_dict method
        match.history_redo = [MatchMoment.from_dict(moment) for moment in data['history_redo']]  # assuming MatchMoment has a from_dict method
        match.title = data['title']
        return match
    
    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls.from_dict(data)
    
    def start_match(self):
        self.match_moment.current_set = Set()
        self.match_moment.current_game = Game()
        

    def end_match(self):
        # Perform any necessary cleanup or calculations
        pass

    def point(self, player):
        self.history_undo.append(copy.deepcopy(self.match_moment))
        self.history_redo = []
        if type(self.match_moment.current_game) == Tiebreak:            
            self.update_tiebreak(player)
        
        elif type(self.match_moment.current_game) == Game:            
            self.update_game(player)
        else:           
            return
        


    def update_game(self, player):
        
        if player == self.player1:
                   
            #0 -> 15 pontos
            if self.match_moment.current_game.player1_score == '0':
                self.match_moment.current_game.player1_score = '15'
            #15 ->30 pontos
            elif self.match_moment.current_game.player1_score == '15':
                self.match_moment.current_game.player1_score = '30'
            #30 -> 40 pontos
            elif self.match_moment.current_game.player1_score == '30':
                self.match_moment.current_game.player1_score = '40'
            #40->game
            elif self.match_moment.current_game.player1_score == '40' and self.match_moment.current_game.player2_score in ['0', '15', '30']:
                self.update_set(player)
            #40 iguais
            elif self.match_moment.current_game.player1_score == '40' and self.match_moment.current_game.player2_score == '40':
                self.match_moment.current_game.player1_score = 'AD'
            #vantagem player1 (game)
            elif self.match_moment.current_game.player1_score == 'AD':
                self.update_set(player)
            #vantagem player2
            elif self.match_moment.current_game.player2_score == 'AD':
                self.match_moment.current_game.player1_score = '40'
                self.match_moment.current_game.player2_score = '40'

            
        if player == self.player2:
             
            #0 -> 15 pontos
            if self.match_moment.current_game.player2_score == '0':
                self.match_moment.current_game.player2_score = '15'
            #15 ->30 pontos
            elif self.match_moment.current_game.player2_score == '15':
                self.match_moment.current_game.player2_score = '30'
            #30 -> 40 pontos
            elif self.match_moment.current_game.player2_score == '30':
                self.match_moment.current_game.player2_score = '40'
            #40->game
            elif self.match_moment.current_game.player2_score == '40' and self.match_moment.current_game.player1_score in ['0', '15', '30']:
                self.update_set(player)
            #40 iguais
            elif self.match_moment.current_game.player2_score == '40' and self.match_moment.current_game.player1_score == '40':
                self.match_moment.current_game.player2_score = 'AD'
            #vantagem player2 (game)
            elif self.match_moment.current_game.player2_score == 'AD':
                self.update_set(player)
            #vantagem player1
            elif self.match_moment.current_game.player1_score == 'AD':
                self.match_moment.current_game.player1_score = '40'
                self.match_moment.current_game.player2_score = '40'
                    
    def update_set(self, player): 
        if player == self.player1:
            self.match_moment.current_set.player1_score += 1
            self.match_moment.current_game = Game()
            #6x4,7x5 player 1
            if self.match_moment.current_set.player1_score >= 6 and self.match_moment.current_set.player1_score - self.match_moment.current_set.player2_score>=2:
                self.match_moment.sets.append(self.match_moment.current_set)
                self.match_moment.current_set = Set()
                self.match_moment.current_game = Game()
                self.match_moment.match_score_p1 += 1
                return
            #7x6,6x7 player 1
            elif self.match_moment.current_set.player1_score == 7:
                self.match_moment.sets.append(self.match_moment.current_set)
                self.match_moment.current_set = Set()
                self.match_moment.current_game = Game()
                self.match_moment.match_score_p1 += 1
                return

        if player == self.player2:
            self.match_moment.current_set.player2_score += 1
            self.match_moment.current_game = Game()

            #4x6,5x7  player2
            if self.match_moment.current_set.player2_score >= 6 and self.match_moment.current_set.player2_score - self.match_moment.current_set.player1_score>=2:
                self.match_moment.sets.append(self.match_moment.current_set)
                self.match_moment.current_set = Set()
                self.match_moment.match_score_p2 += 1
                return
            #6x7 player 2
            elif self.match_moment.current_set.player2_score == 7:
                self.match_moment.sets.append(self.match_moment.current_set)
                self.match_moment.current_set = Set()
                self.match_moment.current_game = Game()
                self.match_moment.match_score_p2 += 1
                return
      
        #6x6
        if self.match_moment.current_set.player1_score == 6 and self.match_moment.current_set.player2_score == 6:
            self.match_moment.current_game = Tiebreak()
            

    def update_tiebreak(self, player):
        
        if player == self.player1:
            self.match_moment.current_game.player1_score += 1
        if player == self.player2:
            self.match_moment.current_game.player2_score += 1
        
        if self.match_moment.current_game.player1_score >= self.match_moment.current_game.max_score and self.match_moment.current_game.player1_score - self.match_moment.current_game.player2_score >= self.match_moment.current_game.min_difference:
            self.update_set(self.player1)
        elif self.match_moment.current_game.player2_score >= self.match_moment.current_game.max_score and self.match_moment.current_game.player2_score - self.match_moment.current_game.player1_score >= self.match_moment.current_game.min_difference:
            self.update_set(self.player2)

    def update_history(self):
        self.history_undo.append(self.match_moment)

    def undo(self):
        if len(self.history_undo)> 0:
            self.history_redo.append(copy.deepcopy(self.match_moment))
            self.match_moment = self.history_undo.pop()
            return
        return

    def redo(self):
        if len(self.history_redo) > 0:
            self.history_undo.append(copy.deepcopy(self.match_moment))
            self.match_moment = self.history_redo.pop()
            return
        return

    def relatorio(self):
        print("Match id: ", self.match_id)
        print("Player 1: ", self.player1)
        print("Player 2: ", self.player2)

        for set in range(len(self.match_moment.sets)):
            print(str(set)+" set : ")
            self.match_moment.sets[set].print_scores()
        print("Current Set: ") 
        self.match_moment.current_set.print_scores()
        print("Current game: ")
        self.match_moment.current_game.print_scores()


class MatchMoment():
    def __init__(self):
        self.sets = []
        self.current_set = None
        self.current_game = None
        self.match_score_p1 = 0
        self.match_score_p2 = 0

    def to_dict(self):
        return {
            'sets': [set.to_dict() for set in self.sets],  # assuming Set has a to_dict method
            'current_set': self.current_set.to_dict() if self.current_set else None,  # assuming Set has a to_dict method
            'current_game': self.current_game.to_dict() if self.current_game else None,  # assuming Game has a to_dict method
            'match_score_p1': self.match_score_p1,
            'match_score_p2': self.match_score_p2,
        }
    
    @classmethod
    def from_dict(cls, data):
        moment = cls()
        moment.sets = [Set.from_dict(set) for set in data['sets']]  
        moment.current_set = Set.from_dict(data['current_set']) if data['current_set'] else None     
        moment.match_score_p1 = int(data['match_score_p1'])
        moment.match_score_p2 = int(data['match_score_p2'])

        if moment.current_set.player1_score==6 and moment.current_set.player2_score==6:
            moment.current_game = Tiebreak.from_dict(data['current_game'])
        else:
            moment.current_game = Game.from_dict(data['current_game'])

        return moment
    

class Set:
    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0
    def print_scores(self):
        print("(Set)Player 1 Score:", self.player1_score)
        print("(Set)Player 2 Score:", self.player2_score)

    def to_dict(self):
        return {
            'player1_score': self.player1_score,
            'player2_score': self.player2_score,
        }
    
    @classmethod
    def from_dict(cls, data):
        set = cls()
        set.player1_score = int(data['player1_score'])
        set.player2_score = int(data['player2_score'])
        return set

class Game:
    def __init__(self):
        self.player1_score = '0'
        self.player2_score = '0'
    def print_scores(self):
        print("(Game)Player 1 Score no game:", self.player1_score)
        print("(Game)Player 2 Score no game:", self.player2_score)
    def to_dict(self):
        return {
            'player1_score': self.player1_score,
            'player2_score': self.player2_score,
        }
    @classmethod
    def from_dict(cls, data):
        game = cls()
        game.player1_score = data['player1_score']
        game.player2_score = data['player2_score']
        return game

class Tiebreak:
    def __init__(self, max_score=7, min_difference=2):
        self.player1_score = 0
        self.player2_score = 0
        self.max_score = max_score
        self.min_difference = min_difference
    def print_scores(self):
        print("(Tiebreak)Player 1 Score:", self.player1_score)
        print("(Tiebreak)Player 2 Score:", self.player2_score)
    def to_dict(self):
        return {
            'player1_score': self.player1_score,
            'player2_score': self.player2_score,
        }
    @classmethod
    def from_dict(cls, data):
        game = cls()
        game.player1_score = int(data['player1_score'])
        game.player2_score = int(data['player2_score'])
        return game
    
'''
p = TennisMatch('Davi','Gustavo',13)
p.start_match()

for i in range(20):
    p.point('Davi')
for i in range(24):
    p.point('Gustavo')
for i in range(6):
    p.point('Davi')
p.point('Gustavo')


p.relatorio()
print("==========================================")
#print(p.to_json())
print("==========================================")

q = TennisMatch.from_json(p.to_json())
q.relatorio()
q.point('Davi')
q.relatorio()
''' 