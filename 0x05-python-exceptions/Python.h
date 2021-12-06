#ifndef PYTHON_H
#define PYTHON_H
#include <stdio.h>
#include <stdlib.h>
/**
 * @C- Fucntin that print some basic info about python list
 * python bytes 
 * and python float objects
 */
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
#endif /* #ifndef PYTHON_H */
