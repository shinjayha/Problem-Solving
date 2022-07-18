'''
https://school.programmers.co.kr/learn/courses/30/lessons/64061

Crane Picking Game
Game developer "Jordi" wants to make a crane puppet machine into a mobile game.
"Jordi" tries to reflect the screen composition and 
rules in the game logic as follows to increase the fun of the game.

크레인 인형뽑기 게임
문제 설명
게임개발자인 "죠르디"는 크레인 인형뽑기 기계를 모바일 게임으로 만들려고 합니다.
"죠르디"는 게임의 재미를 높이기 위해 화면 구성과 규칙을 다음과 같이 게임 로직에 반영하려고 합니다.

게임 화면은 "1 x 1" 크기의 칸들로 이루어진 "N x N" 크기의 정사각 격자이며 위쪽에는 크레인이 있고 오른쪽에는 바구니가 있습니다. 
(위 그림은 "5 x 5" 크기의 예시입니다). 각 격자 칸에는 다양한 인형이 들어 있으며 인형이 없는 칸은 빈칸입니다. 
모든 인형은 "1 x 1" 크기의 격자 한 칸을 차지하며 격자의 가장 아래 칸부터 차곡차곡 쌓여 있습니다. 
게임 사용자는 크레인을 좌우로 움직여서 멈춘 위치에서 가장 위에 있는 인형을 집어 올릴 수 있습니다. 
집어 올린 인형은 바구니에 쌓이게 되는 데, 이때 바구니의 가장 아래 칸부터 인형이 순서대로 쌓이게 됩니다. 
다음 그림은 [1번, 5번, 3번] 위치에서 순서대로 인형을 집어 올려 바구니에 담은 모습입니다.

만약 같은 모양의 인형 두 개가 바구니에 연속해서 쌓이게 되면 두 인형은 터뜨려지면서 바구니에서 사라지게 됩니다. 
위 상태에서 이어서 [5번] 위치에서 인형을 집어 바구니에 쌓으면 같은 모양 인형 두 개가 없어집니다.

크레인 작동 시 인형이 집어지지 않는 경우는 없으나 만약 인형이 없는 곳에서 크레인을 작동시키는 경우에는 
아무런 일도 일어나지 않습니다. 또한 바구니는 모든 인형이 들어갈 수 있을 만큼 충분히 크다고 가정합니다. 
(그림에서는 화면표시 제약으로 5칸만으로 표현하였음)

게임 화면의 격자의 상태가 담긴 2차원 배열 board와 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves가 
매개변수로 주어질 때, 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return 하도록 solution 함수를 완성해주세요.

입출력 예
board
[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves
[1,5,3,5,1,2,1,4]
result
4
'''
def solution(board, moves):
  count = 0
  bb = []
  answer_list = ""
  bb = list(zip(*board) )  # built-in 2D-list-transpose
  for i in range(len(bb)) : bb[i] = list(bb[i][::-1] ) # order reverse, then change to stack
  for i in range(len(bb)) : 
    try : bb[i] = bb[i][0:bb[i].index(0)]  # 0 지우기
    except : pass
  print(bb, "/", moves)

  for move in moves :
    try : 
      answer_list = answer_list + str(bb[move-1].pop() )
      if answer_list[-2]==answer_list[-1] : 
        answer_list = answer_list[0:-2]
        count += 2
    except : pass





  # temporary block to see the answer_list after moves
  bb = []
  answer_list = ""
  bb = list(zip(*board) )  # built-in 2D-list-transpose
  for i in range(len(bb)) : bb[i] = list(bb[i][::-1] ) # 순서 바꾼 다음에, 리스트로 변경하기
  for i in range(len(bb)) : 
    try : bb[i] = bb[i][0:bb[i].index(0)]  # 0 지우기
    except : pass
  for move in moves :
    try : 
      answer_list = answer_list + str(bb[move-1].pop() )
    except : pass
  print(answer_list)
  # END of temporary block
  



  return count
#
board, moves = 	[[0,0,0,0,0], [0,0,1,0,3], [0,2,5,0,1], [4,2,4,4,2], [3,5,1,3,1]], [1,5,3,5,1,2,1,4]
board, moves = 	[[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]], [1,1,2,2,3,3,4,4,5]
solution(board, moves)



# Solution by other

# END
