class People:
    population = 0  # Class variable to track population

    def __init__(self, name):
        self.name = name
        People.population += 1  # Increment population when a new instance is created

    @classmethod
    def get_population(cls):
        return f"Number people: {cls.population}" # Return the current population
# Example usage:
p1 = People("Alice")
p2 = People("Bob")
p3 = People("Charlie")
p4 = People("bob")
p5 = People("Alice")
print(People.get_population())  # Gọi từ Class  
print(p5.get_population())  # Gọi từ object