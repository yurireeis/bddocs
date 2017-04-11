# import os
#
# from models.feature import Feature
#
# root_dir = os.getenv('path', 'example')
#
# dirs_and_files = os.walk(root_dir)
#
# for i, (root, sub_dir, file) in enumerate(dirs_and_files):
#     with open('./%s/%s' % (root_dir, file[i]), 'r') as feature_file:
#         feature = Feature()
#         pass
from models.artifact import Artifact

bdd = Artifact('jdasi')
