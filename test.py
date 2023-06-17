# O(Log(N)

# push - отправлять
# commit - коммит
# add - добовляет
# init - Инициализация

# 1 3 4 2

def palindrome():
    """ palindrome function """
    string_symbols = input().strip()
    return string_symbols == string_symbols[::-1]


if __name__ == "__main__":
    print(palindrome())

