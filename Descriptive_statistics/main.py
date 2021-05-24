# Расчет описательной статистики
import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd

x = [10.0, 2, 2.5, 5, 26.0]
x_with_nan = [10.0, 2, 2.5, math.nan, 5, 26.0]
print(f'Вывод исходных данных, которые содержатся в x:{x}')
print(f'Вывод исходных данных, которые содержатся в x_with_nan:{x_with_nan}')

y, y_with_nan = np.array(x), np.array(x_with_nan)
z, z_with_nan = pd.Series(x), pd.Series(x_with_nan)
print(f'Вывод данных, которые содержатся в y и y_with_nan:{y}, {y_with_nan}')
print(f'Вывод данных, которые содержатся в z и в z_with_nan: {z}, {z_with_nan}')

# Рассчет средних значений
mean_1 = sum(x) / len(x)
print(f'Расчет среднего значения, используя sum и len: {mean_1}')
mean_2 = statistics.mean(x)
print(f'Расчет среднего значения, используя встроенные функции статистики Python (statistics.mean(x)): {mean_2}')
mean_3 = statistics.fmean(x)
print(f'Расчет среднего значения, используя встроенные функции статистики Python (statistics.fmean(x)): {mean_3}')
mean_4 = statistics.mean(x_with_nan)
print(
    f'Расчет среднего значения, который содержит значения nan, используя встроенные функции статистики Python (statistics.mean(x)): {mean_4}')
mean_5 = np.mean(y)
print(f'Расчет среднего значения, используя NumPy: {mean_5}')
np.nanmean(y_with_nan)
print(f'Расчет среднего значения с помощью NumPy, игнорируя nan: {np.nanmean(y_with_nan)}')
mean_6 = z.mean()
print(f'Расчет среднего значения объекта pd.Series: {mean_6}')

# Рассчет средневзвешанных значений
x = [6.0, 1, 2.5, 6, 25.0]
w = [0.1, 0.2, 0.3, 0.25, 0.15]
wmean = sum(w[i] * x[i] for i in range(len(x))) / sum(w)
print(f'Расчет средневзвешанного с помощью range: {wmean}')
wmean2 = sum(x_ * w_ for (x_, w_) in zip(x, w)) / sum(w)
print(f'Расчет средневзвешанного с помощью zip: {wmean2}')
y, z, w = np.array(x), pd.Series(x), np.array(w)
wmean3 = np.average(y, weights=w)
print(f'Расчет средневзвешанного с помощью np.average для массивово NumPy или серии Pandas: {wmean3}')
o = (w * y).sum() / w.sum()
print(f'Расчет средневзвешанного с помощью поэлементного умножения w * y: {o}')
w = np.array([0.1, 0.2, 0.3, 0.0, 0.2, 0.1])
print(f'Расчет средневзвешанного для набора, который содержит nan : {(w * y_with_nan).sum() / w.sum()}')

# Гармоническое среднее
hmean = len(x) / sum(1 / item for item in x)
print(f'Расчет гармонического среднего: {hmean}')
hmean2 = statistics.harmonic_mean(x)
print(f'Расчет гармонического среднего с помощью statistics.harmonic_mean(): {hmean2}')
statistics.harmonic_mean(x_with_nan)
print(f'Расчет гармонического среднего, где есть nan: {statistics.harmonic_mean(x_with_nan)}')
statistics.harmonic_mean([1, 0, 2])
print(f'Расчет гармонического среднего, где есть 0: {statistics.harmonic_mean([1, 0, 2])}')
scipy.stats.hmean(y)
print(f'Расчет гармонического среднего с помощью  scipy.stats.hmean(): {scipy.stats.hmean(y)}')

# Среднее геометрическое
gmean = 1
for item in x:
    gmean *= item
    gmean **= 1 / len(x)
print(f'Вычисление геометрического среднего: {gmean}')
gmean2 = statistics.geometric_mean(x)
print(f'Вычисление геометрического среднего с помощью  statistics.geometric_mean(): {gmean2}')
gmean3 = statistics.geometric_mean(x_with_nan)
print(f'Вычисление геометрического среднего где есть nan: {gmean3}')
scipy.stats.gmean(y)
print(f'Вычисление геометрического среднего с помощью scipy.stats.gmean(): {scipy.stats.gmean(y)}')

# Медиана
n = len(x)
if n % 2:
    median_ = sorted(x)[round(0.5 * (n - 1))]
