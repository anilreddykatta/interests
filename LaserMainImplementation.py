__author__ = 'KattaAnil'

import os
import PacketExtractor, FlowExtractor
from laserimplementation import  Laser
import FileHandler

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

def main(file_path, output_file):
    only_files = get_filepaths(file_path)
    print(only_files)
    packet_informations = []
    for file_name in only_files:
        packet_informations.extend(PacketExtractor.Extractor().read_file(file_name))
    flow_extractor = FlowExtractor.FlowConstructor()
    count = 0
    #packet_informations.sort(key=lambda x:x.get_payload_size())

    for i_packet_information in packet_informations:
        if i_packet_information.get_ending_packet():
            count += 1
    returned_map = flow_extractor.construct_flow(packet_informations)
    flow_informations = returned_map.values()
    flow_informations.sort(key=lambda x:x.get_payload_size())
    FileHandler.FileHandler(output_file+'.csv').write_to_file(returned_map)
    laser = Laser(returned_map.values())
    print(laser.signature_generation())

def init():
    for root, directories, files in os.walk("./input"):
        for dir in directories:
            dir_path = os.path.join(root, dir)
            for root, directories, files in os.walk(dir_path):
                for inner_dir in directories:
                    inner_dir_path = os.path.join(root, inner_dir)
                    print("Processing "+str(inner_dir))
                    only_files = main(inner_dir_path, inner_dir)
                    print("Processing Complete Of "+str(inner_dir))

if __name__=='__main__':
    init()