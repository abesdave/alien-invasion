import random
import sys


class City:
    def __init__(self, name):
        self.name = name
        self.roads = {}

    def add_road(self, direction, city):
        self.roads[direction] = city

    def remove_road(self, direction):
        del self.roads[direction]


class WorldMap:
    def __init__(self):
        self.cities = {}

    def add_city(self, name):
        if name not in self.cities:
            self.cities[name] = City(name)

    def add_road(self, from_city, direction, to_city):
        if from_city in self.cities and to_city in self.cities:
            self.cities[from_city].add_road(direction, self.cities[to_city])
        else:
            print("City not found in the map.")

    def remove_city(self, city_name):
        if city_name in self.cities:
            del self.cities[city_name]
            for city in self.cities.values():
                city.roads = {
                    dir: c for dir, c in city.roads.items() if c.name != city_name
                }


def move_alien(alien):
    current_city = alien["current_city"]
    try: 
        next_direction = random.choice(list(current_city.roads.keys()))
        next_city = current_city.roads[next_direction]
        alien["current_city"] = next_city
    except:
        pass


def main():
    max_iterations = 10000
    map_file = 'aliens_data.txt'
    num_aliens = int(sys.argv[1])

    world_map = WorldMap()

    with open(map_file, 'r') as file:    
        for line in file:
            city_record = line.strip().split()
            city_name = city_record[0]
            world_map.add_city(city_name)

    with open('aliens_data.txt', 'r') as file:    
        for line in file:
            city_record = line.strip().split()
            city_name = city_record[0]
            for i in range(1, len(city_record)):
                directed_road = city_record[i].strip().split("=")
                direction = directed_road[0]
                connected_city_name = directed_road[1]
                world_map.add_road(city_name, direction, connected_city_name)

    aliens = [
        {"current_city": random.choice(list(world_map.cities.values()))}
        for _ in range(num_aliens)
    ]

    iteration = 1
    while iteration <= max_iterations:
        for alien in aliens:
            move_alien(alien)

        city_counts = {}
        for alien in aliens:
            current_city = alien["current_city"]
            if current_city.name in city_counts:
                city_counts[current_city.name].append(alien)
            else:
                city_counts[current_city.name] = [alien]

        for city_name, aliens_in_city in city_counts.items():
            if len(aliens_in_city) > 1:
                if(len(aliens_in_city) > 2):
                    print(
                            f"{city_name} has been destroyed by a battle involving a large number of aliens"
                        )
                else:
                    print(
                        f"{city_name} has been destroyed by {''.join([f"Alien {index}{f"{' and ' if index < len(aliens_in_city) - 1 else ''}"}" for index, value in enumerate(aliens_in_city)])}!"
                    )
                for alien in aliens_in_city:
                    
                    aliens.remove(alien)
                world_map.remove_city(city_name)

        if not city_counts or len(aliens) == 0:
            print(
                "All aliens have been destroyed or each alien has moved at least 10,000 times. End of simulation."
            )
            break

        iteration += 1

    print('')
    print('Remaining Cities:')
    for city_name, city in world_map.cities.items():
        print(
            f"{city_name} {' '.join([f'{dir}={c.name}' for dir, c in city.roads.items()])}"
        )

if __name__ == "__main__":
    main()
