class Baloon():
    def __init__(self, image, pos, name, gender, material, speed, weigh, health):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.name = name
        self.gender = gender
        self.material = material
        self.speed = speed
        self.weigt = weigh
        self.health = health
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)

    def ballonClick(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
