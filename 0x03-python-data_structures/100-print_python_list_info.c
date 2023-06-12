#include "Python.h"

/**
 * print_python_list_info - C function to print basic about Python lists
 * @p: A Python List Object
 * Description: The function first allocates memory with the appropriate
 * The "PyObject*" is a pointer to a struct, used to represent a python object
 * as everything is an object in the Python language.
 *
 * The Py_ssize_t is the data type used for numerical values
 * and is usually same size as long integers.
 *
 * The PyTypeObject is a structure that defines a new type.
 * They store a large number of value, each of which implement
 * a small part of the type's functionality. They can be used to get
 * information about a particular PyObject. E.g the name of the type
 *
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t i = 0, len, alloc;
	PyObject *item;
	PyTypeObject *item_type;
	const char *item_type_name;

	if (PyList_Check(p))
		len = PyList_Size(p);
	else
		return;

	alloc = ((PyListObject *)(p))->allocated;

	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", alloc);
	for (i = 0; i < len; i++)
	{
		item = PyList_GetItem(p, i);
		item_type = Py_TYPE(item);
		item_type_name = item_type->tp_name;

		printf("Element %ld: %s\n", i, item_type_name);
	}
}
