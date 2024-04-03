
# This section was built with some help from Chat GPT. I wanted to see what it could create
# from the following prompt

class TokenManager:
    def __init__(self, initial_tokens):
        self.tokens = initial_tokens

    def add_tokens(self, tokens_to_add):
        for color, quantity in tokens_to_add.items():
            self.tokens[color] += quantity

    def remove_tokens(self, tokens_to_remove):
        for color, quantity in tokens_to_remove.items():
            if self.tokens[color] < quantity:
                raise ValueError(f"Not enough {color} tokens available")
            self.tokens[color] -= quantity

    """
    def get_tokens(self):
        return self.tokens.copy()
    """

    def __str__(self):
        return str(self.tokens)


# Example usage:
"""
initial_tokens = {'red': 7, 'blue': 7, 'green': 7, 'white': 7, 'black': 7, 'gold': 5}
token_manager = TokenManager(initial_tokens)

print("Initial Tokens:")
print(token_manager)

tokens_to_add = {'red': 2, 'gold': 1}
token_manager.add_tokens(tokens_to_add)
print("\nAfter adding tokens:")
print(token_manager)

tokens_to_remove = {'green': 3, 'white': 2}
token_manager.remove_tokens(tokens_to_remove)
print("\nAfter removing tokens:")
print(token_manager)

"""
