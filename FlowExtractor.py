#!/usr/bin/env python

from math import sqrt

from PayloadObject import Payload


class FlowConstructor(object):
    def __init__(self, regular_expression_map):
        self.payload_map = {}
        self.already_filled_tcp = set()
        self.already_filled_udp = set()
        self.regular_expression_map = regular_expression_map

    def construct_flow(self, packet_information_list, file_object):
        for i_packet_information in packet_information_list:
            if i_packet_information.get_protocol() == 'TCP':
                if i_packet_information.get_starting_packet():
                    ending_packet = self.find_ending_packet(i_packet_information, packet_information_list)
                    if ending_packet is not None:
                        self.merge_payload_from_start_to_end(i_packet_information, ending_packet, packet_information_list, file_object)
            #elif i_packet_information.get_protocol() == 'UDP':
            #   self.merge_payloads(i_packet_information,
            #   packet_information_list, file_object)
        return self.payload_map

    def find_other_packets_of_flow(self, packet_information, packet_information_list):
        return_packet_information_list = []
        return_packet_information_list.append(packet_information)
        for i_packet_information in packet_information_list:
            if i_packet_information == packet_information and id(i_packet_information) != id(packet_information):
                return_packet_information_list.append(i_packet_information)
        return return_packet_information_list
    
    def find_other_packets_of_flow_from_start_to_end(self, starting_packet, ending_packet, packet_information_list):
        return_packet_information_list = []
        return_packet_information_list.append(starting_packet)
        for i_packet_information in packet_information_list:
            if i_packet_information == starting_packet and id(i_packet_information) != id(starting_packet) and i_packet_information.get_time() <= ending_packet.get_time() and i_packet_information.get_time() >= starting_packet.get_time():
                return_packet_information_list.append(i_packet_information)
        return_packet_information_list.append(ending_packet)
        return return_packet_information_list
    
    def merge_payload_from_start_to_end(self, starting_packet, ending_packet, packet_information_list, file_object):
        if self.get_flow_attr_string(starting_packet) not in self.already_filled_tcp:
            payload = Payload()
            payload.set_flow('f' + str(len(self.payload_map)))
            payload.set_source_ip(starting_packet.get_source_ip())
            payload.set_source_port(starting_packet.get_source_port())
            payload.set_destination_ip(starting_packet.get_destination_ip())
            payload.set_destination_port(starting_packet.get_destination_port())
            payload.set_protocol(starting_packet.get_protocol())
            payload.set_flow_duration(ending_packet.get_time() - starting_packet.get_time())
            returned_packet_information_list = self.find_other_packets_of_flow_from_start_to_end(starting_packet, ending_packet, packet_information_list)

            if len(returned_packet_information_list) > 0:
                payload.set_number_of_packets(len(returned_packet_information_list))
                payload.set_size(self.get_ip_packet_size(returned_packet_information_list))
                payload.set_iat_list(self.get_iat(returned_packet_information_list))
                payload.set_pkt_sizes(self.get_pkt_sizes(returned_packet_information_list, payload))
                for i_packet_information in returned_packet_information_list:
                    if i_packet_information is None:
                        continue
                    payload.get_packet_list().append(i_packet_information)
                    if payload.get_payload() is not None and i_packet_information.get_payload() is not None:
                        payload.set_payload(payload.get_payload() + str(i_packet_information.get_payload()))
                    elif payload.get_payload() is None and i_packet_information.get_payload() is not None:
                        payload.set_payload(str(i_packet_information.get_payload()))
                if payload.get_payload() is not None:
                    matched_files = self.match(payload.get_payload())
                    if matched_files and len(matched_files) > 0:
                        matched_string = ""
                        for st in matched_files:
                            matched_string += st + '~'
                        matched_string = matched_string[:len(matched_string) - 1]
                    else:
                        return
                    payload.set_application(matched_string)
                    payload.set_payload_size(len(payload.get_payload()))
                    self.calculate_min_max_avg_values(payload)
                    payload.set_payload_hex(self.toHex(payload.get_payload()))
                    self.already_filled_tcp.add(self.get_flow_attr_string(i_packet_information))

            if payload.get_payload() is None:
                print("Interesting!!!!")
                return
            print(payload)
            payload._packet_list = []
            payload._payload = None

            if len(returned_packet_information_list) >= 2:
                temp_returned_packet_information_list = returned_packet_information_list[:2]
                payload._2total_packet_size = self.get_ip_packet_size(temp_returned_packet_information_list)
                payload.set_iat_list(self.get_iat(temp_returned_packet_information_list))
                payload.set_pkt_sizes(self.get_pkt_sizes(temp_returned_packet_information_list, payload))
                for i_packet_information in temp_returned_packet_information_list:
                    if i_packet_information is None:
                        continue
                    payload.get_packet_list().append(i_packet_information)
                    if payload._2payload is not None and i_packet_information.get_payload() is not None:
                        payload._2payload += str(i_packet_information.get_payload())
                    elif payload._2payload is None and i_packet_information.get_payload() is not None:
                        payload._2payload = str(i_packet_information.get_payload())
                if payload._2payload is not None:
                    payload._2payload_size = len(payload._2payload)
                    payload._2payload_hex = self.toHex(payload._2payload)
                    print('##################')
                    self.calculate_min_max_avg_values2(payload)
                    print(payload)
                    print('##################')

            payload._packet_list = []
            payload._payload = None

            if len(returned_packet_information_list) >= 3:
                temp_returned_packet_information_list = returned_packet_information_list[:3]
                payload._3total_packet_size = self.get_ip_packet_size(temp_returned_packet_information_list)
                payload.set_iat_list(self.get_iat(temp_returned_packet_information_list))
                payload.set_pkt_sizes(self.get_pkt_sizes(temp_returned_packet_information_list, payload))
                for i_packet_information in temp_returned_packet_information_list:
                    if i_packet_information is None:
                        continue
                    payload.get_packet_list().append(i_packet_information)
                    if payload._3payload is not None and i_packet_information.get_payload() is not None:
                        payload._3payload += str(i_packet_information.get_payload())
                    elif payload._3payload is None and i_packet_information.get_payload() is not None:
                        payload._3payload = str(i_packet_information.get_payload())
                if payload._3payload is not None:
                    payload._3payload_size = len(payload._3payload)
                    payload._3payload_hex = self.toHex(payload._3payload)
                    self.calculate_min_max_avg_values3(payload)

            payload._packet_list = []
            payload._payload = None

            if len(returned_packet_information_list) >= 4:
                temp_returned_packet_information_list = returned_packet_information_list[:4]
                payload._4total_packet_size = self.get_ip_packet_size(temp_returned_packet_information_list)
                payload.set_iat_list(self.get_iat(temp_returned_packet_information_list))
                payload.set_pkt_sizes(self.get_pkt_sizes(temp_returned_packet_information_list, payload))
                for i_packet_information in temp_returned_packet_information_list:
                    if i_packet_information is None:
                        continue
                    payload.get_packet_list().append(i_packet_information)
                    if payload._4payload is not None and i_packet_information.get_payload() is not None:
                        payload._4payload += str(i_packet_information.get_payload())
                    elif payload._4payload is None and i_packet_information.get_payload() is not None:
                        payload._4payload = str(i_packet_information.get_payload())
                if payload._4payload is not None:
                    payload._4payload_size = len(payload._4payload)
                    payload._4payload_hex = self.toHex(payload._4payload)
                    self.calculate_min_max_avg_values4(payload)

            payload._packet_list = []
            payload._payload = None

            if len(returned_packet_information_list) >= 5:
                temp_returned_packet_information_list = returned_packet_information_list[:5]
                payload._5total_packet_size = self.get_ip_packet_size(temp_returned_packet_information_list)
                payload.set_iat_list(self.get_iat(temp_returned_packet_information_list))
                payload.set_pkt_sizes(self.get_pkt_sizes(temp_returned_packet_information_list, payload))
                for i_packet_information in temp_returned_packet_information_list:
                    if i_packet_information is None:
                        continue
                    payload.get_packet_list().append(i_packet_information)
                    if payload._5payload is not None and i_packet_information.get_payload() is not None:
                        payload._5payload += str(i_packet_information.get_payload())
                    elif payload._5payload is None and i_packet_information.get_payload() is not None:
                        payload._5payload = str(i_packet_information.get_payload())
                if payload._5payload is not None:
                    payload._5payload_size = len(payload._5payload)
                    payload._5payload_hex = self.toHex(payload._5payload)
                    self.calculate_min_max_avg_values5(payload)

            payload._packet_list = []
            payload._payload = None

            if len(returned_packet_information_list) >= 6:
                temp_returned_packet_information_list = returned_packet_information_list[:6]
                payload._6total_packet_size = self.get_ip_packet_size(temp_returned_packet_information_list)
                payload.set_iat_list(self.get_iat(temp_returned_packet_information_list))
                payload.set_pkt_sizes(self.get_pkt_sizes(temp_returned_packet_information_list, payload))
                for i_packet_information in temp_returned_packet_information_list:
                    if i_packet_information is None:
                        continue
                    payload.get_packet_list().append(i_packet_information)
                    if payload._6payload is not None and i_packet_information.get_payload() is not None:
                        payload._6payload += str(i_packet_information.get_payload())
                    elif payload._6payload is None and i_packet_information.get_payload() is not None:
                        payload._6payload = str(i_packet_information.get_payload())
                if payload._6payload is not None:
                    payload._6payload_size = len(payload._6payload)
                    payload._6payload_hex = self.toHex(payload._6payload)
                    self.calculate_min_max_avg_values6(payload)

            payload._packet_list = []
            payload._payload = None

            if len(returned_packet_information_list) >= 7:
                temp_returned_packet_information_list = returned_packet_information_list[:7]
                payload._7total_packet_size = self.get_ip_packet_size(temp_returned_packet_information_list)
                payload.set_iat_list(self.get_iat(temp_returned_packet_information_list))
                payload.set_pkt_sizes(self.get_pkt_sizes(temp_returned_packet_information_list, payload))
                for i_packet_information in temp_returned_packet_information_list:
                    if i_packet_information is None:
                        continue
                    payload.get_packet_list().append(i_packet_information)
                    if payload._7payload is not None and i_packet_information.get_payload() is not None:
                        payload._7payload += str(i_packet_information.get_payload())
                    elif payload._7payload is None and i_packet_information.get_payload() is not None:
                        payload._7payload = str(i_packet_information.get_payload())
                if payload._7payload is not None:
                    payload._7payload_size = len(payload._7payload)
                    payload._7payload_hex = self.toHex(payload._7payload)
                    self.calculate_min_max_avg_values7(payload)

            file_object.write(str(payload))

    def match(self, payload):
        print("Inside Match")
        matches = []
        for ke in self.regular_expression_map.keys():
            if self.regular_expression_map[ke].search(payload):
                matches.append(ke)
        return matches

    def get_next_key(self, flow_attr_string):
        count = 0
        while flow_attr_string not in self.payload_map.keys():
            count += 1
            flow_attr_string += str(count)
        return flow_attr_string

    def get_ip_packet_size(self, refined_packet_information_list):
        ip_packet_length = 0
        for i_packet_information in refined_packet_information_list:
            ip_packet_length += len(i_packet_information.get_ip_packet())
        return ip_packet_length

    def get_iat(self, refined_packet_information_list):
        iat_list = []
        if refined_packet_information_list is None:
            return iat_list
        for i in range(len(refined_packet_information_list) - 1):
            iat = refined_packet_information_list[i + 1].get_time() - refined_packet_information_list[i].get_time()
            if iat > 0:
                iat_list.append(iat)
        return iat_list

    def toHex(self, s):
        try:
            return_string = ''
            for ch in s:
                hv = hex(ord(ch)).replace('0x', '')
                if len(hv) == 1:
                    hv = '0' + hv
                return_string = return_string + hv
            return return_string
        except Exception:
            return ''
    def get_pkt_sizes(self, refined_packet_information_list, payload):
        pkt_size = []
        total_pkt_size = 0
        for i_packet_information in refined_packet_information_list:
            pkt_size.append(len(i_packet_information.get_ip_packet()))
            total_pkt_size += len(i_packet_information.get_ip_packet())
        payload.set_total_pkt_size(total_pkt_size)
        return pkt_size
    
    def get_flow_duration_for_udp(self, packet_information_list):
        min_time = 0
        max_time = 0
        for i_packet_information in packet_information_list:
            if i_packet_information.get_time() >= max_time:
                max_time = i_packet_information.get_time()
            if i_packet_information.get_time() <= min_time:
                min_time = i_packet_information.get_time()
        print(max_time - min_time)
        return max_time - min_time

    # def merge_payloads(self, packet_information, packet_information_list,
    # file_object):
    #     if self.get_flow_attr_string(packet_information) not in
    #     self.already_filled_udp:
    #         payload = Payload()
    #         payload.set_flow('f' + str(len(self.payload_map)))
    #         payload.set_source_ip(packet_information.get_source_ip())
    #         payload.set_source_port(packet_information.get_source_port())
    #         payload.set_destination_ip(packet_information.get_destination_ip())
    #         payload.set_destination_port(packet_information.get_destination_port())
    #         payload.set_protocol(packet_information.get_protocol())
    #         payload.set_flow_duration(self.get_flow_duration_for_udp(packet_information_list))
    #         returned_packet_information_list =
    #         self.find_other_packets_of_flow(packet_information,
    #         packet_information_list)
    #         payload.set_number_of_packets(len(returned_packet_information_list))
    #         payload.set_size(self.get_ip_packet_size(returned_packet_information_list))
    #         payload.set_iat_list(self.get_iat(returned_packet_information_list))
    #         payload.set_pkt_sizes(self.get_pkt_sizes(returned_packet_information_list,
    #         payload))
    #         if len(returned_packet_information_list) > 2:
    #             for i_packet_information in returned_packet_information_list:
    #                 if i_packet_information is None:
    #                     continue
    #                 payload.get_packet_list().append(i_packet_information)
    #                 if payload.get_payload() is not None and
    #                 i_packet_information.get_payload() is not None:
    #                     payload.set_payload(payload.get_payload() +
    #                     str(i_packet_information.get_payload()))
    #                 elif payload.get_payload() is None and
    #                 i_packet_information.get_payload() is not None:
    #                     payload.set_payload(str(i_packet_information.get_payload()))
    #             if payload.get_payload() is not None:
    #                 payload.set_payload_size(len(payload.get_payload()))
    #                 self.calculate_min_max_avg_values(payload)
    #                 payload.set_payload_hex(self.toHex(payload.get_payload()))
    #                 self.already_filled_udp.add(self.get_flow_attr_string(i_packet_information))
    #                 file_object.write(str(payload))

    def calculate_min_max_avg_values(self, payload):
        self.get_rita_list(payload)
        payload.set_min_iat(min(payload.get_iat_list()))
        payload.set_max_iat(max(payload.get_iat_list()))
        payload.set_avg_iat(float(sum(payload.get_iat_list())) / len(payload.get_iat_list()))
        payload.set_std_div_iat(self.std_div(payload.get_iat_list()))
        payload.set_min_riat(min(payload.get_rita_list()))
        payload.set_max_riat(max(payload.get_rita_list()))
        payload.set_avg_riat(float(sum(payload.get_rita_list())) / len(payload.get_rita_list()))
        payload.set_std_div_riat(self.std_div(payload.get_rita_list()))
        payload.set_min_pkt_size(min(payload.get_pkt_sizes()))
        payload.set_max_pkt_size(max(payload.get_pkt_sizes()))
        payload.set_avg_pkt_size(float(sum(payload.get_pkt_sizes())) / len(payload.get_pkt_sizes()))
        payload.set_std_div_pkt_size(self.std_div(payload.get_pkt_sizes()))
        payload.set_avg_pkt_per_sec(float(len(payload.get_packet_list())) / payload.get_flow_duration())
        payload.set_avg_bytes_per_sec(float(payload.get_total_pkt_size()) / payload.get_flow_duration())

    def calculate_min_max_avg_values2(self, payload):
        self.get_rita_list(payload)
        print(payload.get_iat_list())
        payload._2min_iat = min(payload.get_iat_list())
        payload._2max_iat = max(payload.get_iat_list())
        payload._2avg_iat = float(sum(payload.get_iat_list())) / len(payload.get_iat_list())
        payload._2std_div_iat = self.std_div(payload.get_iat_list())
        payload._2min_riat = min(payload.get_rita_list())
        payload._2max_riat = max(payload.get_rita_list())
        payload._2avg_riat = float(sum(payload.get_rita_list())) / len(payload.get_rita_list())
        payload._2std_div_riat = self.std_div(payload.get_rita_list())
        payload._2min_pkt_size = min(payload.get_pkt_sizes())
        payload._2max_pkt_size = max(payload.get_pkt_sizes())
        payload._2avg_pkt_size = float(sum(payload.get_pkt_sizes())) / len(payload.get_pkt_sizes())
        payload._2std_div_pkt_size = self.std_div(payload.get_pkt_sizes())

    def calculate_min_max_avg_values3(self, payload):
        self.get_rita_list(payload)
        payload._3min_iat = min(payload.get_iat_list())
        payload._3max_iat = max(payload.get_iat_list())
        payload._3avg_iat = float(sum(payload.get_iat_list())) / len(payload.get_iat_list())
        payload._3std_div_iat = self.std_div(payload.get_iat_list())
        payload._3min_riat = min(payload.get_rita_list())
        payload._3max_riat = max(payload.get_rita_list())
        payload._3avg_riat = float(sum(payload.get_rita_list())) / len(payload.get_rita_list())
        payload._3std_div_riat = self.std_div(payload.get_rita_list())
        payload._3min_pkt_size = min(payload.get_pkt_sizes())
        payload._3max_pkt_size = max(payload.get_pkt_sizes())
        payload._3avg_pkt_size = float(sum(payload.get_pkt_sizes())) / len(payload.get_pkt_sizes())
        payload._3std_div_pkt_size = self.std_div(payload.get_pkt_sizes())

    def calculate_min_max_avg_values4(self, payload):
        self.get_rita_list(payload)
        payload._4min_iat = min(payload.get_iat_list())
        payload._4max_iat = max(payload.get_iat_list())
        payload._4avg_iat = float(sum(payload.get_iat_list())) / len(payload.get_iat_list())
        payload._4std_div_iat = self.std_div(payload.get_iat_list())
        payload._4min_riat = min(payload.get_rita_list())
        payload._4max_riat = max(payload.get_rita_list())
        payload._4avg_riat = float(sum(payload.get_rita_list())) / len(payload.get_rita_list())
        payload._4std_div_riat = self.std_div(payload.get_rita_list())
        payload._4min_pkt_size = min(payload.get_pkt_sizes())
        payload._4max_pkt_size = max(payload.get_pkt_sizes())
        payload._4avg_pkt_size = float(sum(payload.get_pkt_sizes())) / len(payload.get_pkt_sizes())
        payload._4std_div_pkt_size = self.std_div(payload.get_pkt_sizes())

    def calculate_min_max_avg_values5(self, payload):
        self.get_rita_list(payload)
        payload._5min_iat = min(payload.get_iat_list())
        payload._5max_iat = max(payload.get_iat_list())
        payload._5avg_iat = float(sum(payload.get_iat_list())) / len(payload.get_iat_list())
        payload._5std_div_iat = self.std_div(payload.get_iat_list())
        payload._5min_riat = min(payload.get_rita_list())
        payload._5max_riat = max(payload.get_rita_list())
        payload._5avg_riat = float(sum(payload.get_rita_list())) / len(payload.get_rita_list())
        payload._5std_div_riat = self.std_div(payload.get_rita_list())
        payload._5min_pkt_size = min(payload.get_pkt_sizes())
        payload._5max_pkt_size = max(payload.get_pkt_sizes())
        payload._5avg_pkt_size = float(sum(payload.get_pkt_sizes())) / len(payload.get_pkt_sizes())
        payload._5std_div_pkt_size = self.std_div(payload.get_pkt_sizes())

    def calculate_min_max_avg_values6(self, payload):
        self.get_rita_list(payload)
        payload._6min_iat = min(payload.get_iat_list())
        payload._6max_iat = max(payload.get_iat_list())
        payload._6avg_iat = float(sum(payload.get_iat_list())) / len(payload.get_iat_list())
        payload._6std_div_iat = self.std_div(payload.get_iat_list())
        payload._6min_riat = min(payload.get_rita_list())
        payload._6max_riat = max(payload.get_rita_list())
        payload._6avg_riat = float(sum(payload.get_rita_list())) / len(payload.get_rita_list())
        payload._6std_div_riat = self.std_div(payload.get_rita_list())
        payload._6min_pkt_size = min(payload.get_pkt_sizes())
        payload._6max_pkt_size = max(payload.get_pkt_sizes())
        payload._6avg_pkt_size = float(sum(payload.get_pkt_sizes())) / len(payload.get_pkt_sizes())
        payload._6std_div_pkt_size = self.std_div(payload.get_pkt_sizes())

    def calculate_min_max_avg_values7(self, payload):
        self.get_rita_list(payload)
        payload._7min_iat = min(payload.get_iat_list())
        payload._7max_iat = max(payload.get_iat_list())
        payload._7avg_iat = float(sum(payload.get_iat_list())) / len(payload.get_iat_list())
        payload._7std_div_iat = self.std_div(payload.get_iat_list())
        payload._7min_riat = min(payload.get_rita_list())
        payload._7max_riat = max(payload.get_rita_list())
        payload._7avg_riat = float(sum(payload.get_rita_list())) / len(payload.get_rita_list())
        payload._7std_div_riat = self.std_div(payload.get_rita_list())
        payload._7min_pkt_size = min(payload.get_pkt_sizes())
        payload._7max_pkt_size = max(payload.get_pkt_sizes())
        payload._7avg_pkt_size = float(sum(payload.get_pkt_sizes())) / len(payload.get_pkt_sizes())
        payload._7std_div_pkt_size = self.std_div(payload.get_pkt_sizes())

    def std_div(self, value_list):
        avg_value = float(sum(value_list)) / len(value_list)
        sum_value = 0.0
        for value in value_list:
            sum_value += (value - avg_value) ** 2
        return sqrt(sum_value / len(value_list))

    def get_rita_list(self, payload):
        rta = []
        if payload.get_iat_list() is None:
            return rta
        min_ita = min(payload.get_iat_list())
        for ita in payload.get_iat_list():
            rta.append(float(ita) / min_ita)
        payload.set_rita_list(rta)

    def find_ending_packet(self, starting_packet, packet_information_list):
        for i_packet_information in packet_information_list:
            if i_packet_information == starting_packet and i_packet_information.get_ending_packet():
                return i_packet_information
        return None

    def get_flow_attr_string(self, packet_information):
        return_string = ""
        return_string += str(packet_information.get_source_ip()) + '-'
        return_string += str(packet_information.get_destination_ip()) + '-'
        return_string += str(packet_information.get_source_port()) + '-'
        return_string += str(packet_information.get_destination_port()) + '-'
        return_string += str(packet_information.get_protocol())
        return return_string
