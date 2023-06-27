#include "Python.h"
#include <float.h>

/**
 * print_python_float - Function to print info about Python Float
 * @p: A Python Object
 */
void print_python_float(PyObject *p)
{
	double v;
	char *v_str = NULL;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (!(PyFloat_Check(p)))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	v = PyFloat_AsDouble(p);
	v_str = PyOS_double_to_string(v, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", v_str);
	PyMem_Free(v_str);
}

/**
 * print_python_bytes - C function to print basic about Python lists
 * @p: A Python List Object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t len, i, len_to_pr;
	char *byte_str;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
		len = ((PyVarObject *)p)->ob_size;
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	byte_str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", len);
	printf("  trying string: %s\n", byte_str);

	len_to_pr = len <= 10 ? len + 1 : 10;
	printf("  first %ld bytes: ", len_to_pr);

	for (i = 0; i < len_to_pr - 1; i++)
		printf("%02hhx ", byte_str[i]);
	printf("%02hhx\n", byte_str[i]);
}



/**
 * print_python_list - C function to print basic about Python lists
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

void print_python_list(PyObject *p)
{
	Py_ssize_t i = 0, len, alloc;
	PyObject *item;
	PyTypeObject *item_type;
	PyListObject *e_list;
	const char *item_type_name;


	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (PyList_Check(p))
		len = ((PyVarObject *) p)->ob_size;
	else
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	e_list = (PyListObject *) p;
	alloc = (e_list)->allocated;

	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", alloc);
	for (i = 0; i < len; i++)
	{
		item = e_list->ob_item[i];
		item_type = item->ob_type;
		item_type_name = item_type->tp_name;
		printf("Element %ld: %s\n", i, item_type_name);

		if (strcmp(item_type_name, "bytes") == 0)
			print_python_bytes(item);
		else if (strcmp(item_type_name, "float") == 0)
			print_python_float(item);
	}
}
