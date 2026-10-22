from gale_shapley import Person


def test_person_marry():
    a = Person("A", {"B": 1})
    b = Person("B", {"A": 1})
    a.marry(b)
    assert a.oPartner is b
    assert b.oPartner is a
