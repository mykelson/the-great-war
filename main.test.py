import unittest

from main import Solution

class SolutionMethods(unittest.TestCase):
	def test_run1(self):
		solution = Solution()
		self.assertEqual(solution.run("Seven Kingdom Army", 4, 1), "White Walker Army|6")
	
	def test_run2(self):
		solution = Solution()
		self.assertEqual(solution.run("Seven Kingdom Army", 10, 5), "Seven Kingdom Army|5")
	
	def test_run3(self):
		solution = Solution()
		self.assertEqual(solution.run("Seven Kingdom Army", 16, 18), "Seven Kingdom Army|3")

	def test_run4(self):
		solution = Solution()
		self.assertEqual(solution.run("Seven Kingdom Army", 2, 6), "White Walker Army|4")

if __name__ == "__main__":
	unittest.main()
