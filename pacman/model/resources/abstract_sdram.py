from six import add_metaclass

from spinn_utilities.abstract_base import AbstractBase, abstractmethod


@add_metaclass(AbstractBase)
class AbstractSDRAM(object):
    """ Represents an amount of SDRAM used on a chip in the\
        machine.
    """

    @abstractmethod
    def get_total_sdram(self):
        """ The total sdram. Or the best quess based on the assume runtime"""
        return self._sdram

    @abstractmethod
    def extend(self, other):
        """
        Combines this SDRAM resource with the other one and creates a new one

        :param other: another  SDRAM resource
        :type other: AbstractSDRAM
        :return: a New AbstractSDRAM
        :rtype AbstractSDRAM
        """