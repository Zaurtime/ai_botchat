import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_START = "Car engine is ready to fly please adjust seat belt"
R_LIGHTS = "Your lights is on.Now turn on music and command further"
R_MUSIC = "Volume to the maximum and your favorite music will play in 5 seconds..."
R_NAV = "Google map find and show direction and drive to exact location "
R_AC = "A/C is On and cabin temperature auto regulated it is works perfectly "
R_PILOT = "Auto pilot mode activited please relax and fully enjoy "
R_PARK = "Parking assistant will do work for you in 10 seconds.We are scanning obstacles.Please wait for a moment"
R_HORN = "Horn pressed and biping bip-bip anything else I can do?!"
R_CONSUMPTION = "Your car consumption is an economical mode and you have 1000km more energy to drive forward"
R_CH = "Near staion is closer by 33km and we will stop to recharge battery"
R_SPEED = "Speed limit is blocked 140km per hour if you wish drive faster you need change setting to Manual mode"
R_MANUAL = "You are ready to drive faster than 140km per hour and your top speed 500km/h 'Good Luck'"
R_RADIO = "Radio fm is On and podcast playing now"
R_CAMERA = "Live camera working and recording.Face recognition system activated"
R_MOB = "All mobile app synchronized just check bluetooth"
R_BLUETOOTH = "Connecting bluetooth device and updating all mobile apps"
R_DOORS = "Door open be careful "
R_CLOSE = "The Car is locked and anti-theft future responsible for protection"
R_WIPER = "The wiper blade works and the glass is almost clean"


def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response