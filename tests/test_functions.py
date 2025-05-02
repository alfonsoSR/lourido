from nastro import catalog as nc
from lourido import get_sun_mass, get_earth_mu


def test_earth():

    assert get_earth_mu() == nc.Earth.mu


def test_sun():

    assert get_sun_mass() == nc.Sun.mass
