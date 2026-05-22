import json

years = [
    {"year": 2012, "count": 48, "memes": [
        {"emoji": "😾", "name": "Grumpy Cat", "desc": "The feline embodiment of Monday mornings.", "score": 95, "platform": "Reddit"},
        {"emoji": "💃", "name": "Gangnam Style", "desc": "The invisible horse dance that broke YouTube's view counter.", "score": 99, "platform": "YouTube"},
        {"emoji": "🤦‍♂️", "name": "Overly Attached Girlfriend", "desc": "The stare that launched a thousand restraining orders.", "score": 88, "platform": "YouTube"},
        {"emoji": "🤷‍♂️", "name": "Ridiculously Photogenic Guy", "desc": "Looking flawless while running a marathon.", "score": 85, "platform": "Reddit"},
        {"emoji": "👀", "name": "Ermahgerd", "desc": "Goosebumps enthusiasm taken to phonetic extremes.", "score": 82, "platform": "Reddit"},
        {"emoji": "🐻", "name": "Ted", "desc": "The foul-mouthed teddy bear that ruined childhoods.", "score": 78, "platform": "Twitter"}
    ]},
    {"year": 2013, "count": 52, "memes": [
        {"emoji": "🐕", "name": "Doge", "desc": "Much wow. Very meme. Such internet.", "score": 98, "platform": "Reddit"},
        {"emoji": "🕺", "name": "Harlem Shake", "desc": "30 seconds of chaotic, uncoordinated dancing.", "score": 94, "platform": "YouTube"},
        {"emoji": "🦊", "name": "What Does the Fox Say?", "desc": "The existential question of the year.", "score": 91, "platform": "YouTube"},
        {"emoji": "😒", "name": "Side Eyeing Chloe", "desc": "The ultimate expression of unimpressed skepticism.", "score": 89, "platform": "YouTube"},
        {"emoji": "👑", "name": "Lord Disick", "desc": "Reality TV royalty declaring his supremacy.", "score": 75, "platform": "Twitter"},
        {"emoji": "🏃", "name": "Prancing Cera", "desc": "Michael Cera awkwardly skipping through history.", "score": 72, "platform": "Reddit"}
    ]},
    {"year": 2014, "count": 61, "memes": [
        {"emoji": "🐸", "name": "Kermit Sipping Tea", "desc": "But that's none of my business.", "score": 96, "platform": "Twitter"},
        {"emoji": "🧊", "name": "Ice Bucket Challenge", "desc": "Freezing for a good cause.", "score": 99, "platform": "Facebook"},
        {"emoji": "🍑", "name": "Kim K Break the Internet", "desc": "The magazine cover that spawned a million parodies.", "score": 92, "platform": "Twitter"},
        {"emoji": "👦", "name": "Alex from Target", "desc": "Accidental retail heartthrob.", "score": 85, "platform": "Twitter"},
        {"emoji": "🥔", "name": "Potato Salad Kickstarter", "desc": "Raising $55,000 for a side dish.", "score": 81, "platform": "Kickstarter"},
        {"emoji": "🦈", "name": "Left Shark", "desc": "The Super Bowl halftime show's true MVP.", "score": 88, "platform": "Twitter"}
    ]},
    {"year": 2015, "count": 58, "memes": [
        {"emoji": "👗", "name": "The Dress", "desc": "Black and blue or white and gold? The debate that tore families apart.", "score": 99, "platform": "Tumblr"},
        {"emoji": "🐸", "name": "Pepe the Frog", "desc": "Feels good, man.", "score": 95, "platform": "4chan"},
        {"emoji": "🔥", "name": "This is Fine", "desc": "A dog calmly accepting his fiery demise.", "score": 97, "platform": "Reddit"},
        {"emoji": "🎺", "name": "Unexpected John Cena", "desc": "His name is John Cena! *horns blare*", "score": 91, "platform": "Vine"},
        {"emoji": "🍕", "name": "Pizza Rat", "desc": "A New York hero carrying a slice down the subway stairs.", "score": 89, "platform": "YouTube"},
        {"emoji": "👟", "name": "What Are Those?!", "desc": "The ultimate footwear roast.", "score": 86, "platform": "Vine"}
    ]},
    {"year": 2016, "count": 74, "memes": [
        {"emoji": "🦍", "name": "Harambe", "desc": "Gone but never forgotten.", "score": 98, "platform": "Twitter"},
        {"emoji": "🐸", "name": "Dat Boi", "desc": "Here come dat boi! O shit waddup!", "score": 92, "platform": "Tumblr"},
        {"emoji": "🤔", "name": "Roll Safe", "desc": "You can't fail if you don't try.", "score": 94, "platform": "Twitter"},
        {"emoji": "🗑️", "name": "Evil Kermit", "desc": "Me: Save money. Inner me: Buy it.", "score": 95, "platform": "Twitter"},
        {"emoji": "🚶", "name": "Arthur's Fist", "desc": "Suppressed rage in cartoon form.", "score": 91, "platform": "Twitter"},
        {"emoji": "💧", "name": "Water Bottle Flip", "desc": "The satisfying thud of a perfect landing.", "score": 88, "platform": "YouTube"}
    ]},
    {"year": 2017, "count": 69, "memes": [
        {"emoji": "👀", "name": "Distracted Boyfriend", "desc": "The stock photo that defined a generation of choices.", "score": 99, "platform": "Twitter"},
        {"emoji": "🧠", "name": "Expanding Brain", "desc": "Ascending levels of cosmic irony.", "score": 96, "platform": "Reddit"},
        {"emoji": "🧂", "name": "Salt Bae", "desc": "Sprinkling seasoning with unnecessary flair.", "score": 93, "platform": "Instagram"},
        {"emoji": "🌭", "name": "Dancing Hot Dog", "desc": "Snapchat's greatest contribution to society.", "score": 89, "platform": "Snapchat"},
        {"emoji": "🐒", "name": "Mocking SpongeBob", "desc": "tHe StOcK pHoTo ThAt DeFiNeD a GeNeRaTiOn.", "score": 95, "platform": "Twitter"},
        {"emoji": "🗑️", "name": "Trash Dove", "desc": "The purple bird that headbanged its way into our hearts.", "score": 82, "platform": "Facebook"}
    ]},
    {"year": 2018, "count": 83, "memes": [
        {"emoji": "🦋", "name": "Is This a Pigeon?", "desc": "Anime android misidentifying basic objects.", "score": 97, "platform": "Twitter"},
        {"emoji": "😲", "name": "Surprised Pikachu", "desc": "When the obvious consequence actually happens.", "score": 98, "platform": "Reddit"},
        {"emoji": "🚗", "name": "Car Salesman Slaps Roof", "desc": "This bad boy can fit so much spaghetti in it.", "score": 92, "platform": "Reddit"},
        {"emoji": "🗣️", "name": "Yanny vs Laurel", "desc": "The auditory sequel to The Dress.", "score": 95, "platform": "Twitter"},
        {"emoji": "🚶", "name": "Moth Lamp", "desc": "Bröther, may I have some lämp?", "score": 90, "platform": "Reddit"},
        {"emoji": "💪", "name": "Weird Flex But OK", "desc": "The perfect response to bizarre bragging.", "score": 94, "platform": "Twitter"}
    ]},
    {"year": 2019, "count": 91, "memes": [
        {"emoji": "🐱", "name": "Woman Yelling at Cat", "desc": "The ultimate clash of raw emotion and feline confusion.", "score": 99, "platform": "Twitter"},
        {"emoji": "👽", "name": "Storm Area 51", "desc": "They can't stop all of us.", "score": 96, "platform": "Facebook"},
        {"emoji": "👶", "name": "Baby Yoda", "desc": "The cutest thing in the galaxy sipping soup.", "score": 98, "platform": "Twitter"},
        {"emoji": "🤡", "name": "Joker Stairs", "desc": "Dancing your way down into madness.", "score": 91, "platform": "Reddit"},
        {"emoji": " Kombucha", "name": "Kombucha Girl", "desc": "The rapid cycle of disgust and intrigue.", "score": 93, "platform": "TikTok"},
        {"emoji": "📈", "name": "Stonks", "desc": "Financial genius in a surreal 3D render.", "score": 95, "platform": "Reddit"}
    ]},
    {"year": 2020, "count": 127, "memes": [
        {"emoji": "⚰️", "name": "Coffin Dance", "desc": "Astronomical consequences set to EDM.", "score": 99, "platform": "TikTok"},
        {"emoji": "🌍", "name": "Nature is Healing", "desc": "We are the virus. The dolphins are returning.", "score": 95, "platform": "Twitter"},
        {"emoji": "🍰", "name": "Everything is Cake", "desc": "Trust nothing. Slice everything.", "score": 97, "platform": "Twitter"},
        {"emoji": "🐕", "name": "Swole Doge vs Cheems", "desc": "Glorious past vs pathetic present.", "score": 96, "platform": "Reddit"},
        {"emoji": "🐯", "name": "Tiger King", "desc": "The chaotic distraction we needed in lockdown.", "score": 94, "platform": "Netflix"},
        {"emoji": "🧑‍🚀", "name": "Always Has Been", "desc": "The ultimate betrayal in space.", "score": 93, "platform": "Reddit"}
    ]},
    {"year": 2021, "count": 108, "memes": [
        {"emoji": "🚢", "name": "Ever Given", "desc": "One boat blocking global trade.", "score": 98, "platform": "Twitter"},
        {"emoji": "🧤", "name": "Bernie's Mittens", "desc": "Cozy, practical, and unimpressed at the inauguration.", "score": 99, "platform": "Twitter"},
        {"emoji": "🦍", "name": "Ape Together Strong", "desc": "Diamond hands holding the line.", "score": 97, "platform": "Reddit"},
        {"emoji": "🔴", "name": "Squid Game", "desc": "Red light, green light, existential dread.", "score": 95, "platform": "TikTok"},
        {"emoji": "🚩", "name": "Red Flags", "desc": "When they say they don't like Shrek.", "score": 92, "platform": "Twitter"},
        {"emoji": " Anakin", "name": "Anakin and Padme", "desc": "For the better, right?", "score": 94, "platform": "Reddit"}
    ]},
    {"year": 2022, "count": 95, "memes": [
        {"emoji": "🦇", "name": "Morbius", "desc": "It's Morbin' time.", "score": 96, "platform": "Twitter"},
        {"emoji": "👦", "name": "Kid Named Finger", "desc": "Breaking Bad irony reaching critical mass.", "score": 91, "platform": "Reddit"},
        {"emoji": "🐶", "name": "Let Me Do It For You", "desc": "The long-snouted borzoi offering assistance.", "score": 94, "platform": "TikTok"},
        {"emoji": "🌽", "name": "Corn Kid", "desc": "It has the juice.", "score": 95, "platform": "TikTok"},
        {"emoji": "🧍", "name": "Kevin James Smirk", "desc": "The king of queens looking mischievously shy.", "score": 92, "platform": "Twitter"},
        {"emoji": "🧠", "name": "Wise Mystical Tree", "desc": "If you're over 25 and own a computer...", "score": 89, "platform": "TikTok"}
    ]},
    {"year": 2023, "count": 88, "memes": [
        {"emoji": "🚽", "name": "Skibidi Toilet", "desc": "Gen Alpha's incomprehensible masterpiece.", "score": 98, "platform": "YouTube"},
        {"emoji": "🩷", "name": "Barbenheimer", "desc": "The ultimate cinematic double feature.", "score": 99, "platform": "Twitter"},
        {"emoji": "👽", "name": "Mexican Alien", "desc": "The papier-mâché extraterrestrial.", "score": 93, "platform": "Twitter"},
        {"emoji": "🧢", "name": "Smurf Cat", "desc": "We live, we love, we lie.", "score": 95, "platform": "TikTok"},
        {"emoji": "🍟", "name": "Grimace Shake", "desc": "Happy birthday Grimace... *collapses*", "score": 96, "platform": "TikTok"},
        {"emoji": " Roman", "name": "Roman Empire", "desc": "How often do you think about it?", "score": 94, "platform": "TikTok"}
    ]},
    {"year": 2024, "count": 79, "memes": [
        {"emoji": "🐻", "name": "Man vs Bear", "desc": "The hypothetical question that divided the internet.", "score": 95, "platform": "TikTok"},
        {"emoji": "🥥", "name": "Coconut Tree", "desc": "You think you just fell out of a coconut tree?", "score": 97, "platform": "Twitter"},
        {"emoji": "🕺", "name": "Raygun", "desc": "Olympic breakdancing redefined.", "score": 98, "platform": "Twitter"},
        {"emoji": "🍎", "name": "Apple Vision Pro Bros", "desc": "Walking through the city pinching the air.", "score": 92, "platform": "Twitter"},
        {"emoji": "🧠", "name": "Brainrot", "desc": "What the sigma?", "score": 96, "platform": "TikTok"},
        {"emoji": "🐱", "name": "Pop Cat Returns", "desc": "The classic returns with a vengeance.", "score": 88, "platform": "Reddit"}
    ]},
    {"year": 2025, "count": 67, "memes": [
        {"emoji": "🤖", "name": "AI Hallucinations", "desc": "When the LLM insists 2+2=5 with absolute confidence.", "score": 96, "platform": "Twitter"},
        {"emoji": "🕶️", "name": "Neuralink Glitch", "desc": "When your brain chip buffers mid-sentence.", "score": 94, "platform": "TikTok"},
        {"emoji": "🚀", "name": "Mars Colony HOA", "desc": "Complaining about the neighbor's rover parking.", "score": 91, "platform": "Reddit"},
        {"emoji": "🧊", "name": "Deep Freeze Challenge", "desc": "The new ice bucket, but with liquid nitrogen.", "score": 89, "platform": "TikTok"},
        {"emoji": "👽", "name": "Disclosure Day", "desc": "They're real, and they're judging our memes.", "score": 98, "platform": "Twitter"},
        {"emoji": "🕰️", "name": "Time Traveler's Regret", "desc": "Going back to 2012 just to buy Bitcoin.", "score": 93, "platform": "Reddit"}
    ]}
]

