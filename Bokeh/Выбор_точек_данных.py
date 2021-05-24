# Биьлиотеки Bokeh
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, NumeralTickFormatter
import pandas as pd

player_stats = pd.read_csv('2017-18_playerBoxScore.csv', parse_dates=['gmDate'])

# Найдите игроков, которые сделали хотя бы 1 трехочковый бросок за сезон
three_takers = player_stats[player_stats['play3PA'] > 0]
# Убрать имена игроков, поместив их в один столбец
three_takers['name'] = [f'{p["playFNm"]} {p["playLNm"]}'
                        for _, p in three_takers.iterrows()]
# Суммируйте общее количество трехочковых попыток и количество попыток для каждого игрока
three_takers = (three_takers.groupby('name')
                .sum()
                .loc[:, ['play3PA', 'play3PM']]
                .sort_values('play3PA', ascending=False))
# Отфильтровать всех, кто не сделал хотя бы 100 трехочковых бросков
three_takers = three_takers[three_takers['play3PA'] >= 100].reset_index()
# Добавить столбец с рассчитанным трехбалльным процентом (выполнено / предпринято)
three_takers['pct3PM'] = three_takers['play3PM'] / three_takers['play3PA']
# Файл вывода
output_file('three-point-att-vs-pct.html',
            title='Three-Point Attempts vs. Percentage')

# Сохраним данные в ColumnDataSource
three_takers_cds = ColumnDataSource(three_takers)

# Укажите инструменты выбора, которые будут доступны
select_tools = ['box_select', 'lasso_select', 'poly_select', 'tap', 'reset']

# Создание картинки
fig = figure(plot_height=400,
             plot_width=600,
             x_axis_label='Three-Point Shots Attempted',
             y_axis_label='Percentage Made',
             title='3PT Shots Attempted vs. Percentage Made (min. 100 3PA), 2017-18',
             toolbar_location='below',
             tools=select_tools)

# Отформатируйте метки делений оси Y в процентах
fig.yaxis[0].formatter = NumeralTickFormatter(format='00.0%')

# Добавить квадрат, представляющий каждого игрока
fig.square(x='play3PA',
           y='pct3PM',
           source=three_takers_cds,
           color='royalblue',
           selection_color='deepskyblue',
           nonselection_color='lightgray',
           nonselection_alpha=0.3)

# Показать результат
# Библиотека Bokeh
from bokeh.models import HoverTool
# Отформатируйте всплывающую подсказку
tooltips = [
            ('Player','@name'),
            ('Three-Pointers Made', '@play3PM'),
            ('Three-Pointers Attempted', '@play3PA'),
            ('Three-Point Percentage','@pct3PM{00.0%}'),
           ]
# Добавляем HoverTool к фигуре
fig.add_tools(HoverTool(tooltips=tooltips))
# Визуализировать
show(fig)
