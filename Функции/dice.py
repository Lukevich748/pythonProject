def calc_dice_scores(scores):
    return print(sum([k + v for k, v in scores]) if not any([k == v for k, v in scores]) else 0)

calc_dice_scores([(1, 2), (3, 4), (5, 6)])