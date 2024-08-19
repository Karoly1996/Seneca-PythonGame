# Main Author:
# Main Reviewer:

from a1_partd import overflow, get_overflow_list
from a1_partc import Queue

# This function duplicates and returns the board. You may find this useful
def copy_board(board):
        current_board = []
        height = len(board)
        for i in range(height):
            current_board.append(board[i].copy())
        return current_board


# if you were responsible for the game tree and evaluation functions, 
# describe your evaluation function and why you scored the board that way, 
# explain what you did.

def evaluate_board(board, player):
    # Initialize variables for the player's score and the total number of gems.
    score = 0
    total_gem = 0
    
    # Loop through each row of the board.
    for row in board:
        # Loop through each cell in the current row.
        for col in row:
            # Add the absolute number of gems in the cell to the total gem count.
            total_gem += abs(col)
            
            # If the cell is occupied by the player, add the gems to the player's score.
            if col != 0 and (abs(col)/col) == player:
                score += abs(col)
    
    # If the board is empty, return a score of 0.
    if total_gem == 0:
        return 0
    
    # Return the player's score normalized by the total number of gems.
    return score / total_gem

class GameTree:
    class Node:
        def __init__(self, board, depth, player, tree_height = 4):
            self.board = board
            self.depth = depth
            self.player = player
            self.tree_height = tree_height

            self.last_move = None
            self.children = []
            self.score = None
            self.best_move = None
        
        def get_possible_moves(self):
            moves = []
            for i in range(len(self.board)):
                for j in range(len(self.board[0])):
                    if self.board[i][j] == 0 or (abs(self.board[i][j])/self.board[i][j]) == self.player:
                        moves.append((i, j))
            return moves
        
        def add_child(self):
            next_player = -self.player
            possible_moves = self.get_possible_moves()
            if len(possible_moves) == 0 or self.depth >= self.tree_height - 1:
                return False
            for each_move in possible_moves:
                # add gem to the cordinate
                i, j = each_move
                new_board = copy_board(self.board)
                new_board[i][j] += self.player

                # overflow action
                a_queue = Queue()
                overflow(new_board, a_queue)

                # update the current node
                child_node = GameTree.Node(new_board, self.depth + 1, next_player, self.tree_height)
                child_node.last_move = each_move
                self.children.append(child_node)
            return True

    def __init__(self, board, player, tree_height = 4):
        self.player = player
        self.board = copy_board(board)
        # you will need to implement the creation of the game tree here.  After this function completes,
        # a full game tree will be created.
        # hint: as with many tree structures, you will need to define a self.root that points to the root
        # of the game tree.  To create the tree itself, a recursive function will likely be the easiest as you will
        # need to apply the minimax algorithm to its creation.

        self.root = GameTree.Node(self.board, 0, self.player, tree_height)
        self.recursive_build(self.root, player)

    def recursive_build(self, node, player):
        if node.add_child():
            best_score = float('-inf') if node.depth % 2 == 0 else float('inf')
            for child in node.children:
                child_score = self.recursive_build(child, player)
                if node.depth % 2 == 0:
                    if child_score > best_score:
                        node.best_move = child.last_move
                        best_score = child_score
                else:
                    if child_score < best_score:
                        node.best_move = child.last_move
                        best_score = child_score
            node.score = best_score
        else:
            node.score = evaluate_board(node.board, player)
        return node.score
        
    # this function is a pure stub.  It is here to ensure the game runs.  Once you complete
    # the GameTree, you will use it to determine what to return.
    def get_move(self):
        return self.root.best_move
   
    def clear_tree(self):
        self.root = None 