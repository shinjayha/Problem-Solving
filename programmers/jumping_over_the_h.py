'''
Jumping over the "h"
k = how small each jump is
boxes = heights of boxes in list, that can be used in any order
'''
h, k, boxes = 12, 3, [1,2,3,5,8,9]
# h, k, boxes = 10, 1, [9,8,7,6,5,4,3,2,1]
def solution(h, k, boxes):
    ch=0
    answer_arr = []
    boxes=sorted(boxes)
    for index in range(len(boxes)) :
        if(h > (ch + k)) :
            if ( k >= (boxes[index]-ch) ) :
                if(index < (len(boxes)-1)) :
                    if( (ch+k) < boxes[index+1] ) :
                        answer_arr.append(boxes[index])
                        ch = boxes[index]
                else :
                    answer_arr.append(boxes[index])
                    ch = boxes[index]
    print(answer_arr)
    if (h <= (ch + k)) :
        answer = len(answer_arr)
    else :
        answer = -1
    return answer
solution(h, k, boxes)
