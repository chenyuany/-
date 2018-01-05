#coding=utf-8
#__author__ = 'chenyuanyuan'
import random
#大乐透彩票数据生成
def lottery():
    daletou_qian = [i for i in range(1, 36)]
    daletou_hou = [i for i in range(1, 13)]
    daletou = random.sample(daletou_qian, k=5)+random.sample(daletou_hou, k=2)
    print(daletou)


def shuffle_card():
    #随机洗牌
    card_number = [i for i in range(2, 11)]
    card_str = ["A", "J", "Q", "K"]
    card_color = ["红桃", "梅花", "黑桃", "方片"]
    card_king = ["大王", "小王"]
    card = ["%s%s" % (s, j) for s in card_color for j in (card_number + card_str)] + card_king
    random.shuffle(card)
    print(card)

    #斗地主
    dizhu = random.sample(card[:-3], k=1)[0]
    print(dizhu)
    persona = card[0:51:3]
    personb = card[1:51:3]
    personc = card[2:51:3]
    last_card = card[-3:]
    print(last_card)

    if dizhu in persona:
       persona = persona + last_card

    elif dizhu in personb:
        personb = personb + last_card

    else:
        personc = personc + last_card

    print(persona)
    print(personb)
    print(personc)






shuffle_card()