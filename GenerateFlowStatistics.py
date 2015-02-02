from posixfile import _posixfile_

__author__ = 'KattaAnil'

#!/usr/bin/env python

import os
import PacketExtractor, FlowExtractor
from laserimplementation import  Laser
import FileHandler
import re

regular_expression_map = {}


def init_regular_expression_map():
    """    :rtype : object
    """
    regular_expression_map["Armagetron"] = re.compile("YCLC_E|CYEL")
    regular_expression_map["battlefield1942"] = re.compile("^\x01\x11\x10\|\xf8\x02\x10\x40\x06")
    regular_expression_map["battlefield2"] = re.compile("^(\x11\x20\x01...?\x11|\xfe\xfd.?.?.?.?.?.?(\x14\x01\x06|\xff\xff\xff))|[]\x01].?battlefield2")
    regular_expression_map["battlefield2142"] = re.compile("^(\x11\x20\x01\x90\x50\x64\x10|\xfe\xfd.?.?.?(\x18))|[]\x01].?battlefield2")
    regular_expression_map["bittorrent"] = re.compile("^(\x13bittorrent protocol|azver\x01$|get /scrape\?info_hash=get /announce\?info_hash=|get /client/bitcomet/|GET /data\?fid=)|d1:ad2:id20:|\x08'7P\)[RP]")
    regular_expression_map["bgp"] = re.compile("^\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff..?\x01[\x03\x04]")
    regular_expression_map["citrix"] = re.compile("\x32\x26\x85\x92\x58")
    regular_expression_map["dhcp"] = re.compile("\x32\x26\x85\x92\x58")
    regular_expression_map["dns"] = re.compile("^.?.?.?.?[\x01\x02].?.?.?.?.?.?[\x01-?][a-z0-9][\x01-?a-z]*[\x02-\x06][a-z][a-z][fglmoprstuvz]?[aeop]?(um)?[\x01-\x10\x1c][\x01\x03\x04\xFF]")
    regular_expression_map["edonkey"] = re.compile("^[\xc5\xd4\xe3-\xe5].?.?.?.?([\x01\x02\x05\x14\x15\x16\x18\x19\x1a\x1b\x1c\x20\x21\x32\x33\x34\x35\x36\x38\x40\x41\x42\x43\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58[\x60\x81\x82\x90\x91\x93\x96\x97\x98\x99\x9a\x9b\x9c\x9e\xa0\xa1\xa2\xa3\xa4]|\x59................?[ -~]|\x96....$)")
    regular_expression_map["ftp"] = re.compile("^220.*ftp")
    regular_expression_map["gnutella"] = re.compile("^(gnd[\x01\x02]?.?.?\x01|gnutella connect/[012]\.[0-9]\x0d\x0a|get /uri-res/n2r\?urn:sha1:|get /.*user-agent: (gtk-gnutella|bearshare|mactella|gnucleus|gnotella|limewire|imesh)|get /.*content-type: application/x-gnutella-packets|giv [0-9]*:[0-9a-f]*/|queue [0-9a-f]* [1-9][0-9]?[0-9]?\.[1-9][0-9]?[0-9]?\.[1-9][0-9]?[0-9]?\.[1-9][0-9]?[0-9]?:[1-9][0-9]?[0-9]?[0-9]?|gnutella.*content-type: application/x-gnutella|...................?lime)")
    regular_expression_map["http"] = re.compile("http/(0\.9|1\.0|1\.1) [1-5][0-9][0-9]|post [\x09-\x0d -~]* http/[01]\.[019]")
    regular_expression_map["irc"] = re.compile("^(nick[\x09-\x0d -~]*user[\x09-\x0d -~]*:|user[\x09-\x0d -~]*:[\x02-\x0d -~]*nick[\x09-\x0d -~]*\x0d\x0a)")
    regular_expression_map["jabber"] = re.compile("<stream:stream[\x09-\x0d ][ -~]*[\x09-\x0d ]xmlns=['\"]jabber")
    regular_expression_map["msnmessenger"] = re.compile("ver [0-9]+ msnp[1-9][0-9]? [\x09-\x0d -~]*cvr0\x0d\x0a$|usr 1 [!-~]+ [0-9. ]+\x0d\x0a$|ans 1 [!-~]+ [0-9. ]+\x0d\x0a$")
    regular_expression_map["pop3"] = re.compile("^(\+ok |-err )")
    regular_expression_map["netbios"] = re.compile("\x81.?.?.[A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P][A-P]")
    regular_expression_map["skype"] = re.compile("^..\x02.............")
    regular_expression_map["smtp"] = re.compile("^220[\x09-\x0d -~]* (e?smtp|simple mail)userspace pattern=^220[\x09-\x0d -~]* (E?SMTP|[Ss]imple [Mm]ail)userspace flags=REG_NOSUB REG_EXTENDED")
    regular_expression_map["ssh"] = re.compile("^ssh-[12]\.[0-9]")
    regular_expression_map["svn"] = re.compile("^\( success \( 1 2 \(")
    regular_expression_map["telnet"] = re.compile("^\xff[\xfb-\xfe].\xff[\xfb-\xfe].\xff[\xfb-\xfe]")
    regular_expression_map["worldofwarcraft"] = re.compile("^\x06\xec\x01")
    regular_expression_map["xboxlive"] = re.compile("^\x58\x80........\xf3|^\x06\x58\x4e")
    regular_expression_map["yahoo"] = re.compile("^(ymsg|ypns|yhoo).?.?.?.?.?.?.?[lwt].*\xc0\x80")
    regular_expression_map["vnc"] = re.compile("^rfb 00[1-9]\.00[0-9]\x0a$")


