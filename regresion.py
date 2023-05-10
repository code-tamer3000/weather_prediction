import pandas as pd
from sklearn.linear_model import LinearRegression

def make_suggestion(file_path) :
    sheet_name = "Sheet1"

    # Прочитайте таблицу Excel с помощью функции read_excel() из библиотеки pandas
    # Извлеките первый столбец с помощью оператора []
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    first_column = df.iloc[:, 0]
    fourth_column = df.iloc[:, 3]

    df1 = pd.DataFrame({"date": first_column,
                       "temperature": fourth_column})

    # Установка столбца с датами в качестве индекса
    df1.set_index("date", inplace=True)

    # Создание словаря из DataFrame с помощью метода to_dict()
    result_dict = df1.to_dict()["temperature"]

    by_year = {}
    for date, temperature in result_dict.items():
        year = int(date.split('.')[2]) # выделяем год из даты
        month = int(date.split('.')[1]) # выделяем месяц из даты
        if month in [6, 7, 8]: # проверяем, что месяц летний
            if year not in by_year:
                by_year[year] = []
            by_year[year].append(temperature)

    # Создаем словарь со средней температурой летом для каждого года
    avg_temp_by_year = {}
    for year, temperatures in by_year.items():
        avg_temp = sum(temperatures) / len(temperatures)
        avg_temp_by_year[year] = avg_temp

    for i in range(2021, 2023):
        print(f"Cредняя температура летом в Уфе {i} года: {avg_temp_by_year[i]}")

    # Создаем DataFrame из словаря
    data = pd.DataFrame({'Year': avg_temp_by_year.keys(),
                         'Temp': avg_temp_by_year.values()})

    # Создаем и обучаем модель линейной регрессии
    model = LinearRegression()
    model.fit(data[['Year']], data['Temp'])

    # Предсказываем среднюю температуру летом текущего года
    current_year = 2023
    prediction = model.predict([[current_year]])

    # Выводим предсказанное значение
    print(f"Ожидаемая средняя температура летом в Уфе {current_year} года: {prediction[0]:.2f}")
