# 要求用戶輸入一個單字
word = input("請輸入一個英文單字：")

# 使用迴圈反轉字串
reversed_word = ''
for char in word:
    reversed_word = char + reversed_word

# 輸出反轉後的字串
print("反轉字串：", reversed_word)
