# main.py

from Yutplaypkg.gamestart import Gamestart
from Yutplaypkg.yutpan import Yutpan
from Yutplaypkg.myturn import Myturn

# 메인 함수 - 게임 실행
def main():
    verbose = False
    game = Gamestart(verbose)
    game.set_mal()
    yutpan = Yutpan(verbose)

    print('윷놀이를 시작합니다!')
    print('(참고 : 윷판에 해당하는 인덱스는 좌측 상단부터 우측 하단 순서로 실행됩니다!)')

    while True:
        print(f"{game.current_player}님의 차례입니다.")
        yutpan.print_board(game.players_mal_dict)

        turn = Myturn(game, yutpan, verbose)
        result = turn.turn_process()

        if result == "WIN":
            print(f"{game.current_player}님이 게임에서 승리하셨습니다! 축하드립니다!")
            break
        elif result in [None, "CONTINUE"]:
            game.switch_player()

if __name__ == "__main__":
    main()
