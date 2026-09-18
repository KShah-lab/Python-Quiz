# The Python Quiz

Welcome to my (drum roll) **The Python Quiz** — a Python quiz game covering **Biology, Chemistry and Maths** across three different difficulty levels! This game is not school work or anything related to school. In fact I dropped computer science as a subject since I am really bad at coding and anything remotely software related so feed back on this would be AMAZING!

I created this project to 

## Features

* **3 difficulty levels**

  * Easy
  * Medium
  * Hard

* **3 subjects**

  * Biology
  * Chemistry
  * Maths

* **27 questions in total**

  * 3 Biology questions per difficulty
  * 3 Chemistry questions per difficulty
  * 3 Maths questions per difficulty

* **Score system**

  * Correct answer = **+1 point**
  * Wrong answer = **-1 point**

* **Questions repeat until answered correctly**

  * If you get a question wrong, you can try again.
  * Your score is reduced by 1 for each incorrect attempt.

* **Subject switching**

  * After completing a subject, you can choose another subject or stop playing.

* **Different reactions and jokes**

  * Correct answers give you a joke and a reaction.
  * Wrong answers give you a different response depending on the question.

## How It Works

When the program starts, you are welcomed into the quiz and asked to choose a difficulty:

```text
What difficulty do you want to choose? Choose from Easy, Medium or Hard
```

You then choose one of the three available subjects:

```text
What subject do you want? Biology, Chemistry or Maths?
```

The program takes your answer and uses `if`, `elif` and `else` statements to send you to the appropriate section of the quiz.

### Example

```python
if difficulty == 'easy':
    print('Easy mode selected.')

elif difficulty == 'medium':
    print('Medium mode selected!')

elif difficulty == 'hard':
    print('Hard mode selected!')
```

## Scoring System

The quiz uses a variable called `score` to keep track of the player's score throughout the game.

It starts at:

```python
score = 0
```

When the player gets an answer correct:

```python
score += 1
```

When the player gets an answer wrong:

```python
score -= 1
```

The current score is then displayed:

```python
print('Score:', score)
```

This means that getting an answer wrong actually has a consequence, rather than simply allowing the player to keep guessing without affecting their score.

## Question System

Each question is placed inside a `while True` loop.

For example:

```python
while True:
    answer = input('What is the derivative of x squared? ').strip().lower()

    if answer == '2x':
        print('')
        print('Why was the derivative so confident? Because it knew exactly how things were changing!')
        print('')
        print('You actually know calculus. Respect!')
        print('')
        score += 1
        print('Score:', score)
        break
    else:
        print('Try again')
        score -= 1
```

The `while True` loop means the question continues until the player gives the correct answer.

The `break` command stops the loop once the correct answer has been entered.

## Subjects

### Biology

Biology questions range from basic knowledge in Easy mode to much more difficult biological terminology in Hard mode.

Examples include:

* Bone marrow
* Chlorophyll
* Lungs
* Transpiration
* DNA
* Mitochondria
* Apoptosis
* Translation
* Phagocytosis

### Chemistry

The Chemistry section contains questions covering basic chemical knowledge through to harder formula and chemistry questions.

Examples include:

* Diamond
* Sodium chloride
* Helium
* Exothermic reactions
* Electrons
* Catalysts
* Calcium carbonate
* Relative formula mass
* Sulfuric acid

### Maths

The Maths section progresses from very simple questions to significantly harder mathematical concepts.

Examples include:

* Triangles
* Time
* Even numbers
* Tangents
* Chords
* Perfect numbers
* Inflection points
* Orthogonal vectors
* Derivatives

## Difficulty Levels

### Easy

Designed to be straightforward questions that most players should be able to answer.

The game itself warns you:

> THIS IS SO EASY. AT LEAST CHALLENGE YOURSELF.

### Medium

The questions become more challenging and require more subject knowledge.

The game introduces this mode with:

> HERE WE GO NOW. THESE ARE ACTUAL QUESTIONS

### Hard

The hardest section of the quiz contains more advanced terminology and concepts.

Some questions are deliberately difficult, particularly in Biology and Maths.

## Technologies Used

The project is written entirely in **Python**.

Some of the Python concepts used include:

* `input()`
* `print()`
* Variables
* `if`, `elif` and `else`
* `while True`
* `break`
* `.strip()`
* `.lower()`
* `score += 1`
* `score -= 1`

## What I Learned

While creating this project, I have learned how to use several important Python concepts together to create an interactive program.

In particular, the project helped me understand:

* How variables can store information and change during a program.
* How `if`, `elif` and `else` statements control what happens.
* How `while` loops can repeatedly run code.
* How `break` can stop a loop.
* How user input can be cleaned using `.strip()` and `.lower()`.
* How to create a scoring system.
* How different sections of a program can work together.
* How to structure a larger Python program rather than just writing individual commands.

## Future Improvements

There are several things that could be added to the quiz in the future:

* A larger question bank
* Randomly selected questions
* A timer
* Multiple-choice questions
* A high-score system
* More subjects
* More difficulty levels
* A final percentage/grade
* A leaderboard
* Better input validation
* Different endings depending on the final score

## Final Score

At the end of the game, the player's final score is displayed:

```text
=================
FINAL SCORE: 12
=================
```

The score represents the number of correct answers minus the number of incorrect attempts.

## Credits

Created as a Python learning project.

And yes, the jokes are intentionally terrible.
