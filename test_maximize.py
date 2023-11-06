import maximize


def test_f():
    assert maximize.f(0) == 0


def test_maximize():
    assert maximize.maximize(maximize.f, maximize.a, maximize.b, maximize.epsilon)[1] > 0
    assert maximize.f(maximize.maximize(maximize.f, maximize.a, maximize.b, maximize.epsilon)[0]) >= maximize.f((maximize.a + maximize.b) / 2)
    assert maximize.maximize(maximize.f, maximize.a, maximize.b, maximize.epsilon)[0] <= maximize.b
    assert maximize.maximize(maximize.f, maximize.a, maximize.b, maximize.epsilon)[0] >= maximize.a
