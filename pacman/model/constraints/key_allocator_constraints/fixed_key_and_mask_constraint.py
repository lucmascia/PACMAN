from .abstract_key_allocator_constraint import AbstractKeyAllocatorConstraint
from pacman.model.routing_info import BaseKeyAndMask
from pacman.exceptions import PacmanConfigurationException


class KeyAllocatorFixedKeyAndMaskConstraint(AbstractKeyAllocatorConstraint):
    """ Key allocator constraint that fixes the key and mask of an edge
    """

    __slots__ = [
        # The key and mask combinations to fix
        "_keys_and_masks",

        #  Optional function which will be called to translate the
        # keys_and_masks list into individual keys If missing, the keys will
        # be generated by iterating through the keys_and_masks list directly.
        #  The function parameters are:
        #           An iterable of keys and masks
        #           A machine edge
        #           Number of keys to generate (may be None)
        "_key_list_function"

    ]

    def __init__(self, keys_and_masks, key_list_function=None):
        """

        :param keys_and_masks: The key and mask combinations to fix
        :type keys_and_masks: iterable of\
                    :py:class:`pacman.model.routing_info.BaseKeyAndMask`
        :param key_list_function: Optional function which will be called to\
                    translate the keys_and_masks list into individual keys.\
                    If missing, the keys will be generated by iterating\
                    through the keys_and_masks list directly.  The function\
                    parameters are:
                    * An iterable of keys and masks
                    * A machine edge
                    * Number of keys to generate (may be None)
        :type key_list_function: (iterable of\
                    :py:class:`pacman.model.routing_info.BaseKeyAndMask`,\
                    :py:class:`pacman.model.graph.machine.MachineEdge`,
                    int)\
                    -> iterable of int
        """
        for keys_and_mask in keys_and_masks:
            if not isinstance(keys_and_mask, BaseKeyAndMask):
                raise PacmanConfigurationException(
                    "the keys and masks object contains a object that is not"
                    "a key_and_mask object")

        self._keys_and_masks = keys_and_masks
        self._key_list_function = key_list_function

    @property
    def keys_and_masks(self):
        """ The keys and masks to be fixed

        :return: An iterable of key and mask combinations
        :rtype: iterable of\
                    :py:class:`pacman.model.routing_info.BaseKeyAndMask`
        """
        return self._keys_and_masks

    @property
    def key_list_function(self):
        """ A function to call to generate the keys

        :return: A python function, or None if the default function can be used
        """
        return self._key_list_function

    def __repr__(self):
        return (
            "KeyAllocatorFixedKeyAndMaskConstraint("
            "keys_and_masks={}, key_list_function={})".format(
                self._keys_and_masks, self.key_list_function))

    def __eq__(self, other):
        if not isinstance(other, KeyAllocatorFixedKeyAndMaskConstraint):
            return False
        if other.key_list_function != self._key_list_function:
            return False
        for key_and_mask in self._keys_and_masks:
            if key_and_mask not in other.keys_and_masks:
                return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return (
            frozenset(self._keys_and_masks),
            self._key_list_function).__hash__()
