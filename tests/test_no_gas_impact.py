
def test_if_greater_equal(new_nogasimpact, owner):
    new_nogasimpact.if_greater1(7, sender=owner)
    new_nogasimpact.if_greater1(3, sender=owner)

def test_if_greater(new_nogasimpact, owner):
    new_nogasimpact.if_greater2(3, sender=owner)
    new_nogasimpact.if_greater2(7, sender=owner)

def test_compare_initializer_bool(new_compare_init_bool, owner):
    new_compare_init_bool.uninitialize(sender=owner)
    new_compare_init_bool.reinitialize(sender=owner)
    assert new_compare_init_bool.is_initialized(sender=owner)

def test_compare_initializer_int(new_compare_init_int, owner):
    new_compare_init_int.uninitialize(sender=owner)
    new_compare_init_int.reinitialize(sender=owner)
    assert new_compare_init_int.is_initialized(sender=owner)
