'''
https://school.programmers.co.kr/learn/courses/30/lessons/81301

Numeric strings and English words
Neo and Frodo are playing with numbers. When Neo hands Frodo a number, she hands him a card 
with some digits changed to English words, and Frodo change it back to the original number.

숫자 문자열과 영단어
네오와 프로도가 숫자놀이를 하고 있습니다. 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 
영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.

다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

1478 → "one4seveneight"
234567 → "23four5six7"
10203 → "1zerotwozero3"
이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. 
s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.

참고로 각 숫자에 대응되는 영단어는 다음 표와 같습니다.

숫자	영단어
0	zero
1	one
2	two
3	three
4	four
5	five
6	six
7	seven
8	eight
9	nine

제한사항
1 ≤ s의 길이 ≤ 50
s가 "zero" 또는 "0"으로 시작하는 경우는 주어지지 않습니다.
return 값이 1 이상 2,000,000,000 이하의 정수가 되는 올바른 입력만 s로 주어집니다.

입출력 예
s		                result
"one4seveneight"  	1478
"23four5six7"	      234567
"2three45sixseven"	234567
"123"		            123
'''
def solution(s):
    answer = s.replace("zero","0") \
              .replace("one","1") \
              .replace("two","2") \
              .replace("three","3") \
              .replace("four","4") \
              .replace("five","5") \
              .replace("six","6") \
              .replace("seven","7") \
              .replace("eight","8") \
              .replace("nine","9")
    return int(answer)
s = "one4seveneight"
solution(s)

# Solution by other
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
# END

