from typing import List, Optional


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        _min = None
        _min_index = None
        _max = None
        _max_index = None

        for i in range(1, len(prices)):
            price = prices[i]

            if (_min is None) or (price < _min):
                _min = price
                _min_index = i

            if (price > _min) & ((_max is None) or (price > _max)):
                _max = prices[i]
                _max_index = i

        if (_min_index is None): # no sell
            return 0
        if (_max_index is None): # no buy
            return 0
        if _max_index > _min_index: # max occur after min even though code covers this but double check
            return _max - _min
        return 0



def test_buy_appears_multiple_times():
    prices = [8, 1, 8, 2]
    expected_output = 7
    assert expected_output == Solution().maxProfit(prices)

def test_ex_profit():
    prices = [7, 1, 5, 3, 6, 4]
    expected_output = 5
    assert expected_output == Solution().maxProfit(prices)

def test_ex_no_profit():
    prices = [7, 6, 4, 3, 1]
    expected_output = 0
    assert expected_output == Solution().maxProfit(prices)

def test_sell_after_buy():
    prices = [6, 2, 8, 7]
    min_price = min(prices)
    max_price = max(prices)
    assert prices.index(min_price) < prices.index(max_price)

def test_no_buy():
    prices = []
    assert Solution().maxProfit(prices) is None

def test_no_sell():
    prices = [10]
    assert 0 == Solution().maxProfit(prices)

def test_no_profit():
    prices = [7, 7]
    expected_output = 0
    assert expected_output == Solution().maxProfit(prices)

def test_negative_buy_price():
    prices = [8, -1, 7]
    expected_output = 8
    assert expected_output == Solution().maxProfit(prices)

def test_negative_prices():
    prices = [-8, -1, -7]
    expected_output = 0
    assert expected_output == Solution().maxProfit(prices)

def test_zero_prices():
    prices = [0,0]
    expected_output = 0
    assert expected_output == Solution().maxProfit(prices)

def test_decreasing_then_increasing():
    prices = [10, 1, 5]
    expected_output = 4  # Buy at 1, sell at 5
    assert expected_output == Solution().maxProfit(prices)