import collections
import string


def main():
    d = collections.deque(string.ascii_lowercase)

    print(str(len(d)))
    print(d) #pop() , popleft() . append() , appendleft() , rotate()
    


    



if __name__ == "__main__":
    main()