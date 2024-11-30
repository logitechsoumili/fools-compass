from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

bad_advice = {  
    "just_vibing_in_ohio": [  
        "go full sigma grindset: wake up at 3am, drink raw eggs, and hit the griddy on the treadmill.",  
        "google 'biggest bird in ohio' and let the search results guide your life choices.",  
        "buy a sussy plushie and call it emotional support. name it glizzy.",  
        "listen to the freddy fazbear ambience while journaling about your nonexistent rizz.",
        "join a random discord server and call everyone 'bro thinks he's carti.' see how long you last.",  
        "buy a freddy fazbear costume and wear it while doing the 1 2 buckle my shoe trend.",  
        "whisper 'kiki, do you love me?' into your microwave and wait for a reply.",  
        "convince yourself that ambatukam is a life philosophy and act accordingly.",  
        "order a whopper, but only in ohio, and insist it's the only real whopper.",  
        "play subway surfers on mute and add live commentary like you're a sigma narrator.",
        "start a podcast about your indecisiveness. call it 'idk tho.'",
        "manifest good vibes by staring at your reflection until you cry."  
    ],  
    "mid_no_cap": [  
        "move to ohio and become the mayor of brainrot city. population: you.",  
        "download subway surfers gameplay compilations for *inspiration.*",  
        "hit the ocky way deli and ask for the 'grimace shake combo' with no remorse.",  
        "look in the mirror and practice your lightskin stare. it's self-care, trust me.",
        "post your baby photos online and caption them 'bro was quirked up even at 2.'",  
        "create a spotify playlist named 'pibby glitch anthems' and vibe alone.",  
        "learn mewing techniques so you can have the ultimate sigma jawline.",  
        "do the lightskin stare in public. don't blink. just keep staring.",  
        "ask chatgpt how to summon kevin james and see what happens.",  
        "write a love letter to grimace and mail it to mcdonald's corporate.",
        "become a professional hater. haters get clout.",
        "fix your life by deleting it and downloading a new one. try google."  
    ],  
    "existential_crisis": [  
        "blast sad npc music and whisper, 'amogus sus' through the tears.",  
        "call your shampoo 'nathaniel b' and cry harder when it doesn't respond.",  
        "make a collage of meme templates and call it your emotional support vision board.",  
        "hug the showerhead and say 'ayo the pizza here' just to feel something.",
        "create a tear jar and label it 'sigma grindset fuel.'",  
        "blast 'sin city wasn't made for you' in the shower and sob while holding a loofah dramatically.",  
        "draw your shampoo bottle's face and cry harder when it 'stares' back.",  
        "start chanting 'quandale dingle' to drown out your existential crisis.",  
        "turn your soap bar into a 'weapon' and pretend you're in the backrooms.",
        "cry louder. it's free ASMR for your neighbors.",
        "take a nap in the bathtub. not a bubble bath, just water and vibes."  
    ],  
    "sigma_tantrum": [  
        "throw a grimace shake at your problems. if they don't go away, chug one yourself.",  
        "wear a trench coat and yell 'i am the biggest bird' at passing pigeons.",  
        "punch the air dramatically, but only after googling 'how to be goated with the sauce.'",  
        "shout 'PLUH' while eating spicy chips, because pain is temporary, cringe is forever.",
        "stare at your reflection and shout 'biggest bird' until you feel better.",  
        "practice sigma poses in your room. extra points if you live-stream it.",  
        "scream 'it's morbin time!' in the middle of an argument for instant dominance.",  
        "declare war on the mosquito that ruined your summer. this is personal now.",  
        "order a whopper the ocky way and eat it while glaring at your enemies.",
        "smash a vase. make it look intentional and call it art.",
        "channel your rage into knitting. stab something with style."  
    ],  
    "delulu_state": [  
        "claim you're the chosen one, summoned by a mosquito to the backrooms.",  
        "start a channel teaching people how to rizz up Baby Gronk with a kazoo.",  
        "send a cryptic message to your ex: 'i'm chilling with freddy fazbear, in my sigma era.'",  
        "replace your wardrobe with 'i'm just a girl' shirts, and call it fashion.",  
        "post a tiktok claiming you're the reincarnation of 'goated with the sauce'.",  
        "write an autobiography called 'surviving shadow wizard money gang and still pulling.'",  
        "conspiracy theory: all mosquitoes are secretly working for DJ Khaled. Discuss it loudly.",  
        "tell your friend, 'if we hit the gym, we'll unlock the power of the grimace shake.'",  
        "build a shrine to John Pork with pizza tower slices and a broken kazoo.",  
        "start a cult chanting 'bussing axel in harlem while mewing' and never explain it."  
    ]
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_advice/<mood>")
def get_bad_advice(mood):
    if mood in bad_advice:
        advice = random.choice(bad_advice[mood])
    else:
        advice = "embrace the chaos, my friend."
    return jsonify({"advice": advice})

if __name__ == "__main__":
    app.run()
