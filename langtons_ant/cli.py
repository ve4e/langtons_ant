import os
from memory_profiler import profile
from langtons_ant.ant import Direction, Ant
from langtons_ant.area import Area, Color


@profile
def main():
    # начальные настройки карты и положения муравья
    AREA_SIZE = (1024, 1024)
    ANT_POSITION = (512, 512)
    ANT_DIRECTION = Direction.UP

    # директория с картинкой
    img_path = os.path.dirname(os.path.dirname(__file__))
    img_path = os.path.join(img_path, 'img', 'area.png')

    # запускаем муравья в дикую местность
    area = Area(AREA_SIZE, img_path)
    area = Ant().make_way(position=ANT_POSITION, direction=ANT_DIRECTION, area=area)

    # выводим результат
    count = area.color_pixel_count(Color.BLACK)
    print(f'Количество чёрных пикселей: {count}')


if __name__ == '__main__':
    main()



