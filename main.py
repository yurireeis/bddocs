import os

from models.feature import Feature
from language.ptbr import config

root_dir = os.getenv('path', 'example')

feature_list = []

dirs_and_files = os.walk(root_dir)


for i, (root, sub_dir, file) in enumerate(dirs_and_files):
    with open('./%s/%s' % (root_dir, file[i]), 'r') as feature_file:
        feature = Feature(config, feature_file)
        feature.get_feature()
