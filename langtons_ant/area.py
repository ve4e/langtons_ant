import itertools
from typing import Tuple
from PIL import Image
from enum import Enum


class Color(Enum):
    """
    Цвет пикселя
    """
    BLACK = 0
    WHITE = 1


class Area:
    def __init__(self, size: Tuple[int, int], image_path: str):
        self._size = size
        self._image_path = image_path
        self._image = Image.new('1', size, Color.WHITE.value)
        self.save()

    @property
    def size(self):
        """Размер местности"""
        return self._size

    def color(self, coordinate: Tuple[int, int]) -> Color:
        """Цвет клетки"""
        return Color(self._image.getpixel(coordinate))

    def set_color(self, coordinate: Tuple[int, int], color: Color):
        """Установить цвет клетки"""
        self._image.putpixel(coordinate, color.value)

    def save(self):
        """Сохранить картинку"""
        self._image.save(self._image_path)

    def color_pixel_count(self, color: Color) -> int:
        """Количество клеток определенного цвета"""
        count = 0
        for coord in itertools.product(range(self._size[0]), range(self._size[1])):
            if self.color(coord) == color:
                count += 1
        return count








