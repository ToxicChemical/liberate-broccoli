import pandas as pd
import matplotlib.pyplot as plt
from Graphs import *

def plotfile(data, x_name, y_name):
    df = pd.concat([data[x_name], data[y_name]], sort=False, axis=1)
    with(open('plotfile', 'w') as f):
        for i in range(len(df)):
            print(df.iloc[i][x_name], df.iloc[i][y_name], file=f, sep=' ')

'''def gystfile(df):
    with(open('tablefile', 'w') as f):
        for i in df.columns:
            for j in df[i].tolist():
                print(str(j), file=f)'''
def execute_Excel_Read():
    print('Число графиков:')
    plot_num = int(input())  #Ввод числа графиков (опционально)

    print('Путь сохранения:')
    path = input()  # Ввод пути папки сохранения
    # path = '/home/fima/Documents/uni/labs/' + lab_num + '/figs/graph_' + graph_num + '.png'
    print('Имя .xlsx файла(data по default(оставьте строчку пустой))')
    name = input()
    if (name == ''):
        name = 'data'
    data = pd.read_excel(name + ".xlsx")
    QuestionsGraphs()
    # gystfile(data)
    for i in range(plot_num):
        print('XY-координаты' + str(i) + '-го графика(через пробел, названия не содержат пробелы)')
        x, y = input().split()   # Ввод x,y координат i-го графика
        plotfile(data, x, y)
        # tablefile(data)
        PlotBuild()
    PlotShow(path)
# print('Вид таблиции:')
# table_name = input()
# TableBuild(data, tablename)
