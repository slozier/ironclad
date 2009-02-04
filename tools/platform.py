

type_codes = {
    # trivial
    'void': # no return value
        'void',
    'noargs': # er, no args
        '',
    
    # special
    'str': # char*s; marshalled into strings
        'string',
    'obj': # PyFoo*s; needs to be stored/retrieved/cleaned up
        'object',
    'cpx': # Py_complex, defined in Python25Structs.cs
        'Py_complex',
    
    # platform-specific C types
    'ptr': # unknown ptr types; not translated
        'IntPtr',
    'size': # Py_ssize_t -- should obviously be uint, but complications arose
        'uint',
    'int': # int
        'int',
    'long': # long
        'int',
    'llong': # long long
        'long',
    'uint': # unsigned int
        'uint',
    'ulong': # unsigned long
        'uint',
    'ullong': # unsigned long long
        'ulong',
    'double': # double
        'double',
}

