#!/usr/bin/env python
class Payload(object):
    def __init__(self):
        self._application = None
        self._flow = None
        self._client_or_server = None
        self._payload = None
        self._paylod_in_hex = None
        self._end = False
        self._start = False
        self._packet_list = []
        self._number_of_packets = None
        self._payload_size = None
        self._flow_duration = None
        self._size = None
        self._iat_list = None
        self._pkt_sizes = None
        self._rita_list = None
        self._min_pkt_size = None
        self._max_pkt_size = None
        self._avg_pkt_size = None
        self._std_div_pkt_size = None
        self._min_iat = None
        self._max_iat = None
        self._avg_iat = None
        self._std_div_iat = None
        self._min_riat = None
        self._max_riat = None
        self._avg_riat = None
        self._std_div_riat = None
        self._avg_pkts_per_sec = None
        self._avg_bytes_per_sec = None
        self._total_pkt_size = None
        self._source_ip = None
        self._destination_ip = None
        self._source_port = None
        self._destination_port = None
        self._protocol = None

        self._2payload = None
        self._2payload_hex = None
        self._2avg_iat = None
        self._2min_iat = None
        self._2max_iat = None
        self._2std_div_iat = None
        self._2avg_pkt_size = None
        self._2min_pkt_size = None
        self._2max_pkt_size = None
        self._2std_div_pkt_size = None
        self._2avg_riat = None
        self._2min_riat = None
        self._2max_riat = None
        self._2std_div_riat = None
        self._2payload_size = None
        self._2total_packet_size = None
        self._2avg_pkts_per_sec = None
        self._2avg_bytes_per_sec = None

        self._3payload = None
        self._3payload_hex = None
        self._3avg_iat = None
        self._3min_iat = None
        self._3max_iat = None
        self._3std_div_iat = None
        self._3avg_pkt_size = None
        self._3min_pkt_size = None
        self._3max_pkt_size = None
        self._3std_div_pkt_size = None
        self._3avg_riat = None
        self._3min_riat = None
        self._3max_riat = None
        self._3std_div_riat = None
        self._3payload_size = None
        self._3total_packet_size = None
        self._3avg_pkts_per_sec = None
        self._3avg_bytes_per_sec = None

        self._4payload = None
        self._4payload_hex = None
        self._4avg_iat = None
        self._4min_iat = None
        self._4max_iat = None
        self._4std_div_iat = None
        self._4avg_pkt_size = None
        self._4min_pkt_size = None
        self._4max_pkt_size = None
        self._4std_div_pkt_size = None
        self._4avg_riat = None
        self._4min_riat = None
        self._4max_riat = None
        self._4std_div_riat = None
        self._4payload_size = None
        self._4total_packet_size = None
        self._4avg_pkts_per_sec = None
        self._4avg_bytes_per_sec = None

        self._5payload = None
        self._5payload_hex = None
        self._5avg_iat = None
        self._5min_iat = None
        self._5max_iat = None
        self._5std_div_iat = None
        self._5avg_pkt_size = None
        self._5min_pkt_size = None
        self._5max_pkt_size = None
        self._5std_div_pkt_size = None
        self._5avg_riat = None
        self._5min_riat = None
        self._5max_riat = None
        self._5std_div_riat = None
        self._5payload_size = None
        self._5total_packet_size = None
        self._5avg_pkts_per_sec = None
        self._5avg_bytes_per_sec = None

        self._6payload = None
        self._6payload_hex = None
        self._6avg_iat = None
        self._6min_iat = None
        self._6max_iat = None
        self._6std_div_iat = None
        self._6avg_pkt_size = None
        self._6min_pkt_size = None
        self._6max_pkt_size = None
        self._6std_div_pkt_size = None
        self._6avg_riat = None
        self._6min_riat = None
        self._6max_riat = None
        self._6std_div_riat = None
        self._6payload_size = None
        self._6total_packet_size = None
        self._6avg_pkts_per_sec = None
        self._6avg_bytes_per_sec = None

        self._7payload = None
        self._7payload_hex = None
        self._7avg_iat = None
        self._7min_iat = None
        self._7max_iat = None
        self._7std_div_iat = None
        self._7avg_pkt_size = None
        self._7min_pkt_size = None
        self._7max_pkt_size = None
        self._7std_div_pkt_size = None
        self._7avg_riat = None
        self._7min_riat = None
        self._7max_riat = None
        self._7std_div_riat = None
        self._7payload_size = None
        self._7total_packet_size = None
        self._7avg_pkts_per_sec = None
        self._7avg_bytes_per_sec = None

    def get_source_ip(self):
        return self._source_ip

    def set_source_ip(self, source_ip):
        self._source_ip = source_ip

    def get_destination_ip(self):
        return self._destination_ip

    def set_destination_ip(self, destination_ip):
        self._destination_ip = destination_ip

    def get_source_port(self):
        return self._source_port

    def set_source_port(self, source_port):
        self._source_port = source_port

    def get_destination_port(self):
        return self._destination_port

    def set_destination_port(self, destination_port):
        self._destination_port = destination_port

    def get_protocol(self):
        return self._protocol

    def set_protocol(self, protocol):
        self._protocol = protocol

    def get_total_pkt_size(self):
        return self._total_pkt_size

    def set_total_pkt_size(self, total_pkt_size):
        self._total_pkt_size = total_pkt_size

    def get_min_pkt_size(self):
        return self._min_pkt_size

    def set_min_pkt_size(self, min_pkt_size):
        self._min_pkt_size = min_pkt_size

    def get_max_pkt_size(self):
        return self._max_pkt_size

    def set_max_pkt_size(self, max_pkt_size):
        self._max_pkt_size = max_pkt_size

    def get_avg_pkt_size(self):
        return self._avg_pkt_size

    def set_avg_pkt_size(self, avg_pkt_size):
        self._avg_pkt_size = avg_pkt_size

    def get_std_div_pkt_size(self):
        return self._std_div_pkt_size

    def set_std_div_pkt_size(self, std_div_pkt_size):
        self._std_div_pkt_size = std_div_pkt_size

    def get_min_iat(self):
        return self._min_iat

    def set_min_iat(self, min_iat):
        self._min_iat = min_iat

    def get_max_iat(self):
        return self._max_iat

    def set_max_iat(self, max_iat):
        self._max_iat = max_iat

    def get_avg_iat(self):
        return self._avg_iat

    def set_avg_iat(self, avg_iat):
        self._avg_iat = avg_iat

    def get_std_div_iat(self):
        return self._std_div_iat

    def set_std_div_iat(self, std_div_iat):
        self._std_div_iat = std_div_iat

    def get_min_riat(self):
        return self._min_riat

    def set_min_riat(self, min_riat):
        self._min_riat = min_riat

    def get_max_riat(self):
        return self._max_riat

    def set_max_riat(self, max_riat):
        self._max_riat = max_riat

    def get_avg_riat(self):
        return self._avg_riat

    def set_avg_riat(self, avg_riat):
        self._avg_riat = avg_riat

    def get_std_div_riat(self):
        return self._std_div_riat

    def set_std_div_riat(self, std_div_riat):
        self._std_div_riat = std_div_riat

    def get_avg_pkts_per_sec(self):
        return self._avg_pkts_per_sec

    def set_avg_pkt_per_sec(self, avg_pkts_per_sec):
        self._avg_pkts_per_sec = avg_pkts_per_sec

    def get_avg_bytes_per_sec(self):
        return self._avg_bytes_per_sec

    def set_avg_bytes_per_sec(self, avg_bytes_per_sec):
        self._avg_bytes_per_sec = avg_bytes_per_sec

    def get_rita_list(self):
        return self._rita_list

    def set_rita_list(self, rita_list):
        self._rita_list = rita_list

    def get_pkt_sizes(self):
        return self._pkt_sizes

    def set_pkt_sizes(self, pkt_sizes):
        self._pkt_sizes = pkt_sizes

    def get_iat_list(self):
        return self._iat_list

    def set_iat_list(self, iat_list):
        self._iat_list = iat_list

    def get_size(self):
        return self._size

    def set_size(self, size):
        self._size = size

    def get_flow_duration(self):
        return self._flow_duration

    def set_flow_duration(self, flow_duration):
        self._flow_duration = flow_duration

    def get_payload_size(self):
        return self._payload_size

    def set_payload_size(self, payload_size):
        self._payload_size = payload_size

    def get_number_of_packects(self):
        return self._number_of_packets

    def set_number_of_packets(self, number_of_packets):
        self._number_of_packets = number_of_packets

    def set_application(self, application):
        self._application = application

    def get_application(self):
        return self._application

    def set_flow(self, flow):
        self._flow = flow

    def get_flow(self):
        return self._flow

    def set_client_or_server(self, client_or_server):
        self._client_or_server = client_or_server

    def get_client_or_server(self):
        return self._client_or_server

    def set_payload(self, payload):
        self._payload = payload

    def get_payload(self):
        return self._payload

    def set_payload_hex(self, payload_hex):
        self._paylod_in_hex = payload_hex

    def get_payload_hex(self):
        return self._paylod_in_hex

    def set_end(self, end):
        self._end = end

    def get_end(self):
        return self._end

    def set_start(self, start):
        self._start = start

    def get_start(self):
        return self._start

    def get_packet_list(self):
        return self._packet_list

    def __str__(self):
        return_string = ""
        # Start
        # return_string += "{0:.2f}".format(round(self.get_min_iat(),2))() + ", "
        return_string += self.get_source_ip() + ","
        return_string += self.get_destination_ip() + ","
        return_string += str(self.get_source_port()) + ","
        return_string += str(self.get_destination_port()) + ","
        return_string += str(self.get_protocol()) + ","
        return_string += str(self.get_avg_iat()) + ","
        return_string += str(self.get_min_iat()) + ","
        return_string += str(self.get_max_iat()) + ","
        return_string += str(self.get_std_div_iat()) + ","
        return_string += str(self.get_avg_riat()) + ","
        return_string += str(self.get_min_riat()) + ","
        return_string += str(self.get_max_riat()) + ","
        return_string += str(self.get_std_div_riat()) + ","
        return_string += str(self.get_avg_pkt_size()) + ","
        return_string += str(self.get_min_pkt_size()) + ","
        return_string += str(self.get_max_pkt_size()) + ","
        return_string += str(self.get_std_div_pkt_size()) + ","
        return_string += str(self.get_total_pkt_size()) + ","
        return_string += str(self.get_flow_duration()) + ","
        return_string += str(self.get_number_of_packects()) + ","
        return_string += str(self.get_avg_pkts_per_sec()) + ","
        return_string += str(self.get_avg_bytes_per_sec()) + ","
        return_string += str(self.get_payload_size()) + ","
        return_string += str(self.get_payload_hex()) + ","

        """return_string += str(self._2avg_iat) + ","
        return_string += str(self._2min_iat) + ","
        return_string += str(self._2max_iat) + ","
        return_string += str(self._2std_div_iat) + ","
        return_string += str(self._2avg_riat) + ","
        return_string += str(self._2min_riat) + ","
        return_string += str(self._2max_riat) + ","
        return_string += str(self._2std_div_riat) + ","
        return_string += str(self._2avg_pkt_size) + ","
        return_string += str(self._2min_pkt_size) + ","
        return_string += str(self._2max_pkt_size) + ","
        return_string += str(self._2std_div_pkt_size) + ","
        return_string += str(self._2total_packet_size) + ","
        return_string += str(self._2payload_size) + ","
        return_string += str(self._2payload_hex) + "," """

        return_string += str(self._3avg_iat) + ","
        return_string += str(self._3min_iat) + ","
        return_string += str(self._3max_iat) + ","
        return_string += str(self._3std_div_iat) + ","
        return_string += str(self._3avg_riat) + ","
        return_string += str(self._3min_riat) + ","
        return_string += str(self._3max_riat) + ","
        return_string += str(self._3std_div_riat) + ","
        return_string += str(self._3avg_pkt_size) + ","
        return_string += str(self._3min_pkt_size) + ","
        return_string += str(self._3max_pkt_size) + ","
        return_string += str(self._3std_div_pkt_size) + ","
        return_string += str(self._3total_packet_size) + ","
        return_string += str(self._3payload_size) + ","
        return_string += str(self._3payload_hex) + ","

        return_string += str(self._4avg_iat) + ","
        return_string += str(self._4min_iat) + ","
        return_string += str(self._4max_iat) + ","
        return_string += str(self._4std_div_iat) + ","
        return_string += str(self._4avg_riat) + ","
        return_string += str(self._4min_riat) + ","
        return_string += str(self._4max_riat) + ","
        return_string += str(self._4std_div_riat) + ","
        return_string += str(self._4avg_pkt_size) + ","
        return_string += str(self._4min_pkt_size) + ","
        return_string += str(self._4max_pkt_size) + ","
        return_string += str(self._4std_div_pkt_size) + ","
        return_string += str(self._4total_packet_size) + ","
        return_string += str(self._4payload_size) + ","
        return_string += str(self._4payload_hex) + ","

        return_string += str(self._5avg_iat) + ","
        return_string += str(self._5min_iat) + ","
        return_string += str(self._5max_iat) + ","
        return_string += str(self._5std_div_iat) + ","
        return_string += str(self._5avg_riat) + ","
        return_string += str(self._5min_riat) + ","
        return_string += str(self._5max_riat) + ","
        return_string += str(self._5std_div_riat) + ","
        return_string += str(self._5avg_pkt_size) + ","
        return_string += str(self._5min_pkt_size) + ","
        return_string += str(self._5max_pkt_size) + ","
        return_string += str(self._5std_div_pkt_size) + ","
        return_string += str(self._5total_packet_size) + ","
        return_string += str(self._5payload_size) + ","
        return_string += str(self._5payload_hex) + ","

        return_string += str(self._6avg_iat) + ","
        return_string += str(self._6min_iat) + ","
        return_string += str(self._6max_iat) + ","
        return_string += str(self._6std_div_iat) + ","
        return_string += str(self._6avg_riat) + ","
        return_string += str(self._6min_riat) + ","
        return_string += str(self._6max_riat) + ","
        return_string += str(self._6std_div_riat) + ","
        return_string += str(self._6avg_pkt_size) + ","
        return_string += str(self._6min_pkt_size) + ","
        return_string += str(self._6max_pkt_size) + ","
        return_string += str(self._6std_div_pkt_size) + ","
        return_string += str(self._6total_packet_size) + ","
        return_string += str(self._6payload_size) + ","
        return_string += str(self._6payload_hex) + ","

        return_string += str(self._7avg_iat) + ","
        return_string += str(self._7min_iat) + ","
        return_string += str(self._7max_iat) + ","
        return_string += str(self._7std_div_iat) + ","
        return_string += str(self._7avg_riat) + ","
        return_string += str(self._7min_riat) + ","
        return_string += str(self._7max_riat) + ","
        return_string += str(self._7std_div_riat) + ","
        return_string += str(self._7avg_pkt_size) + ","
        return_string += str(self._7min_pkt_size) + ","
        return_string += str(self._7max_pkt_size) + ","
        return_string += str(self._7std_div_pkt_size) + ","
        return_string += str(self._7total_packet_size) + ","
        return_string += str(self._7payload_size) + ","
        return_string += str(self._7payload_hex) + ","

        return_string += str(self._application)+'\n'
        # return_string += str(self.get_payload())+"\n"
        # End
        return return_string
