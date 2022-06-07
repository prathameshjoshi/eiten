# Basic libraries
import os
import warnings
from strategies.genetic_algo_strategy import GeneticAlgoStrategy
from strategies.maximum_sharpe_ratio_strategy import MaximumSharpeRatioStrategy
from strategies.eigen_portfolio_strategy import EigenPortfolioStrategy
from strategies.minimum_variance_strategy import MinimumVarianceStrategy
from strategies.strategy_helper_functions import StrategyHelperFunctions
warnings.filterwarnings("ignore")

class StrategyManager:
	"""
	Runs and manages all strategies
	"""
	def __init__(self):
		print("\n--= Strategy manager has been created...")
		self.geneticAlgoStrategy = GeneticAlgoStrategy()
		self.minimumVarianceStrategy = MinimumVarianceStrategy()
		self.eigenPortfolioStrategy = EigenPortfolioStrategy()
		self.maximumSharpeRatioStrategy = MaximumSharpeRatioStrategy()
		self.strategyHelperFunctions = StrategyHelperFunctions()

	def calculate_genetic_algo_portfolio(self, symbols, returns_matrix_percentages):
		"""
		Genetic algorithm based portfolio that maximizes sharpe ratio. This is my own implementation
		"""
		print("-* Calculating portfolio weights using genetic algorithm...")
		return self.geneticAlgoStrategy.generate_portfolio(
		    symbols, returns_matrix_percentages)

	def calculate_eigen_portfolio(self, symbols, covariance_matrix, eigen_portfolio_number):
		"""
		2nd Eigen Portfolio
		"""
		print("-$ Calculating portfolio weights using eigen values...")
		return self.eigenPortfolioStrategy.generate_portfolio(
		    symbols, covariance_matrix, eigen_portfolio_number)

	def calculate_minimum_variance_portfolio(self, symbols, covariance_matrix):
		"""
		Minimum variance portfolio
		"""
		print("-! Calculating portfolio weights using minimum variance portfolio algorithm...")
		return self.minimumVarianceStrategy.generate_portfolio(
		    symbols, covariance_matrix)

	def calculate_maximum_sharpe_portfolio(self, symbols, covariance_matrix, returns_vector):
		"""
		Maximum sharpe portfolio
		"""
		print("-# Calculating portfolio weights using maximum sharpe portfolio algorithm...")
		return self.maximumSharpeRatioStrategy.generate_portfolio(
		    symbols, covariance_matrix, returns_vector)

	def random_matrix_theory_based_cov(self, returns_matrix):
		"""
		Covariance matrix filtering using random matrix theory
		"""
		return self.strategyHelperFunctions.random_matrix_theory_based_cov(
		    returns_matrix)