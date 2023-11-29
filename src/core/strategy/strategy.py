from settings.config import BASE_DIR, NANE_DB, START_DATE, END_DATE, STRATEGY, SYMBOL



from loguru import logger

import pandas as pd
from datetime import datetime as dt
from datetime import timedelta
from tabulate import tabulate
from time import sleep

import os
import sqlite3
import copy


class Coin:
    def __init__(self, symbol, sl, tp, connect):
        self.symbol = symbol
        self.tp = tp
        self.sl = sl
        self.trade = False


class ChangePrice:
    def __init__(self, start_price, current_price, grid_step_percentage):
        self.percentage_change = 0
        self.steps_taken = 0
        self.change(start_price, current_price, grid_step_percentage)

    def change(self, start_price, current_price, grid_step_percentage):
        price_difference = current_price - start_price
        self.percentage_change = round((price_difference / start_price) * 100, 2)
        self.steps_taken = round(abs(self.percentage_change / grid_step_percentage))
        pass


class PositionTemplate:
    def __init__(self, side, price, profit, date, start_price, current_price, grid_step_percentage, positions,
                 price_start):
        self.side = side
        self.price = price
        self.profit = profit
        self.date = date
        self.change_price = ChangePrice(start_price, current_price, grid_step_percentage)
        self.online = 0
        self.count_online = 0
        self.fn_online_profit(positions, price_start)

    def fn_online_profit(self, positions, price):
        pass
        positions = copy.deepcopy(positions)

        for item in positions:
            if item.profit == 0:
                if item.side == 1:
                    item.profit = (price * 100 / item.price - 100) + 0.07
                    # print(item)
                elif item.side == -1:
                    item.profit = (100 - price * 100 / item.price) + 0.07
                    # print(item)
            # print(item)
        self.online =round(sum(position.profit for position in positions),1)
        self.count_online=len(positions)-1

    def __str__(self):
        return f"Position: side: {self.side}, price: {self.price}, profit: {self.profit}, " \
               f"date: {self.date}| " \
               f"% change: {self.change_price.percentage_change}," \
               f" step: {self.change_price.steps_taken} " \
               f" on_line profit:{self.online}| count {self.count_online}"


