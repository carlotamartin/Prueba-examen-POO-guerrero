# Source packages.

class Warrior():
    """Python class to implement a basic version of a warrior of the game.

    This Python class implements the basic version of a warrior of the game.

    Syntax
    ------
      obj = Warrior(id, warrior_type, weapon_type, health_points,
                    attack_rating, defense_rating)

    Parameters
    ----------
      [in] id Id of warrior.
      [in] warrior_type Type of warrior.
      [in] weapon_type Type of weapon that carries out the warrior.
      [in] health_points Points of health that the warrior has.
      [in] attack_rating Attack rating of the warrior.
      [in] defense_rating Defense rating of the warrior.

    Returns
    -------
      obj Python object output parameter that represents an instance
          of the class Warrior.

    Attributes
    ----------

    Example
    -------
      >>> from warrior import Warrior
      >>> from warrior_type import WarriorType
      >>> from weapon_type import WeaponType
      >>> obj_Warrior = Warrior(1, WarriorType.GLADIATOR, WeaponType.SWORD, 100, 7, 10)
    """

def main():
    """Function main of the module.

    The function main of this module is used to test the Class Warrior.

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
    print("Test Case 1: Create a Warrior.")
    print("=================================================================.")
    warrior1 = Warrior(1,WarriorType.GLADIATOR, WeaponType.SWORD, 100, 8, 9)

    if warrior1.get_warrior_type().name == "GLADIATOR":
        print("Test PASS. The parameter warrior_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if warrior1.get_weapon_type().name == "SWORD":
        print("Test PASS. The parameter weapon_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if warrior1.get_health_points() == 100:
        print("Test PASS. The parameter health_points has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if warrior1.get_attack_rating() == 8:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if warrior1.get_defense_rating() == 9:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    warrior2 = Warrior(2,WarriorType.GLADIATOR, WeaponType.SWORD, 100, 7, 10)

    if str(warrior2) == "GLADIATOR with a SWORD":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__().")


    print("=================================================================.")
    print("Test Case 3: Warrior alive?¿?.")
    print("=================================================================.")
    warrior3 = Warrior(3,WarriorType.UFC, WeaponType.KICK, 97, 8, 9)

    if warrior3.is_alive():
        warrior3.fight_defense(200)  # With this the warrior should be retired.

        if not warrior3.is_alive():
            print("Test PASS. The method is_alive() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method is_alive().")
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    warrior4 = Warrior(4,WarriorType.MMA, WeaponType.ELBOW, 93, 9, 6)

    warrior4.fight_defense(70)

    if warrior4.get_health_points() == 29:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    warrior5 = Warrior(5,WarriorType.BOXER, WeaponType.PUNCH, 99, 10, 7)
    warrior6 = Warrior(6,WarriorType.BOXER, WeaponType.PUNCH, 99, 9, 8)

    warrior_hit = warrior5.fight_attack(warrior6)

    if warrior_hit:
        if warrior6.get_health_points() == 97:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")
    else:
        if warrior6.get_health_points() == 99:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")



# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
