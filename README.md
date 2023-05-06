# legendary-toolbox
Relatively "niche" tools/simulations/applications that are useful in day-to-day life, especially when working closely with numbers and other math-adjacent projects.

## decimal-to-fraction
Sometimes numbers are given only in terms of decimals, which is annoying when you actually need the fraction. Of course, any decimal $d$ can be written as a fraction $\frac{x}{10^m},$ but this is generally not what is being looked for. This useful and incredibly simple tool generates instances of fully reduced fractions that would round to your inputted decimal; for instance, $ratl(0.43, 1)$ will return $3/7$ since $3/7 = 0.42857...$ 

## explore-exploit
This simulation explores the following "explore or exploit" premise: suppose you are playing a game, in which every red card drawn grants $1$ point and every black card drawn grants $0$ points. You have $n$ infinitely large decks in front of you, and are told that the density of red cards in each deck is $p_1, p_2, \cdots, p_n,$ but you don't know which probability matches with which deck -- so, the player must balance the decision to "explore" new decks"vs. "exploit" a deck that they currently know has pretty good odds. If you are told that you have $m$ moves and want to maximize the expected value of the number of points you get, what should the strategy be?

The current code snippet solves the problem for $n = 2$ and all $m$ and should be easily extendable to $n > 3.$ Great activity to try in a math circle/advanced lesson on applications of math!
