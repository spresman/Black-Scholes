# Black-Scholes
A class to model Black-Scholes.

The Black-Scholes model is a differential equation that simulates the dynamics of valuations of stock options. It was published in 1973 and determines the "fair" value 
of options and other financial derivatives. 

The option pricing formula for a put can be written as:

![](https://latex.codecogs.com/png.image?\dpi{110}\bg{black}P&space;=&space;-S_{0}^{}N(-d_{1}^{})-Xe^{-rt}N(d_{2}))

The option pricing formula for a call can be written as:

![](https://latex.codecogs.com/png.image?\dpi{110}\bg{black}C&space;=&space;S_{0}^{}N(d_{1}^{})-Xe^{-rt}N(d_{2}))

where

![](https://latex.codecogs.com/png.image?\dpi{110}\bg{black}d_{1}&space;=&space;\frac{ln(S_{0}/X)&space;&plus;&space;(r&space;&plus;&space;\sigma&space;^2/2)\tau&space;}{\sigma&space;\sqrt{\tau&space;}})


![](https://latex.codecogs.com/png.image?\dpi{110}\bg{black}d_{2}&space;=&space;d_{1}-\sigma&space;\sqrt{\tau&space;})

The variables 
![](https://latex.codecogs.com/png.image?\dpi{110}\bg{black}S_{0},&space;X,&space;r,&space;\tau&space;)
stand for the current price of the stock, the option's strike price, annualized risk-free interest rate, and time to maturity, respectively.

![](https://latex.codecogs.com/png.image?\dpi{110}\bg{black}N()) stands for the cumulative distribution function of standard normal distribution.

The five Greek letters are derived from the equations of the model, and describe different attributes of the underlying option.

Delta, the rate of change of the value of the option with respect to only the changes in the stock price, can be described as:

![](https://latex.codecogs.com/png.image?\dpi{110}\bg{black}\Delta&space;=&space;\frac{\partial&space;V}{\partial&space;S_{0}}&space;)

Theta, the rate of change of the value of the option with respect to only the passage of time, can be described as:

![](https://latex.codecogs.com/png.image?\dpi{110}\bg{black}\Theta&space;&space;=&space;\frac{\partial&space;V}{\partial&space;\tau&space;}&space;)

Gamma, the rate of change in the delta with respect to only the changes in the stock price, can be described as:

![](https://latex.codecogs.com/png.image?\dpi{110}\bg{black}\Gamma&space;&space;&space;=&space;\frac{\partial&space;\Delta&space;}{\partial&space;S_{0}&space;}&space;)

Vega, the rate of change of the value of the option with respect to only the volatility of the stock, can be described as:

![](https://latex.codecogs.com/png.image?\dpi{110}\bg{black}\nu&space;&space;&space;&space;=&space;\frac{\partial&space;V&space;}{\partial&space;\sigma&space;&space;}&space;)

And finally rho, the rate of change of the value of the option with respect to only the interest rate, can be described as:

![](https://latex.codecogs.com/png.image?\dpi{110}\bg{black}\rho&space;&space;&space;&space;&space;=&space;\frac{\partial&space;V&space;}{\partial&space;r&space;&space;}&space;)
