import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import argparse


# функция считывания аргумента
def createParser():

    parser = argparse.ArgumentParser()
    parser.add_argument('month', type=str, default='0')
    parser.add_argument('year', type=str, default='0')

    return parser


# считывание аргументов при запуске  кода
if __name__ == '__main__':

    parser = createParser()
    agrs_inp = parser.parse_args()
    if agrs_inp.month:
        if agrs_inp.year:
            month = agrs_inp.month
            year = agrs_inp.year
        else:
            print('Проверьте корректность ввода аргумента.')


# проверка валидности аргументов
# создание графика, его вывод на экран и сохранение
filename = r'C:\Users\Nastya\Documents\project\outcome_' + \
    month + '.' + year + '.xlsx'
try:
    file = open(filename, encoding="utf-8")
except IOError:
    print(u'Ошибка: не получилось открыть файл')
else:
    with file:
        outcome_data = pd.read_excel(file)
        outcome_data['День'] = [int(x.split()[0])
                                for x in outcome_data['Дата']]
        fig, ax = plt.subplots(constrained_layout=True)
        sns.barplot(
            data=outcome_data.loc[
                    (outcome_data['Месяц'] == int(month))
                    & (outcome_data['Год'] == int(year))],
            y='Категория',
            x='Сумма',
            orient='h',
            estimator='sum',
            errorbar=None,
            ax=ax)
        plt.show()
        plt.savefig('graph.png')
