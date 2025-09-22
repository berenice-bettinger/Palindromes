"""
Module pour vérifier si une chaîne est un palindrome.
"""

#### Fonction secondaire


def ispalindrome(s):
    """Retourne True si s est un palindrome, False sinon."""
    return s == s[::-1]

#### Fonction principale


def main():
    """Fonction principale pour tester la détection de palindrome."""
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
