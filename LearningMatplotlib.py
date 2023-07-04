#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
#-----------------------------------Matplotlib------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------
#----------------------------------LinePlots and Scatter Plots----------------------------------------------------
#------------------------------------------------------------------------------------------------------------------

'''
import matplotlib.pyplot as plt

year=[1997,2001,2005,2009]
population=[5.6,6.1,6.8,7.3]

#Line Plot
plt.plot(year,population)
plt.show()

#Scatter Plot
plt.scatter(year,population)
plt.show()
'''

#------------------------------------------------------------------------------------------------------------------
#-----------------------------------Histograms----------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------

'''
To build a histogram for these values,
you can divide the line into equal chunks, called bins.
Suppose we go for three bins that each have a width of 2.
Next, we count how many data points sit inside each bin.
There's 4 variables in the first bin,
6 variables in the second bin, and 2 in the third bin.
Finally, you draw a bar for each bin.
The height of the bar corresponds to the number of
data points that fall in this bin.
Result is a histogram, which gives us a nice overview
on how to develop values or distribute it.
Most values are in the middle, and there are more values below
two than there are values above four.

hist(x, bins=None, range=None, density=None, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, normed=None, *, data=None, **kwargs)

help(plt.hist)  for details
'''

'''
import matplotlib.pyplot as plt

val=[10,13,15,19,17,15,25]
plt.hist(val,bins=10)
plt.show()
'''

#-------------------------------------Customization-----------------------------------------------------------------------------

'''
import matplotlib.pyplot as plt

year=[1950,1960,1970,1980,1990,2000,2010,2020,2030]
population=[1.5,1.8,2.1,3.3,4.9,5.8,6.8,7.6,8.2]
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("World Population")
plt.yticks([0,2,4,6,8,10],['0B','2B','4B','6B','8B','10B'])
plt.fill_between(year,population,0,color='blue')
plt.show()
'''







