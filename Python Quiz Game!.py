print('=================')
print(' The Python Quiz')
print('=================')
print('Welcome!')

score = 0
# I have created a score variable where the score is tracked throughout the game. If the question is wrong, you lose a point, if the score is 0, the game will not deduct any points.
difficulty = input('What difficulty do you want to choose? Choose from Easy, Medium or Hard ').strip().lower()
# The game has 3 modes and will ask you to choose from one. If you choose e.g. biology, you will be asked biology questions but if you then finish them, you can choose either maths or chemistry.
if difficulty == 'easy':
    print('Easy mode selected. THIS IS SO EASY. AT LEAST CHALLENGE YOURSELF. TRY IT IF YOU WANT THOUGH')
# this is a big if-clause and contains the easy, medium and hard selection. If you choose easy you will be directed to the section below, if you choose medium the one after it and if you choose hard the last one
    subject = input('What subject do you want? Biology, Chemistry or Maths? ').strip().lower()
    # here is the question
    while True:

        if subject == 'biology':

            while True:
                question = input('What part of the human body is responsible for the production of red blood cells?? ').strip().lower()

                if question == 'bone marrow':
                    print('')
                    print('Why did the bone marrow get a big promotion at the body factory? Because it was always doing a bloody good job and working right down to the marrow!')
                    print('')
                    print('Nice one bro!')
                    print('')
                    score += 1
                    print('Score:', score)
                    break
                else:
                    print('Its not that hard I swear, try again')
                    score -= 1

            while True:
                answer = input('What is the green pigment in plants that traps sunlight for making food? ').strip().lower()

                if answer == 'chlorophyll':
                    print('')
                    print('Why are plants so good at math? Because they have square roots!')
                    print('')
                    print('Nice on buddy, you got it right this time')
                    print('')
                    score += 1
                    print('Score:', score)
                    break
                else:
                    print('Try again')
                    score -= 1

            while True:
                answer = input('Which organs in your chest fill up with air when you breathe in? ').strip().lower()

                if answer == 'lungs':
                    print('')
                    print('What did one lung say to the other? We need to stick together, we are a breath-taking pair! ')
                    print('')
                    print('Someone knows a little biology...')
                    print('')
                    score += 1
                    print('Score:', score)
                    break
                else:
                    print('Try again')
                    score -= 1

            subject = input('Would you like to do Chemistry or Maths next? Type Chemistry, Maths or No: ').strip().lower()

            if subject == 'no':
                break


        elif subject == 'chemistry':

            while True:
                question = input('What is the hardest natural substance on Earth, made completely out of carbon atoms? ').strip().lower()

                if question == 'diamond':
                    print('')
                    print('Why are diamonds so good at chemistry? Because they are full of brilliant elements!' )
                    print('')
                    print('Idk how you got this, your luck will soon run out')
                    print('')
                    score += 1
                    print('Score:', score)
                    break
                else:
                    print('Try again')
                    score -= 1

            while True:
                answer = input('What is the common name for the chemical compound "sodium chloride"? ').strip().lower()

                if answer == 'salt':
                    print('')
                    print('Did you hear the joke about the element sodium? Na, I dont think you have')
                    print('')
                    print('Bro you are getting so much luck, this is actually crazy')
                    print('')
                    score += 1
                    print('Score:', score)
                    break
                else:
                    print('Try again')
                    score -= 1

            while True:
                answer = input('Which very light gas is used to make balloons float in the air? ').strip().lower()

                if answer == 'helium':
                    print('')
                    print('What happened when the scientist told a joke about helium? Nobody laughed, it just got a high-pitched giggle! ')
                    print('')
                    print('No way you got this, ngl i thought it was oxygen the first time i came across this question')
                    print('')
                    score += 1
                    print('Score:', score)
                    break
                else:
                    print('Try again')
                    score -= 1

            subject = input('Would you like to do Biology or Maths next? Type Biology, Maths or No: ').strip().lower()

            if subject == 'no':
                break


        elif subject == 'maths':

            while True:
                question = input('What shape do you get if you slice a round pizza into perfect triangles? ').strip().lower()

                if question == 'triangle':
                    print('')
                    print('Why was the triangle so popular? Because it always had three acute points to make! ')
                    print('')
                    print('Tried to trick you there. Btw these jokes are so bad.')
                    print('')
                    score += 1
                    print('Score:', score)
                    break
                else:
                    print('Try again')
                    score -= 1

            while True:
                answer = input('How many minutes are there in a quarter of an hour? ').strip().lower()

                if answer == '15':
                    print('')
                    print('Why did the clock get sent to the principals office? It wouldnt stop ticking people off!')
                    print('')
                    print('This could not be any easier. Do you want a medal for getting it right?')
                    print('')
                    score += 1
                    print('Score:', score)
                    break
                else:
                    print('Genuinely what are you doing with your life')
                    score -= 1

            while True:
                answer = input('What do you call any number that can be divided by 2 without leaving a remainder? ').strip().lower()

                if answer == 'even':
                    print('')
                    print('Why did the odd number get scared of the number 2? Because 2 was trying to make things even! ')
                    print('')
                    print('This almost tested your maths skill, like almost.')
                    print('')
                    score += 1
                    print('Score:', score)
                    break
                else:
                    print('Your wasting your time, go learn how to do division first before attempting this question again. You are hopeless.')
                    score -= 1

            subject = input('Would you like to do Biology or Chemistry next? Type Biology, Chemistry or No: ').strip().lower()

            if subject == 'no':
                break

        else:
            print('That is not one of the subjects!')
            subject = input('Choose Biology, Chemistry or Maths: ').strip().lower()


