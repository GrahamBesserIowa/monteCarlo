import numpy as np
import matplotlib.pyplot as plt1


class Pricing:
    import numpy as np
    import matplotlib.pyplot as plt

    def priceSim(S, T, r, q, sigma, steps, N):
        """
        Inputs
        #S = Current stock Price
        #K = Strike Price
        #T = Time to maturity 1 year = 1, 1 months = 1/12
        #r = risk free interest rate
        #q = dividend yield
        # sigma = volatility

        Output
        # [steps,N] Matrix of asset paths
        """
        dt = T / steps
        # S_{T} = ln(S_{0})+\int_{0}^T(\mu-\frac{\sigma^2}{2})dt+\int_{0}^T \sigma dW(t)
        ST = np.log(S) + np.cumsum(((r - q - sigma ** 2 / 2) * dt + sigma * np.sqrt(dt) * np.random.normal(size=(steps, N))), axis=0)

        return np.exp(ST)

    S = 100  # stock price S_{0}
    K = 110  # strike
    T = 1 / 2  # time to maturity
    r = 0.05  # risk free risk in annual %
    q = 0.02  # annual dividend rate
    sigma = 0.25  # annual volatility in %
    steps = 100  # time steps
    N = 1000  # number of trials

    paths = priceSim(S, T, r, q, sigma, steps, N)

    plt1.plot(paths)
    plt1.xlabel("Time Increments")
    plt1.ylabel("Stock Price")
    plt1.title("Pricing Sim")

    plt1.show()