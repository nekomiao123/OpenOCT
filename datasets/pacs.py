import os
from .imagelist import ImageList
from ._util import download as download_data, check_exits

CLASSES = ['dog', 'elephant', 'giraffe', 'guitar', 'horse', 'house', 'person']

class PACS(ImageList):

    def __init__(self, root, task, filter_class, split='all', **kwargs):
        if split == 'all':
            self.image_list = {
                "A": "image_list/art_painting_test_kfold.txt",
                "C": "image_list/cartoon_test_kfold.txt",
                "P": "image_list/photo_test_kfold.txt",
                "S": "image_list/sketch_test_kfold.txt",
            }
        elif split == 'train':
            self.image_list = {
                "A": "image_list/art_painting_train_kfold.txt",
                "C": "image_list/cartoon_train_kfold.txt",
                "P": "image_list/photo_train_kfold.txt",
                "S": "image_list/sketch_train_kfold.txt",
            }
        elif split == 'val':
            self.image_list = {
                "A": "image_list/art_painting_crossval_kfold.txt",
                "C": "image_list/cartoon_crossval_kfold.txt",
                "P": "image_list/photo_crossval_kfold.txt",
                "S": "image_list/sketch_crossval_kfold.txt",
            }

        assert task in self.image_list
        data_list_file = os.path.join(root, self.image_list[task])
        class_names = [CLASSES[i] for i in filter_class]
        
        super(PACS, self).__init__(root, num_classes=len(filter_class), class_names=class_names, data_list_file=data_list_file,
                                       filter_class=filter_class, **kwargs)
        
        # self.classesname = CLASSES[:len(filter_class)]

    # @property
    # def classesname(self):
    #     """Number of classes"""
    #     return self.classesname

