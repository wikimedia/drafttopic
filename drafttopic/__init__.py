"""
This package contains a set of utilities and assets for predicting topics to
new drafts based on Wikiprojects on English Wikipedia.

In this package, you'll find the
:mod:`feature lists <drafttopic.feature_lists>` used to train models
for the supported wiki.  There's a set of
:mod:`command-line utilities <drafttopic.utilities>`
that are used to perform data pipeline operations specific to training and
testing draft t opic models.

See the :ref:`API Reference <api_reference>` for low level details.
"""

from .about import (__author__, __author_email__, __description__, __name__,
                    __url__, __version__)

__all__ = [__name__, __version__, __author__, __author_email__,
           __description__, __url__]
