"""hidrokit - analisis hidrologi dengan python
"""

from hidrokit.__version__ import __version__ as ver

__author__ = 'Taruma Sakti Megariansyah'
__email__ = 'hi@taruma.info'
__version__ = ver

from . import prep, analysis, viz, contrib

__all__ = ['prep', 'analysis', 'viz', 'contrib']
