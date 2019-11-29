import json
import os


class Config:
    REFRESH_INTERVAL = None
    INSTRUMENT_INDEPEND = None
    SLIPPAGE_SHORT = None
    SLIPPAGE_BUY = None
    SLIPPAGE_COVER = None
    SLIPPAGE_SELL = None
    CLOSE_PATTERN = None
    SHARED_FUNC = None

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        self.to_file()

    def update(self, data: dict):
        for k, v in data.items():
            if hasattr(self, k):
                setattr(self, k, v)

    def to_dict(self):
        pr = {}
        for name in dir(self):
            value = getattr(self, name)
            if not name.startswith('__') and not callable(value):
                pr[name] = value
        return pr

    def to_file(self):
        config_path = os.path.join(G.user_path, ".config.json")
        with open(config_path, 'w')as f:
            json.dump(self.to_dict(), f)


class G(dict):
    mainwindow = None
    user_path = None
    config = Config()
    # log
    log_history = []
    # market
    all_contracts = {}
    subscribes = {}
    market_tick = {}
    market_tick_row_map = []
    # account
    current_account = None
    account = {}
    account_row_map = []
    # order
    choice_local_symbol = None
    order_tick_row_map = []  # with tick ={}
    order_position_row_map = []

    # kline
    kline_folder = "/static/kline.html"
