# Create a Pokemon
class Pokemon:
    def __init__(self, name, primary_type, max_hp):
        self.name = name
        self.primary_type = primary_type
        self.hp = max_hp
        self.max_hp = max_hp

    def __str__(self):
        return f'{self.name} ({self.primary_type}: {self.hp}/{self.max_hp})'
    
    # Feed them to increase the health
    def feed(self):
        if self.hp < self.max_hp:
            self.hp += 1
            print(f'{self.name} has now: {self.hp} HP.')
        else:
            print(f'{self.name} is full HP.')

    # Make them battle and decide for a winner
    def battle(self, other):
        print('Battle:', self.name, other.name)

        # Call typewheel()
        res = self.typewheel(self.primary_type, other.primary_type)
        print(f'{self.name} fought {other.name} and the result is {res}')

        # Depending on the result, have effects
        if res == 'lose':
            self.hp = 0
            print(f'{self.name} fainted!')
        
        elif res == 'win':
            other.hp = 0
            print(f'{self.name} won. Congratulations!')

        elif res == 'tie':
            self.hp -= 10
            other.hp -= 10
            print(f'Draw: {self.name} and {other.name} battled hard.')


    @staticmethod
    def typewheel(type1, type2):
        results = {0 : 'lose', 1 : 'win', -1 : 'tie'}
        # Mapping between types and result conditions
        game_map = {'water' : 0, 'fire' : 1, 'grass' : 2}
        # Implement win-lose matrix
        wl_matix = [
            [-1, 1, 0], # water
            [0, -1, 1], # fire
            [1, 0, -1] # grass
        ]
        # Declare a winner
        return results[wl_matix[game_map[type1]][game_map[type2]]]



# Take a look at it
if __name__ == '__main__':
    bulbi = Pokemon('bulbasaur', 'grass',100)
    charm = Pokemon('charmander', 'fire',150)
    bulbi.battle(charm)

