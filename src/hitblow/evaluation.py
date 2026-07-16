# hitblow/evaluation.py

def get_rank_message(tries: int) -> str:
    """予想回数（tries）を受け取り、対応する評価（ランク）のメッセージを返します。
    
    ランク基準:
    - 4回以下：ランク S 
    - 5〜6回：ランク A 
    - 7〜8回：ランク B 
    - 9回以上：ランク C 
    """
    if tries <= 4:
        return " ランク S （あっぱれ！）"
    elif tries <= 6:
        return " ランク A （お見事！）"
    elif tries <= 8:
        return " ランク B （まずまず！）"
    else:
        return " ランク C （がんばりましょう！）"