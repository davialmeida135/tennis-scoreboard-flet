import copy
from datetime import datetime
class TennisMatch:
    def __init__(self, player1 : str, player2 : str, max_sets=3):
        self.player1 = player1
        self.player2 = player2
        self.match_moment = MatchMoment()
        self.history_undo = []
        self.history_redo = []
        self.max_sets = max_sets
        self.title = f"{player1} x {player2} : {datetime.now().strftime('%Y-%m-%d %H:%M')}"
        

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
        if player == self.player2:
            self.match_moment.current_set.player2_score += 1
            self.match_moment.current_game = Game()

        #6x4,7x5 
        if self.match_moment.current_set.player1_score >= 6 and self.match_moment.current_set.player1_score - self.match_moment.current_set.player2_score>=2:
            self.match_moment.sets.append(self.match_moment.current_set)
            self.match_moment.current_set = Set()
            self.match_moment.current_game = Game()
        #4x6,5x7   
        elif self.match_moment.current_set.player2_score >= 6 and self.match_moment.current_set.player2_score - self.match_moment.current_set.player1_score>=2:
            self.match_moment.sets.append(self.match_moment.current_set)
            self.match_moment.current_set = Set()
        #6x6
        elif self.match_moment.current_set.player1_score == 6 and self.match_moment.current_set.player2_score == 6:
            self.match_moment.current_game = Tiebreak()
        #7x6,6x7
        elif self.match_moment.current_set.player1_score == 7 or self.match_moment.current_set.player2_score == 7:
            self.match_moment.sets.append(self.match_moment.current_set)
            self.match_moment.current_set = Set()
            self.match_moment.current_game = Game()      

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

    

class Set:
    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0
    def print_scores(self):
        print("(Set)Player 1 Score:", self.player1_score)
        print("(Set)Player 2 Score:", self.player2_score)


class Game:
    def __init__(self):
        self.player1_score = '0'
        self.player2_score = '0'
    def print_scores(self):
        print("(Game)Player 1 Score no game:", self.player1_score)
        print("(Game)Player 2 Score no game:", self.player2_score)
    

class Tiebreak:
    def __init__(self, max_score=7, min_difference=2):
        self.player1_score = 0
        self.player2_score = 0
        self.max_score = max_score
        self.min_difference = min_difference
    def print_scores(self):
        print("(Tiebreak)Player 1 Score:", self.player1_score)
        print("(Tiebreak)Player 2 Score:", self.player2_score)
