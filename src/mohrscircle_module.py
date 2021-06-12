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
        return ""

    def max_principal_stress(self):
        """max_principal_stress returns the max principal stress"""
        return ""

    def min_principal_stress(self):
        """min_principal_stress returns the min principal stress"""
        return ""

    def principal_angle(self):
        """principal_angle returns the principle angle in degrees"""
        return ""

    def shear_angle(self):
        """shear_angle returns the shear angle in degrees"""
        return ""
