from mohrscircle_module import *
import pytest


def test_get_sigma_x():
    """sigma_x of MohrsCircle(50, -10, 40) should be 50"""
    assert MohrsCircle(50, -10, 40).get_sigma_x() == 50


def test_get_sigma_y():
    """sigma_y of MohrsCircle(50, -10, 40) should be -10"""
    assert MohrsCircle(50, -10, 40).get_sigma_y() == -10


def test_get_tau_xy():
    """tau_xy of MohrsCircle(50, -10, 40) should be 40"""
    assert MohrsCircle(50, -10, 40).get_tau_xy() == 40


def test_get_sigma_x_valueError():
    """get_sigma_x of MohrsCircle('50', -10, 40) should raise a ValueError"""
    with pytest.raises(ValueError):
        MohrsCircle('50', -10, 40).get_sigma_x()


def test_get_sigma_y_valueError():
    """get_sigma_y of MohrsCircle(50, '-10', 40) should raise a ValueError"""
    with pytest.raises(ValueError):
        MohrsCircle(50, '-10', 40).get_sigma_y()


def test_get_tau_xy_valueError():
    """tau_xy of MohrsCircle(50, -10, "40") should raise a Value error"""
    with pytest.raises(ValueError):
        MohrsCircle(50, -10, '40').get_tau_xy()


def test_sigma_avg():
    """tau_xy of MohrsCircle(50, -10, 40) should be 20"""
    assert MohrsCircle(50, -10, 40).sigma_avg() == 20