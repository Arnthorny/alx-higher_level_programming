#!/usr/bin/python3
"""
This module defines the class Node of a singly linked list.
It also defines the class SinglyLinkedList for a singly linked list
"""


def detIndex(head, value):
    """
    This function determines the index to place a given "value"
    inside of a singly linked list

    Args:
        head (Node): The head of the singly linked list
        value (int): Data of node to be inserted

    Returns:
        int: The index to place given Node
    """
    i = 0
    tmp = head
    while tmp:
        if tmp.data <= value:
            tmp = tmp.next_node
        else:
            return i
        i += 1
    return i


class Node:
    """
    A class that defines the node in a singly linked list.

    Args:
        data (int): Data contained in node
        next_node (:obj:`Node`, optional): Next node to point to

    Attributes:
        __data (int): Data contained in node
        __next_node (Node): Next node to point to
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """int: Getter to get the value of data"""
        return self.__data

    @data.setter
    def data(self, value):
        if (type(value) != int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Node: Getter to get the next_node object

        The setter raises a TypeError if value passed is not
        a Node object
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if (type(value) == self.__class__ or value is None):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """
    A class that defines a singly linked list.

    Attributes:
        __head (Node): Head of singly linked list
    """

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into correct sorted positon
        in the list (increasing order)
        """
        i = 0
        new = Node(value, self.__head)
        if self.__head is None:
            self.__head = new
        else:
            curr = self.__head
            index = detIndex(curr, value)
            while (curr is not None):
                if (i == index == 0):
                    new.next_node = self.__head
                    self.__head = new
                    break
                elif i == index - 1:
                    new.next_node = curr.next_node
                    curr.next_node = new
                    break
                else:
                    i += 1
                    curr = curr.next_node

    def __str__(self):
        """
        This prints the entire list, each node on one line
        to stdout.
        """
        tmp = self.__head
        tmp_str = ""
        while (tmp):
            tmp_str += "{:d}".format(tmp.data)
            if (tmp := tmp.next_node):
                tmp_str += "\n"
        return (tmp_str)
