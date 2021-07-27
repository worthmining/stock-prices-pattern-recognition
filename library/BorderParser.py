from time import time
from library.Border import Border
from library.PriceMovementEnum import PriceMovement
import pandas as pd


class BorderParser:


    def __init__(self, timeseries: pd.Series, border_width=2) -> None:
        self._parsed_border = self.__parse_border(timeseries, border_width)

    def get_content(self) -> Border:
        return self._parsed_border

    def __parse_border(self, timeseries: pd.Series, border_width) -> Border:
        upper_bound = timeseries.head(border_width + 1)
        lower_bound = timeseries.tail(border_width + 1)

        upper_border = self.__parse_price_movement(upper_bound)
        lower_border = self.__parse_price_movement(lower_bound)

        return Border(upper_border, lower_border)

    def __parse_price_movement(self, timeseries: pd.Series):
        price_movement = []

        previous_value = timeseries.values[0]
        for current_value in timeseries.values[1:]:
            if current_value > previous_value:
                price_movement.append(PriceMovement.UP)
            else:
                price_movement.append(PriceMovement.DOWN)

        return price_movement