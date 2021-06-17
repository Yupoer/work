class Planet:

    shape = 'round'

    def __init__(self,name,radius,gravity,system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

    @classmethod
    def commons(cls):
        return f'All planet are {cla.shape} because of gravity'

    @staticmethod
    def spin(speed = '2000 miles per hour'):
        return f'The planet spins and spins at {speed}'

naboo = Planet('Naboo',30000,8,'Naboo System')
# print(Planet.spin())
print(naboo.spin('a very high speed'))
