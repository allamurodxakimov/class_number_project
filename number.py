class Number:
    def __init__(self, value: int):
        self.value = value

    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        return self.value

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        return self.value % 2 == 1

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        return not self.is_odd()

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        for i in range(2, self.value):
            if self.value % i:
                return False
        return True

    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        divisors = []
        for i in range(1, self.value + 1):
            if self.value % i == 0:
                divisors.append(i)
        return divisors

    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        c=0
        while self.value>0:
            a=self.value%10
            self.value //=10
            c+=1
        return c
    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        sum = 0
        while self.value>0:
            sum += self.value%10
            self.value //=10
        return sum

    def get_reverse(self):
        """
        Returns the number in reverse.
        returns: int
        """
        newvalue = self.value
        sum = 0
        while abs(self.value)>0:
            a = abs(self.value)%10
            sum = sum*10 + a
            self.value=abs(self.value)//10
        return sum if newvalue>=0 else -1*sum

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
        s = str(self.value)
        return s==s[-1::-1]

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        return  [int(i) for i in str(self.value) if i.isdigit()]

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        ls = [int(i) for i in str(self.value) if i.isdigit()]
        return max(ls)

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        minlist = [int(i) for i in str(self.value) if i.isdigit()]
        return min(minlist)

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        averagelist = sum(int(i) for i in str(self.value) if i.isdigit())
        return averagelist/len(str(self.value)) if len(str(self.value))!=0 else "Nomer nolga teng bo'lmasin"

    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        12345
        medianalist = [int(i) for i in str(self.value) if i.isdigit()]
        medianalist.sort()
        a = len(medianalist)
        if len(medianalist)%2==0:
            return (medianalist[a//2-1]+medianalist[a//2])/2
        else:
            return float(medianalist[a//2])
    def get_range(self):
        """
        Returns the range of all the digits in the number.

        returns: list
        """
        if int(str(self.value)[0])<=int(str(self.value)[-1]):
            rangelist = list(range(int(str(self.value)[0]), int(str(self.value)[-1]) + 1))
        else:
            rangelist = list(range(int(str(self.value)[-1]), int(str(self.value)[0]) + 1))
        return rangelist
    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        dic={}
        string = str(self.value)
        for i in string:
            lenth = string.count(i)
            dic[int(i)]=lenth
        return dic
