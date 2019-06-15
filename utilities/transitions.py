from enum import Enum
from root.pyobject import PyObject
from entities.geometry.circle import Circle
from utilities.camera import Camera
from utilities.color import Color
from utilities.camera import CameraType


class PinholeType(Enum):
    OPEN = 0
    CLOSE = 1


class Pinhole(PyObject):
    def __init__(self, type=PinholeType.OPEN):
        super(Pinhole, self).__init__(
            Camera.BOUNDS.width / 2, Camera.BOUNDS.height/2)
        self.speed = 100
        self.acceleration = 250
        self.done = False
        self.type = type
        if self.type == PinholeType.OPEN:
            self.circle = Circle(
                self.x, self.y, Camera.BOUNDS.width * 0.75, Camera.BOUNDS.width * 0.75 - 1, Color.BLACK)
        if self.type == PinholeType.CLOSE:
            self.circle = Circle(
                self.x, self.y, Camera.BOUNDS.width * 0.75, 1, Color.BLACK)

    def update(self, delta_time):
        if self.done:
            return

        if self.type == PinholeType.OPEN:
            if self.circle.thickness > 1:
                self.circle.set_thickness(
                    self.circle.thickness - self.speed * delta_time)
            else:
                self.circle.set_thickness(1)
                self.done = True
        if self.type == PinholeType.CLOSE:
            if self.circle.thickness < self.circle.radius:
                self.circle.set_thickness(
                    self.circle.thickness + self.speed * delta_time)
            else:
                self.circle.set_thickness(0)
                self.done = True
        self.speed += self.acceleration * delta_time

    def draw(self, surface):
        self.circle.draw(surface, CameraType.STATIC)