textos = [
    """
CHAPTER 7
Formulation and
Specification
Now that we have completed our review of the necessary back-
ground material, we can begin a detailed presentation of the eight
stages of strategy development with the first step: formulation and
specification.
A trading idea begins as an idea. The trading idea may be quite precise
in which case the balance of this stage will unfold in a straightforward
manner. Or the idea may be vague. In this case, the formulation process
becomes more involved. Without a clear and precise formulation of the
strategy, the development process ends before it starts. If the strategy is
vague, then it first needs to be made precise.
The first stage in the strategy development process, in a nutshell, is
the translation of a trading idea into a scripted form understandable to a
trading strategy development application in order to produce a historical
trading simulation. As we have seen in the previous chapter, the historical
simulation is the lifeblood of the strategy evaluation process.
FORMULATE THE TRADING STRATEGY
As previously stated, a trading strategy begins as an idea or set of related
ideas. In its totality, it will comprise various formulae, indicators, rules,
order prices, and so on. Each of these different components of the strategy
must be specified individually and in detail. The interconnections of these
components also must be made specific.
""",
"""
A strategy can be very simple or extremely complex. The simplicity or
complexity of the strategy is of no consequence in itself. What does matter,
however, is that the strategy be specified accurately, completely, and
consistently.
Consider the clarity of this simple trading strategy, for example. Go
long on a stop when the market rallies to a price level that is equal to or
more than yesterday’s close plus 125 percent of yesterday’s daily range. Go
short on a stop when the market falls to a price level that is equal to or less
than yesterday’s close minus 145 percent of yesterday’s daily range. Exit
and reverse positions on opposite entry signals.
It goes without saying that exact and precise specification of a trading
strategy in all of the necessary detail is essential to success in this process.
That being said, the incomplete specification of each and every rule, for-
mula, and detail of a strategy is one of the most common mistakes that is
made in strategy development. This is especially true of traders new to the
strategy development process.
No successful trader would begin trading without being completely
prepared. In the same way, every successful trading strategy developer
must cross every t and dot every i. In the trading strategy development
process, like in so many other intricate processes, the devil is in the
details.
""",
"""
The ease or difficulty with which the strategist will perform this first
stage is highly variable. The more organized, thorough, logical, and clear-
thinking strategist will have little difficulty with this process. The strate-
gist lacking in these qualities, however, will find it a more formidable task.
As with all skills, this process becomes easier with practice and repeated
application.
The process of organizing and specifying a trading strategy is much
like the planning and organization required to proceed with any project
or design. All the pieces—formulae, rules, and indicators—must first be
assembled. Their accuracy must be verified. All of the pieces of the
puzzle must then be placed in the correct order. In other words, we
must calculate and obtain all of the information necessary. We must
follow the trading decision process through all of its steps and in or-
der. The decision tree must be in correct logical order. Thorough or-
ganization and attention to detail are the keys to successful strategy
specification.
After all of the trading formulae and rules have been assembled and
organized, it is best to write out the trading strategy in some form of abbre-
viated English. In programming, this process is called pseudocoding. The
more detailed and specific the pseudocode, the better. This pseudocode
will then be translated into a scripting test language. The more detailed the
specification, the easier the translation.
""",
"""
One of the greatest advantages of the pseudocoding process is that it is
a very effective means of determining whether all the elements have been
assembled and that all of the steps in the process have been identified.
SPECIFICATION—TRANSLATE THE IDEA
INTO A TESTABLE STRATEGY
The following fictional dialogue presents an extreme example of the type
of vagueness with which a trading idea can be surrounded. The dialogue is
between Joe Trader, a highly intuitive, nonanalytical, and successful trader
and Alex Programmer who is a highly analytical, logical, and organized pro-
grammer. His specialty is the interview process, whereby he engages in a
structured dialogue with a trader and extracts all of the methods that the
trader uses to form his trading decisions. Alex then organizes this infor-
mation into a precisely formulated trading strategy suitable for translation
into a scripting language.
Before Alex takes this step, however, he and Joe review his formula-
tion and correct any errors and misunderstandings. Alex then incorporates
these corrections, additions, deletions, and so on and once again has it re-
viewed by Joe. This back-and-forth process will continue until the strategy
is in the form that Joe thinks best represents his trading strategy and Alex
thinks can be coded for testing.
""",
"""
Please note that this dialogue is a bit tongue in check and has been
exaggerated for the sake of illustration. Traders obviously come from all
types of different backgrounds, especially in the highly competitive con-
temporary trading environment, and will range in organizational and ana-
lytic ability anywhere from that of Joe Trader to the mindset of a highly
trained Ph.D. That being said, let us continue with our dialogue.
Joe Trader uses a trading strategy that employs moving averages in a
quasi-systematic manner. He has enjoyed some degree of success employ-
ing moving averages in a somewhat unique manner. Joe believes he would
be able to make more money trading if he understood more about how
they worked and why they were effective. In pursuit of this information, he
hired Alex Programmer to write a computer program that will allow him to
formulate and test his trading strategy. The following conversation ensued
as Joe explained his methods.
“I buy when the moving averages look good and I sell when the aver-
ages look bad,” says Joe Trader.
“Hmm, that’s pretty interesting. Does it work?” says Alex
Programmer.
""",
"""
“Sometimes,” says Joe T.
“Interesting,” says Alex P. “But we are going to need to be a lit-
tle more specific to test this idea. Do you mind if I ask you a few
questions?”
Joe: “I guess not, but I hope it won’t take too long.”
Alex: “Okay. Can you first tell me what you mean by the averages look-
ing good?”
Joe: “Yeah, but I think it’s pretty obvious. The averages look good when
the short one just blasts through the long one.”
Alex: “Well, it may be obvious to you, but it is not to me nor will it
be to the computer. By ‘blasts through’ do you mean that the faster
moving average—MA1—crosses from under to over the slower moving
average—MA2?”
Joe: “Yep.”
Alex: “Good. Does it matter how much MA1 crosses over MA2?”
Joe: “Sometimes yes, sometimes no. It all depends.”
Alex: “On what?”
Joe: “It’s hard to say.”
""",
"""
Alex: “Well, then, maybe we should leave how much it crosses over for
future improvements. Let’s just get the basic system formulated first.
We know that we will go long if MA1 crosses from under to over MA2.
Now, what do you mean by ‘the averages look bad’?”
Joe: “That should be obvious, too. They just fall apart, go to hell in a
handcart.”
Alex: “Well, since we go long when MA1 comes from under to over
MA2, am I correct in assuming that we go short when MA1 crosses
from over to under MA2?”
Joe: “Uh-huh, you got it, Alex.”
Alex: “Good. This looks like we are always in a position. Is that cor-
rect?”
Joe: “Most of the time.”
Alex: “When are you not in a position?”
Joe: “When the whole thing just falls apart.”
Alex: “What do you mean by that?”
Joe: “When the market isn’t moving, moving averages just cut me to
pieces.”
Alex: “What do you mean when you say ‘the market isn’t moving’?”
""",
"""
Joe: “There is just no action. Lots of little swings, but no big swings.”
Alex: “Does that mean that this moving average strategy is really only
able to catch big swings?”
Joe: “Yes.”
Alex: “What is a big swing, then?”
Joe: “That depends.”
Alex: “On what?”
Joe: “The market.”
Alex: “I see. Does this vary from market to market and from year to
year?”
Joe: “You got it.”
Alex: “Do different length moving averages have an impact on this?”
Joe: “Yeah.”
Alex: “How do you determine which ones to use?”
Joe: “I play around with different moving averages in my charting pro-
gram and use the ones that look good.”
""",
"""
Alex: “Well, you don’t know anything about the profit and risk perfor-
mance of these averages that ‘look pretty good,’ do you?”
Joe: “No I don’t. That’s why I hired you. You’re supposed to figure this
all out for me.”
Alex: “Well, I will do my best. How do you control your risk when you
take a position?”
Joe: “It depends. If one average just blows through the other like a bat
out of hell, I usually make some money right away and it’s no problem.
But sometimes the market just looks pretty lame, and I put in a close
stop on the position.”
Alex: “You mean sometimes you use a stop, and sometimes you don’t?”
Joe: “Uh-huh.”
Alex: “That sounds inconsistent and could be dangerous as well. Do
you want to test the strategy with and without a risk stop?”
Joe: “Yes, that’s a good idea.”
Alex: “Okay. I will build this in as an option. What do you do when you
have a winner?”
Joe: “If I get a couple of grand in it, I usually ring the cash register and
take profits.”
Alex: “Do you mean that you take a profit after you have made a certain
amount of money in position?”
""",
"""
Joe: “Yep.”
Alex: “How much is enough?”
Joe: “It depends.”
Alex: “On what?”
Joe: “The market. How I have been doing lately. How I feel. A lot of
stuff.”
Alex: “Well should I build in some kind of profit idea as an option in
the program?”
Joe: “That would be great.”
Alex: “Let us see what we have here. Our basic trading model uses
two different-length moving averages. The model is always either long
or short unless our optional risk or profit management exits a trade.
We go long if the faster average goes from under to over the slower
average. We go short when the faster average goes from above to below
the slower average. Is that correct?”
""",
"""
Joe: “So far, so good.”
Alex: “There are two variations on this basic model. A risk stop and a
profit target order. The use of either of these will lead to an alteration
of the model. If a position is exited using a risk stop or a profit or better
target order, then the model will not always be in the market. Is that
okay?”
Joe: “Let’s just play it by ear and find out.”
Alex: “Okay. I will set up this program to have user-definable moving
average lengths. It will have an option to use a risk stop, a target profit,
or both. The program will be capable of testing a batch of different-
length moving average combinations. Do you think this will do it?”
Joe: “It’s a start. Let’s see what happens.”
MAKE A VAGUE IDEA PRECISE
This little melodrama serves to highlight the vagueness that can surround
a trading strategy at the inception of the development process. Joe Trader
may seem a bit extreme. The number of ways in which a trading strategy
can lack clarity, however, are too numerous to list. And, in truth, Alex Pro-
grammer was a lot better communicator and far more accommodating than
many programmers.
""",
"""
You may engage yourself in this type of dialogue or you may enlist
outside help. However, the collection, organization, and exact specification
of the trading strategy, which are done next, and as were illustrated in this
dialogue, are the essential first steps.
A trading strategy is a set of precise rules and formulae, no matter how
simple or complex. If the trading idea cannot be expressed in a way that is
precise and logical, then it is not a trading strategy.
The trading strategy discussed in the dialogue above can be described
in three ways: ordinary English, precise rules and formulae, and computer
code. The English version is pseudocode. The formulae represent a more
exact representation of pseudocode on its way to becoming computer-
testable code. The strategy expressed as C code is in a form that a com-
puter can understand.
As English language pseudocode, this moving average trading strategy
can be expressed as follows:
1. Calculate a fast moving average
2. Calculate a slow moving average
3. Go long when yesterday the fast moving average was below the slow
moving average and today the fast moving average is above the slow
moving average
4. Once long, stay long until a sell entry occurs
5. Go short when yesterday the fast moving average was above the slow
moving average and today the fast moving average is below the slow
moving average
6. Once short, stay short until a buy entry occurs
""",
"""
This strategy pseudocode can be converted to the following set of def-
initions, formulae, and logic rules:
1. C(t) is the close of the t th day with t = 1, the present day
2. X is the length of moving average one (MA1)
3. Y is the length of moving average two (MA2)
4. MA1 = [C(t) + C(t + 1) + . . . + C(t + X − 1)]/X
5. MA2 = [C(t) + C(t + 1) + . . . + C(t + Y − 1)]/Y
6. Y is never less than 2 times X
7. If we have no position and MA1 (t) > MA2 (t) and MA1 (t − 1) < MA2
(t − 1), then go long.
8. If we are short and MA1(t) > MA2(t) and MA1(t − 1) < MA2(t − 1),
then go long.
9. If we have no position and MA1 (t) < MA2 (t) and MA1 (t − 1) > MA2
(t − 1), then go short.
10. If we are long and MA1(t) < MA2(t) and MA1(t − 1) > MA2(t − 1), then
go short.
""",
"""
Such ideas look quite a bit different in the C programming language.
The C code to calculate the value of a moving average is displayed in
Example 1.
Of course, there is no need to understand this C code unless you are a
programmer. It is simply included as an illustration of the degree of preci-
sion that is required at this level of programming. To complete this exam-
ple, the final version of this trading strategy in C takes care of every last
detail and is 8,187 lines long. In this form, it can be tested precisely against
price data.
For those not proficient in C, or some other programming language,
such as Visual Basic, there are more user-friendly trading applications that
have been specifically designed for the nonprogramming trader. 1 These
applications enable the strategist to describe and test trading ideas with-
out programming proficiency. This is not to say that proper results can
be expected from an incorrectly specified system. They cannot. These pro-
grams do, however, have a number of built-in functions and operations that
make the specifications of a computer-testable trading strategy a great deal
easier.
Examples in this book will use Metastock, TradeStation, and Traders-
Studio interchangeably. Any trading strategy development application
must give the user the same abilities to express rules precisely and to test
and optimize these rules.
""",
"""
We will refer to any coded expression of a trading idea as a script. An
EasyLanguage script (TradeStation’s scripting language) that expresses the
earlier-specified two moving-average trading strategy looks like this:
...
A script expressing this trading strategy in Metastock looks as
follows:
...
A script expressing this trading strategy in TradersStudio looks as
follows:
...
As you can see, these three different scripts are a lot easier to under-
stand than the C code. They are more condensed than the English version
and it looks a lot like the definition and formula version. The EasyLanguage
script sets the value for the variable “MA1 Period” as the number 10 and
for “MA2 Period” as 30. It further sets “MA1 Today” as a simple moving
average of length 10 for the current day [that is, average(close,MA1
Period)], and so on for other values of the moving average on close prices.
""",
"""
The buy condition is set in what is called an “i” statement. An if state-
ment is a way of setting a condition, that is, “if this is true, then do this; if
it is false, then do something else.” When these conditions are met—in this
case when the MA1 crosses over MA2—an order is set to buy and reverse
the current short position with the open of the next bar. The sell condition
is also set in a different “if” statement. When its conditions are met, an or-
der is set to sell and reverse the current long position with an order placed
at the open of the next bar.
These scripts will do the exact same thing as the C code with a lot
less effort and in a lot less time because of all the built-in features that are
included in these different trading strategy development applications.
A comparison of these three different script versions of the moving
average trading strategy reveals two main things. First, they all accom-
plish the same thing, but each in their own way. Second, they are, in
essence, programming languages and they each have their strong points,
weak points, and idiosyncrasies.
As we indicated in Chapter 4: The Strategy Development Platform, it is
essential to the success of any trading strategy development process that
the strategist choose that application that has the features required and the
ease of use desired.
Even if the application has the needed capabilities, however, it is up
to the strategist to be certain that the trading strategy has been correctly
specified and programmed in the scripting language of choice.
"""
]