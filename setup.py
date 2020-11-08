from setuptools import setup, find_packages

setup (
  name='spicelexer',
  packages=find_packages(),
  entry_points =
  """
  [pygments.lexers]
  spicelexer = spice.spice:SpiceLexer
  """,
)