elif difficulty == 'medium':

    print('Medium mode selected! HERE WE GO NOW. THESE ARE ACTUAL QUESTIONS')

    subject = input('What subject do you want? Biology, Chemistry or Maths? ').strip().lower()

    while True:

        if subject == 'biology':

            while True:
                question = input('What is the name of the process where plants lose water vapor through tiny holes in their leaves? ').strip().lower()

                if question == 'transpiration':
                    print('')
                    print('Why did the leaf go to the doctor? It was feeling a little green and losing its breath! ')
                    print('')
                    print('Nice on buddy, your doing okay ig.')
                    print('')
                    score += 1
                    print('Score:', score)
                    break
                else:
                    print('I mean, I almost understand you getting this wrong but if you have a done even a little of botany you shouldve got this.')
                    score -= 1

            while True:
                answer = input('What molecule is shaped like a double helix and holds all the genetic instructions for life? ').strip().lower()

                if answer == 'dna':
                    print('')
                    print('Why did the DNA molecule go to prison? Because it was caught making a bad replication!')
                    print('')
                    print('The double helix gave it away right... bad questiom :(')
                    print('')
                    score += 1
                    print('Score:', score)
                    break
                else:
                    print('THE ANSWER IS IN THE QUESTION!')
                    score -= 1

            while True:
                answer = input('Which organelle is known as the powerhouse of the cell because it generates chemical energy? ').strip().lower()

                if answer == 'mitochondria':
                    print('')
                    print('Why did the cell take the mitochondria to court? It was charged with a power trip! ')
                    print('')
                    print('You knew the meaning of organelle right? Good good good...')
                    print('')
                    score += 1
                    print('Score:', score)
                    break
                else:
                    print('I almost understand why you got this wrong. Go search organelle up')
                    score -= 1

            subject = input('Would you like to do Chemistry or Maths next? Type Chemistry, Maths or No: ').strip().lower()

            if subject == 'no':
                break


        elif subject == 'chemistry':

            while True:
                question = input('What is the term for a chemical reaction that releases energy in the form of heat or light? ').strip().lower()

                if question == 'exothermic':
                    print('')
                    print('Why are exothermic reactions so popular at parties? Because they always bring the heat! ')
                    print('')
                    print('This is good. Nice answer. Exo vs endo gets me confused.')
                    print('')
                    score += 1
                    print('Score:', score)
                    break
                else:
                    print('Its the other one, if ykyk')
                    score -= 1

            while True:
                answer = input('What are the tiny, negatively charged particles that spin around the outside of an atoms nucleus? ').strip().lower()

                if answer == 'electrons':
                    print('')
                    print('Why should you never trust an atom? Because they make up everything!')
                    print('')
                    print('This is easy but the joke is better right? You have to admit it')
                    print('')
                    score += 1
                    print('Score:', score)
                    break
                else:
                    print('Just list all the sub atomic particles, youll eventually get it. trust me')
                    score -= 1

            while True:
                answer = input('What do you call a substance that speeds up a chemical reaction without being used up itself? ').strip().lower()

                if answer == 'catalyst':
                    print('')
                    print('Why did the catalyst get a speeding ticket? It couldnt stop accelerating the process!')
                    print('')
                    print('This is some proper chemistry now. Nice job')
                    print('')
                    score += 1
                    print('Score:', score)
                    break
                else:
                    print('if you dont know much chem you wont get this unless u search on google but at that point why are u even doing this quiz')
                    score -= 1

            subject = input('Would you like to do Biology or Maths next? Type Biology, Maths or No: ').strip().lower()

            if subject == 'no':
                break


        elif subject == 'maths':

            while True:
                question = input('What is the mathematical term for a straight line that touches the outside of a circle at only one point? ').strip().lower()

                if question == 'tangent':
                    print('')
                    print('Why did the teacher get mad when the student changed the subject? Because they went off on a tangent! ')
                    print('')
                    print('I mean this is a half decent joke. nice one tho')
                    print('')
                    score += 1
                    print('Score:', score)
                    break
                else:
                    print('Its all circle theorums...')
                    score -= 1

            while True:
                answer = input('What is the term for a straight line segment that connects two points on a curve?' ).strip().lower()

                if answer == 'chord':
                    print('')
                    print('Why did the math book look so sad? Because it had too many problems, and nobody could ever strike a chord with it!' )
                    print('')
                    print('Cant lie, but this is a similar question to the first. If youve done circle theorums youll find this easy')
                    print('')
                    score += 1
                    print('Score:', score)
                    break
                else:
                    print('If you got tanget, you must have got this come on... ')
                    score -= 1

            while True:
                answer = input('What is the term for a natural number that is equal to the sum of its proper positive divisors (excluding the number itself)? ').strip().lower()

                if answer == 'perfect':
                    print('')
                    print('Why was the number 6 so confident? Because it knew it was perfect!')
                    print('')
                    print('like me')
                    print('')
                    print('Well done! this was reasonably hard ig')
                    score += 1
                    print('Score:', score)
                    break
                else:
                    print('This, I will admit, is hard...')
                    score -= 1

            subject = input('Would you like to do Biology or Chemistry next? Type Biology, Chemistry or No: ').strip().lower()

            if subject == 'no':
                break

        else:
            print('That is not one of the subjects!')
            subject = input('Choose Biology, Chemistry or Maths: ').strip().lower()