class Bot:
    def __init__(self):


        self.df = pd.DataFrame()


        self.profit_now = 0
        self.profit_db_ = 0

        self.dop_profit = 0

    def run(self):
        conn = sqlite3.connect(BASE_DIR + fr'\{NANE_DB}.db')

        start_date = START_DATE
        end_date = END_DATE  # Дата окончания - не включительно (это будет 9 января)

        # Цикл перебора дней и выполнения запроса для каждого дня

        start_time = start_date.replace(hour=START_DATE.hour, minute=START_DATE.minute).strftime(
            '%Y-%m-%d %H:%M:%S')

        next_date = end_date.replace(hour=end_date.hour, minute=0).strftime(
            '%Y-%m-%d %H:%M:%S')
        symbol = SYMBOL
        # Получаем начальное и конечное время для каждого дня

        query = f"""
                 SELECT * 
                 FROM my_table 
                   WHERE timestamp >= '{start_time}' 
                 AND timestamp < '{next_date}'
                 AND symbol = '{symbol}'
             """
        logger.info(f"Отчет за монету: {symbol} ")
        self.df = pd.read_sql_query(query, conn)
        self.df['timestamp'] = pd.to_datetime(self.df['timestamp'])
        self.df.set_index('timestamp', inplace=True)
        # print(tabulate(self.df.head(10), headers='keys', tablefmt='psql'))
        # self.grid_bot_strategy(self.df,STRATEGY[0],STRATEGY[1])
        positions, price = self.grid_bot_strategy(self.df, STRATEGY[0], STRATEGY[1])
        self.calculate_profit(positions, price)
        logger.info("Готово")

    def grid_bot_strategy(self, df, grid_step_pct, number_of_orders):

        prev_price = df['close'][0]
        positions = [PositionTemplate(0, prev_price, 0, None, 1, 1,
                                      1, [],
                                      1)]  # Здесь будем хранить позиции (1 - покупка, -1 - продажа, 0 - без действий)

        positions_activ = positions[0]
        for i in range(1, len(df)):
            date = df.index[i]
            price = df['close'][i]
            pr_long = prev_price * (1 + grid_step_pct / 100)
            pr_short = prev_price * (1 - grid_step_pct / 100)
            if positions_activ.side == 0:
                if df['close'][i] > prev_price * (1 + grid_step_pct / 100):  # Если цена выросла на шаг сетки
                    prev_price = df['close'][i]
                    positions.append(PositionTemplate(-1, prev_price, 0, date, positions[0].price, prev_price,
                                                      grid_step_pct,
                                         positions, price))  # шорт
                    positions_activ = positions[-1]



                elif df['close'][i] < prev_price * (1 - grid_step_pct / 100):  # Если цена упала на шаг сетки
                    prev_price = df['close'][i]
                    positions.append(
                        PositionTemplate(1, prev_price, 0, date, positions[0].price, prev_price, grid_step_pct,
                                         positions, price))  # лонг
                    positions_activ = positions[-1]


            elif positions_activ.side == 1:
                if df['close'][i] > prev_price * (1 + grid_step_pct / 100):  # Если цена выросла на шаг сетки
                    prev_price = df['close'][i]
                    for position in reversed(positions):
                        if position.profit == 0:
                            position.profit = (prev_price * 100 / position.price - 100) - 0.07
                            break
                    for position in reversed(positions):
                        if position.profit == 0:
                            prev_price = position.price
                            positions_activ = position
                            break



                elif df['close'][i] < prev_price * (1 - grid_step_pct / 100):  # Если цена упала на шаг сетки

                    prev_price = df['close'][i]
                    positions.append(
                        PositionTemplate(1, prev_price, 0, date, positions[0].price, prev_price, grid_step_pct,
                                         positions, price))
                    positions_activ = positions[-1]  # шорт






            elif positions_activ.side == -1:

                if df['close'][i] > prev_price * (1 + grid_step_pct / 100):  # Если цена выросла на шаг сетки

                    prev_price = df['close'][i]
                    positions.append(
                        PositionTemplate(-1, prev_price, 0, date, positions[0].price, prev_price, grid_step_pct,
                                         positions, price))
                    positions_activ = positions[-1]  # шорт


                elif df['close'][i] < prev_price * (1 - grid_step_pct / 100):  # Если цена упала на шаг сетки
                    prev_price = df['close'][i]
                    for position in reversed(positions):
                        if position.profit == 0:
                            position.profit = (100 - prev_price * 100 / position.price) - 0.07
                            break
                    for position in reversed(positions):
                        if position.profit == 0:
                            prev_price = position.price
                            positions_activ = position
                            break

        a = positions
        b = positions[:-(number_of_orders + 1)]
        return positions, price

    def calculate_profit_online(self, positions, price):
        positions = positions.copy()

        for item in positions:
            if item.profit == 0:
                if item.side == 1:
                    item.profit = (price * 100 / item.price - 100) + 0.07
                    # print(item)
                elif item.side == -1:
                    item.profit = (100 - price * 100 / item.price) + 0.07
                    # print(item)
            print(item)
        total_profit = sum(position.profit for position in positions)
        return total_profit

    def calculate_profit(self, positions, price):
        # pnl = []  # Здесь будем хранить прибыль/убыток от сделок
        for item in positions:
            if item.profit == 0:
                if item.side == 1:
                    item.profit = (price * 100 / item.price - 100) + 0.07
                    # print(item)
                elif item.side == -1:
                    item.profit = (100 - price * 100 / item.price) + 0.07
                    # print(item)
            print(item)
        step = max([item.change_price.steps_taken for item in positions])
        total_profit = sum(position.profit for position in positions)
        min_online= min(position.online for position in positions)
        print(f'profit: {round(total_profit, 2)}, count: {len(positions) - 1}, max step: {step}, min online: {min_online} ')

        return total_profit


