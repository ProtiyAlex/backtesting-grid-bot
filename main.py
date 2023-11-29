
def main():
    grid_percentage = 1.5  # Размер сетки в процентах
    number_of_orders = 10  # Количество ордеров


    df = pd.DataFrame(ohlcvs, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])


    def grid_bot_strategy(df, grid_step_pct, number_of_orders):
        def grid_bot_strategy(df, grid_step_pct, number_of_orders):
            long_position = False  # Переменная для отслеживания длинной позиции
            short_position = False  # Переменная для отслеживания короткой позиции
            positions = []  # Здесь будем хранить позиции (1 - покупка, -1 - продажа, 0 - без действий)
            prev_price = df['close'][0]

            for i in range(1, len(df)):
                if df['close'][i] > prev_price * (1 + grid_step_pct / 100):  # Если цена выросла на шаг сетки
                    if not long_position:
                        positions.append(1)  # Покупаем
                        long_position = True  # Установка флага длинной позиции
                        short_position = False  # Сброс флага короткой позиции
                        prev_price = df['close'][i]
                    else:
                        positions.append(0)  # Уже в длинной позиции, ничего не делаем
                elif df['close'][i] < prev_price * (1 - grid_step_pct / 100):  # Если цена упала на шаг сетки
                    if not short_position:
                        positions.append(-1)  # Продаем
                        short_position = True  # Установка флага короткой позиции
                        long_position = False  # Сброс флага длинной позиции
                        prev_price = df['close'][i]
                    else:
                        positions.append(0)  # Уже в короткой позиции, ничего не делаем
                else:
                    positions.append(0)  # Ничего не делаем

            return positions[:-(number_of_orders + 1)]

        # Получаем сигналы от стратегии
    signals = grid_bot_strategy(df,grid_percentage,number_of_orders)

    # Рассчитываем доходность
    pnl = []
    position = 0  # Начальная позиция - не в рынке

    for signal, close_price in zip(signals, df['close'][1:]):
        if signal == 1 and position <= 0:  # Сигнал на покупку
            position = 1  # Входим в длинную позицию (покупаем)
            entry_price = close_price
        elif signal == -1 and position >= 0:  # Сигнал на продажу
            position = -1  # Входим в короткую позицию (продаем)
            pnl.append((close_price - entry_price) / entry_price)  # Рассчитываем доходность
            position = 0  # Выходим из рынка
    if position == 1:  # Если остались в открытой позиции, закрываем ее
        pnl.append((close_price - entry_price) / entry_price)

    # Вычисляем общую доходность стратегии
    total_return = sum(pnl)

    # Выводим результат
    print(f"Общая доходность: {total_return * 100:.2f}%")

if __name__ == '__main__':
    main()

