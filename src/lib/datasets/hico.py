from .dataset import HOIDataset


class HICO(HOIDataset):
    num_classes = 80
    num_classes_verb = 117
    dataset_tag = 'hico_det'
    ann_tag = {'train': 'trainval_hico_list.json', 'test': 'test_hico.json'}
    _valid_ids = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13,
        14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
        24, 25, 27, 28, 31, 32, 33, 34, 35, 36,
        37, 38, 39, 40, 41, 42, 43, 44, 46, 47,
        48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
        58, 59, 60, 61, 62, 63, 64, 65, 67, 70,
        72, 73, 74, 75, 76, 77, 78, 79, 80, 81,
        82, 84, 85, 86, 87, 88, 89, 90]
    _valid_ids_verb = list(range(1, 118))
