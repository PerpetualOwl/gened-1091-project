class GameState:
    def __init__(self, province_name, agricultural_yield, population, military_strength, terrain_defensibility, neighbors):
        self.province_name = province_name
        self.agricultural_yield = agricultural_yield  # E.g., tons of grain
        self.population = population  # Total number of people
        self.military_strength = military_strength  # E.g., number of soldiers
        self.terrain_defensibility = terrain_defensibility  # E.g., scale from 1-10
        self.neighbors = neighbors  # List of neighboring provinces

    def __str__(self):
        return f"Province: {self.province_name}\nAgricultural Yield: {self.agricultural_yield}\nPopulation: {self.population}\nMilitary Strength: {self.military_strength}\nTerrain Defensibility: {self.terrain_defensibility}\nNeighbors: {', '.join(self.neighbors)}"

  class Advisor:
    def __init__(self, name, philosophy):
        self.name = name
        self.philosophy = philosophy

    def give_advice(self):
        return f"{self.name} advises based on {self.philosophy} insights."

class LegalistAdvisor(Advisor):
    def give_advice(self):
        return f"{self.name} (Legalist) advises: Focus on strict laws and punishments to maintain order."

class ConfucianAdvisor(Advisor):
    def give_advice(self):
        return f"{self.name} (Confucian) advises: Promote moral virtues and societal harmony."

class DaoistAdvisor(Advisor):
    def give_advice(self):
        return f"{self.name} (Daoist) advises: Embrace simplicity and harmony with nature."

class MohistAdvisor(Advisor):
    def give_advice(self):
        return f"{self.name} (Mohist) advises: Focus on universal love and meritocracy."

def next_cycle(game_state):
    options = []
    options.append(f"1. Allocate resources for agriculture: Current yield is {game_state.agricultural_yield}.")
    options.append(f"2. Increase military strength: Current strength is {game_state.military_strength}.")
    options.append(f"3. Form alliances with neighbors: {', '.join(game_state.neighbors)}.")
    options.append(f"4. Focus on trade to boost population: Current population is {game_state.population}.")

    print(f"Options for the next cycle in {game_state.province_name}:")
    for option in options:
        print(option)

    # Simulate a player's decision (for now just a placeholder)
    player_choice = 1  # Placeholder for actual player choice

    # Update game state based on choice (this could be dynamic)
    if player_choice == 1:
        game_state.agricultural_yield += 100  # Example increase
        print(f"Increased agricultural yield to {game_state.agricultural_yield}.")
    elif player_choice == 2:
        game_state.military_strength += 50  # Example increase
        print(f"Increased military strength to {game_state.military_strength}.")
    elif player_choice == 3:
        print("Formed alliances with neighboring provinces.")
    elif player_choice == 4:
        game_state.population += 20  # Example increase
        print(f"Population increased to {game_state.population}.")
    else:
        print("Invalid choice, no changes made.")