def get_application_name(dir_name_with_extension):
    if len(dir_name_with_extension.split(".")) > 1:
        return dir_name_with_extension.split(".")[-1]
    else:
        return dir_name_with_extension


def get_filepaths(directory):
    """
    This function will generate the file names in a directory
    tree by walking the tree either top-down or bottom-up. For each
    directory in the tree rooted at directory top (including top itself),
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.
    return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.


def generate_stats(output_file_object, list_of_file_paths, p_flow_extractor, packet_extractor):
    for fil in list_of_file_paths:
        packet_information_list = packet_extractor.read_file(fil)
        p_flow_extractor.construct_flow(packet_information_list, output_file_object)


def get_file_paths_with_app_name_map(input_root_dir, output_dir, p_flow_extractor, packet_extractor):
    inner_dirs = [os.path.join(input_root_dir, di) for di in os.listdir(input_root_dir) if
                  os.path.isdir(os.path.join(input_root_dir, di))]
    dir_paths_map = {}
    for dir in inner_dirs:
        inner_inner_dirs = {di : os.path.join(dir, di) for di in os.listdir(dir) if os.path.isdir(os.path.join(dir, di))}
        dir_paths_map.update(inner_inner_dirs)
    for ke in dir_paths_map:
        with open(output_dir+get_application_name(ke)+".csv", 'w', 20) as output_file:
            output_file.write(FileHandler.format_string)
            p_flow_extractor.already_filled_tcp = set()
            p_flow_extractor.already_filled_udp = set()
            generate_stats(output_file, get_filepaths(dir_paths_map[ke]), p_flow_extractor, packet_extractor)


def main():
    init_regular_expression_map()
    flow_extractor = FlowExtractor.FlowConstructor(regular_expression_map)
    packet_extractor = PacketExtractor.Extractor()
    input_dir = '/media/sf_Datasets/GTT'
    output_dir = '/media/sf_Datasets/Output/'
    get_file_paths_with_app_name_map(input_dir, output_dir, flow_extractor, packet_extractor)


if __name__ == '__main__':
    main()
