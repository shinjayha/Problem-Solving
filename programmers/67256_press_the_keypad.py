'''
https://school.programmers.co.kr/learn/courses/30/lessons/67256
[Kakao Intern] Press the keypad
I'm trying to enter only numbers on the phone keypad using only the thumbs of my left and right hands.
The first thumb of the left hand starts at the * keypad, 
and the thumb of the right hand starts at the # keypad position, 
and the rules for using the thumb are as follows.

[카카오 인턴] 키패드 누르기
문제 설명
전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.
맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 엄지손가락을 사용하는 규칙은 다음과 같습니다.

엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.
순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 
각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.

입출력 예
numbers				hand	result
[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	"LRLLLRLLRRL"
[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	"left"	"LRLLRRLLLRR"
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	"right"		"LLRLLRLLRL"
'''
switch=['_','L','_','R','L','_','R','L','_','R']
# 10th index indicates either "*" or "#" in keypad
distance=[[0,4,3,4,3,2,3,2,1,2,1],[],
          [3,1,0,1,2,1,2,3,2,3,4],[],[],
          [2,2,1,2,1,0,1,2,1,2,4],[],[],
          [1,3,2,3,2,1,2,1,0,1,2]]
def solution(numbers, hand):
    answer = ''
    last_r_thumb = 10
    last_l_thumb = 10
    for v in numbers :
        if v==2 or v==5 or v==8 or v==0 :
            if distance[v][last_l_thumb]==distance[v][last_r_thumb] :
                if hand=="right":
                    answer = answer+'R'
                    last_r_thumb = v
                else:
                    answer = answer+'L'
                    last_l_thumb = v
            elif distance[v][last_l_thumb] < distance[v][last_r_thumb] :
                answer = answer+'L'
                last_l_thumb = v
            else:
                answer = answer+'R'
                last_r_thumb = v
        else :
            answer = answer+switch[v]
            if v==1 or v==4 or v==7 :
                last_l_thumb = v
            else:
                last_r_thumb = v
    return answer

# numbers, hand = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right" # "LRLLLRLLRRL"
numbers, hand = [8,0,2,0], "right"  # "RRRL"
solution(numbers, hand)

# Solution by other
def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}
    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])
            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i
    return answer
# END
