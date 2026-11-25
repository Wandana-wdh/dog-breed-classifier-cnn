from os import listdir


def get_pet_labels(image_dir):
    results_dic = dict()
    for filename in listdir(image_dir):
        if filename.startswith('.'):
            continue
        words = filename.lower().split('_')
        pet_label = ' '.join(word for word in words if word.isalpha()).strip()
        if filename not in results_dic:
            results_dic[filename] = [pet_label]
        else:
            print("** Warning: Duplicate file exists in directory:", filename)
    return results_dic
