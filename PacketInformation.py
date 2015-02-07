#!/usr/bin/env python

import datetime

class PacketInformation(object):    
    def __init__(self):
        self._time = None
        self._inter_arrival = None
        self._source_ip = None
        self._source_port = None
        self._destination_ip = None
        self._destination_port = None
        self._protocol = None
        self._header_chksm = None
        self._transport_chksm = None
        self._payload_length = None
        self._payload = None
        self._syn = 'N'
        self._ack = 'N'
        self._fin = 'N'
        self._push = 'N'
        self._urgent = 'N'
        self._rst = 'N'
        self._client_or_server = None
        self._flow_name = None
        self._application = None
        self._starting_packet = False
        self._ending_packet = False
        self._ip_packet = None
        self._transport_packet = None

    def set_transport_packet(self, transport_packet):
        self._transport_packet = transport_packet

    def get_transport_packet(self):
        return self._transport_packet

    def set_ip_packet(self, ip_packet):
        self._ip_packet = ip_packet

    def get_ip_packet(self):
        return self._ip_packet

    def set_rst(self, value):
        self._rst = value

    def get_rst(self):
        return self._rst

    def set_time(self, time):
        self._time = time

    def get_time(self):
        return self._time

    def set_inter_arrival(self, inter_arrival):
        self._inter_arrival = inter_arrival

    def get_inter_arrival(self):
        return self._inter_arrival

    def set_source_ip(self, source_ip):
        self._source_ip = source_ip

    def get_source_ip(self):
        return self._source_ip

    def set_source_port(self, source_port):
        self._source_port = source_port

    def get_source_port(self):
        return self._source_port

    def set_destination_ip(self, destination_ip):
        self._destination_ip = destination_ip

    def get_destination_ip(self):
        return self._destination_ip

    def set_destination_port(self, destination_port):
        self._destination_port = destination_port

    def get_destination_port(self):
        return self._destination_port

    def set_protocol(self, protocol):
        self._protocol = protocol

    def get_protocol(self):
        return self._protocol

    def set_header_chksm(self, header_chksm):
        self._header_chksm = header_chksm

    def get_header_chksm(self):
        return self._header_chksm

    def set_transport_chksm(self, transport_chksm):
        self._transport_chksm = transport_chksm

    def get_transport_chksm(self):
        return self._transport_chksm

    def set_payload_length(self, payload_length):
        self._payload_length = payload_length

    def get_payload_length(self):
        return self._payload_length

    def set_syn(self, syn):
        self._syn = syn

    def get_syn(self):
        return self._syn

    def set_ack(self, ack):
        self._ack = ack

    def get_ack(self):
        return self._ack

    def set_fin(self, fin):
        self._fin = fin

    def get_fin(self):
        return self._fin

    def set_push(self, push):
        self._push = push

    def get_push(self):
        return self._push

    def set_urgent(self, urgent):
        self._urgent = urgent

    def get_urgent(self):
        return self._urgent

    def set_client_or_server(self, client_or_server):
        self._client_or_server = client_or_server

    def get_client_or_server(self):
        return self._client_or_server

    def set_flow_name(self, flow_name):
        self._flow_name = flow_name

    def get_flow_name(self):
        return self._flow_name

    def set_application(self, application):
        self._application = application

    def get_application(self):
        return self._application

    def set_payload(self, payload):
        self._payload = payload

    def get_payload(self):
        return self._payload

    def set_starting_packet(self, starting_packet):
        self._starting_packet = starting_packet

    def get_starting_packet(self):
        return self._starting_packet

    def set_ending_packet(self, ending_packet):
        self._ending_packet = ending_packet

    def get_ending_packet(self):
        return self._ending_packet

    def set_flags(self, ether_frame):
        flags = ether_frame.sprintf('%TCP.flags%')
        count = 0
        if 'F' in flags:
            self.set_fin('Y')
            self.set_ending_packet(True)
        if 'S' in flags:
            self.set_syn('Y')
            if 'S' == flags:
                self.set_starting_packet(True)
                self.set_client_or_server('C')
        if 'R' in flags:
            self.set_rst('Y')
        if 'P' in flags:
            self.set_push('Y')
        if 'A' in flags:
            self.set_ack('Y')
        if 'U' in flags:
            self.set_urgent('Y')
             
    def __str__(self):
        return_string = "Protocol: " + self.get_protocol() + " | Source IP: " + ('{:<14}'.format(self.get_source_ip())) + " | Source PORT: " + ('{:<6}'.format(str(self.get_source_port()))) + " | Destination IP: " + ('{:<14}'.format(self.get_destination_ip())) + " | Destination PORT: " + ('{:<6}'.format(str(self.get_destination_port()))) + " | Payload Length: " + ('{:<6}'.format(str(self.get_payload_length()))) + " | F: " + str(self.get_fin()) + " | S: " + str(self.get_syn()) + " | A: " + str(self.get_ack()) + " | P: " + str(self.get_push()) + " | U: " + str(self.get_urgent()) + " | R: " + str(self.get_rst()) + " | CS: " + str(self.get_client_or_server())

        """ return_string = 
                        "Application is: "+self.get_application()+"\n"+\
                        "Client Or Server: "+self.get_client_or_server()+"\n"+\
                        "Payload Length: "+str(self.get_payload_length()) + "\n"+ \
                        "Payload: "+self.get_payload() + "\n" +\
                        "Time: "+ datetime.datetime.fromtimestamp(self.get_time()).strftime('%Y-%m-%d %H:%M:%S') +"\n"+\
                        "Inter Arrival: "+self.get_inter_arrival() + "\n"+\
                        "Source IP: "+self.get_source_ip()+"\n"+\
                        "Destination IP: "+self.get_destination_ip()+"\n"+ \
                        "Source Port: "+self.get_source_port()+"\n"+\
                        "Destination Port: "+(self.get_destination_port() if self.get_destination_port() else "")+"\n"
                       # "Protocol: "+(self.get_protocol() if self.get_protocol() else "")+"\n" """
        return return_string

    def __eq__(self, other_packet_information):
        """
        :param other_packet_information:
        :return:
        """
        if self.get_source_ip() == other_packet_information.get_source_ip() and self.get_destination_ip() == other_packet_information.get_destination_ip() and \
           self.get_source_port() == other_packet_information.get_source_port() and self.get_destination_port() == other_packet_information.get_destination_port() and \
           self.get_protocol() == other_packet_information.get_protocol():
            return True
        else:
            return False
        """ if  ((other_packet_information.get_source_ip() == self.get_source_ip() and other_packet_information.get_destination_ip() == self.get_destination_ip() and other_packet_information.get_source_port() == self.get_source_port() and other_packet_information.get_destination_port() == self.get_destination_port()) or \
             (other_packet_information.get_source_ip() == self.get_destination_ip() and other_packet_information.get_destination_ip() == self.get_source_ip() and other_packet_information.get_destination_port() == self.get_source_port() and other_packet_information.get_source_port() == self.get_destination_port())) and \
              other_packet_information.get_protocol() == self.get_protocol():
            return True
        else:
            return False """

    def __ne__(self, other_packet_information):
        return not self == other_packet_information