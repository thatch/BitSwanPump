import unittest
import logging

import asab.abc.singleton

import bspump
import bspump.unittest


class TestMatrix(bspump.unittest.TestCase):


	def test_matrix(self):
		matrix = bspump.Matrix(
			app = self.App,
			dtype = [
				('c1', 'i8'),
				('c2', 'i8'),
				('c3', 'i8'),
			]
		)

		for i in range(100):
			n = matrix.add_row()
			matrix.Matrix[n][0] = 1
			matrix.Matrix[n]['c2'] = 1
			matrix.Matrix[n][2] = 1
			self.assertEqual(n, i)

		closed = set()
		closed |= matrix.ClosedRows

		for i in range(20, 40):
			matrix.close_row(i)
			closed.add(i)
			self.assertIn(i, matrix.ClosedRows)

		self.assertEqual(closed, matrix.ClosedRows)

		for i in range(20):
			n = matrix.add_row()
			self.assertIn(n, closed)


	def test_matrix_zeros(self):
		matrix = bspump.Matrix(app=self.App)

		for i in range(100):
			n = matrix.add_row()
			self.assertEqual(n, i)

		matrix.zeros()

		self.assertEqual(matrix.Matrix.shape, (0,))


	def test_matrix_flush(self):
		matrix = bspump.Matrix(app=self.App)

		for i in range(100):
			n = matrix.add_row()
			self.assertEqual(n, i)

		for i in range(20, 40):
			matrix.close_row(i)
			self.assertIn(i, matrix.ClosedRows)

		matrix.flush()

		self.assertEqual(len(matrix.ClosedRows), 0)
