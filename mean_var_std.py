import numpy as np


def calculate(l):
    if len(l) != 9 or not all([isinstance(item, int) for item in l]):
        raise ValueError("List must contain nine numbers.")
    else:
        tab = np.array([l[:3], l[3:6], l[6:]])
        calculations = {}
        """Moyenne"""
        mean_axe1 = [(tab[0][i] + tab[1][i] + tab[2][i]) / 3 for i in range(3)]
        mean_axe2 = [(tab[i][0] + tab[i][1] + tab[i][2]) / 3 for i in range(3)]
        calculations['mean'] = [mean_axe1, mean_axe2, np.average(tab)]
        """Variance"""
        variance_axe1 = [np.var([tab[0][i], tab[1][i], tab[2][i]]) for i in range(3)]
        variance_axe2 = [np.var(item) for item in tab]
        calculations['variance'] = [variance_axe1, variance_axe2, np.var(tab)]
        """Ecart-type"""
        std_axe1 = [np.std([tab[0][i], tab[1][i], tab[2][i]]) for i in range(3)]
        std_axe2 = [np.std(item) for item in tab]
        calculations['standard deviation'] = [std_axe1, std_axe2, np.std(tab)]
        """Max"""
        max_axe1 = [np.max([tab[0][i], tab[1][i], tab[2][i]]) for i in range(3)]
        max_axe2 = [np.max(item) for item in tab]
        calculations['max'] = [max_axe1, max_axe2, np.max(tab)]
        """Min"""
        min_axe1 = [np.min([tab[0][i], tab[1][i], tab[2][i]]) for i in range(3)]
        min_axe2 = [np.min(item) for item in tab]
        calculations['min'] = [min_axe1, min_axe2, np.min(tab)]
        """Sum"""
        sum_axe1 = [np.sum([tab[0][i], tab[1][i], tab[2][i]]) for i in range(3)]
        sum_axe2 = [np.sum(item) for item in tab]
        calculations['sum'] = [sum_axe1, sum_axe2, np.sum(tab)]
        return calculations
