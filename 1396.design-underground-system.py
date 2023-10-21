#
# @lc app=leetcode id=1396 lang=python3
#
# [1396] Design Underground System
#

# @lc code=start
class UndergroundSystem:
    # Plan:
    # Store check_in data with hashmap, key: id, value: (stationName, t)
    # To make sure that customers are checked in only once, we can check if id is in hashmap

    # Stre check_out data in another hashmap, key: (startStation, endStation), value: (totalTime, count)
    # To make sure that customers are correctly checked out, we can delete the check_in data from hashmap

    # To get average time, we can get the total time and count from check_out hashmap, and divide them

    def __init__(self):
        self.check_in = {}
        self.check_out = {}
    

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        key = (self.check_in[id][0], stationName)
        if key not in self.check_out:
            self.check_out[key] = (t - self.check_in[id][1], 1)
        else:
            time = self.check_out[key][0] + (t - self.check_in[id][1])
            count = self.check_out[key][1] + 1
            self.check_out[key] = (time, count)

        del self.check_in[id]    
  

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time = self.check_out[(startStation, endStation)][0]
        count = self.check_out[(startStation, endStation)][1]
        return total_time / count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.check_in(id,stationName,t)
# obj.check_out(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
# @lc code=end

