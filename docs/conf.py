import sys
import os

src_dir = os.path.realpath(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, src_dir)

from peewee_validates import __version__

project = 'peewee-validates'
copyright = 'Tim Shaffer'
version = __version__
release = __version__

extensions = [
    'sphinx.ext.autodoc',
]

add_module_names = False

# templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

exclude_patterns = ['_build']

pygments_style = 'pastie'

html_theme = 'sphinx_rtd_theme'

# html_static_path = ['_static']

htmlhelp_basename = 'peewee-validates'

man_pages = [
    ('index', 'peewee-validates', 'peewee-validates documentation', ['Tim Shaffer'], 1)
]
