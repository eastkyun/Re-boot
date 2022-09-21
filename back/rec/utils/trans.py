kor_money = "3억 7,770"


def change_currency_language(kor_money):
    for i, word in enumerate(kor_money):
        if word == "억":
            kor_money = kor_money[:i] + kor_money[i+1:]
            break
    kor_money = kor_money.replace(" ", "")
    kor_money = kor_money.replace(",", "")
    kor_money = kor_money.replace(".", "")
    return int(kor_money)


print(change_currency_language(kor_money))
