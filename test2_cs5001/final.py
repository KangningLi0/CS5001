import Stack

PRIZE_INDEX = {"h": 1.2, "p": 0.9, "e": 0.7}
ATTRIBUTE = {"hardcover": "h", "paperback": "p", "electronic": "e"}

class Book:
    def __init__(self, title: str, author: str, avai: str, cost: float):
        # check whether title is valid
        if len(title) == 0:
            raise ValueError
        else:
            self.title = title
        
        # check whether author is valid
        if len(author) == 0:
            raise ValueError
        else:
            self.author = author

        # check whether cost is valid
        self.avai_attribute = avai
        if cost < 0 or cost > 200:
            raise ValueError
        else:
            self.base_cost = cost
    
    def __eq__(self, another_book) -> bool:
        # if author and title is equal then check equal
        if self.author.lower() == another_book.get_author().lower() and \
        self.title.lower() == another_book.get_title().lower():
            return True
        else:
            return False
    
    def __str__(self):
        return self.title.upper() + ":" + self.author.upper() + ":" + str(self.base_cost)
    
    def get_base_cost(self) -> float:
        return self.base_cost

    def get_title(self) -> str:
        return self.title
    
    def get_author(self) -> str:
        return self.author
        
    def get_price_for(self, quantity: int, kind: str) -> float:
        # calculate price with quantity and attribute type
        if quantity < 0 or quantity > 50:
            raise ValueError
        else:
            if kind.lower() not in self.avai_attribute.lower():
                return 0
            format_index = PRIZE_INDEX[kind.lower()]
            return self.base_cost * quantity * format_index

    def is_available_as(self, key: str) -> bool:
        # check whether key in the attribute
        key = key.lower()
        if key in ATTRIBUTE:
            key = ATTRIBUTE[key]
        
        if key in self.avai_attribute.lower():
            return True
        else:
            return False

def make_upper(word: str) -> str:
    return word.upper()

def make_lower(word: str) -> str:
    return word.lower()

def capitalize(word: str) -> str:
    # make the first char of string capitalized, other lowercase
    char_list = list(word)
    for i in range(len(char_list)):
        if i == 0:
            char_list[i] = char_list[i].upper()
        else:
            char_list[i] = char_list[i].lower()
    return "".join(char_list)

def apply_to_all(function, _lst: list):
    # apply transform function for all string in the list
    len_list = len(_lst)
    for i in range(len_list):
        _lst[i] = function(_lst[i])

def write_scores(file_name: str, lst_scores: list, lst_names: list):
    # write name and score for the list in the file
    len_list = len(lst_names)
    with open(file_name, "w") as file:
        for i in range(len_list):
            file.write(lst_names[i] + " " + str(lst_scores[i]) + "\n")

def square_series(num: int, _lst: list):
    # recursively append square in the front of list
    if num > 0:
        _lst.insert(0, num ** 2)
        square_series(num - 1, _lst)

def is_missing(a_list: list) -> int:
    n = len(a_list) + 1 # O(1)
    sum_of_range = n * (n + 1) / 2 # O(1)
    sum_of_list = sum(a_list) # O(n)
    miss_number = sum_of_range - sum_of_list # O(1)
    return int(miss_number)

def equal_stacks(stack1, stack2):
    # check whether two stack is equal
    while not stack1.is_empty() and not stack2.is_empty():
        if stack1.pop() != stack2.pop():
            return False
    if stack1.is_empty() and stack2.is_empty():
        return True
    else:
        return False