from ...abc import Expression


class IN(Expression):
	"""
	Checks if expression is of given list.
	"""


	def __init__(self, app, *, arg_what, arg_where):
		super().__init__(app)
		self.Where = arg_where
		self.What = arg_what


	def __call__(self, context, event, *args, **kwargs):
		return self.evaluate(self.What, context, event, *args, **kwargs) in self.evaluate(self.Where, context, event, *args, **kwargs)
