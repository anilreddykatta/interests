#!/usr/bin/env python
import FlowExtractor
import FileHandler
import PacketExtractor


def main():
    packet_informations = PacketExtractor.Extractor().read_file("facebook-chrome-1.pcap")
    flow_extractor = FlowExtractor.FlowConstructor()
    count = 0
    for i_packet_information in packet_informations:
        if i_packet_information.get_ending_packet():
            count += 1
    returned_map = flow_extractor.construct_flow(packet_informations)
    FileHandler.FileHandler('output.csv').write_to_file(returned_map)

if __name__ == '__main__':
    main()
