import argparse
import random
import subprocess
import textwrap

import asyncio
import discord

client = discord.Client()


#@client.event#
#async def on_member_join(member):#
    #server = member.server#
    #fmt = 'Welcome {0.mention} to {1.name}! An injury to one is an injury to all!'#
    #await client.send_message(server, fmt.format(member, server))#

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
print('------')

insult1 = ["a Lazy", "a Stupid", " an Insecure", "an Idiotic", "a Slimy", "a Jerky", "a Smelly", "a Pompous", "a Communist", "a Dicknose", "a Pie-eating", "a Racist", "an Elitist", "a White Trash", "a Drug-Loving", "a Butterface", "a Tone Deaf", "an Ugly", "a Creepy"]
insult2 = ["Douche", "Ass", "Turd", "Rectum", "Butt", "Cock", "Shit", "Crotch", "Fascist", "Prick", "Jerk", "Taint", "Fuck", "Dick", "Boner", "Shart", "Nut", "Sphincter" ]
insult3 = ["Pilot", "Canoe", "Captain", "Pirate", "Hammer", "Knob", "Box", "Jockey", "Nazi", "Waffle", "Goblin", "Blossum", "Biscuit", "Clown", "Socket", "Monster", "Hound", "Dragon", "Balloon"]
compliment1 = ["a Gentle", "a Inviting", " an Obliging", "a Pleasant", "a Delightful", "a Considerate", "a Attractive", "a Helpful", "a Commendable", "a Courteous", "a Well-mannered", "a Ducky", "a Copacetic", "a Simpatico", "a Swell", "a Pleasurable", "a Peachy", "a Polite", "a Lovely"]
compliment2 = ["Gracious", "Civil", "Kindly", "Warm", "Sociable", "Approachable", "Breezy", "Congenial", "Dandy", "Marvelous", "Elegant", "Alluring", "Classy", "Fascinating", "Cute", "Dazzling", "Sublime", "Splendid" ]
compliment3 = ["Pilot", "Canoe", "Captain", "Pirate", "Hammer", "Knob", "Box", "Jockey", "Nazi", "Waffle", "Goblin", "Blossum", "Biscuit", "Clown", "Socket", "Monster", "Hound", "Dragon", "Balloon"]
ball = ['It is certain','It is decidedly so','Without a doubt','Yes, definitely','You may rely on it','As I see it, yes','Most likely','Outlook good','Yes','Signs point to yes','Reply hazy try again','Ask again later','Better not tell you now','Cannot predict now','Concentrate and ask again','Don\'t count on it','My reply is no','My sources say no','Outlook not so good','Very doubtful']
help_msg = ('''\
!help 
!4chan
!8ball
!acab
!afaq
!anarchism
!ancap
!ancom
!anfem
!anti-civ
!antifa
!bakunin
!bash
!bestshit
!bathroom
!bonanno
!bookchin
!bookclub
!bordiga
!bourge
!brd
!bread
!btfo
!bubbles
!chomsky
!cnt
!coffee
!coin 
!compliment
!cowsay 
!cyberpunk
!durruti
!encounter 
!ezln
!facepalm
!fascist
!feminism
!fresh
!fullcommunism
!goldman
!gulag
!hacktheplanet
!horseshoe
!insult
!kitty
!kronstadt
!kropotkin
!leftcom
!leftunity
!lenin
!lenny
!liberals
!linux
!makhno
!marx
!memes
!motivation
!mutualism
!ohwell
!outside
!poblacht
!proudhon
!pusheen
!rainbowstalin
!reddit
!rsoc
!rules
!sexist
!sjw
!space
!sparkles
!spook
!stirner
!stirnerwave
!tankie
!tea
!trotsky
!trump
!usa
!vaporwave
!vegan
!vote


''')

changelog = ('''
v0.1.1
-changed !gold to !inventory
-Added shop
-Added whisper
-Added insult
-Added RPG Dice Roller
-Added encounters
-Added potions
-Added fresh and wtf
''')

user_gold = {}
user_potions={}


@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

"""
@client.event
@asyncio.coroutine
def on_message(message):
    if message.content.startswith(''):
"""

def build_saycow():
    return """
     \   ^__^
      \  (oo)\_______
         (__)\       )\/\\
             ||----w |
             ||     ||
    """

def build_thinkcow():
    return """
     o   ^__^
      o  (oo)\_______
         (__)\       )\/\\
             ||----w |
             ||     ||
    """

def build_box(body, length=40):
    bubble = []

    lines = normalize_text(body, length)

    bordersize = len(lines[0])

    bubble.append("  "  + "_" * bordersize)

    for index, line in enumerate(lines):
        border = get_border(lines, index)

        bubble.append("%s %s %s" % (border[0], line, border[1]))

    bubble.append("  " + "-" * bordersize)

    return "\n".join(bubble)