elif difficulty == 'hard':

    print('Hard mode selected!')

    subject = input('What subject do you want? Biology, Chemistry or Maths? ').strip().lower()

    while True:

        if subject == 'biology':

            while True:
                question = input('What is the term for the programed cell death that occurs as a normal, controlled part of an organisms growth or development? ').strip().lower()

                if question == 'apoptosis':
                    print('')
                    print('Why did the cell get single-handedly voted out of the biological community? It just couldnt stop taking things personally and chose to go out in a blaze of apoptosis! ')
                    print('')
                    print('These are seriously hard, like actually your good if you are getting this')
                    print('')
                    score += 1
                    print('Score:', score)
                    break
                else:
                    print('Understandable, this is quite difficult')
                    score -= 1

            while True:
                answer = input('What is the specific enzymatic process where mRNA is converted into an amino acid chain to form a protein? ').strip().lower()

                if answer == 'translation':
                    print('')
                    print('Why are ribosomes terrible at foreign languages? Because no matter how hard they try, every sentence just turns into a chain of amino acids!')
                    print('')
                    print('These jokes are really really bad, but again nice one!')
                    print('')
                    score += 1
                    print('Score:', score)
                    break
                else:
                    print('You chose this difficulty, i didnt')
                    score -= 1

            while True:
                answer = input('What is the term for the process by which a cell engulfs solid particles to form an internal vesicle? ').strip().lower()

                if answer == 'phagocytosis':
                    print('')
                    print('Why did the cell eat its homework? Because it was practicing phagocytosis!')
                    print('')
                    print('These questions are getting ridiculous now. Nice one!')
                    print('')
                    score += 1
                    print('Score:', score)
                    break
                else:
                    print('You chose this difficulty, i didnt')
                    score -= 1

            subject = input('Would you like to do Chemistry or Maths next? Type Chemistry, Maths or No: ').strip().lower()

            if subject == 'no':
                break


        elif subject == 'chemistry':

            while True:
                question = input('What is the formula for calcium carbonate? No capitals needed format like hno3 for nitric acid as an example  ').strip().lower()

                if question == 'caco3':
                    print('')
                    print('Why did calcium carbonate get invited to every party? Because it always had good chemistry!')
                    print('')
                    print('You got it. Starting strong.')
                    print('')
                    score += 1
                    print('Score:', score)
                    break
                else:
                    print('Try again')
                    score -= 1

            while True:
                answer = input('What is the relative formula mass of H2O? ').strip().lower()

                if answer == '18':
                    print('')
                    print('Why was H2O always calm? Because it knew how to go with the flow!')
                    print('')
                    print('You got it. Water is carrying this section.')
                    print('')
                    score += 1
                    print('Score:', score)
                    break
                else:
                    print('Try again')
                    score -= 1

            while True:
                answer = input('What is the formula for sulfuric acid? No capitals needed format like hno3 for nitric acid as an example ').strip().lower()

                if answer == 'h2so4':
                    print('')
                    print('Why did the acid get kicked out of chemistry class? Because it was acting too basic!')
                    print('')
                    print('Nice one buddy. You actually know your acids.')
                    print('')
                    score += 1
                    print('Score:', score)
                    break
                else:
                    print('Try again')
                    score -= 1

            subject = input('Would you like to do Biology or Maths next? Type Biology, Maths or No: ').strip().lower()

            if subject == 'no':
                break


        elif subject == 'maths':

            while True:
                question = input('What is the term for a point on a curve where the concavity changes from concave up to concave down (or vice versa)? 1 word answer ').strip().lower()

                if question == 'inflection':
                    print('')
                    print('My life had a similar moment, but instead of the concavity changing, I just realized I was going downhill fast.')
                    print('')
                    print('Nice one buddy! This was a hard starting question.')
                    print('')
                    score += 1
                    print('Score:', score)
                    break
                else:
                    print('Unlucky but understandable.')
                    score -= 1

            while True:
                answer = input('What do you call two vectors whose dot product equals zero? Not perpendicular but it is correct.').strip().lower()

                if answer == 'orthogonal':
                    print('')
                    print('Why did the two vectors stop talking? Because they just could not find the right angle between them!')
                    print('')
                    print('Nice one buddy! This is quite impressive if ur getting it right..')
                    print('')
                    score += 1
                    print('Score:', score)
                    break
                else:
                    print('Try again')
                    score -= 1

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

            subject = input('Would you like to do Biology or Chemistry next? Type Biology, Chemistry or No: ').strip().lower()

            if subject == 'no':
                break

        else:
            print('That is not one of the subjects!')
            subject = input('Choose Biology, Chemistry or Maths: ').strip().lower()


else:
    print('That is not a valid difficulty!')

print('=================')
print('FINAL SCORE:', score)
print('=================')