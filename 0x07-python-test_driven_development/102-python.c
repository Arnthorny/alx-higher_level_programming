#include "Python.h"
#include <locale.h>
#include <wchar.h>

/**
 * print_python_string - C function to print basic info about Python strings
 * @p: A Python String Object
 *
 * Description: The wprintf function is notmally used to print
 * wide-character strings but you can't mix it with printf
 * as the latter makes the output stream(stdout) be
 * narrow-oriented while functions like wprintf which are
 * wide I/O function make the stream wide oriented
 *
 * You could use freopen to make the stdout stream "not defined"
 * SYNTAX: freopen(NULL, "w", stdout)
 * But on testing this, I find the buffer to be disoriented.
 *
 * Note: printf with the format specifier %ls can be used to
 * print wide character strings too.
 * All strings to be printed by wprintf must be prefixed by 'L'
 * to tell the compiler thati the string is to be stored with wide chararcters.
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t len, size = 0;
	wchar_t *str;

	printf("[.] string object info\n");
	if (PyUnicode_Check(p))
		len = PyUnicode_GetLength(p);
	else
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	setlocale(LC_ALL, "C.UTF-8");

	str = PyUnicode_AsWideCharString(p, &size);

	if (!PyUnicode_IS_ASCII(p) && PyUnicode_IS_COMPACT(p))
		printf("  type: compact unicode object\n");
	else if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: unicode object\n");

	printf("  length: %ld\n", len);
	printf("  value: %ls\n", str);

	PyMem_Free(str);
}
