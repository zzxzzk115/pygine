import pygame
from entities.entity import Entity
from utilities.color import Color
from utilities.camera import Camera
from utilities.camera import CameraType
from utilities.vector import Vector2


class Circle(Entity):
    def __init__(self, x=0.0, y=0.0, radius=0, thickness=0, color=Color.WHITE):
        super(Circle, self).__init__(x, y, radius * 2, radius*2)
        self.radius = radius
        self.thickness = thickness
        self.color = color

    def set_location(self, x, y):
        super().set_location(x, y)
        self.bounds = pygame.Rect(
            self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def set_thickness(self, thickness):
        self.thickness = thickness
        if self.thickness < 0:
            self.thickness = 1
        if self.thickness > self.radius:
            self.thickness = self.radius

    def draw(self, surface, camera_type=CameraType.DYNAMIC):
        pygame.draw.circle(
            surface,
            self.color,
            (
                int(self.scaled_location(camera_type).x),
                int(self.scaled_location(camera_type).y)
            ),
            int(self.radius * Camera.SCALE),
            int(self.thickness * Camera.SCALE)
        )
