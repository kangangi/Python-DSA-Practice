"""
For the use of inheritance we will develop a hierarchy of classes for iterating numeric progressions
A numeric progression is a sequence of numbers, where each number depends on one or more of the previous numbers. 
For example, an arithmetic progression determines the next number by adding a fixed constant to the previous value, 
and a geometric progression determines the next number by multiplying the previous value by a fixed constant
"""

class Progression:
    """
    Iterator producing a generic progression.
    Default iterartor produces the whole numbers 0, 1, 2,...
    """

    def __init__(self, start=0):
        """
        Initialize current to the first value of the progressiom
        """
        self._current = start

    def _advance(self):
        """
        Updates self._current to a new value
        By convention, if current is set ot None, this designates the end of a finite progression
        """

        self._current += 1

    def __next__(self):
        """Return the next element or else raise StopIteration error"""

        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current  #record current value to return
            self._advance()  # advance to prepare for next time
            return answer  # return the answer
        
    def __iter__(self):
        """By convention, an iterator must return itself as an iterator"""
        return self


    def print_progression(self, n):
        """Print next n values of the progression""" 

        x = ([next(self) for i in range(n)])
        print(x)

            


class ArithmeticProgression(Progression):
    """Iterator producing an arithmentic pogression"""

    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment


    def _advance(self):
        self._current += self._increment


class GeometricProgression(Progression):
    """Iterator producing a geometric progression"""

    def __init__(self, base=2, start=1):
        super().__init__(start)
        self._base = base

    def _advance(self):
        self._current *= self._base


class FibonacciProgression(Progression):
    """Iterator producing a generalized Fibonacci progression."""

    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first

    
    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current


if __name__ == '__main__':
    print('Default progression:')
    Progression().print_progression(10)

    print("Arithmetic Progression with increment -5:")
    ArithmeticProgression(-5).print_progression(10)

    print("Arithmetic Progression with increment 5 and start 2:")
    ArithmeticProgression(5, 2).print_progression(10)

    print("Geometric Progression with default base:")
    GeometricProgression().print_progression(10)

    print("Geometric Progression with base 3:")
    GeometricProgression(3).print_progression(10)

    print("Fibonacci progression with default start values")
    FibonacciProgression().print_progression(10)

    print("Fibonacci progression with start values 4 and 6")
    FibonacciProgression(4, 6).print_progression(10)


    