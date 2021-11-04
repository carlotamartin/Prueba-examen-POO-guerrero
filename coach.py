#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python module contains not only the class Coach, but also the test of
this Python class.

@contents :  This module contains not only a single Python class, but also the
             test cases to probe its functionality.
@project :  N/A
@program :  N/A
@file :  coach.py
@author :  Antonio Artes Garcia (antonio.artesgarcia@ceu.es)
           Alberto Gil De la Fuente (alberto.gildelafuente@ceu.es)

@version :  0.0.1, 04 January 2021
@information :  The Zen of Python
                  https://www.python.org/dev/peps/pep-0020/
                Style Guide for Python Code
                  https://www.python.org/dev/peps/pep-0008/
                Example NumPy Style Python Docstrings
                  http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html
                doctest – Testing through documentation
                  https://pymotw.com/2/doctest/

@copyright :  Copyright 2021 GNU AFFERO GENERAL PUBLIC.
              All rights are reserved. Reproduction in whole or in part is
              prohibited without the written consent of the copyright owner.
"""


# Source packages.


class Coach:
    """Python class to implement a Coach which owns a set of warriors in the Game.

    This Python class implements a coach of the Game. Each coach owns a set of
    warriors in the Game.

    Syntax
    ------
      obj = Coach(coach_name, set_of_warriors)

    Parameters
    ----------
      [in] coach_name Name of the Coach.
      [in] set_of_warrior Set of warriors handled by the Coach.

    Returns
    -------
      obj Python object output parameter that represents an instance
          of the class Coach.

    Attributes
    ----------

    Example
    -------
      >>> from user import User
      >>> obj_Coach = Coach()
    """


def main():
    """Function main of the module.

    The function main of this module is used to test the Class Coach.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """
    from warrior_type import WarriorType
    from weapon_type import WeaponType
    print("=================================================================.")
    print("Test Case 1: Create a Coach with an empty list.")
    print("=================================================================.")
    coach1_warriors = []
    try:
        coach1 = Coach("", coach1_warriors)
        print("Test FAIL. It should raise a ValueError exception. Check the method __init__() based on the object: " + str(coach1))
    except ValueError as value_error:
        print("Test PASS. The exception was raised: " + str(value_error) + " .")


    print("=================================================================.")
    print("Test Case 2: Create a Coach with a NON empty list.")
    print("=================================================================.")
    warrior1 = Warrior(1, WarriorType.BOXER, WeaponType.KICK, 99, 10, 7)
    warrior2 = Warrior(2, WarriorType.BOXER, WeaponType.KICK, 99, 9, 8)
    coach2_warriors = []
    coach2_warriors.append(warrior1)
    coach2_warriors.append(warrior2)
    try:
        coach2 = Coach("Rocky Balboa", coach2_warriors)
        print("The following coach has been generated: " + str(coach2))
        print("Test PASS. The method __init__() has been implemented correctly.")
    except ValueError as value_error:
        print("Test FAIL. Check the method __init__(): " + str(value_error))


    print("=================================================================.")
    print("Test Case 3: Human-readable format of the object.")
    print("=================================================================.")
    coach3_warriors = []
    coach3_warriors.append(warrior1)
    coach3_warriors.append(warrior2)
    coach3 = Coach("Rocky Balboa", coach3_warriors)

    if str(coach3) == "Rocky Balboa with 2 warriors.":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__().")


    print("=================================================================.")
    print("Test Case 4: Coach undefeated?¿?.")
    print("=================================================================.")
    coach4_warriors = []
    coach4_warriors.append(warrior1)
    coach4_warriors.append(warrior2)
    coach4 = Coach("Rocky Balboa", coach3_warriors)

    if coach4.is_undefeated():
        print("Test PASS. The method is_undefeated() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method is_undefeated().")

    coach4.surrender()

    if coach4.is_undefeated():
        print("Test FAIL. Check the method is_undefeated().")
    else:
        print("Test PASS. The method is_undefeated() has been implemented correctly.")


# Checking whether this script is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
