
#linear.py
def linear_search(data,key):
    location=-1
    for index,value in enumerate(data):
        if value==key:
            location=index
            break
    return location
import numpy as np
def main():
    data=np.random.randint(1,101,20)
    print(data)
    k=int(input('Enter a number you want to locate in the array: '))
    loc=linear_search(data,k)
    if loc==-1:
        print(f'Key {k} is not found.')
    else:
        print(F'Key {k} is found at location {loc}.')

if __name__=='__main__':
              main()
