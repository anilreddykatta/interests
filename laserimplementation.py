from scapy.packet import NoPayload
import FlowExtractor, PacketExtractor

__author__ = 'KattaAnil'

from enum import Enum


class Laser(object):
    def __init__(self, flows):
        self._size_threshold = 2000
        self._packet_constraint = 10
        self._flows = flows
        self.lcs_pool = set()
        self.REPR = Enum('DIAGONAL', 'UP', 'LEFT')
        self.SPECIAL_BREAK_CHARACTER = '/'
        self.MINIMUM_SUBSTRING_LENGTH = 2

    def signature_generation(self):
        return self.find_signature_from()

    def find_signature_from(self):
        print("Inside Find Signature From")
        flow1 = self._flows[0]
        flow2 = self._flows[1]
        start_index = 0
        for if1 in flow1.get_packet_list():
            for if2 in flow2.get_packet_list():
                if if1.get_payload_length() and if2.get_payload_length() and abs(if1.get_payload_length() - if2.get_payload_length()) < self._size_threshold:
                    if type(if1.get_payload()) is not NoPayload and type(if2.get_payload()) is not NoPayload:
                        result_lcs = self.lcs(if1.get_payload(), if2.get_payload())
                        if result_lcs:
                            self.lcs_pool.update(result_lcs)
        print(self.lcs_pool)
        longest_string = self.find_longest_from_set(self.lcs_pool)
        for indexflow in range(2, len(self._flows)):
            iflow = self._flows[indexflow]
            #result_lcs = self.laser(longest_string, iflow.get_payload())
            result_lcs = self.lcs(longest_string, iflow.get_payload())
            longest_string = self.find_longest_from_set(result_lcs)
        return longest_string


    def find_longest_from_set(self, from_iter):
        longest_string = ""
        if from_iter is None:
            return longest_string
        for st in from_iter:
            if len(st) > len(longest_string):
                longest_string = st
        return longest_string

    def laser(self, payload1, payload2):
        print(type(payload1))
        print(type(payload2))
        if type(payload1) is not str or type(payload2) is not str:
            return None
        payload1 = payload1[::-1]
        payload2 = payload2[::-1]
        matrix = [0]*len(payload1)
        for i in range(len(matrix)):
            matrix[i] = [0]*len(payload2)

        for i in range(len(payload1)):
            for j in range(len(payload2)):
                if i == 0 or j == 0:
                    matrix[i][j] = 0
                elif payload1[i] == payload2[j]:
                    matrix[i][j] = 0 #self.REPR.DIAGONAL
                elif matrix[i][j] != matrix[i][j - 1]:
                    matrix[i][j] = 1 #self.REPR.UP
                else:
                    matrix[i][j] = 2 #self.REPR.LEFT
        for i in matrix:
            print(i)
        i = len(payload1) - 1
        j = len(payload2) - 1
        if i < 0 or j < 0:
            return None
        return_string = ""
        while matrix[i][j] != 0:
            if matrix[i][j] == 2: #self.REPR.LEFT:
                j = j - 1
            elif matrix[i][j] == 1: #self.REPR.UP:
                i = i - 1
            elif matrix[i][j] == 0 :#self.REPR.DIAGONAL:
                return_string = return_string + payload1[i]

            if matrix[i - 1][j - 1] != 0 :# self.REPR.DIAGONAL:
                return_string = return_string + self.SPECIAL_BREAK_CHARACTER
            j -= 1
            i -= 1

        substring_array = return_string.split(self.SPECIAL_BREAK_CHARACTER)
        return_string_array = []
        for st in substring_array:
            if len(st) > self.MINIMUM_SUBSTRING_LENGTH:
                return_string_array.append(st)

        return return_string_array

    def lcs(self, xstr, ystr):
        print(xstr)
        print(ystr)
        if not (xstr and ystr): return # if string is empty
        lcs = [''] #  longest common subsequence
        lcslen = 0 # length of longest common subsequence so far
        for i in xrange(len(xstr)):
            cs = '' # common subsequence
            start = 0 # start position in ystr
            for item in xstr[i:]:
                index = ystr.find(item, start) # position at the common letter
                if index != -1: # if common letter is found
                    cs += item # add common letter to the cs
                    start = index + 1
                if index == len(ystr) - 1: break # if reached to the end of ystr
            # updates lcs and lcslen if found better cs
            if len(cs) > lcslen: lcs, lcslen = [cs], len(cs)
            elif len(cs) == lcslen: lcs.append(cs)
        return lcs


if __name__=='__main__':
    ra = []
    laser = Laser(ra)
    a = laser.lcs('abcssd', 'ad3asasdas')
    print(a)
