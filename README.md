# nanoblog

A tiny, silly example of a flask app with a database backend, intended
to illustrate flask's decoupling of the database engine from the web
framework (as opposed to django).

There is no reference to flask in either of the model implementations
(one using sqlite and the other using redis), and they can easily be
swapped out by importing one instead of the other.
