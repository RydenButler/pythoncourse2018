## Fill in the following methods for the class 'Clock'

class Clock(object):
    def __init__(self, hour, minutes):
        self.minutes = minutes
        self.hour = hour

    @classmethod
    def at(cls, hour, minutes=0):
        return cls(hour, minutes)

    ## Print the time
    def __str__(self):
    	return "%02d:%02d" % (self.hour, self.minutes)
    
    ## Add time
    ## Don't return anything
    def __add__(self,minutes):
    	self.minutes += minutes
    	while self.minutes >= 60:
    		self.hour += 1
    		self.minutes -= 60
    	while self.hour >= 24:
    		self.hour -= 24
    
    ## Subtract time
    ## Don't return anything
    def __sub__(self,minutes):
    	self.minutes -= minutes
    	while self.minutes < 0:
    		self.hour -= 1
    		self.minutes += 60
    	while self.hour < 0:
    		self.hour += 24
    
    ## Are two times equal?
    def __eq__(self, other):
    	if self.minutes == other.minutes and self.hour == other.hour:
    		return True
    	else:
    		return False
    
    ## Are two times not equal?
    def __ne__(self, other):
    	return not self.__eq__(other)
