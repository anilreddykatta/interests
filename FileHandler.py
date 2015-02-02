__author__ = 'KattaAnil'
format_string = ""
format_string += "Source IP, "
format_string += "Destination IP, "
format_string += "Source Port, "
format_string += "Destination Port, "
format_string += "Protocol, "
format_string += "Avg IAT, "
format_string += "Min IAT, "
format_string += "Max IAT, "
format_string += "Std Div IAT, "
format_string += "Avg RIAT, "
format_string += "Min RIAT, "
format_string += "Max RIAT, "
format_string += "Std Div RIAT, "
format_string += "Avg Pkt Size, "
format_string += "Min Pkt Size, "
format_string += "Max Pkt Size, "
format_string += "Std Div Pkt Size, "
format_string += "Packets Size, "
format_string += "Flow Duration, "
format_string += "Number Of Packets, "
format_string += "Average Pkts Per Sec, "
format_string += "Average Bytes Per Sec, "
format_string += "Payload Size, "
format_string += "Payload In Hex,"

"""
format_string += "2 Avg IAT, "
format_string += "2 Min IAT, "
format_string += "2 Max IAT, "
format_string += "2 Std Div IAT, "
format_string += "2 Avg RIAT, "
format_string += "2 Min RIAT, "
format_string += "2 Max RIAT, "
format_string += "2 Std Div RIAT, "
format_string += "2 Avg Pkt Size, "
format_string += "2 Min Pkt Size, "
format_string += "2 Max Pkt Size, "
format_string += "2 Std Div Pkt Size, "
format_string += "2 Packets Size, "
format_string += "2 Payload Size, "
format_string += "2 Payload In Hex,"
"""

format_string += "3 Avg IAT, "
format_string += "3 Min IAT, "
format_string += "3 Max IAT, "
format_string += "3 Std Div IAT, "
format_string += "3 Avg RIAT, "
format_string += "3 Min RIAT, "
format_string += "3 Max RIAT, "
format_string += "3 Std Div RIAT, "
format_string += "3 Avg Pkt Size, "
format_string += "3 Min Pkt Size, "
format_string += "3 Max Pkt Size, "
format_string += "3 Std Div Pkt Size, "
format_string += "3 Packets Size, "
format_string += "3 Payload Size, "
format_string += "3 Payload In Hex,"

format_string += "4 Avg IAT, "
format_string += "4 Min IAT, "
format_string += "4 Max IAT, "
format_string += "4 Std Div IAT, "
format_string += "4 Avg RIAT, "
format_string += "4 Min RIAT, "
format_string += "4 Max RIAT, "
format_string += "4 Std Div RIAT, "
format_string += "4 Avg Pkt Size, "
format_string += "4 Min Pkt Size, "
format_string += "4 Max Pkt Size, "
format_string += "4 Std Div Pkt Size, "
format_string += "4 Packets Size, "
format_string += "4 Payload Size, "
format_string += "4 Payload In Hex,"

format_string += "5 Avg IAT, "
format_string += "5 Min IAT, "
format_string += "5 Max IAT, "
format_string += "5 Std Div IAT, "
format_string += "5 Avg RIAT, "
format_string += "5 Min RIAT, "
format_string += "5 Max RIAT, "
format_string += "5 Std Div RIAT, "
format_string += "5 Avg Pkt Size, "
format_string += "5 Min Pkt Size, "
format_string += "5 Max Pkt Size, "
format_string += "5 Std Div Pkt Size, "
format_string += "5 Packets Size, "
format_string += "5 Payload Size, "
format_string += "5 Payload In Hex,"

format_string += "6 Avg IAT, "
format_string += "6 Min IAT, "
format_string += "6 Max IAT, "
format_string += "6 Std Div IAT, "
format_string += "6 Avg RIAT, "
format_string += "6 Min RIAT, "
format_string += "6 Max RIAT, "
format_string += "6 Std Div RIAT, "
format_string += "6 Avg Pkt Size, "
format_string += "6 Min Pkt Size, "
format_string += "6 Max Pkt Size, "
format_string += "6 Std Div Pkt Size, "
format_string += "6 Packets Size, "
format_string += "6 Payload Size, "
format_string += "6 Payload In Hex,"

format_string += "7 Avg IAT, "
format_string += "7 Min IAT, "
format_string += "7 Max IAT, "
format_string += "7 Std Div IAT, "
format_string += "7 Avg RIAT, "
format_string += "7 Min RIAT, "
format_string += "7 Max RIAT, "
format_string += "7 Std Div RIAT, "
format_string += "7 Avg Pkt Size, "
format_string += "7 Min Pkt Size, "
format_string += "7 Max Pkt Size, "
format_string += "7 Std Div Pkt Size, "
format_string += "7 Packets Size, "
format_string += "7 Payload Size, "
format_string += "7 Payload In Hex,"

format_string += "Applications\n"
# format_string += "Payload \n"

class FileHandler(object):
    def __init__(self, file_object):
        self._f = file_object  # open(filename, 'w')

    def write_to_file(self, payloadmap):
        for ke in payloadmap:
            self._f.write(str(payloadmap[ke]))
        # self.close_file()
    
    def toHex(self, s):
        lst = []
        for ch in s:
            hv = hex(ord(ch)).replace('0x', '')
            if len(hv) == 1:
                hv = '0' + hv
            lst.append(hv)
        if len(lst) > 0:
            return reduce(lambda x, y:x + y, lst)
        else:
            return ''

    def close_file(self):
        self._f.close()