else:
    x_ord, index = sorted(x), round(0.5 * n)
    median_ = 0.5 * (x_ord[index - 1] + x_ord[index])
print(f'Расчет медианы: {median_}')
median_2 = statistics.median(x)
print(f'Расчет медианы с помощью statistics.median(): {median_2}')
statistics.median_low(x[:-1])
print(f'Расчет медианы с помощью statistics.median_low: {statistics.median_low(x[:-1])}')
statistics.median_high(x[:-1])
print(f'Расчет медианы с помощью statistics.median_high {statistics.median_high(x[:-1])}')
median_2 = np.median(y)
print(f'Расчет медианы с помощью np.median: {median_2}')

# Мода
u = [2, 3, 2, 8, 12]
mode_ = max((u.count(item), item) for item in set(u))[1]
print(f'Вычисление моды: {mode_}')
mode_2 = statistics.mode(u)
print(f'Вычисление моды с помощью statistics.mode(): {mode_2}')
mode_3 = statistics.multimode(u)
print(f'Вычисление моды с помощью statistics.multimode(): {mode_3}')
mode_4 = scipy.stats.mode(u)
print(f'Вычисление моды с помощью scipy.stats.mode(): {mode_4}')

# Метрики оценки вариативности данных
n = len(x)
mean = sum(x) / n
var_ = sum((item - mean) ** 2 for item in x) / (n - 1)
print(f'Оценка дисперсии на чистом Python: {var_}')
var_1 = statistics.variance(x)
print(f'Оценка дисперсии с помощью statistics.variance(): {var_1}')
statistics.variance(x_with_nan)
print(f'Оценка дисперсии с помощью statistics.variance(), где есть nan: {statistics.variance(x_with_nan)}')
var_2 = np.var(y, ddof=1)
print(f'Оценка дисперсии, используя NumPy с помощью np.var(): {var_2}')
var_3 = y.var(ddof=1)
print(f'Оценка дисперсии, используя NumPy с помощью метода .var(): {var_3}')

# Среднеквадратичное отклонение
std_ = var_ ** 0.5
print(f'Расчет среднеквадратичного отклонения на чистом Python: {std_}')
std_2 = statistics.stdev(x)
print(f'Расчет среднеквадратичного отклонения с помощью  statistics.stdev(): {std_2}')
np.std(y, ddof=1)
print(f'Расчет среднеквадратичного отклонения с помощью  NumPy: {np.std(y, ddof=1)}')

# Смещение
x = [8.0, 1, 2.5, 4, 28.0]
n = len(x)
mean_ = sum(x) / n
var_ = sum((item - mean_) ** 2 for item in x) / (n - 1)
std_ = var_ ** 0.5
skew_ = (sum((item - mean_) ** 3 for item in x)
         * n / ((n - 1) * (n - 2) * std_ ** 3))
print(f'Расчет смещения на чистом Python: {skew_}')
z, z_with_nan = pd.Series(x), pd.Series(x_with_nan)
print(f'Расчет смещения с помощью Pandas: {z.skew()}')

# Процентили
x = [-5.0, -1.1, 0.1, 2.0, 8.0, 12.8, 21.0, 25.8, 41.0]
print(f'Расчет процентилей с помощью  statistics.quantiles(): {statistics.quantiles(x, n=2)}')
statistics.quantiles(x, n=4, method='inclusive')
print(f"Расчет процентилей с помощью  statistics.quantiles(): {statistics.quantiles(x, n=4, method='inclusive')}")
y = np.array(x)
np.percentile(y, 5)
print(f'Нахождение 5 процентиля : {np.percentile(y, 5)}')
np.percentile(y, 95)
print(f'Нахождение 95 процентиля : {np.percentile(y, 95)}')
z, z_with_nan = pd.Series(y), pd.Series(y_with_nan)
z.quantile(0.05)
print(f'Нахождение процентиля используя метод .quantile(): {z.quantile(0.05)}')

# Диапазон
np.ptp(y)
np.ptp(z)
np.ptp(y_with_nan)
np.ptp(z_with_nan)
print(
    f'Нахождение диапазона с помощью функции  np.ptp(): {np.ptp(y), np.ptp(z), np.ptp(y_with_nan), np.ptp(z_with_nan)}')

# Сводка описательной статистики
result = scipy.stats.describe(y, ddof=1, bias=False)
print(f'Сводка описательной статистики с помощью  scipy.stats.describe(): {result}')
result2 = z.describe()
print(f'Сводка описательной статистики с помощью  метода .describe() в Pandas: {result2}')
