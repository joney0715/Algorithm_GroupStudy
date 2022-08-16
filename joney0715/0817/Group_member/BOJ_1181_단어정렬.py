
N = int(input())

words = []
for _ in range(N):
    word  = input()
    l = len(word)
    # 단어 길이와 단어를 리스트에 저장
    words.append((l,word))

# 중복 제거
words = set(words)

# 단어 길이로 정렬
# 길이가 같으면 사전순으로 정렬
words = sorted(words, key = lambda words : (words[0], words[1]))

for word in words:
    print(word[1])

