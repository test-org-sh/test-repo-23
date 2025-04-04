from scipy.stats import hypergeom
from math import comb

class HypergeometricCalculator:
    def __init__(self, N=None, K=None, n=None, k=None, name="Hypergeometric Probability"):
        """
        Initialize the HypergeometricCalculator with optional parameters.
        
        Parameters:
        N (int): Total population size
        K (int): Number of success states in the population
        n (int): Number of draws (sample size)
        k (int): Number of observed successes
        name (str): Description of the probability being calculated
        """
        self.N = N  # Total population
        self.K = K  # Success states in population
        self.n = n  # Sample size
        self.k = k  # Required successes
        self.name = name  # Description of the probability
        
    def set_parameters(self, N, K, n, k, name=None):
        """Set the parameters for the hypergeometric calculation."""
        self.N = N
        self.K = K
        self.n = n
        self.k = k
        if name is not None:
            self.name = name
        
    def get_user_inputs(self):
        """Get parameters from user input."""
        self.name = input("Enter a description of the probability being calculated\n-> ")
        self.N = int(input("Enter the total population size (N)\n-> "))
        self.K = int(input("Enter the number of successes in the total population (K)\n-> "))
        self.n = int(input("Enter the sample size (n)\n-> "))
        self.k = int(input("Enter the number of successes required (k)\n-> "))
        
    def validate_inputs(self):
        """Validate that all inputs meet the requirements for hypergeometric calculation."""
        if None in (self.N, self.K, self.n, self.k):
            raise ValueError("All parameters must be set before calculating")
        if not all(isinstance(x, int) for x in [self.N, self.K, self.n, self.k]):
            raise ValueError("All parameters must be integers")
        if any(x < 0 for x in [self.N, self.K, self.n, self.k]):
            raise ValueError("All parameters must be non-negative")
        if self.n > self.N or self.K > self.N or self.k > self.n:
            raise ValueError("Invalid parameter combinations")
            
    def calculate_probability(self):
        """
        Calculate the exact probability of k successes.
        
        Returns:
        float: The probability of exactly k successes
        """
        self.validate_inputs()
        return hypergeom.pmf(self.k, self.N, self.K, self.n)
        
    def calculate_all_probabilities(self):
        """
        Calculate probabilities for less than k, exactly k, and more than k successes.
        
        Returns:
        tuple: (P(X < k), P(X = k), P(X > k))
        """
        self.validate_inputs()
        
        prob_exact = hypergeom.pmf(self.k, self.N, self.K, self.n)
        prob_less = hypergeom.cdf(self.k - 1, self.N, self.K, self.n)
        prob_more = 1 - (prob_less + prob_exact)
        
        return prob_less, prob_exact, prob_more
    
    def display_probabilities(self):
        """Display the probability results in a formatted table."""
        try:
            prob_less, prob_exact, prob_more = self.calculate_all_probabilities()
            
            print(f"\n{self.name}")
            print(f"Total population size: {self.N}, with {self.K} success states in population")
            print(f"Number of draws: {self.n}, with a target number of {self.k} successes")
            
            # Calculate the width needed for centering
            line_width = 80
            column_width = 22
            
            # Create the column headers and values with consistent spacing
            headers = [f"Less than {self.k}", f"Exactly {self.k}", f"More than {self.k}"]
            values = [f"{prob_less*100:.2f}", f"{prob_exact*100:.2f}", f"{prob_more*100:.2f}"]
            
            # Format each column with equal spacing
            header_line = "- " + " - ".join(f"{h:^{column_width}}" for h in headers) + " -"
            values_line = "- " + " - ".join(f"{v:^{column_width}}" for v in values) + " -"
            
            print(header_line.center(line_width))
            print(values_line.center(line_width))
            
        except ValueError as e:
            print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    # Example with direct parameter setting
    calc = HypergeometricCalculator()

    """
    calc.set_parameters(N=52, K=13, n=5, k=2, name="Drawing Hearts from a Deck")  # Example: Drawing hearts from a deck
    calc.display_probabilities()
    """    

    calc.set_parameters(N=99, K=22, n=13, k=3, name="Drawing 3 1-drops from a Deck by turn 5")  # Example: Drawing hearts from a deck
    calc.display_probabilities()
    
    calc.set_parameters(N=99, K=10, n=9, k=1, name="Drawing 1 Ramp from a Deck by turn 3")  # Example: Drawing hearts from a deck
    calc.display_probabilities()
    
    calc.set_parameters(N=99, K=37, n=13, k=4, name="Drawing 4 Lands from a Deck by turn 5")  # Example: Drawing hearts from a deck
    calc.display_probabilities()
    
    calc.set_parameters(N=99, K=13, n=13, k=2, name="Drawing 2 Removal from a Deck by turn 5")  # Example: Drawing hearts from a deck
    calc.display_probabilities()
    


    """
    print("\n--- Using input method ---\n")

    # Example with user inputs
    calc2 = HypergeometricCalculator()
    try:
        calc2.get_user_inputs()
        calc2.display_probabilities()
    except ValueError as e:
        print(f"Error: {e}") 
    """
