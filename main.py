left1, top1, width1, height1 = map(int, input().split())
left2, top2, width2, height2 = map(int, input().split())
if (left1 <= left2 <= left1 + width1 or left1 <= left2 + width2 <= left1 + width1) and \
        (top1 <= top2 <= top1 + height1 or top1 <= top2 + height2 <= top1 + height1) or \
        (left2 <= left1 <= left2 + width2 or left2 <= left1 + width1 <= left2 + width2) and \
        (top2 <= top1 <= top2 + height2 or top2 <= top1 + height1 <= top2 + height2):
    print('YES')
else:
    print('NO')
