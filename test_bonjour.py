from bonjour import saluer


def test_saluer_safae():
    assert saluer("Safae") == "Bonjour Safae"


def test_saluer_vide():
    assert saluer("") == "Bonjour "