def show_hint(secret, guess):
    """
    入力が正しい形式かチェックし、条件に合えば大小のヒントを直接表示する。
    """
    # 桁数が secret と同じ で、かつ 数字だけ の場合のみ処理する
    if len(guess) == len(secret) and guess.isdigit():
        secret_num = int(secret)
        guess_num = int(guess)
        
        if secret_num > guess_num:
            print("💡 ヒント: 答えはもっと【大きな】数字です")
        elif secret_num < guess_num:
            print("💡 ヒント: 答えはもっと【小さな】数字です")
        # 大正解（同じ数字）の時は何もしない