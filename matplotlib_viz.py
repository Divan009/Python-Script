# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 16:46:45 2018

@author: lenovo
"""

import matplotlib.pyplot as plt
from collections import Counter

#Line
# =============================================================================
# years	=	[1950,	1960,	1970,	1980,	1990,	2000,	2010] 
# gdp	=	[300.2,	543.3,	1075.9,	2862.5,	5979.6,	10289.7,	14958.3]
# 
# plt.plot(years,gdp,color='green', marker='o', linestyle='solid')
# plt.title("Nominal GDP")
# plt.ylabel("Billions of $")
# plt.show()
# 
# =============================================================================


#BARCHARTS
# =============================================================================
# movies	=	["Annie	Hall",	"Ben-Hur",	"Casablanca",	"Gandhi",	"West	Side	Story"] 
# num_oscars	=	[5,	11,	3,	8,	10]
# 
# #	bars	are by	default width 0.8, so	we'll	add	 0.1 to the left coordinates
# #	so	that	each	bar	is	centered 
# xs = [i+0.1 for i,_ in enumerate(movies)]
# plt.bar(xs, num_oscars)
# plt.ylabel("# of Academy Awards")
# plt.title("My movies")
# 
# #label x-axis with movies names at center bar
# plt.xticks([i+0.5 for i,_ in enumerate(movies)], movies)
# plt.show()
# =============================================================================

# =============================================================================
# grades = [83,95,91,87,70,0,85,82,100,67,73,77,0] 
# decile = lambda grade: grade // 10 * 10  #83//10*10<- 80
# #{80:4,90:2,70:3,0:2,100:1,60:1}
# histogram = Counter(decile(grade) for grade in grades) 
# #shifts each bar toleft by 4
# # =============================================================================
# # plt.bar([x-4 for x in histogram.keys()],
# #          histogram.values(), #gives bar its correct height
# #          8) #each bar gets a width of 8
# # =============================================================================
# 
# plt.bar(histogram.keys(),
#          histogram.values(), #gives bar its correct height
#          8) 
# plt.axis([-5,105,0,5])
# plt.xticks([10*i for i in range(11)])
# plt.xlabel("Decile")
# plt.ylabel("# of Students")
# plt.title("Distro of Exam Grade")
# plt.show()
# 
# =============================================================================
#Theres a HUGE DIFFERENCE
mentions	=	[500,	505] 
years	=	[2013,	2014]

plt.bar(years, mentions)
plt.xticks(years)
plt.ylabel("The num of time someone mentions Data Sc.")
#plt.ticklabel_format(useOffset = False)
#plt.axis([2012.5,2014.5, 499, 506])
plt.axis([2012.5,2014.5, 0, 550])















































