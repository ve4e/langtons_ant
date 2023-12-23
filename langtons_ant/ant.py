from enum import Enum
from operator import add
from typing import Tuple

from langtons_ant.area import Area, Color


class Direction(Enum):
    """
    Направление движения
    """
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)

    def __init__(self, *_):
        setattr(self, '_index', len(self.__class__))

    def next(self):
        """Следующее направление"""
        try:
            return list(self.__class__)[getattr(self, '_index') + 1]
        except IndexError:
            return list(self.__class__)[0]

    def prev(self):
        """Предыдущее направление"""
        try:
            return list(self.__class__)[getattr(self, '_index') - 1]
        except IndexError:
            return list(self.__class__)[-1]


class Ant:
    def __init__(self):
        self._area = None
        self._direction = None
        self._position = None

    def make_way(self,
                 position: Tuple[int, int],
                 direction: Direction,
                 area: Area) -> Area:
        """
        Функция прокладывает путь от стартового положения муравья до границы местности
        """

        self._position = position
        self._direction = direction
        self._area = area

        while not self._is_finish():
            self._turn()
            self._mark()
            self._step()

        self._area.save()
        return self._area

    def _is_finish(self) -> bool:
        """
        Функция проверяет факт достижения муравьём границы местности
        """
        x, y = self._position
        ax, ay = self._area.size
        if x < 0 or y < 0 or x > ax - 1 or y > ay - 1:
            return True
        return False

    def _turn(self):
        """
        Повернуть муравья в зависимости от типа текущей клетки
        """
        current_color = self._area.color(self._position)
        if current_color == Color.WHITE:
            self._direction = self._direction.next()
        elif current_color == Color.BLACK:
            self._direction = self._direction.prev()

    def _step(self):
        """
        Переместить муравья на одну клетку в текущем направлении
        """
        self._position = tuple(map(add, self._position, self._direction.value))

    def _mark(self):
        """
        Пометить (инвертировать) клетку
        """
        color = Color.WHITE if self._area.color(self._position) == Color.BLACK else Color.BLACK
        self._area.set_color(self._position, color)