html_output = ""
for year_data in years:
    year = year_data["year"]
    count = year_data["count"]
    memes = year_data["memes"]
    
    html_output += f'''
    <!-- YEAR {year} -->
    <section class="year-section" id="year-{year}">
        <div class="year-header">
            <h2 class="year-label" data-speed="0.3">{year}</h2>
            <div class="year-stats fade-up">
                <span class="stat-label">Memes Catalogued</span>
                <span class="stat-number counter" data-target="{count}">0</span>
            </div>
        </div>
        
        <div class="meme-grid">'''
    
    for meme in memes:
        html_output += f'''
            <div class="meme-card fade-up">
                <div class="meme-emoji">{meme["emoji"]}</div>
                <h3 class="meme-name">{meme["name"]}</h3>
                <p class="meme-desc">{meme["desc"]}</p>
                
                <div class="meme-meta">
                    <span class="platform-tag">{meme["platform"]}</span>
                    <div class="virality-container">
                        <span class="virality-label">Virality Score</span>
                        <div class="virality-bar">
                            <div class="virality-fill" data-width="{meme["score"]}%"></div>
                        </div>
                    </div>
                </div>
            </div>'''
            
    html_output += '''
        </div>
    </section>'''

with open("/home/ubuntu/meme_html.txt", "w") as f:
    f.write(html_output)

print("Generated HTML content for memes.")
