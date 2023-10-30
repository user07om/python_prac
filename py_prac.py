class Iteration_is:
    def __init__(self, max_val):
        self.max_val = max_val
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.max_val:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration

class Fibo:
    def __init__(self, num):
        self.num = num
        self.prev, self.next = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.prev < self.num:
            self.prev += 1
            self.prev, self.next = self.next, self.prev + self.next
            return self.prev
        else:
            raise StopIteration

def odd_is(x):
    if x%2==0:
        return False
    else: return True

def is_upper(x):
    if x.isupper():
        return True
    else: return False

def Grades_are(n):
    if n >= 90:
        return "A"
    elif (n>=80 and n<90):
        return "B"
    elif (n>=70 and n<80):
        return "C"
    elif (n>=65 and n<70):
        return "C"
    return "Failed"

def main():
    #use any() and all() to test the list_one
    #CHECK IS ANY STRING IS EMPYT THE LIST
    if any(not s for s in string_is): print("some strings are empty in the list")
    else: print("soemthing went wrong")

    #CHECK IF ANY WORD IS PALINDROME IT THE FOLLOWING OWRD
    if any(pal[::-1] == pal for pal in palindrome_words):
        print("the word is palindrome")

    #iterables
    i = iter(numbers)
    #print(next(i))

    my_iter = Iteration_is(5)
    for x in my_iter:
        pass
        # print(x)


if __name__=="__main__":
    # main()
    fibo_is = Fibo(500)
    numbers = [x for x in fibo_is]; print(numbers)
    grades = [85, 92, 78, 95, 88, 76, 90, 82, 70, 89]
    string_is = ["hello", "world", "", "howru"]
    palindrome_words = ["racecar", "python" "", "MADAM", "LOST_IT"]
    char_are = "abdwKJEHnfkdBGKDJ"

    odd_numbers = list(filter(lambda x: x%2!=0, numbers)); print(odd_numbers)
    check_upp = list(filter(lambda x: x.isupper(), palindrome_words)); print(check_upp)
    square_up = list(map(lambda x: 2**x, numbers[:4])); print(square_up)
    letter_grades = list(map(Grades_are, grades)); print(letter_grades)


