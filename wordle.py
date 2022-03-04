# %%
import random
file = open('ukenglish.txt',encoding='ISO-8859-15')
words = file.read().split('\n')
all_words = words.copy()
print('Enter the size of words ')
word_size = int(input())
no_of_tries = 6

words = [word for word in words if len(word) == word_size ]
print('Current possible number of words is ' + str(len(words)))

target_word = random.choice(words)
# print(target_word)
# %%
flag = 0
guess_word=''
result_graphic=[]

smilies = {1:'\U0001F600',0:'\U0001F910',-1:'\U0001F61F'}
def print_status_graphic(lines,emoji_map={1:'\U0001F7E9',0:'\U0001F7E8',-1:'\U0001F7E5'}):
    # print(lines)
    for line in lines:
        line = [ emoji_map[i] for i in line ]
        print(''.join(line))



for attempt in range(no_of_tries):
    
    print('Attempt :'+str(attempt+1))

    guess_word=''
    while True :
        guess_word = input('Enter your guess ').strip()
        if len(guess_word) != word_size:
           print('Words of size {} only'.format(word_size))
           continue
        elif guess_word not in all_words :
            print('Word not found in our dictionary')
            continue
        break
    
    

    if guess_word == target_word :
        print('Congratulations !! you found the word in {} attempts'.format(attempt+1))
        result_graphic.append([ 1 for i in range(word_size)])
        flag = 1
        break
    
    guess_word_status = [None] * word_size

    for i in range(word_size):
        letter = guess_word[i]
        if letter == target_word[i]:
            guess_word_status[i] = 1
            words = [word for word in words if word[i] == letter]
        elif letter in target_word:
            guess_word_status[i] = 0
            words = [word for word in words if word[i] != letter]
        else:
            guess_word_status[i] = -1
            words = [word for word in words if letter not in word]

    result_graphic.append(guess_word_status)
    print_status_graphic([guess_word_status])
    print('you have narrowed it down to {} words'.format(len(words)))

if flag == 0 :
    print("You failed !!! \n word was "+target_word)
else :
    print_status_graphic(result_graphic)
    # print_status_graphic(result_graphic,smilies)



