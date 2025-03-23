import math

def water_jugs_game():
    # Define jug capacities and target volume
    A = int(input("Enter the capacity of Jug A: "))
    B = int(input("Enter the capacity of Jug B: "))
    T = int(input("Enter the target volume: "))
    
    initial_state = (0, 0)  # Both jugs are initially empty
    
    def valid_moves(state):
        x, y = state
        moves = set()
        
        # Fill either jug completely
        moves.add((A, y))
        moves.add((x, B))
        
        # Empty either jug completely
        moves.add((0, y))
        moves.add((x, 0))
        
        # Pour water from one jug to the other
        pour_x_to_y = min(x, B - y)
        pour_y_to_x = min(y, A - x)
        
        moves.add((x - pour_x_to_y, y + pour_x_to_y))
        moves.add((x + pour_y_to_x, y - pour_y_to_x))
        
        return moves
    
    def utility(state, is_ai_turn):
        x, y = state
        if x == T or y == T:
            return 100 if is_ai_turn else -100  # Win for AI or opponent
        return abs(T - x) + abs(T - y)  # Distance from the target
    
    def minimax(state, depth, is_ai_turn, alpha, beta):
        if state[0] == T or state[1] == T:
            return utility(state, is_ai_turn)
        
        if depth == 0:
            return utility(state, is_ai_turn)
        
        if is_ai_turn:
            max_eval = -math.inf
            for move in valid_moves(state):
                eval = minimax(move, depth - 1, False, alpha, beta)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = math.inf
            for move in valid_moves(state):
                eval = minimax(move, depth - 1, True, alpha, beta)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval
    
    def best_move(state):
        best_val = -math.inf
        best_action = None
        for move in valid_moves(state):
            move_val = minimax(move, 5, False, -math.inf, math.inf)
            if move_val > best_val:
                best_val = move_val
                best_action = move
        return best_action
    
    # Game loop
    current_state = initial_state
    is_ai_turn = False  # Human starts first
    
    while True:
        print(f"Current State: {current_state}")
        if current_state[0] == T or current_state[1] == T:
            print("Game Over!", "AI Wins!" if is_ai_turn else "You Win!")
            break
        
        if is_ai_turn:
            current_state = best_move(current_state)
            print("AI chooses:", current_state)
        else:
            print("Your turn! Choose a valid move:")
            moves = valid_moves(current_state)
            print("Valid moves:", moves)
            chosen_move = tuple(map(int, input("Enter move as x y: ").split()))
            while chosen_move not in moves:
                print("Invalid move. Try again.")
                chosen_move = tuple(map(int, input("Enter move as x y: ").split()))
            current_state = chosen_move
        
        is_ai_turn = not is_ai_turn

# Run the game
water_jugs_game()