#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 17:24:55 2020

@author: vanish
"""

#%%
class UndergroundSystem:

    def __init__(self):
        self.cust_data = dict()
        self.station_data = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.cust_data:
            self.cust_data[id] = (stationName, t)
            
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        time_taken = t - self.cust_data[id][1]
        key = self.cust_data[id][0] + stationName
        if str(key) not in self.station_data:
            self.station_data[key] = [time_taken, 0]
        else:
            self.station_data[key][0] += time_taken
        
        self.station_data[key][1] += 1 
        del self.cust_data[id]
               
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.station_data[startStation + endStation][0] / self.station_data[startStation + endStation][1]

#%%
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
obj = UndergroundSystem()
obj.checkIn(1, "Mumbai", 2)
obj.checkIn(2, "Thane", 3)
obj.checkOut(1, "Thane", 4)
obj.checkIn(3, "Mumbai", 4)
obj.checkOut(3, "Thane", 7)
print (obj.getAverageTime("Mumbai", "Thane"))