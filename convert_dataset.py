import xml.etree.ElementTree as ET
import os
import shutil


def main():
    anno_dir = "/home2/lgfm95/ILSVRC/Annotations/CLS-LOC/val/"
    data_dir_orig = "/home2/lgfm95/ILSVRC/Data/CLS-LOC/val/1"
    data_dir_new = "/home2/lgfm95/ILSVRC/Data/CLS-LOC/val/full"
    for file in os.listdir(data_dir_orig):
        print(file)
        file_name = file[:-4]
        val_name = file_name + ".xml"
        class_label = get_class_label(anno_dir + val_name)
        if not os.path.isdir(os.path.join(data_dir_new, class_label)):
            os.mkdir(os.path.join(data_dir_new, class_label))
        shutil.copy(os.path.join(data_dir_orig, file), os.path.join(data_dir_new, class_label, file))


def get_class_label(anno_path):
    tree = ET.parse(anno_path)
    root = tree.getroot()
    print(root)
    object_1 = root.find("object") # get first object
    name = object_1.find("name").text
    print(name)
    return name


if __name__ == "__main__":
    main()
