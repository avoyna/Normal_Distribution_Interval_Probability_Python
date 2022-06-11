### Computes probability of being between 2 values with normal disctribution given mean and deviation

import math

import scipy.stats


def norm_pdf(x, mean, std_dev):
    var = float(std_dev)**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

def norm_cdf(mean, std_dev, x_left, x_right, width=0.000001):
    CDF = 0
 
    the_range = int((x_right - x_left) / width) + 1
    for i in range(the_range):
        x = x_left + i * width
        y =norm_pdf(x, mean, std_dev)
        panel = y * width 
        CDF += panel
       
    return CDF

	
print("Computes probability of being between 2 values with normal disctributiongiven mean and deviation")
i1 = input("Input mean Mu ")
i2 = input("Input mean Standard Deviation Sigma ")
bi1 = input("Input beginning of interval ")
ei1 = input("Input end of interval ")
mu = float(i1)
sigma = float(i2)
interval_begin = float(bi1)
interval_end = float(ei1)


print("\n Calculation using Math")
#probability_lower_limit = norm_pdf(interval_begin, mu, sigma)
#print(probability_lower_limit)
#probability_upper_limit = norm_pdf(interval_end, mu, sigma)
#print(probability_upper_limit)
probability_result = norm_cdf(mu, sigma, interval_begin, interval_end)

print(probability_result)

print("\n Calculation using Scipy")
probability_lower_limit_scipy = scipy.stats.norm(loc=mu, scale=sigma).cdf(interval_begin)
#print(probability_lower_limit_scipy)
probability_upper_limit_scipy = scipy.stats.norm(loc=mu, scale=sigma).cdf(interval_end)
#print(probability_upper_limit_scipy)
probability_result_scipy = probability_upper_limit_scipy - probability_lower_limit_scipy
print(probability_result_scipy)