def adjust_results4_isadog(results_dic, dogfile):
    dognames_dic = dict()
    with open(dogfile, 'r') as infile:
        for line in infile:
            name = line.rstrip().lower().strip()
            if not name:
                continue
            if name not in dognames_dic:
                dognames_dic[name] = 1
            else:
                print("** Warning: Duplicate dogname:", name)

    for key in results_dic:
        pet_is_dog = 1 if results_dic[key][0] in dognames_dic else 0
        classifier_is_dog = 1 if results_dic[key][1] in dognames_dic else 0
        results_dic[key].extend([pet_is_dog, classifier_is_dog])
