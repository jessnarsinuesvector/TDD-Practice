# Roman Numeral Converter

The general approach was to validate the input then do the conversion afterward. The validation is done by creating rules that should ensure that we are getting valid Roman numerals as inputs. Although, there were a lot of challenges doing that especially checking for `valid numeral sequences` where I had to "cheat" by adding the invalid sequences explicitly (see: src/rules/valid_numeral_sequence.py).

Key takeaway from this activity was that it was generating tests would have been a lot easier if the design were as perfect as possible. Improper design caused the tests to be brittle and I had to do it from scratch.
It is also worth noting that changes in-between are inevitable and this is where flexibility and simplicity in the design and implementation matters the most.

A time box of 20mins/day is also very challenging. At first, I thought it would easy where I did this in parallel of other things but that only got in the way. I changed that by putting aside 20 mins with pure focus and had better results. I proved the point that Jim shared with us through the activity that he fostered: multitasking takes more time to get things finished versus a focused effort to finish one task at a time.


In summary, the requirements were straight forward:

Exercise
Converting Roman Numerals to Decimal

Create a class with one method that converts a string of Roman numerals to a decimal number and returns that number as an integer.  You can assume that only correct Roman numerals will be presented.  The Roman numerals we will need to process are I, V, X, L, C, D and M
- Jim Gildea, et al.


Understanding how the rules work, identifying key aspects, and designing the flow is harder than I thought (and this is a simple exercise versus what we are actually doing at work). Asking relevant questions (monologues, yep.) during the design phase definitely improved the testability of the implementation.
Generating the tests was so much easier when I had clarity in the design. 

---
How to use:
Install all needed python modules
> pip install -r requirements

Run tests
> pytest --cov=src --cov-report=html

Run app
> Edit main.py and modify input_str
> python main.py