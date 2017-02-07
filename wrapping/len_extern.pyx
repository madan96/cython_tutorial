# Wrapping external C functions for use in Python

cdef extern from "string.h":
    int strlen(char *c)


def get_len(char *message):
    return strlen(message)