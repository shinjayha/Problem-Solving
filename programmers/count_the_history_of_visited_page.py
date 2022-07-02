'''
Count the most visted page from "s".
'B' = backward
'F' = Forward
#
[2021 대학모의고사 하반기] 가장 많이 방문한 페이지_lv1
웹 페이지를 이동할 때, 뒤로 가기 버튼과 앞으로 가기 버튼을 이용하면 
방문했던 페이지를 쉽게 이동할 수 있습니다. 
이동한 페이지 번호와 뒤로 가기 또는 앞으로 가기 버튼을 누른 기록이 주어졌을 때, 
가장 많이 방문한 페이지를 몇 번 방문했는지 알아보고자 합니다.
기록은 하나의 문자열로 주어집니다. 페이지 번호는 자연수로, 
뒤로 가기 버튼은 'B'로, 앞으로 가기 버튼은 'F'로 나타냅니다. 
각 이동 명령은 띄어쓰기 한 칸으로 구분됩니다. 다음은 이동 기록의 예시입니다.
"1 2 3 4 B B 42 B F F"
1. 1번 페이지로 이동합니다.
2. 2번 페이지로 이동합니다.
3. 3번 페이지로 이동합니다.
4. 4번 페이지로 이동합니다.
5. 뒤로 가기를 이용해 3번 페이지로 이동합니다.
6. 뒤로 가기를 이용해 2번 페이지로 이동합니다.
7. 42번 페이지로 이동합니다.
8. 뒤로 가기를 이용해 2번 페이지로 이동합니다.
9. 앞으로 가기를 이용해 42번 페이지로 이동합니다.
10. 이동할 페이지가 없기 때문에 앞으로 가기 명령이 무시됩니다.
뒤로 가기를 이용해 이전 페이지로 돌아간 후, 
앞으로 가기 버튼을 누르지 않고 페이지 번호를 지정하여 이동하면 
그 순간이동한 페이지가 맨 앞 페이지가 됩니다. 
즉, 위 예시에서 7번째 명령인 '42번 페이지로 이동'을 실행하면, 
페이지 나열 순서는 (1 - 2 - 42)가 되며 42번 페이지가 맨 앞 페이지가 됩니다.
뒤로 가기 또는 앞으로 가기 명령 시, 이동할 페이지가 없다면 명령이 무시됩니다. 
위 예시에서 마지막 명령인 'F'는 현재 보고 있는 페이지(=42번 페이지)가 맨 앞 페이지이므로, 
더 이상 앞으로 이동할 페이지가 없어 무시됩니다.
'''
s = "1 2 3 4 B B 42 B F F"
def solution(s) :
  s = s.split()
  visit_history = []
  back_history = []
  back_index = -1
  for val in s :
    if ((val!='B') & (val!='F')) :
      visit_history.append(val)
      back_history = visit_history.copy()
      back_index = len(back_history)-1
      print( val, visit_history, back_history, back_index )
    elif ((val=="B")) :
      if(back_index>0) :
        back_index -= 1
        visit_history.append(back_history[back_index])
        print( val, visit_history, back_history, back_index )
    elif ((val=="F")) :
      if(back_index<=(len(back_history)-2)) :
        back_index += 1
        visit_history.append(back_history[back_index])
        print( val, visit_history, back_history, back_index )
  print("visit_history: ", visit_history)
  maxcount = 0
  for ii in visit_history :
    maxcount = visit_history.count(ii) if visit_history.count(ii)>maxcount else maxcount
  answer = maxcount
  return answer
solution(s)
