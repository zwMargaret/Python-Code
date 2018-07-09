import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




#######################################

def Sum_profit(day_profit):
    sum_profit = day_profit.cumsum()
    return sum_profit
    

def Annual_profit(trade_date, sum_profit):

    data = {'trade_date': trade_date,
            'sum_profit': sum_profit}
    
    dataframe = pd.DataFrame(data)
    trade_days = len(dataframe.index)
    annual_profit = dataframe.sum_profit.iloc[-1]*252/trade_days
    return annual_profit, trade_days

def Max_drawdown(trade_date, sum_profit):
    
    data = {'trade_date': trade_date,
            'sum_profit': sum_profit}
    dataframe = pd.DataFrame(data)
    dataframe['max2here'] = pd.expanding_max(dataframe['sum_profit'])
    dataframe['drawdown'] = dataframe['sum_profit'] - dataframe['max2here']
    temp = dataframe.sort_values(by = 'drawdown').iloc[0]
    max_drawdown = temp.drawdown
    max_drawdown_enddate = temp.trade_date.strftime('%Y-%m-%d')
    sub_dataframe = dataframe[dataframe.trade_date <= max_drawdown_enddate]
    max_drawdown_startdate = sub_dataframe.sort_values(by = 'sum_profit', ascending = False).iloc[0]['trade_date'].strftime('%Y-%m-%d')

    return max_drawdown, max_drawdown_startdate, max_drawdown_enddate



def Day_win_chance(trade_date, day_profit):
    data = {'trade_date': trade_date,
            'day_profit': day_profit}
    dataframe = pd.DataFrame(data)
    day_win_chance = len(dataframe[dataframe['day_profit'] > 0 ])/len(dataframe)
    return day_win_chance

def Max_sequent_days(trade_date, day_profit):
    '''
    calculate the max of going up days, and the max of going down days
    '''
    data = {'trade_date': trade_date,
            'day_profit': day_profit}
    dataframe = pd.DataFrame(data)
    if dataframe.day_profit[0] > 0:
        dataframe.loc[0, 'count'] = 1
    else:
        dataframe.loc[0, 'count'] = -1
    for i in dataframe.index[1:]:
        if dataframe.day_profit[i] > 0 and dataframe.day_profit[i - 1] > 0:
            dataframe.loc[i, 'count'] = dataframe.loc[i-1,'count'] + 1
        elif dataframe.day_profit[i] <= 0 and dataframe.day_profit[i - 1] <= 0:
            dataframe.loc[i, 'count'] = dataframe.loc[i-1,'count']-1
        elif dataframe.day_profit[i] > 0 and dataframe.day_profit[i - 1] <= 0:
            dataframe.loc[i, 'count'] = 1
        elif dataframe.day_profit[i] <= 0 and dataframe.day_profit[i - 1] > 0:
            dataframe.loc[i, 'count'] = -1

    
    dataframe.count = list(dataframe['count'])
    return max(dataframe.count), min(dataframe.count)


def VIX(day_profit):
    return np.std(day_profit)*np.sqrt(252)


def Sharp_ratio(annual_profit, VIX):
    return (annual_profit - 0.025)/VIX


def Infromation_ratio(day_profit, benchmark_profit):
    diff = pd.Series(day_profit - benchmark_profit)
    return diff.mean() * 252/(diff.std() * np.sqrt(252))


def Draw_Line_chart(trade_date, sum_profit, sum_benchmark_profit):

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(trade_date, sum_profit, color = 'r', label = 'sum_profit')
    ax.set_title('The line chart of sum_profit')
    ax.set_xlabel('trade_date')
    ax.set_ylabel('sum_profit')
    ax.legend(loc = 'best')

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(trade_date, sum_profit, color = 'r', label = 'sum_profit')
    ax.plot(trade_date, sum_benchmark_profit, color = 'b', label ='sum_benchmark_profit')
    ax.set_title('Comaprison diagram')
    ax.set_xlabel('trade_date')
    ax.set_ylabel('sum_profit')
    ax.legend(loc = 'best')
    plt.show()
