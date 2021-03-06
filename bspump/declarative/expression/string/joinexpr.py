from ...abc import Expression


class JOIN(Expression):
	"""
	Joins strings in "items" using "char".
	"""

	def __init__(self, app, *, arg_items, arg_delimiter=" "):
		super().__init__(app)
		self.Items = arg_items
		self.Char = arg_delimiter

	def __call__(self, context, event, *args, **kwargs):
		return self.Char.join([
			str(self.evaluate(item, context, event, *args, **kwargs))
			for item in self.Items
		])
