import math
import numpy
import matplotlib.pyplot


class MohrsCircle():
    def __init__(self, sigma_x, sigma_y, tau_xy):
        """constructor"""
        if not isinstance(tau_xy, int) or not isinstance(sigma_x, int) or not isinstance(sigma_y, int):
            raise ValueError('Please enter an integer')
        self.sigma_x = sigma_x
        self.sigma_y = sigma_y
        self.tau_xy = tau_xy

    def get_sigma_x(self):
        """get_sigma_x returns the normal stress in the x-direction."""
        return self.sigma_x

    def get_sigma_y(self):
        """get_sigma_y returns the normal stress in the x-direction."""
        return self.sigma_y

    def get_tau_xy(self):
        """get_tau_xy returns the shear stress in the xy-direction."""
        return self.tau_xy

    def sigma_avg(self):
        """sigma_avg returns the average normal stress (the center of mohr's circle)"""
        return (self.sigma_x + self.sigma_y) / 2

    def tau_max_xy(self):
        """tau_max_xy returns the max shear stress (radius of mohr's circle)"""
        a = (self.sigma_x - self.sigma_y) / 2
        b = self.tau_xy
        return math.sqrt(a**2 + b**2)

    def max_principal_stress(self):
        """max_principal_stress returns the max principal stress"""
        return self.sigma_avg() + self.tau_max_xy()

    def min_principal_stress(self):
        """min_principal_stress returns the min principal stress"""
        return self.sigma_avg() - self.tau_max_xy()

    def principal_angle(self):
        """principal_angle returns the principle angle in degrees"""
        return math.degrees(math.atan((2*self.tau_xy)/(self.sigma_x - self.sigma_y))) / 2

    def shear_angle(self):
        """shear_angle returns the shear angle in degrees"""
        return (90 - self.principal_angle()*2)/2

    def plot_circle(self):
        radians = numpy.linspace(0, 360, 361) * (2 * numpy.pi/360)
        sigma_x = self.sigma_avg() + self.tau_max_xy() * numpy.cos(radians)
        tau_y = self.tau_max_xy() * numpy.sin(radians)

        matplotlib.pyplot.figure(figsize=[6, 6])
        matplotlib.pyplot.plot(sigma_x, tau_y)
        matplotlib.pyplot.plot(self.sigma_avg(), 0, 'ro')
        matplotlib.pyplot.plot([self.sigma_x, self.sigma_y], [
            self.tau_xy, -self.tau_xy], 'g')

        matplotlib.pyplot.text(self.max_principal_stress(), 0.25,
                               r'$\sigma_{max}$', va='bottom', ha='right', fontsize=12)
        matplotlib.pyplot.text(self.min_principal_stress(), 0.25,
                               r'$\sigma_{min}$', va='bottom', ha='left', fontsize=12)
        matplotlib.pyplot.text(self.sigma_avg(), self.tau_max_xy(),
                               r'$\tau_{max}$', va='top', ha='center', fontsize=12)
        matplotlib.pyplot.text(self.sigma_avg(), 2,
                               r'$\sigma_{avg}$', fontsize=12)

        matplotlib.pyplot.title(
            "Mohr's circle for two-dimensional state of stress")
        matplotlib.pyplot.ylabel(r'$\tau$ (shear stess)')
        matplotlib.pyplot.xlabel(r'$\sigma$ (normal stress)')
        matplotlib.pyplot.axhline(c='k')
        matplotlib.pyplot.axvline(c='k')
        matplotlib.pyplot.grid()
        matplotlib.pyplot.tight_layout()
        matplotlib.pyplot.figtext(.85, .9,
                                  "$\\theta_{}$ = {:.1f}°".format("p", self.principal_angle()))
        matplotlib.pyplot.figtext(.85, .85,
                                  "$\\theta_{}$ = {:.1f}°".format("s", self.shear_angle()))
        matplotlib.pyplot.show()


# x = MohrsCircle(50, -10, 40)
# print(x.sigma_avg())
# print(x.tau_max_xy())
# print(x.max_principal_stress())
# print(x.min_principal_stress())
# print(x.principal_angle())
# print(x.shear_angle())
# x.plot_circle()