def normalize_text(body, length):
    lines  = textwrap.wrap(body, length)
    maxlen = len(max(lines, key=len))
    return [ line.ljust(maxlen) for line in lines ]

def get_border(lines, index):
    if len(lines) < 2:
        return [ "<", ">" ]

    elif index == 0:
        return [ "/", "\\" ]

    elif index == len(lines) - 1:
        return [ "\\", "/" ]

    else:
        return [ "|", "|" ]


@client.event
@asyncio.coroutine
def on_message(message):

    if message.author == client.user:
        return

    elif message.content.startswith('!cowsay'):
        body = " ".join(message.content.split()[1:])
        cowsaid = build_box(body, 40) + build_saycow()
        yield from client.send_message(message.channel, '```txt\n{0}```'.format(cowsaid))

    elif message.content.startswith('!cowthink'):
        body = " ".join(message.content.split()[1:])
        cowsaid = build_box(body, 40) + build_thinkcow()
        yield from client.send_message(message.channel, '```txt\n{0}```'.format(cowsaid))

    elif message.content.startswith('!help'):
        yield from client.send_message(message.channel, help_msg)

    elif message.content.startswith('!changelog'):
        yield from client.send_message(message.channel, changelog)

    elif message.content.startswith('Voltairine, introduce yourself'):
        yield from client.send_message(message.channel, '```Hi everyone! I\'m Voltairine. Nice to meet you all```')

    elif message.content.startswith('!4chan'):
        yield from client.send_message(message.channel, '**ITS LITERALLY THE MOST TOXIC ASPECTS OF HUMANITY THROWN INTO A BLENDER AND PULSED INTO A SICKENING MASS OF SHIT, THATS BEEN SLOWLY FUCKING CREEPING INTO THE REAL WORLD AND JUST UGH 4CHAN IS KILLING THE WORLD**')

    elif message.content.startswith('!8ball'):
        j = random.randint(0,11)
        yield from client.send_message(message.channel, ball[j])

    elif message.content.startswith('!acab'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/acab1.png\nhttp://www.gooseberrycollective.net/bots/acab2.png')

    elif message.content.startswith('!afaq'):
        yield from client.send_message(message.channel, ':books: https://libcom.org/files/Iain%20McKay%20-%20Anarchist%20FAQ.pdf')

    elif message.content.startswith('!anarchism'):
        yield from client.send_message(message.channel, 'Anarchism is a social movement that seeks liberation from oppressive systems of control including but not limited to the state, capitalism, racism, sexism, speciesism, and religion. Anarchists advocate a self-managed, classless, stateless society without borders, bosses, or rulers where everyone takes collective responsibility for the health and prosperity of themselves and the environment.')

    elif message.content.startswith('!antifa'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/antifa.gif')

    elif message.content.startswith('!bathroom'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/bathroom.png')

    elif message.content.startswith('!bash'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/bash.gif')

    elif message.content.startswith('!berkman'):
        yield from client.send_message(message.channel, '**Alexander Berkman** (November 21, 1870 – June 28, 1936) was a leading member of the anarchist movement in the early 20th century, famous for both his political activism and his writing.Berkman was born in Vilnius, Lithuania and emigrated to the United States in 1888. He lived in New York City, where he became involved in the anarchist movement. He was the one-time lover and lifelong friend of anarchist Emma Goldman. In 1892, undertaking an act of propaganda of the deed, Berkman made an unsuccessful attempt to assassinate businessman Henry Clay Frick, for which he served 14 years in prison. His experience in prison was the basis for his first book, Prison Memoirs of an Anarchist.\nAfter his release from prison, Berkman served as editor of Goldman\'s anarchist journal, Mother Earth, and later established his own journal, The Blast. In 1917, Berkman and Goldman were sentenced to two years in jail for conspiracy against the newly instated draft. After their release from prison, they were arrested—along with hundreds of others—and deported to Russia. Initially supportive of that country\'s Bolshevik revolution, Berkman and Goldman soon became disillusioned, voicing their opposition to the Soviet\'s use of terror after seizing power and their repression of fellow revolutionaries.\n\n:books: **Prison Memoirs of an Anarchist **: https://theanarchistlibrary.org/library/alexander-berkman-prison-memoirs-of-an-anarchist\n:books: **Bolsheviks Shooting Anarchists** with Emma Goldman: https://theanarchistlibrary.org/library/emma-goldman-alexander-berkman-bolsheviks-shooting-anarchists \n:books: **The Russian Tragedy (A Review and An Outlook)**: https://theanarchistlibrary.org/library/alexander-berkman-the-russian-tragedy-a-review-and-an-outlook \n:books: **What Is Communist Anarchism?**: https://theanarchistlibrary.org/library/alexander-berkman-what-is-communist-anarchism \nhttp://www.gooseberrycollective.net/bots/berkman.png')

    elif message.content.startswith('!bonanno'):
        yield from client.send_message(message.channel, '**Alfredo Bonanno** was born 1937 in Catania, Italy, and is a main theorist of contemporary insurrectionary anarchism who wrote essays such as *Armed Joy* (*for which he was imprisoned for 18 months by the Italian government*). He is an editor of *Anarchismo Editions* and many other publications, only some of which have been translated into English. He has been involved in the anarchist movement for over thirty years.\n\n:books: **Armed Joy**: https://theanarchistlibrary.org/library/alfredo-m-bonanno-armed-joy\n\n:books: **The Anarchist Tension **: https://theanarchistlibrary.org/library/alfredo-m-bonanno-the-anarchist-tension \n\n:books: **From Riot to Insurrection**: https://theanarchistlibrary.org/library/alfredo-m-bonanno-from-riot-to-insurrection-analysis-for-an-anarchist-perspective-against-post \n\n:books: **Insurrectionalist Anarchism — Part One **: https://theanarchistlibrary.org/library/alfredo-m-bonanno-insurrectionalist-anarchism-part-one \nhttp://www.gooseberrycollective.net/bots/bonanno.jpg')

    elif message.content.startswith('!ancap'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/ancap1.png \n http://www.gooseberrycollective.net/bots/ancap2.png')

    elif message.content.startswith('!ancom'):
        yield from client.send_message(message.channel, 'A theory of anarchism which advocates the abolition of the state, capitalism, wage labour, and private property (while retaining respect for personal property), and in favour of common ownership of the means of production, direct democracy, and a horizontal network of voluntary associations and workers\' councils with production and consumption based on the guiding principle: "from each according to his ability, to each according to his need"\n:books: **Recommended Reading**:books: \n\n:closed_book:  **Anarchist communism - an introduction** https://libcom.org/thought/anarchist-communism-an-introduction\n:closed_book:  **A Short Introduction to Anarchist Communism**  https://afed.org.uk/short-intro/')

    elif message.content.startswith('!anfem'):
        yield from client.send_message(message.channel, 'Anarchism and feminism have always been closely linked. Anfems see patriarchy as a manifestation of involuntary coercive hierarchy, that should be replaced by decentralized free association. It is an anti-authoritarianism, anti-capitalism, anti-oppressive philosophy, with the goal of creating an "equal ground" between males and females. The term "anarcha-feminism" suggests the social freedom and liberty of women, without needed dependence upon other groups or parties.\n:books: **Recommended Reading**:books: \n\n :closed_book:  **Anarchy and the Sex Question ** by Emma Goldman: https://theanarchistlibrary.org/library/emma-goldman-anarchy-and-the-sex-question\n:closed_book:  **The Question of Feminism ** by Lucia Sanchez Saornil: https://theanarchistlibrary.org/library/lucia-sanchez-saornil-the-question-of-feminism\nhttp://www.gooseberrycollective.net/bots/anfem.png')

    elif message.content.startswith('!anti-civ'):
        yield from client.send_message(message.channel, ':books: **The Network of Domination by Wolfi Landstreicher**: https://theanarchistlibrary.org/library/wolfi-landstreicher-the-network-of-domination\n:books: **Against His-story, Against Leviathan by Fredy Perlman**: https://theanarchistlibrary.org/library/fredy-perlman-against-his-story-against-leviathany\n:books: **What is Green Anarchy? **: https://theanarchistlibrary.org/library/anonymous-what-is-green-anarchy\n:books: **Desert**: https://theanarchistlibrary.org/library/anonymous-desert\n http://www.gooseberrycollective.net/bots/anticiv.png')

    elif message.content.startswith('!bakunin'):
        yield from client.send_message(message.channel, ':books: **Statism and Anarchy**: https://theanarchistlibrary.org/library/michail-bakunin-statism-and-anarchy\n:books: **God and the State**: https://theanarchistlibrary.org/library/michail-bakunin-god-and-the-state\n:books: **Marxism, Freedom and the State**: https://theanarchistlibrary.org/library/michail-bakunin-marxism-freedom-and-the-state\n:books: **The Capitalist System**: https://theanarchistlibrary.org/library/michail-bakunin-the-capitalist-system')

    elif message.content.startswith('!benned1'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/benned1.png')

    elif message.content.startswith('!benned2'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/benned2.png')

    elif message.content.startswith('!benned3'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/benned3.png')

    elif message.content.startswith('!benned4'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/benned4.png')

    elif message.content.startswith('!benned5'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/benned5.gif')

    elif message.content.startswith('!bestshit'):
        yield from client.send_message(message.channel, ':books: CONQUEST OF BREAD MOTHERFUCKER\nhttps://theanarchistlibrary.org/library/petr-kropotkin-the-conquest-of-bread \nABC OF ANARCHISM IF YOU LIKE IT IN SIMPLE ENGLISH! \nhttps://libcom.org/library/abc-anarchism-alexander-berkman \nCOMMUNIST MANIFESTO FOR THE CLASSIC SHIT :ok_hand: :ok_hand: :ok_hand:  \nhttps://www.marxists.org/archive/marx/works/1848/communist-manifesto/')

    elif message.content.startswith('!bookchin'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/bookchin.png\n:books: **Social Anarchism or Lifestyle Anarchism**: https://theanarchistlibrary.org/library/murray-bookchin-social-anarchism-or-lifestyle-anarchism-an-unbridgeable-chasm \n:books: **The Ecology of Freedom**: https://we.riseup.net/goatgooseberry/murray-bookchin-the-ecology-of-freedom+375117 \n:books: **Post-Scarcity Anarchism**: https://we.riseup.net/goatgooseberry/murray-bookchin-post-scarcity-anarchism+375119')

    elif message.content.startswith('!bookclub'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/bookclub.png\n\n\n:books: __**Anarchist Book Club**__ :books:\n\nJoin the Book Club! Discussion every Sunday at 17:00 EST in Voice. Text discussion anytime in #library channel. This week\' book is: \n\n :book: **Philosophy and Real Politics** by Raymond Geuss. https://we.riseup.net/goatgooseberry/raymond-geuss-philosophy-and-real-politics+377228')

    elif message.content.startswith('!books'):
        yield from client.send_message(message.channel, ':books: :books: \n* **Peter Marshall - Demanding the Impossible: A History of Anarchism**\n* **Clifford Harper - Anarchy: graphic guide** \n* **Peter Kropotkin - Conquest of Bread**\n* Peter Kropotkin - Mutual Aid\n* Alexander Berkman - The ABC of anarchism\n* Peter Gelderloos - Anarchy Works\n* Emma Goldman - Anarchism and Other Essays\n* Oscar Wilde - The Soul of Man Under Socialism\n* Marx/Engels - Manifesto of the Communist Party\n* **Ursula Le Guin - The Dispossessed**\n* Daniel Guérin - Anarchism: From Theory to Practice\n* Comité Invisible (The Invisible Committee) - The Coming Insurrection\n* Bob Black - The Abolition of Work\n* Karl Marx - Capital\n* Max Stirner - The Unique and His Property\n* Daniel Guerin - Anarchism: Theory and Practice\n* Colin Ward - Anarchism: A Short Introduction\n* Benjamin R. Tucker - Instead of a Book\n* Alexander Berkman - What is Anarchism?\n* Ken Knabb - The Joy of Revolution\n* **Crimethinc - Work**\n* Crimethinc - Days of War, Nights of Love\n* **Daniel Guerin - No Gods, No Masters**\n* The Organizational Platform of the General Union of Anarchists\n* Peter Arshinov - History of the Makhnovist Movement\n* **Prole.info - The Housing Monster**\n* **Prole.info - Abolish Restaurants**\n* Peter Gelderloos - How Nonviolence Protects the State\n* Mikhail Bakunin - God and the State\n* Mikhail Bakunin - Revolutionary Catechism\n* **David Graeber - Debt: The First 5000 Years**\n* Voltairine de Cleyre - Crime and Punishment')

    elif message.content.startswith('!bordiga'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/bordiga.png')

    elif message.content.startswith('!bourge'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/bourge.png')

    elif message.content.startswith('!brd'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/brd.png')

    elif message.content.startswith('!bread'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/bread.png')

    elif message.content.startswith('!btfo'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/btfo.gif')

    elif message.content.startswith('!bubbles'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/bubbles.png')

    elif message.content.startswith('!chart'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/chart1.png\nhttp://www.gooseberrycollective.net/bots/chart2.png')

    elif message.content.startswith('!chomsky'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/chomsky1.png\n :books: **Chomsky on Anarchism**: https://we.riseup.net/goatgooseberry/noam-chomsky-chomsky-on-anarchism-ak+374994\n:books: **Deterring Democracy**: https://we.riseup.net/goatgooseberry/noam-chomsky-deterring-democracy-vintage+374996\n:books: **Manufacturing Consent**: https://we.riseup.net/goatgooseberry/edward-s-herman-noam-chomsky+374993\n:books: **Failed States**: https://we.riseup.net/goatgooseberry/noam-chomsky-failed-states-the-abuse-of+374995')

    elif message.content.startswith('!cnt'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/cnt.png\nhttp://www.gooseberrycollective.net/bots/cnt1.png')

    elif message.content.startswith('!coffee'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/coffee.png')

    elif message.content.startswith('!communism'):
        yield from client.send_message(message.channel, 'A spectre:ghost::ghost: is haunting:ghost: :earth_africa:Europe:earth_africa: — the spectre :ghost:of communism☭☭☭☭. All the :muscle::muscle:powers of old Europe:muscle: have entered into a :pray: holy alliance :pray:to exorcise this spectre:ghost::ghost::ghost:: Pope :poop::poop:and Tsar:poop::thumbsdown::thumbsdown:, Metternich:poop: and Guizot:poop::poop::poop:')

    elif message.content.startswith('!cpusa'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/cpusa.png')

    elif message.content.startswith('!cyberpunk'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/cyberpunk.gif')

    elif message.content.startswith('!durruti'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/durruti.png')

    elif message.content.startswith('!ezln'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/ezlnisbae.png')

    elif message.content.startswith('!fullcommunism'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/fc.png')

    elif message.content.startswith('!facepalm'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/facepalm.png')

    elif message.content.startswith('!fascist'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/antifa2.png')

    elif message.content.startswith('!feminism'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/feminism.png\n```The struggle against patriarchy is an essential part of class conflict and the anarchist struggle against the state and capital. In essence, anarchist struggle is a necessary component of feminist struggle and vice versa.```')

    elif message.content.startswith('!fresh'):
        yield from client.send_message(message.channel, '```Now, this is a story all about how \nMy life got flipped-turned upside down \nAnd I\'d like to take a minute \n Just sit right there \nI\'ll tell you how I became the prince of a town called Bel-Air```')

    elif message.content.startswith('!goldman'):
        yield from client.send_message(message.channel, ':books: **Anarchism and Other Essays**: https://theanarchistlibrary.org/library/emma-goldman-anarchism-and-other-essays\n:books: **My Disillusionment in Russia** with Emma Goldman: https://theanarchistlibrary.org/library/emma-goldman-my-disillusionment-in-russia\n:books: **My Further Disillusionment in Russia**: https://theanarchistlibrary.org/library/emma-goldman-my-further-disillusionment-in-russia\n:books: **Voltairine De Cleyre**: https://theanarchistlibrary.org/library/emma-goldman-voltairine-de-cleyre')

    elif message.content.startswith('!gulag'):
        yield from client.send_message(message.channel, 'https://libcom.org/history/gay-gulag')

    elif message.content.startswith('!hitler'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/hitler.png')

    elif message.content.startswith('!hacktheplanet'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/hacktheplanet.png')

    elif message.content.startswith('!horseshoe'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/horseshoe.png')

    elif message.content.startswith('!hoxha'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/hoxha.png')

    elif message.content.startswith('!ideology'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/ideology.png')


    elif message.content.startswith('!kitty'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/kitty.png')

    elif message.content.startswith('!kronstadt'):
        yield from client.send_message(message.channel, 'http://www.veoh.com/watch/v18771330YDwTzP3g')

    elif message.content.startswith('!kropotkin'):
        yield from client.send_message(message.channel, ':books: **The Conquest of Bread **: https://theanarchistlibrary.org/library/petr-kropotkin-the-conquest-of-bread\n:books: **The Commune of Paris **: https://theanarchistlibrary.org/library/petr-kropotkin-the-commune-of-paris\n:books: **Mutual Aid: A Factor of Evolution **: https://theanarchistlibrary.org/library/petr-kropotkin-mutual-aid-a-factor-of-evolution\n:books: **Communism and Anarchy**: https://theanarchistlibrary.org/library/petr-kropotkin-communism-and-anarchy')

    elif message.content.startswith('!leftcom'):
        yield from client.send_message(message.channel, 'https://i.redd.it/gvz9lqn26kux.png')

    elif message.content.startswith('!leftunity'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/love.png')

    elif message.content.startswith('!lenin'):
        yield from client.send_message(message.channel, 'a counter-revolutionary class traitor, who is responsible for the creation of the state-capitalist dictatorship known as the USSR. Along with other state-capitalist dictators such as Stalin and Mao, Lenin has tarnished the reputation of communism better than any capitalist or fascist ever could. http://www.gooseberrycollective.net/bots/lenin1.png\nhttp://www.gooseberrycollective.net/bots/lenin2.png')

    elif message.content.startswith('!lenny'):
        yield from client.send_message(message.channel, '( ͡° ͜ʖ ͡°)')

    elif message.content.startswith('!liberals'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/liberals.gif')

    elif message.content.startswith('!linux'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/linux.png')

    elif message.content.startswith('!makhno'):
        yield from client.send_message(message.channel, 'https://www.youtube.com/watch?v=WGqkyHd1cZk')

    elif message.content.startswith('!malatesta'):
        yield from client.send_message(message.channel, '**Errico Malatesta** (14 December 1853 – 22 July 1932) was an Italian anarchist. He spent much of his life exiled from Italy and in total spent more than ten years in prison. Malatesta wrote and edited a number of radical newspapers and was also a friend of Mikhail Bakunin.\n\n:books: **At The Café **: https://theanarchistlibrary.org/library/errico-malatesta-at-the-cafe\n\n:books: **Anarchism and Organization **: https://theanarchistlibrary.org/library/errico-malatesta-anarchism-and-organization \n\n:books: **Democracy and Anarchy **: https://theanarchistlibrary.org/library/errico-malatesta-democracy-and-anarchy \n\n:books: **Mutual Aid: An Essay  **: https://theanarchistlibrary.org/library/errico-malatesta-mutual-aid-an-essay \nhttp://www.gooseberrycollective.net/bots/malatesta.jpg')

    elif message.content.startswith('!marx'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/marx1.png')

    elif message.content.startswith('!memes'):
        yield from client.send_message(message.channel, 'https://we.riseup.net/goatgooseberry/meme-commands')

    elif message.content.startswith('!misandry'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/misandry.png')

    elif message.content.startswith('!motivation'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/motivation.png')

    elif message.content.startswith('!mutualism'):
        yield from client.send_message(message.channel, '"Mutualism is not a specific social, political or economic system. It is—at its core—an ethical philosophy. We begin with mutuality or reciprocity—the Golden Rule, more or less—and then seek to apply that principle in a variety of situations. As a result, under mutualism every meaningfully social relation will have the form of an anarchic encounter between equally unique individuals—free absolutes—no matter what layers of convention we pile on it." \n\n—Shawn P. Wilbur, *"Two-Gun Mutualism and The Golden Rule"* \n\nMutualism is an anti-capitalist economic theory and anarchist school of thought that advocates a society where each person might possess a means of production, either individually or collectively, with trade representing equivalent amounts of labor in a "freed market".\nMutualists believe that it is the state enforcement of capitalist property relations that alienates the working class from the means of production and subsistence and allows exploitation in the forms of profit, interest, and rents. Therefore, they wish to see private property abolished and replaced with possession-and-use, "the land to the cultivator, the mine to the miner, the tool to the laborer."\n\n:books: **Recommended reading**: :books: \n\n**[A Mutualist FAQ]** http://www.mutualist.org/id23.html\n **[Markets Not Capitalism]** https://goo.gl/YM4Gx1 \n**[What is Property?]** https://goo.gl/kkAgKx \n:books: **In-Depth**: :books:\n **[Studies in Mutualist Political Economy]** https://goo.gl/3rcWrn \n**[Kevin Carson\'s blog with links to his books]** http://mutualist.blogspot.ca/ \n**[humanispherian\'s blog with translations of Proudhon]** https://www.mutualism.info/ \n:books: **Further reading**: :books: \n**[C4SS Studies]** https://c4ss.org/content/category/studies \n**[Kevin Carson\'s suggested reading list]** http://www.mutualist.org/id6.html')

    elif message.content.startswith('!ohwell'):
        yield from client.send_message(message.channel, '¯\_(ツ)_/¯')

    elif message.content.startswith('!outside'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/outside.png')

    elif message.content.startswith('!poblacht'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/poblacht.png')

    elif message.content.startswith('!popcorn'):
        yield from client.send_message(message.channel, 'https://ipfs.pics/QmW3FgNGeD46kHEryFUw1ftEUqRw254WkKxYeKaouz7DJA')

    elif message.content.startswith('!proudhon'):
        yield from client.send_message(message.channel, '**Pierre-Joseph Proudhon** (15 January 1809 – 19 January 1865) was a French politician and the founder of mutualist philosophy. He was the first person to declare himself an anarchist and is widely regarded as one of the ideology\'s most influential theorists. Proudhon is even considered by many to be the "father of anarchism". He became a member of the French Parliament after the revolution of 1848, whereafter he referred to himself as a federalist.\n:books: **What is Property?**: https://theanarchistlibrary.org/library/pierre-joseph-proudhon-what-is-property-an-inquiry-into-the-principle-of-right-and-of-governmen\n:books: **System of Economical Contradictions**: https://theanarchistlibrary.org/library/pierre-joseph-proudhon-system-of-economical-contradictions-or-the-philosophy-of-poverty\n:books: **God is Evil, Man is Free **: https://theanarchistlibrary.org/library/pierre-joseph-proudhon-god-is-evil-man-is-free\n:books: **General Idea of the Revolution in the Nineteenth Century**: http://fair-use.org/p-j-proudhon/general-idea-of-the-revolution/\nhttp://www.gooseberrycollective.net/bots/proudhon1.png')

    elif message.content.startswith('!pusheen'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/pusheen1.png\nhttp://www.gooseberrycollective.net/bots/pusheen2.png\nhttp://www.gooseberrycollective.net/bots/pusheen3.png\nhttp://www.gooseberrycollective.net/bots/pusheen4.png')

    elif message.content.startswith('!rainbowstalin'):
        yield from client.send_message(message.channel, 'http://rainbowstalin5.ytmnd.com/')

    elif message.content.startswith('!reddit'):
        yield from client.send_message(message.channel, 'http://gooseberrycollective.net/doku.php?id=radical_reddit')

    elif message.content.startswith('!revolution'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/revolution.png')

    elif message.content.startswith('!rsoc'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/rsoc1.png\nhttp://www.gooseberrycollective.net/bots/rsoc2.png')

    elif message.content.startswith('!rules'):
        yield from client.send_message(message.channel, 'http://pastebin.com/KpfbM3iC')

    elif message.content.startswith('!stirnerwave'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/stirnerwave.png')

    elif message.content.startswith('!sjw'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/sjw.png')

    elif message.content.startswith('!space'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/space.png')

    elif message.content.startswith('!sparkles'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/sparkles.gif')

    elif message.content.startswith('!spook'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/spook.png')

    elif message.content.startswith('!stirner'):
        yield from client.send_message(message.channel, '**Max Stirner** (October 25, 1806 – June 26, 1856) was a German philosopher. He is often seen as one of the forerunners of nihilism, existentialism, psychoanalytic theory, postmodernism, and anarchism, especially of individualist anarchism.\n:books: **The Ego and His Own **: https://theanarchistlibrary.org/library/max-stirner-the-ego-and-his-own\n:books: **Art and Religion **: https://theanarchistlibrary.org/library/max-stirner-art-and-religion\n:books: **The False Principle of Our Education **: https://theanarchistlibrary.org/library/max-stirner-the-false-principle-of-our-education\n:books: **Stirner’s Critics **: https://theanarchistlibrary.org/library/max-stirner-stirner-s-critics\nhttp://www.gooseberrycollective.net/bots/stirner.gif')

    elif message.content.startswith('!source'):
        yield from client.send_message(message.channel, 'https://github.com/subvertc/voltairine')

    elif message.content.startswith('!tankie'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/tankie1.png')

    elif message.content.startswith('!tarot'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/tarot.png')

    elif message.content.startswith('!trotsky'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/trotsky.jpg')

    elif message.content.startswith('!trump'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/trump1.png')

    elif message.content.startswith('!tea'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/tea.png')

    elif message.content.startswith('!usa'):
        yield from client.send_message(message.channel, '"The US has done a numerous amount of unspeakable crimes against humanity"')

    elif message.content.startswith('!vaporwave'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/vaporwave.png')

    elif message.content.startswith('!vegan'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/vegan.png')

    elif message.content.startswith('!vote'):
        yield from client.send_message(message.channel, 'http://www.gooseberrycollective.net/bots/vote.png')

    elif message.content.startswith('!whisper'):
        yield from client.send_message(message.author, 'pssst')
        
    elif message.content.startswith('!insult'):
        j = random.randint(0,18)
        k = random.randint(0,17)
        l = random.randint(0,18)
        yield from client.send_message(message.channel, '```You\'re ' + insult1[j] + ' ' + insult2[k] + ' ' + insult3[l] + '```')

    elif message.content.startswith('!compliment'):
        j = random.randint(0,18)
        k = random.randint(0,17)
        l = random.randint(0,18)
        yield from client.send_message(message.channel, '```You\'re ' + compliment1[j] + ' ' + compliment2[k] + ' ' + compliment3[l] + '```')

    elif message.content.startswith('!coin'):
        j = random.randint(1,2)
        if j == 1:
            yield from client.send_message(message.channel, '```Heads!```')
        else:
            yield from client.send_message(message.channel, '```Tails!```')
            
    elif message.content.startswith('!d4'):
        j = random.randint(1,4)
        yield from client.send_message(message.channel, '```Rolling a d4\nRolled a ' + str(j) + '```')

    elif message.content.startswith('!d6'):
        j = random.randint(1,6)
        yield from client.send_message(message.channel, '```Rolling a d6\nRolled a ' + str(j) + '```')

    elif message.content.startswith('!d8'):
        j = random.randint(1,8)
        yield from client.send_message(message.channel, '```Rolling a d8\nRolled a ' + str(j) + '```')

    elif message.content.startswith('!d10'):
        j = random.randint(1,10)
        yield from client.send_message(message.channel, '```Rolling a d10\nRolled a ' + str(j) + '```')

    elif message.content.startswith('!d12'):
        j = random.randint(1,12)
        yield from client.send_message(message.channel, '```Rolling a d12\nRolled a ' + str(j) + '```')
    elif message.content.startswith('!d20'):
        j = random.randint(1,20)
        yield from client.send_message(message.channel, '```Rolling a d20\nRolled a ' + str(j) + '```')

    elif message.content.startswith('!swing'):
        j = random.randint(0,1)
        if j == 0:
            msg = 'They miss, burrying their sword into the ground'
        elif j == 1:
            msg = 'They hit. Cleaving the enemy in two'
        yield from client.send_message(message.channel,'```' +  message.author.name + ' swings their mighty sword\n' +msg+'```')

    elif message.content.startswith('!inventory'):
        if message.author not in user_gold:
           user_gold[message.author] = 0
        if message.author not in user_potions:
            user_potions[message.author] = 0

        yield from client.send_message(message.channel, '```'+message.author.name+' has '+str(user_gold[message.author])+' gold and '+str(user_potions[message.author])+' potions```')

    elif message.content.startswith('!encounter'):
        k = random.randint(0,3)
        enemy = ['ancap', 'tankie', 'fascist', 'liberal', 'trump', 'cop']
        enemy_pic = ['https://ipfs.pics/ipfs/QmUq6F6NbYznU9y65Pc17gG8rSBx9w42224FneG3EspgXX','https://ipfs.pics/QmRCh7AFfyL3ZSXCbF6ax6NjkrMwCCqgar8RoajCYp6Zot','https://ipfs.pics/QmSrPJqzc8dzni8EwvGMg3GJuNLrL4pwgfRNgeM68ZwF1s','https://ipfs.pics/QmTD8o6ZZ4Ppd4sbTMjY9Cf7SXmt7uTZdwuHwojyTLNtcs','https://ipfs.pics/QmdLNzYbiSfkEKp2mDotu1yCRabi43iopkFxdJBfaKJW93','https://ipfs.pics/QmcdWyBSp78n65VhxrFHgvLhjvfkA7FyKtTtwAnFx3Rszp']
        enemy_hp = [15,15, 17, 10, 15,20]
        enemy_hp_l = int(enemy_hp[k])
        player_hp = 20
        player_dmg = 0
        enemy_dmg = 0
        yield from client.send_message(message.channel, enemy_pic[k]+'\n```A '+enemy[k]+' appears!```')

        while enemy_hp_l > 0 and player_hp > 0:
            yield from client.send_message(message.channel, '```The '+enemy[k]+' has ' + str(enemy_hp_l) + ' hp \n'+message.author.name+' has ' + str(player_hp) + ' hp```')
            msg = yield from client.wait_for_message(author=message.author)
            if msg.content == 'attack' or msg.content == '!sttack':
                player_dmg = random.randint(1,12)
                enemy_hp_l = (enemy_hp_l - player_dmg)
                if enemy_hp_l < 0:
                    enemy_hp_l = 0
            elif msg.content == 'potion':
                if message.author not in user_potions:
                    user_potions[message.author] = 0
                if user_potions[message.author] > 0:
                    user_potions[message.author] -=1
                    player_hp +=5
                    yield from client.send_message(message.channel, '``` '+message.author.name+' used a potion. Their hp went up by 5```')
                    continue
                elif user_potions[message.author] == 0:
                    yield from client.send_message(message.channel, '```'+message.author.name+' fumbles around in their bag for a potion that isn\'t there')
            else:
                yield from client.send_message(message.channel, '```Accepted input, attack, potion```')

            if enemy_hp_l <= 0:
                gold = random.randint(1, 8)
                yield from client.send_message(message.channel, '```'+message.author.name+' defeats the '+enemy[k]+' and finds ' + str(gold) + ' gold!```')
                if message.author not in user_gold:
                    user_gold[message.author] = gold
                else:
                    user_gold[message.author] += gold
                break
                
            enemy_dmg = random.randint(1,12)
            player_hp = (player_hp - enemy_dmg)
            yield from client.send_message(message.channel, '```'+message.author.name+' swings, dealing ' + str(player_dmg) + ' damage.\nThe '+enemy[k]+' swings, dealing '+ str(enemy_dmg) +' damage.```')  
        
            if player_hp <= 0:
                yield from client.send_message(message.channel, '```The '+enemy[k]+' overpowers '+message.author.name+' and they black out```')

    elif message.content.startswith ('!shop'):
        if message.author not in user_gold:
            user_gold[message.author] = 0
        if message.author not in user_potions:
            user_potion[message.author] = 0
        yield from client.send_message(message.channel, '```Welcome to the shop!```\nPotion - 5g')
        msg = yield from client.wait_for_message(author=message.author)
        if msg.content == 'potion' or msg.content == 'Potion':
            if user_gold[message.author]<5:
                yield from client.send_message(message.channel, 'You don\'t have enough gold to buy this item')
            user_potions[message.author]+=1
            user_gold[message.author]-=5
            yield from client.send_message(message.channel, '```'+message.author.name+' bought a potion.\nThank you for visiting the shop!```')

    
#    elif message.content.startswith('!d100'):
#       yield from User.mention(message.author)
#        yield from client.send_message(message.channel, 'Rolled a ' + random.randint(1,100))



client.run('token')
