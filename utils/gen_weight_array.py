def gen_weight_table_array(dict_of_weights):
    """
    given a dictionary of {'key': weight}, produce a 1d array
    with n elements of each 'key' where n is the weight.

    this allows for random.choice to be called on the array
    to provide weighted rng
    :param dict_of_weights: {'str': int}
    :return: ['str'*int]
    """

    wt_as_array = []
    for key in dict_of_weights:
        for x in range(dict_of_weights[key]):
            wt_as_array.append(key)

    return wt_as_array
