class GlobalHitTracker:
    def __init__(self):
        # ゲーム全体の最高Hit数（初期値は0）
        self.max_hit = 0

    def check_and_update(self, current_hit, match):
        """今回のHit数が過去最高を超えたか判定し、ターンの維持または切り替えを行う。

        :param current_hit: 今回出たHit数
        :param match: MatchManagerのインスタンス
        :return: Trueなら連続プレイ（ターン維持）、Falseならターン交代
        """
        # 今回のHit数が、全体の過去最高Hit数より大きい（1以上増えた）場合
        if current_hit > self.max_hit:
            increase = current_hit - self.max_hit
            self.max_hit = current_hit  # 最高記録を更新
            print(f"\n★ 全体のHit数が更新されました (+{increase} Hit / 現在最高: {self.max_hit} Hit)! ")
            print("★ CONTINUED TURN — もう一度あなたの番です！ \n")
            return True
        else:
            # 増えていない（維持、減少、または0）場合は交代
            match.switch_turn()
            return False