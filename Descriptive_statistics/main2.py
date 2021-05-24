import numpy as np
import scipy.stats
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

# Формирование исходных данных
x = list(range(-10, 11))
y = [0, 2, 2, 2, 2, 3, 3, 6, 7, 4, 7, 6, 6, 9, 4, 5, 5, 10, 11, 12, 14]
x_, y_ = np.array(x), np.array(y)
x__, y__ = pd.Series(x_), pd.Series(y_)
n = len(x)

# Ковариация
# Расчет ковариации в чистом Python
mean_x, mean_y = sum(x) / n, sum(y) / n
cov_xy = (sum((x[k] - mean_x) * (y[k] - mean_y) for k in range(n)) / (n - 1))
print(f'Расчет ковариации в чистом Python: {cov_xy}')
# Расчет ковариации с помощью NumPy
cov_matrix = np.cov(x_, y_)
print(f'Расчет ковариационной матрицы с помощью NumPy функцией cov(): {cov_matrix}')
print(f'Проверка, что левый элемент ковариационной матрицы — это ковариация x и x или дисперсия x, '
      f'а правый элемент — ковариация y и y или дисперсия y: {x_.var(ddof=1)} и {y_.var(ddof=1)}')
cov_xy = cov_matrix[0, 1]
cov_xy2 = cov_matrix[1, 0]
print(f'Проверка, что два других элемента ковариационной матрицы равны '
      f'и представляют фактическую ковариацию между x и y: {cov_xy} и {cov_xy2}')
# Расчет ковариации с помощью Pandas
cov_xy = x__.cov(y__)
cov_xy3 = y__.cov(x__)
print(f'Расчет ковариации с помощью Pandas методом .cov(): {cov_xy} и {cov_xy3}')

# Коэффициент корреляции
# Расчет коэффициента корреляции в чистом Python
var_x = sum((item - mean_x) ** 2 for item in x) / (n - 1)
var_y = sum((item - mean_y) ** 2 for item in y) / (n - 1)
std_x, std_y = var_x ** 0.5, var_y ** 0.5
r = cov_xy / (std_x * std_y)
print(f'Расчет коэффициента корреляции в чистом Python: {r}')
# Расчет коэффициента корреляции с помощью scipy.stats
r, p = scipy.stats.pearsonr(x_, y_)
print(f'Расчет коэффициента корреляции и p-value, используя функцию pearsonr() в scipy.stats: {r} и {p} ')
scipy.stats.linregress(x_, y_)
print(f'Расчет коэффициента корреляции с помощью scipy.stats.linregress(): {scipy.stats.linregress(x_, y_)}')
result = scipy.stats.linregress(x_, y_)
r = result.rvalue
print(
    f'Получение доступа к определенным значениям из результата linregress(), включая коэффициент корреляции, '
    f'используя точечную запись: {r}')
# Расчет коэффициента корреляции с помощью Pandas
r = x__.corr(y__)
r1 = y__.corr(x__)
print(f'Расчет коэффициента корреляции методом .corr() библиотеки Pandas: {r} и {r1}')

# Работа с данными 2D (таблицы)
# Axis
# Создание 2D массива с помощью Numpy
a = np.array([[2, 3, 1], [4, 9, 2], [8, 27, 4], [16, 1, 1], [2, 3, 1]])
print(f'Вывод, созданного с помощью Numpy, 2D массива: {a}')
# Использование статистических функций и методов Python к 2d массиву с необязательным параметров axis
np.mean(a, axis=0)
a.mean(axis=1)
print(
    f'Вывод среднего значения 2D массива методом NumPy на оси = 0 и на оси = 1 соответствнно: {np.mean(a, axis=0)} '
    f'и {a.mean(axis=1)}')
np.median(a, axis=0)
np.median(a, axis=1)
print(
    f'Вывод медианы 2D массива методом NumPy на оси = 0 и на оси = 1 соответствнно: {np.median(a, axis=0)} и '
    f'{np.median(a, axis=1)}')
scipy.stats.gmean(a)  # Default: axis=0
print(f'Вывод среднего геометрического значения 2D массива функцией SciPy на оси = 0 : {scipy.stats.gmean(a)}')
scipy.stats.gmean(a, axis=None)
print(f'Вывод среднего геометрического значения для всего 2D массива функцией SciPy: {scipy.stats.gmean(a, axis=None)}')

# DataFrames
row_names = ['first', 'second', 'third', 'fourth', 'fifth']
col_names = ['A', 'B', 'C']
df = pd.DataFrame(a, index=row_names, columns=col_names)
print(f'Вывод класса DataFrame с ранее созданным 2d массивом: {df}')
df.mean()
df.var()
print(
    f'Вывод среднего значения и несмещенной дисперсии для всего класса DataFrame с ранее созданным 2d массивом: '
    f'{df.mean()} и {df.var()}')
df.mean(axis=1)
print(f'Вывод среднего значения класса DataFrame с ранее созданным 2d массивом по оси = 1: {df.mean(axis=1)}')
df['A']
print(f'Пример изоляции класса DataFrame с ранее созданным 2d массивом по столбцу A: {df["A"]}')
df['A'].mean()
print(f'Пример расчета среднего значения класса DataFrame с ранее созданным 2d массивом по столбцу A: {df["A"].mean()}')

# Визуализация данных
# Box Plots
np.random.seed(seed=0)
x = np.random.randn(1000)
y = np.random.randn(100)
z = np.random.randn(10)
fig, ax = plt.subplots()
ax.boxplot((x, y, z), vert=False, showmeans=True, meanline=True,
           labels=('x', 'y', 'z'), patch_artist=True,
           medianprops={'linewidth': 2, 'color': 'purple'},
           meanprops={'linewidth': 2, 'color': 'red'})
plt.show()

# Гистограммы
hist, bin_edges = np.histogram(x, bins=10)
fig, ax = plt.subplots()
ax.hist(x, bin_edges, cumulative=False)
ax.set_xlabel('x')
ax.set_ylabel('Frequency')
plt.show()

# Pie Charts круговые диаграммы
x, y, z = 128, 256, 1024
fig, ax = plt.subplots()
ax.pie((x, y, z), labels=('x', 'y', 'z'), autopct='%1.1f%%')
plt.show()

# Bar Charts
x = np.arange(21)
y = np.random.randint(21, size=21)
err = np.random.randn(21)
fig, ax = plt.subplots()
ax.bar(x, y, yerr=err)
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.show()

# X-Y участки
x = np.arange(21)
y = 5 + 2 * x + 2 * np.random.randn(21)
slope, intercept, r, *__ = scipy.stats.linregress(x, y)
line = f'Regression line: y={intercept:.2f}+{slope:.2f}x, r={r:.2f}'
fig, ax = plt.subplots()
ax.plot(x, y, linewidth=0, marker='s', label='Data points')
ax.plot(x, intercept + slope * x, label=line)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(facecolor='white')
plt.show()

# Схемы Зоны активности
matrix = np.cov(x, y).round(decimals=2)
fig, ax = plt.subplots()
ax.imshow(matrix)
ax.grid(False)
ax.xaxis.set(ticks=(0, 1), ticklabels=('x', 'y'))
ax.yaxis.set(ticks=(0, 1), ticklabels=('x', 'y'))
ax.set_ylim(1.5, -0.5)
for i in range(2):
    for j in range(2):
        ax.text(j, i, matrix[i, j], ha='center', va='center', color='w')
plt.show()
