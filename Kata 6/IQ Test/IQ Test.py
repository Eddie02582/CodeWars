'''

Assert.AreEqual(3, IQ.Test("2 4 7 8 10"));
Assert.AreEqual(1, IQ.Test("1 2 2"));
'''



def iq_test(numbers):
    reslut=[ int(i)%2 for i in numbers.split(' ')]
    return array.index(0)+1 if reslut.count(0)==1 else array.index(1)+1       


def iq_test2(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]
    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1
   
def iq_test(numbers):
    array=[int(x)%2 for x in numbers.split(' ')]
    return array.index(1)+1 if sum(array)==1 else array.index(0)+1   
  

print iq_test2("2 4 7 8 10")