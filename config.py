from methods import floor, nroot, reverse, isAnagram

# key: string, value: callable
method_table = {
    'floor': floor,
    'nroot': nroot,
    'reverse': reverse,
    'isAnagram': isAnagram,
}

# key: string, value: type objects list
expected_types = {
    'floor': [float],
    'nroot': [int, int],
    'reverse': [str],
    'isAnagram': [str, str],
}

methods_info = {
    'floor': {
        'description': 'Returns the nearest integer by rounding down.',
        'params': 'double x',
        'return': 'int',
    },
    'nroot': {
        'description': 'Computes the value of r in the equation x = r^n.',
        'params': 'int n, int x',
        'return': 'int',
    },
    'reverse': {
        'description': 'Returns a new string that is the reverse of the input string.',
        'params': 'string s',
        'return': 'string',
    },
    'isAnagram': {
        'description': 'Checks if two strings are anagrams of each other.',
        'params': 'string s1, string s2',
        'return': 'bool',
    },
}