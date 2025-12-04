class GoalUtility:
    """
    Implements the piece-wise linear utility function for goals.
    Reference: Section 3.2.3 and Figure 4.
    """
    def __init__(self, min_h, acc_s, des_g, weights):
        self.h = min_h # Minimum (Poverty line)
        self.s = acc_s # Acceptable
        self.g = des_g # Desirable
        self.w1, self.w2, self.w3 = weights # Slopes/Priorities

    def calculate_utility(self, spending):
        u = 0.0
        # Zone 1: Below Minimum
        if spending <= self.h:
            return self.w1 * (spending - self.h)
            
        # Zone 2: Min -> Acceptable
        val_in_zone2 = min(spending, self.s) - self.h
        u += self.w1 * val_in_zone2
        
        if spending <= self.s: return u
            
        # Zone 3: Acceptable -> Desirable
        val_in_zone3 = min(spending, self.g) - self.s
        u += self.w2 * val_in_zone3
        
        if spending <= self.g: return u
            
        # Zone 4: Above Desirable
        val_in_zone4 = spending - self.g
        u += self.w3 * val_in_zone4
        return u