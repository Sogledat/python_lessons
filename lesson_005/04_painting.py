# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

import simple_draw as sd
import draw_library as dl

screen_width = 1400
screen_height = 800
sd.resolution = (screen_width, screen_height)

# Радуга
rb_center = sd.get_point(500, -200)
rb_start_radius = 800
rb_line_width = 18

dl.draw_rainbow(dl.rainbow_colors, rb_center, rb_start_radius, rb_line_width)

# Стена
brick_width, brick_height = 40, 20
wall_width, wall_height = 600, 400
start_wall_x, start_wall_y = 100, 80

dl.draw_wall(wall_width, wall_height, brick_width, brick_height, start_wall_x, start_wall_y)

# Дерево
root_point = sd.get_point(600, 30)
dl.draw_random_branches(root_point, 90, 50)


sd.pause()

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
