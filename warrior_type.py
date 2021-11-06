# Source packages.


class WarriorType():
    """Python class to implement an enumeration for the attribute Warrior Type.

    This Python class implements an enumeration for the attribute Warrior Type.

    Syntax
    ------
      obj = WarriorType.Enum

    Parameters
    ----------

    Returns
    -------
      obj Python object output parameter that represents an instance
          of the class WarriorType.

    Attributes
    ----------

    Example
    -------
      >>> from warrior_type import WarriorType
      >>> obj_WarriorType = WarriorType.Boxer
    """

def main():
    """Function main of the module.

    The function main of this module is used to test the Class WarriorType.

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

    print("=================================================================.")
    print("Test Case 1: Check Class WarriorType.")
    print("=================================================================.")

    if isinstance(WarriorType.BOXER, WarriorType):
        print("Test PASS. The enum for Boxer has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(WarriorType.GLADIATOR, WarriorType):
        print("Test PASS. The enum for Gladiator has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(WarriorType.UFC, WarriorType):
        print("Test PASS. The enum for UFC has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(WarriorType.MMA, WarriorType):
        print("Test PASS. The enum for MMA has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
