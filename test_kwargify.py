from kwargify import kwargify as _

def test_kwargifies_all_positional_args():
    foo, bar, baz = 1, 2, 'three'
    assert _(foo, bar, baz) == dict(foo=1, bar=2, baz='three')

def test_kwargifies_with_some_kwargs():
    foo, bar, baz = 1, 2, 'three'
    assert _(foo, bar, wibble=baz) == dict(foo=1, bar=2, wibble='three')


thing = 7

def test_using_nonlocal():
    foo, bar, baz = 1, 2, 'three'
    assert _(foo, bar, thing, wibble=baz) == dict(foo=1, bar=2, thing=7, wibble='three')

