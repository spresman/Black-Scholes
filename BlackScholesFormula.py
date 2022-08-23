import numpy as np
from statistics import NormalDist


class BSform:
    """
    A class to model the Black Scholes Formula.

    Attributes
    ----------
    St : double
        current price of stock
    K : double
        the strike price of the option
    r : double
        the annual risk-free interest rate
    o : double
        the annual standard deviation of stock's returns
    t : double
        the time until maturity in years
    details : char
        'C': call and 'P': put


    Methods
    -------
    d1()
        Calculates and returns d1 for use in the price() method
    d2()
        Calculates and returns d2 for use in the price() method
    delta()
        Calculates and returns the delta of the option
    gamma()
        Calculates and returns the gamma of the option
    vega()
        Calculates and returns the vega of the option
    theta()
        Calculates and returns the theta of the option
    rho()
        Calculates and returns the rho of the option
    price()
        Calculates and returns the price of the option

    """
    def __init__(self, St, K, r, o, t, details):

        """
        St : double
            current price of stock
        K : double
            the strike price of the option
        r : double
            the annual risk-free interest rate
        o : double
            standard deviation of stock's returns
        t : double
            the time until maturity in years
        details : char
            'C': call and 'P': put
        """

        self.t = t
        self.r = r
        self.St = St
        self.o = o
        self.K = K
        self.details = details

    def d1(self):
        return (1 / (self.o * np.sqrt(self.t))) * \
        (np.log(self.St/self.K) + (self.r + self.o**2 / 2) * self.t)

    def d2(self):
        return self.d1() - self.o * np.sqrt(self.t)

    # Greeks
    def delta(self):

        n = NormalDist().cdf(self.d1())

        match self.details:
            case 'P':
                return n-1
            case 'C':
                return n

    def gamma(self):
        return NormalDist().cdf(self.d1())/(self.St * self.o * np.sqrt(self.t))

    def vega(self):
        return NormalDist().cdf(self.d1()) * self.St * np.sqrt(self.t)

    def theta(self):

        n = -NormalDist().cdf(self.d1()) * self.St * self.o/(2 * np.sqrt(self.t))

        match self.details:
            case 'P':
                return n - NormalDist().cdf(-self.d2()) * self.r * self.K * np.exp(-self.r * self.t)
            case 'C':
                return n + NormalDist().cdf(self.d2()) * self.r * self.K * np.exp(-self.r * self.t)

    def rho(self):

        k = self.K * self.t * np.exp(-self.r * self.t)

        match self.details:
            case 'P':
                return -k * NormalDist().cdf(-self.d2())
            case 'C':
                return k * NormalDist().cdf(self.d2())

    # Price of particular option
    def price(self):
        match self.details:
            case 'P':
                return NormalDist().cdf(-self.d2()) * self.K * np.exp(-self.r * self.t) - NormalDist().cdf(-self.d1()) * self.St

            case 'C':

                return NormalDist().cdf(self.d1()) * self.St - NormalDist().cdf(self.d2()) * self.K * np.exp(-self.r * self.t)


if __name__ == "__main__":

    K = 100 * 0.9
    r = 0.02
    t = 3
    o = 0.2
    St = 100
    print(BSform(St, K, r, o, t, 'P').price())





