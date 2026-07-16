# hitblow/match.py

class MatchManager:
    def __init__(self, player1="プレイヤー1", player2="プレイヤー2"):
        self.p1 = player1
        self.p2 = player2
        self.current = self.p1

    def start_match(self):
        """① 開始時のあいさつを表示します。"""
        print("\n  2人対戦（交互プレイ）モードを開始します！ ")

    def show_turn(self):
        """② 入力直前に、現在の手番プレイヤーを表示します。"""
        print(f"\n 【 {self.current} 】のターン")

    def show_victory(self, tries, secret):
        """③ 勝利時に、勝者の名前と結果を表示します。"""
        print(f"\n おめでとうございます！【 {self.current} 】の勝利です！")

    def switch_turn(self):
        """次のプレイヤーに手番を切り替えます。"""
        self.current = self.p2 if self.current == self.p1 else self.p1