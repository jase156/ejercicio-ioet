from core.exception import FormatTimeException

class Time(object):
    #def convert_to_time(self,str_time):
    def get_hours(self, start, end):
        try:
            h_start, m_start = start.split(':')
            h_end, m_end = end.split(':')
            total_min = ((int(h_end)*60)+int(m_end)) - ((int(h_start)*60)+int(m_start))
            return self.convert_to_time(total_min)
        except Exception as e:
            raise FormatTimeException()
    
    def convert_to_time(self, minute):
        h = minute // 60
        m = minute % 60
        return h, m
    
    def greater_than(self, time1, time2):
        h_time1, m_time1 = time1.split(':')
        h_time2, m_time2 = time2.split(':')
        time1_m = (int(h_time1)*60)+int(m_time1)
        time2_m = (int(h_time2)*60)+int(m_time2)
        if time1_m > time2_m:
            return True
        else:
            return False
        
    def greater_or_equal_than(self, time1, time2):
        h_time1, m_time1 = time1.split(':')
        h_time2, m_time2 = time2.split(':')
        time1_m = (int(h_time1)*60)+int(m_time1)
        time2_m = (int(h_time2)*60)+int(m_time2)
        if time1_m >= time2_m:
            return True
        else:
            return False
    
    def smaller_or_equal_than(self, time1, time2):
        h_time1, m_time1 = time1.split(':')
        h_time2, m_time2 = time2.split(':')
        time1_m = (int(h_time1)*60)+int(m_time1)
        time2_m = (int(h_time2)*60)+int(m_time2)
        if time1_m <= time2_m:
            return True
        else:
            return False
    
    def smaller_than(self, time1, time2):
        h_time1, m_time1 = time1.split(':')
        h_time2, m_time2 = time2.split(':')
        time1_m = (int(h_time1)*60)+int(m_time1)
        time2_m = (int(h_time2)*60)+int(m_time2)
        if time1_m < time2_m:
            return True
        else:
            return False
    
    def equals(self, time1, time2):
        h_time1, m_time1 = time1.split(':')
        h_time2, m_time2 = time2.split(':')
        time1_m = (int(h_time1)*60)+int(m_time1)
        time2_m = (int(h_time2)*60)+int(m_time2)
        if time1_m == time2_m:
            return True
        else:
            return False

    def subtraction(self, time1, time2):
        h_time1, m_time1 = time1.split(':')
        h_time2, m_time2 = time2.split(':')
        time1_m = (int(h_time1)*60)+int(m_time1)
        time2_m = (int(h_time2)*60)+int(m_time2)
        
        return time1_m - time2_m
        