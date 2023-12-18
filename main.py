# Импорт необходимых библиотек
import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных
data = pd.read_csv('mortality_water_hardness.csv')

# Построение точечного графика
plt.scatter(data['hardness'], data['mortality'])
plt.xlabel('Water Hardness')
plt.ylabel('Mortality')
plt.title('Correlation between Water Hardness and Mortality')
plt.show()

# Расчет коэффициента корреляции Пирсона
correlation_pearson = data['hardness'].corr(data['mortality'], method='pearson')
print('Pearson correlation coefficient:', correlation_pearson)

# Расчет коэффициента корреляции Спирмена
correlation_spearman = data['hardness'].corr(data['mortality'], method='spearman')
print('Spearman correlation coefficient:', correlation_spearman)

# Разделение данных на 2 группы
north_data = data[data['location'] == 'North']
south_data = data[data['location'] == 'South']

# Построение точечного графика для 1-й и 2-й группы по отдельности
plt.scatter(north_data['hardness'], north_data['mortality'])
plt.xlabel('Water Hardness')
plt.ylabel('Mortality')
plt.title('Correlation between Water Hardness and Mortality in North')
plt.show()

plt.scatter(south_data['hardness'], south_data['mortality'])
plt.xlabel('Water Hardness')
plt.ylabel('Mortality')
plt.title('Correlation between Water Hardness and Mortality in South')
plt.show()

# Расчет коэффициента корреляции Пирсона для 1-й и 2-й группы по отдельности
correlation_pearson_north = north_data['hardness'].corr(north_data['mortality'], method='pearson')
correlation_pearson_south = south_data['hardness'].corr(south_data['mortality'], method='pearson')

print('Pearson correlation coefficient in North:', correlation_pearson_north)
print('Pearson correlation coefficient in South:', correlation_pearson_south)

# Расчет коэффициента корреляции Спирмена для 1-й и 2-й группы по отдельности
correlation_spearman_north = north_data['hardness'].corr(north_data['mortality'], method='spearman')
correlation_spearman_south = south_data['hardness'].corr(south_data['mortality'], method='spearman')

print('Spearman correlation coefficient in North:', correlation_spearman_north)
print('Spearman correlation coefficient in South:', correlation_spearman_south)
