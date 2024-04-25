import pandas as pd

# Создаем словарь для кодирования
encoding_dict = {'robot': [1, 0], 'human': [0, 1]}
lst = ['robot'] * 10
lst += ['human'] * 10
data = pd.DataFrame({'whoAmI': lst})
# Применяем one hot кодирование
data['robot'] = data['whoAmI'].apply(lambda x: encoding_dict[x][0])
data['human'] = data['whoAmI'].apply(lambda x: encoding_dict[x][1])

# Удаляем исходный столбец
data.drop('whoAmI', axis=1, inplace=True)

print(data.head())
