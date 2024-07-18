from player_tictac import PlayerTictac
from seahorse.game.action import Action #type: ignore 
from seahorse.game.game_state import GameState, Player #type: ignore

import random


class MyPlayer(PlayerTictac):

    def compute_action(self, current_state: GameState, **kwargs) -> Action:
        
        
        
        scoresDictionary = {}
        nextScoreDictionnary = {}
        mostProfitableMove = None
        #current_state (GameState): The current game state.
        #Returns: Action: The selected action.

        ### ALL OF THE CURRENT CONTENT IS JUST HELPFUL RESSOURCES. THE BOT JUST PLAYS A RANDOM MOVE ###

        # this is the time remaining for the game for your player
        """time_before = self.get_remaining_time()"""

        # this is how to get the next state for the possible actions (like if it was played what would be the new gamestate)
        """for action in possible_actions:
            next_state_for_action = action.get_next_game_state()
        """
        players_list = current_state.get_players()
        player_index = players_list.index(self)
        otherPlayerIndex = 1 if player_index == 0 else 0
        possible_actions: set(Action) = current_state.generate_possible_actions() # type: ignore
        dict_of_current_pieces_played = current_state.get_rep().get_env()
        my_player_id = self.get_my_player_id(current_state=current_state)
        potentially_valuable: list[Action] = []
        valuable: list[Action] = []
        
        #Finds the score difference between the current position and the next position for each move
        def FindScoreDifferences(possible_actions, player_index):
            #Gets the current score
            currentScore = current_state.get_scores()
            #Checks the score for each possible move
            for action in possible_actions:
                nextScore = action.get_next_game_state().get_scores()
                #Score difference is futur score-current score
                scoreDifference = nextScore[list(nextScore)[player_index]] - currentScore[list(currentScore)[player_index]]
                #Adds it to a dictionary if the difference is not 0
                if scoreDifference != 0:
                    scoresDictionary[action] = scoreDifference
            return scoresDictionary
        
        
        #Finding the most scoring move for the current player
        def FindMostScoringMove():
            #Gets the dictionary of all the moves and the score difference
            scoresDictionnary = FindScoreDifferences(list(possible_actions), player_index)
            randomMove = False
            highestScoreDiff = 0
            allActions = []
            actionPosList = []
            #Goes through all the score differences and 
            for actions, currentScoreDiff in scoresDictionnary.items():
                if currentScoreDiff == highestScoreDiff:
                    allActions.append(actions)
                if currentScoreDiff > highestScoreDiff:
                    highestScoreDiff = currentScoreDiff
                    allActions = []
                    allActions.append(actions)
                
            if len(allActions) == 0:
                allActions.append(random.choice(list(possible_actions)))
                randomMove = True
            
            for action in allActions:
                actionPosList.append(self.get_actions_new_coords(action))
            
            return allActions, highestScoreDiff, randomMove, actionPosList
        
        mostScoringMove = FindMostScoringMove()[0][0]
        
        mostScoringMoveScoreDiff = FindMostScoringMove()[1]
        
        #All possible actions after "Best move" is played
        nextPossibleActions: set(Action) = mostScoringMove.get_next_game_state().generate_possible_actions() # type:ignore
        #Score after "Best move" is played
        nextScore = mostScoringMove.get_next_game_state().get_scores()
        #Pieces on board after "Best move" is played
        nextPossibleActionPieces = mostScoringMove.get_next_game_state().get_rep().get_env()
        
        #Uses the same process as finding the scores differences as before
        def FindScoresForOpposite():
            if len(dict_of_current_pieces_played) < 25:
                for action in nextPossibleActions:
                    stateForNextAction = action.get_next_game_state()
                    scoreForNextMove = stateForNextAction.get_scores()
                    scoreDifference = scoreForNextMove[list(scoreForNextMove)[otherPlayerIndex]] - nextScore[list(nextScore)[otherPlayerIndex]]
                    if scoreDifference != 0:
                        nextScoreDictionnary[action] = scoreDifference
            return nextScoreDictionnary

        def FindMostProfitableMove():
            scoresDict = FindScoresForOpposite()
            mostProfitableMove = []
            foundABetterMove = True
            mostProfitableMoves = []
            mostProfitableMovesCoords = []
            potentiallyGood = []
            potentiallyGoodCoords = []
            for action, score in scoresDict.items():
                #Checks if there are any moves that can gain the opponent more points than you can get
                if score > mostScoringMoveScoreDiff:
                    mostProfitableMove.append(action)
                if score == mostScoringMoveScoreDiff and FindMostScoringMove()[2] == False:
                    potentiallyGood.append(action)
                    
            if len(potentiallyGood) != 0:
                for actions in potentiallyGood:
                    potentiallyGoodCoords.append(self.get_actions_new_coords(actions))
                for coords in potentiallyGoodCoords:
                    if coords in FindMostScoringMove()[3]:
                        mostProfitableMoves.append(self.findActionFromCoords(coords, possible_actions))
                        
            if len(mostProfitableMove) != 0:
                for move in mostProfitableMove:
                    #finds the move that blocks the opponent
                    finalState = move.get_next_game_state()
                    finalStatePieces = finalState.get_rep().get_env()
                    for piece in finalStatePieces:
                        pos_i, pos_j = piece
                        if piece not in nextPossibleActionPieces:
                            finalPiece = (pos_i, pos_j)
                            break
                    mostProfitableMoves.append(self.findActionFromCoords(finalPiece, possible_actions))
            
            if len(mostProfitableMoves) == 0:
                foundABetterMove = False
                mostProfitableMoves.append(mostScoringMove)
            
            for moves in mostProfitableMoves:
                mostProfitableMovesCoords.append(self.get_actions_new_coords(moves))
            
            return mostProfitableMoves, foundABetterMove, mostProfitableMovesCoords

        currentClosestToCenter = FindMostScoringMove()[3][0]
        print(FindMostProfitableMove()[1])

        if FindMostProfitableMove()[1] == True:
            for i in range(len(FindMostProfitableMove()[2])):
                currentClosestToCenter = self.get_closer_to_center(FindMostProfitableMove()[2][i], currentClosestToCenter)
            bestMove = self.findActionFromCoords(currentClosestToCenter, possible_actions)
        elif FindMostProfitableMove()[1] == False and FindMostScoringMove()[2] == False:
            for index in range(len(FindMostScoringMove()[3])):
                currentClosestToCenter = self.get_closer_to_center(FindMostScoringMove()[3][index], currentClosestToCenter)
            bestMove = self.findActionFromCoords(currentClosestToCenter, possible_actions)
        
        my_player_id = self.get_my_player_id(current_state=current_state)

        potentially_valuable: list[Action] = []
        valuable: list[Action] = []

        # Get the action closest to the center of the board
        closest = self.get_action_closest_to_middle(current_state)

        potentially_valuable.append(closest)
        
        if self.atleast_points(current_state, 1) == False: # If the board doesnt have a point yet
            possible_points = self.get_existing_lines(current_state=current_state, player_id=my_player_id, reach=1)
            if possible_points != []:
                if self.get_possible_extensions(current_state=current_state, existing_points=possible_points, player_id=my_player_id):
                    for action in self.get_possible_extensions(current_state=current_state, existing_points=possible_points, player_id=my_player_id):
                        if action in potentially_valuable:
                            valuable.append(action)
                        else:
                            potentially_valuable.append(action)
            else:
                return random.choice(potentially_valuable)

        else:
            existing_points = self.get_existing_lines(current_state=current_state, player_id=my_player_id, reach=2)

            possible_extensions = self.get_possible_extensions(current_state=current_state, existing_points=existing_points, player_id=my_player_id)

            if len(possible_extensions) > 0:
                for action in possible_extensions:
                    if action in potentially_valuable:
                        valuable.append(action)
                    else:
                        potentially_valuable.append(action)

        players_list = current_state.get_players()
        player_index = players_list.index(self)
        most_valuable = None
        most_potentially = None
        if valuable != []:
            for action in valuable:
                if most_valuable == None:
                    most_valuable = action
                if action.get_next_game_state().get_player_score(players_list[player_index]) > most_valuable.get_next_game_state().get_player_score(players_list[player_index]):
                    most_valuable = action
        else:
            for action in potentially_valuable:
                if most_potentially == None:
                    most_potentially = action
                if action.get_next_game_state().get_player_score(players_list[player_index]) > most_potentially.get_next_game_state().get_player_score(players_list[player_index]):
                    most_potentially = action
        
        if FindMostProfitableMove()[1] == False and FindMostScoringMove()[2] == True:
            return most_valuable if most_valuable else most_potentially
        else:
            return bestMove
    
    def findActionFromCoords(self, coord: tuple, possibleActions) -> Action:
        for action in possibleActions:
            if coord in action.get_next_game_state().get_rep().get_env():
                return action
    
    def atleast_points(self, current_state: GameState, points: int) -> bool:
        players_list = current_state.get_players()
        player_index = players_list.index(self)
        return current_state.get_player_score(players_list[player_index]) >= points

    def get_action_closest_to_middle(self, current_state: GameState) -> Action:
        """
        Returns the action closest to the center of the board. 
        Playing close to the center allows for better extensions in the future
        """
        actions: list[Action] = current_state.generate_possible_actions() # Generate all the possible actions in the current GameState
        closest: Action = None # Define the variable to contain the closest action
        # Cycle thru the possible actions
        for action in actions:
            closest_coords: tuple = self.get_actions_new_coords(closest) if closest else None # Get the coordinates of the new piece
            # Cycle thru the game board of the gamestate if action is selected
            for piece in action.get_next_game_state().get_rep().get_env():
                pos_i, pos_j = piece
                # Make sure the piece we'er on is new
                if piece not in current_state.get_rep().get_env():
                    # Evaluate if the piece is closer to the center then closest
                    if closest:
                        if self.get_closer_to_center(coord1=(pos_i, pos_j), coord2=closest_coords) == (pos_i, pos_j):
                            closest = action
                    else:
                        closest = action
        
        return closest

    def get_closer_to_center(self, coord1: tuple, coord2: tuple, center=(2, 2)) -> tuple:
        # Calculate squared distance of coord1 from center
        distance_squared_1 = (coord1[0] - center[0])**2 + (coord1[1] - center[1])**2
        
        # Calculate squared distance of coord2 from center
        distance_squared_2 = (coord2[0] - center[0])**2 + (coord2[1] - center[1])**2
        
        # Compare distances and return the closer coordinate
        if distance_squared_1 < distance_squared_2:
            return coord1
        elif distance_squared_2 < distance_squared_1:
            return coord2
        else:
            return coord1

    def get_existing_lines(self, current_state: GameState, player_id: int, reach: int) -> list[list[tuple]]:
        """
        Finds existing 3 piece sequences owned by a player
        """
        current_board = current_state.get_rep().get_env() # Get the representation of the current board
        points: list[list[tuple]] = []

        # Cycle through the pieces in the board
        for piece in current_board:
            pos_i, pos_j = piece
            # Make sure piece exists
            if piece in current_board:
                # Make sure piece is owned by me
                if current_board[piece].get_owner_id() == player_id:
                    # Check all 8 directions: UPLEFT, UP, UPRIGHT, RIGHT, DOWNRIGHT, DOWN, DOWNLEFT, LEFT
                    # TODO Make sure not to append points that are already in the list
                    points.append(self.check_surroundings(piece=(pos_i, pos_j), current_board=current_board, player_id=player_id, reach=reach)) if len(self.check_surroundings(piece=(pos_i, pos_j), current_board=current_board, player_id=player_id, reach=reach)) > 0 else None
    
        return points

    def get_possible_extensions(self, current_state: GameState, existing_points: list[list[tuple]], player_id: int) -> list[Action]:
        possible_extensions: list[Action] = []


        for point in existing_points:
            for subpoint in point:
                extremity1 = subpoint[0]
                extremity2 = subpoint[-1]
                extremity1_i, extremity1_j = extremity1
                extremity2_i, extremity2_j = extremity2
                if extremity1_j > extremity2_j:
                    for action in current_state.generate_possible_actions():
                        if self.get_actions_new_coords(action=action) == (extremity1_i - 1, extremity1_j + 1):
                            possible_extensions.append(action)
                        if self.get_actions_new_coords(action=action) == (extremity2_i + 1, extremity2_i - 1):
                            possible_extensions.append(action)
                if extremity1_j < extremity2_j:
                    for action in current_state.generate_possible_actions():
                        if self.get_actions_new_coords(action=action) == (extremity1_i - 1, extremity1_j - 1):
                            possible_extensions.append(action)
                        if self.get_actions_new_coords(action=action) == (extremity2_i + 1, extremity2_j + 1):
                            possible_extensions.append(action)
            
            

        return possible_extensions

    def find_dir(extremity1: tuple, extremity2: tuple) -> tuple:
        extremity1_i, extremity1_j = extremity1
        extremity2_i, extremity2_j = extremity2

        # Find the direction of the point
        if extremity1_i < extremity1_j:
            is_up = True
        elif extremity1_i > extremity1_j:
            is_up = False
        else:
            is_up = None
        
        if extremity1_j > extremity2_j:
            is_right = True
        elif extremity1_j < extremity2_j:
            is_right = False
        else:
            is_right = None
        
        return (is_up, is_right)

    def check_surroundings(self, piece: tuple, current_board: dict, player_id: int, reach: int) -> list[list[tuple]]:
        pos_i, pos_j = piece
        points = []
        points.append(self.check_upleft((pos_i, pos_j), current_board, player_id, reach=reach)) if self.check_upleft((pos_i, pos_j), current_board, player_id, reach=reach) != '' else None
        points.append(self.check_up((pos_i, pos_j), current_board, player_id, reach=reach)) if self.check_up((pos_i, pos_j), current_board, player_id, reach=reach) != '' else None
        points.append(self.check_upright((pos_i, pos_j), current_board, player_id, reach=reach)) if self.check_upright((pos_i, pos_j), current_board, player_id, reach=reach) != '' else None
        points.append(self.check_right((pos_i, pos_j), current_board, player_id, reach=reach)) if self.check_right((pos_i, pos_j), current_board, player_id, reach=reach) != '' else None
        points.append(self.check_downright((pos_i, pos_j), current_board, player_id, reach=reach)) if self.check_downright((pos_i, pos_j), current_board, player_id, reach=reach) != '' else None
        points.append(self.check_down((pos_i, pos_j), current_board, player_id, reach=reach)) if self.check_down((pos_i, pos_j), current_board, player_id, reach=reach) != '' else None
        points.append(self.check_downleft((pos_i, pos_j), current_board, player_id, reach=reach)) if self.check_downleft((pos_i, pos_j), current_board, player_id, reach=reach) else None
        points.append(self.check_left((pos_i, pos_j), current_board, player_id, reach=reach)) if self.check_left((pos_i, pos_j), current_board, player_id, reach=reach) != '' else None
        return points

    def check_upleft(self,piece: tuple, current_board: dict, player_id: int, reach: int):
        pos_i, pos_j = piece
        if reach == 2:
            if current_board.get((pos_i - 1, pos_j - 1), None) and current_board.get((pos_i - 2, pos_j - 2), None):
                curr_piece_owner = current_board.get((pos_i, pos_j), None).get_owner_id()
                curr_piece2_owner = current_board.get((pos_i - 1, pos_j - 1), None).get_owner_id()
                curr_piece3_owner = current_board.get((pos_i - 2, pos_j - 2), None).get_owner_id()
                if curr_piece_owner == player_id and curr_piece2_owner == player_id and curr_piece3_owner == player_id:
                    return [(pos_i, pos_j), (pos_i - 1, pos_j - 1), (pos_i - 2, pos_j - 2)]
        elif reach == 1:
            if current_board.get((pos_i - 1, pos_j - 1), None):
                curr_piece_owner = current_board.get((pos_i, pos_j), None).get_owner_id()
                curr_piece2_owner = current_board.get((pos_i - 1, pos_j - 1), None).get_owner_id()
                if curr_piece_owner == player_id and curr_piece2_owner == player_id:
                    return [(pos_i, pos_j), (pos_i - 1, pos_j - 1)]
        
        return ''

    def check_up(self,piece: tuple, current_board: GameState, player_id: int, reach: int): 
        pos_i, pos_j = piece
        if reach == 2:
            if current_board.get((pos_i - 1, pos_j), None) and current_board.get((pos_i - 2, pos_j), None):
                curr_piece_owner = current_board.get((pos_i, pos_j), None).get_owner_id()
                curr_piece2_owner = current_board.get((pos_i - 1, pos_j), None).get_owner_id()
                curr_piece3_owner = current_board.get((pos_i - 2, pos_j), None).get_owner_id()
                if curr_piece_owner == player_id and curr_piece2_owner == player_id and curr_piece3_owner == player_id:
                    return [(pos_i, pos_j), (pos_i - 1, pos_j), (pos_i - 2, pos_j)]
        if reach == 1:
            if current_board.get((pos_i - 1, pos_j), None):
                curr_piece_owner = current_board.get((pos_i, pos_j), None).get_owner_id()
                curr_piece2_owner = current_board.get((pos_i - 1, pos_j), None).get_owner_id()
                if curr_piece_owner == player_id and curr_piece2_owner == player_id:
                    return [(pos_i, pos_j), (pos_i - 1, pos_j)]
        
        return ''

    def check_upright(self,piece: tuple, current_board: GameState, player_id: int, reach: int):
        pos_i, pos_j = piece
        if reach == 2:
            if current_board.get((pos_i - 1, pos_j + 1), None) and current_board.get((pos_i - 2, pos_j + 2), None):
                curr_piece_owner = current_board.get((pos_i, pos_j), None).get_owner_id()
                curr_piece2_owner = current_board.get((pos_i - 1, pos_j + 1), None).get_owner_id()
                curr_piece3_owner = current_board.get((pos_i - 2, pos_j + 2), None).get_owner_id()
                if curr_piece_owner == player_id and curr_piece2_owner == player_id and curr_piece3_owner == player_id:
                    return [(pos_i, pos_j), (pos_i - 1, pos_j + 1), (pos_i - 2, pos_j + 2)]
        elif reach == 1:
            if current_board.get((pos_i - 1, pos_j + 1), None):
                curr_piece_owner = current_board.get((pos_i, pos_j), None).get_owner_id()
                curr_piece2_owner = current_board.get((pos_i - 1, pos_j + 1), None).get_owner_id()
                if curr_piece_owner == player_id and curr_piece2_owner == player_id:
                    return [(pos_i, pos_j), (pos_i - 1, pos_j + 1)]
        
        return ''

    def check_right(self,piece: tuple, current_board: GameState, player_id: int, reach: int):
        pos_i, pos_j = piece
        if reach == 2:
            if current_board.get((pos_i, pos_j + 1), None) and current_board.get((pos_i, pos_j + 2), None):
                curr_piece_owner = current_board.get((pos_i, pos_j), None).get_owner_id()
                curr_piece2_owner = current_board.get((pos_i, pos_j + 1), None).get_owner_id()
                curr_piece3_owner = current_board.get((pos_i, pos_j + 2), None).get_owner_id()
                if curr_piece_owner == player_id and curr_piece2_owner == player_id and curr_piece3_owner == player_id:
                    return [(pos_i, pos_j), (pos_i, pos_j + 1), (pos_i, pos_j + 2)]
        elif reach == 1:
            if current_board.get((pos_i, pos_j + 1), None):
                curr_piece_owner = current_board.get((pos_i, pos_j), None).get_owner_id()
                curr_piece2_owner = current_board.get((pos_i, pos_j + 1), None).get_owner_id()
                if curr_piece_owner == player_id and curr_piece2_owner == player_id:
                    return [(pos_i, pos_j), (pos_i, pos_j + 1)]
        
        return ''

    def check_downright(self,piece: tuple, current_board: GameState, player_id: int, reach: int):
        pos_i, pos_j = piece
        if reach == 2:
            if current_board.get((pos_i + 1, pos_j + 1), None) and current_board.get((pos_i + 2, pos_j + 2), None):
                curr_piece_owner = current_board.get((pos_i, pos_j), None).get_owner_id()
                curr_piece2_owner = current_board.get((pos_i + 1, pos_j + 1), None).get_owner_id()
                curr_piece3_owner = current_board.get((pos_i + 2, pos_j + 2), None).get_owner_id()
                if curr_piece_owner == player_id and curr_piece2_owner == player_id and curr_piece3_owner == player_id:
                    return [(pos_i, pos_j), (pos_i + 1, pos_j + 1), (pos_i + 2, pos_j + 2)]
        elif reach == 1:
            if current_board.get((pos_i + 1, pos_j + 1), None):
                curr_piece_owner = current_board.get((pos_i, pos_j), None).get_owner_id()
                curr_piece2_owner = current_board.get((pos_i + 1, pos_j + 1), None).get_owner_id()
                if curr_piece_owner == player_id and curr_piece2_owner == player_id:
                    return [(pos_i, pos_j), (pos_i + 1, pos_j + 1)]
        
        return ''
    
    def check_down(self,piece: tuple, current_board: GameState, player_id: int, reach: int):
        pos_i, pos_j = piece
        if reach == 2:
            if current_board.get((pos_i + 1, pos_j), None) and current_board.get((pos_i + 2, pos_j), None):
                curr_piece_owner = current_board.get((pos_i, pos_j), None).get_owner_id()
                curr_piece2_owner = current_board.get((pos_i + 1, pos_j), None).get_owner_id()
                curr_piece3_owner = current_board.get((pos_i + 2, pos_j), None).get_owner_id()
                if curr_piece_owner == player_id and curr_piece2_owner == player_id and curr_piece3_owner == player_id:
                    return [(pos_i, pos_j), (pos_i + 1, pos_j), (pos_i + 2, pos_j)]
        elif reach == 1:
            if current_board.get((pos_i + 1, pos_j), None):
                curr_piece_owner = current_board.get((pos_i, pos_j), None).get_owner_id()
                curr_piece2_owner = current_board.get((pos_i + 1, pos_j), None).get_owner_id()
                if curr_piece_owner == player_id and curr_piece2_owner == player_id:
                    return [(pos_i, pos_j), (pos_i + 1, pos_j)]
        
        
        return ''

    def check_downleft(self,piece: tuple, current_board: GameState, player_id: int, reach: int):
        pos_i, pos_j = piece
        if reach == 2:
            if current_board.get((pos_i + 1, pos_j - 1), None) and current_board.get((pos_i + 2, pos_j - 2), None):
                curr_piece_owner = current_board.get((pos_i, pos_j), None).get_owner_id()
                curr_piece2_owner = current_board.get((pos_i + 1, pos_j - 1), None).get_owner_id()
                curr_piece3_owner = current_board.get((pos_i + 2, pos_j - 2), None).get_owner_id()
                if curr_piece_owner == player_id and curr_piece2_owner == player_id and curr_piece3_owner == player_id:
                    return [(pos_i, pos_j), (pos_i + 1, pos_j - 1), (pos_i + 2, pos_j - 2)]
        elif reach == 1:
            if current_board.get((pos_i + 1, pos_j - 1), None):
                curr_piece_owner = current_board.get((pos_i, pos_j), None).get_owner_id()
                curr_piece2_owner = current_board.get((pos_i + 1, pos_j - 1), None).get_owner_id()
                if curr_piece_owner == player_id and curr_piece2_owner == player_id:
                    return [(pos_i, pos_j), (pos_i + 1, pos_j - 1)]
        
        return ''

    def check_left(self,piece: tuple, current_board: GameState, player_id: int, reach: int):
        pos_i, pos_j = piece
        if reach == 2:
            if current_board.get((pos_i, pos_j - 1), None) and current_board.get((pos_i, pos_j - 2), None):
                curr_piece_owner = current_board.get((pos_i, pos_j), None).get_owner_id()
                curr_piece2_owner = current_board.get((pos_i, pos_j - 1), None).get_owner_id()
                curr_piece3_owner = current_board.get((pos_i, pos_j - 2), None).get_owner_id()
                if curr_piece_owner == player_id and curr_piece2_owner == player_id and curr_piece3_owner == player_id:
                    return [(pos_i, pos_j), (pos_i, pos_j - 1), (pos_i, pos_j - 2)]
        elif reach == 1:
            if current_board.get((pos_i, pos_j - 1), None):
                curr_piece_owner = current_board.get((pos_i, pos_j), None).get_owner_id()
                curr_piece2_owner = current_board.get((pos_i, pos_j - 1), None).get_owner_id()
                if curr_piece_owner == player_id and curr_piece2_owner == player_id:
                    return [(pos_i, pos_j), (pos_i, pos_j - 1)]
        
        return ''

    def get_my_player_id(self, current_state: GameState):   
        player_list = current_state.get_players()
        player_index = player_list.index(self)

        return player_list[player_index].get_id()

    def get_actions_new_coords(self, action: Action) -> tuple:
        """
        Gets the coordinates of a piece that is the product of an action
        """
        if action:
            for piece in action.get_next_game_state().get_rep().get_env():
                pos_i, pos_j = piece
                if piece not in action.get_current_game_state().get_rep().get_env():
                    return (pos_i, pos_j)

    def __init__(self, piece_type: str, name: str = "bob") -> None:
        super().__init__(piece_type, "XMerge" + name[-2:])