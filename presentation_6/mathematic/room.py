class RoomSize:
    def __init__(self, length, width, height):
        
        self.length = length  # Длина комнаты
        self.width = width    # Ширина комнаты
        self.height = height  # Высота комнаты

    def floor_area(self):
        """ Площадь пола (и потолка) """
        return self.length * self.width

    def wall_area(self):
        """ Общая площадь всех стен """
        return 2 * (self.length * self.height + self.width * self.height)

    def ceiling_area(self):
        """ Площадь потолка (равна площади пола) """
        return self.floor_area()

    def volume(self):
        """ Объем комнаты """
        return self.length * self.width * self.height

# Пример использования
room = RoomSize(15, 10, 8)  # 15x10x8 футов
print(room)
