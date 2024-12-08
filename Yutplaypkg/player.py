# player.py

from Yutplaypkg.gamecomponent import GameComponent
from Yutplaypkg.mal import Mal

class Player(GameComponent):
    def __init__(self, name, mal_symbols, verbose=False):
        super().__init__(verbose)
        self.name = name
        self.mal_symbols = mal_symbols
        print(f"[DEBUG] Initializing Player with name: {name}, mal_symbols: {mal_symbols}")
        # 문제 발생 지점: Mal 클래스 생성 시 문제 확인
        self.mals = []
        for symbol in mal_symbols:
            print(f"[DEBUG] Creating Mal object for symbol: {symbol}")
            self.mals.append(Mal(name, symbol, verbose))

    def get_active_mals(self):
        return [mal for mal in self.mals if not mal.is_finished]
