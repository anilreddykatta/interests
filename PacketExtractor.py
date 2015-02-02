#!/usr/bin/env python

from scapy.all import *
from PacketInformation import PacketInformation


class Extractor(object):
    def __init__(self):
        self.payload_objects = []

    def extract_payload(self, ether_frame):
        try:
            packet_information = PacketInformation()
            if ether_frame.haslayer(TCP):
                packet_information.set_protocol('TCP')
                packet_information.set_transport_packet(ether_frame[TCP])
            elif ether_frame.haslayer(UDP):
                packet_information.set_protocol('UDP')
                packet_information.set_transport_packet(ether_frame[UDP])
            if ether_frame.haslayer(Raw):
                packet_information.set_payload_length(len(ether_frame[Raw]))
                packet_information.set_payload(ether_frame[Raw])
            packet_information.set_destination_ip(ether_frame.payload.dst)
            packet_information.set_source_ip(ether_frame.payload.src)
            packet_information.set_destination_port(ether_frame.payload.payload.dport)
            packet_information.set_source_port(ether_frame.payload.payload.sport)
            packet_information.set_header_chksm(ether_frame.payload.chksum)
            packet_information.set_transport_chksm(ether_frame.payload.payload.chksum)
            packet_information.set_flags(ether_frame)
            if ether_frame.haslayer(IP):
                packet_information.set_ip_packet(ether_frame[IP])
            else:
                return None
            packet_information.set_time(ether_frame.time)
            return packet_information
        except AttributeError, err:
            print(err)
            return None

    def read_file(self, file_name):
        packet_informations = []
        try:
            input_file_name = rdpcap(file_name)
            count = 0
            for pkt in input_file_name:
                count += 1
                print(count)
                packet_information = self.extract_payload(pkt);
                if packet_information:
                    packet_informations.append(packet_information)
        except Exception:
            return packet_informations
        return packet_informations
