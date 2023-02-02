import re
import long_responses as long

print(
    """
    
╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╭╮╱╭╮╱╱╱╱╱╭╮╱╱╱╱╭━━╮╱╱╱╭╮╱╭━━━┳━━╮
┃╭━╮┃╱╭╯╰╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╰╮╭╯┃╱┃┃╱╱╱╱╱┃┃╱╱╱╱┃╭╮┃╱╱╭╯╰╮┃╭━╮┣┫┣╯
┃┃╱┃┣╮┣╮╭╋━━┳━╮╭━━┳╮╭┳━━┳╮╭┳━━╮╰╮┃┃╭┻━┫╰━┳┳━━┫┃╭━━╮┃╰╯╰┳━┻╮╭╯┃┃╱┃┃┃┃
┃╰━╯┃┃┃┃┃┃╭╮┃╭╮┫╭╮┃╰╯┃╭╮┃┃┃┃━━┫╱┃╰╯┃┃━┫╭╮┣┫╭━┫┃┃┃━┫┃╭━╮┃╭╮┃┃╱┃╰━╯┃┃┃
┃╭━╮┃╰╯┃╰┫╰╯┃┃┃┃╰╯┃┃┃┃╰╯┃╰╯┣━━┃╱╰╮╭┫┃━┫┃┃┃┃╰━┫╰┫┃━┫┃╰━╯┃╰╯┃╰╮┃╭━╮┣┫┣╮
╰╯╱╰┻━━┻━┻━━┻╯╰┻━━┻┻┻┻━━┻━━┻━━╯╱╱╰╯╰━━┻╯╰┻┻━━┻━┻━━╯╰━━━┻━━┻━╯╰╯╱╰┻━━╯
    """
)

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies 
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo', 'yes'], single_response=True)
    response('See you!', ['bye', 'goodbye', 'no'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], single_response=True)
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], single_response=True)
    response('It is rainy!', ['weather', 'rain', 'windy'], required_words=['weather',])
    response('Code Institute projects', ['study', 'learn' , 'code' , 'project'], single_response=True)
    response('Lamborghini ASX', ['car', 'drive'], required_words=['car'])
    response('Google map check', ['location', 'where', 'far','near'], required_words=['location'])
    response('Everest Mountain', ['mountain', 'highest', 'top'], required_words=['top'])
    response('Seat belt fastened', ['belt', 'adjust'], required_words=['belt'])
    response('Brake hard', ['brake', 'stop', 'broken'], single_response=True)
    response('Opened please check', ['trunk', 'frunk', 'hood', 'window'], single_response=True)
    response('Reversed without obstacles', ['reverse', 'backside', 'back' ], single_response=True )
    response('Pressed,what is next?', ['gas', 'clutch', 'accelerator'], single_response=True) 
    
    
    
    # Longer responses
    response(long.R_ADVICE, ['give', 'advice', 'search'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['eat'])
    response(long.R_START, ['start', 'power', 'go' , 'move', 'drive'], single_response=True)
    response(long.R_LIGHTS, ['light', 'beam', 'bright', 'lights'], single_response=True)
    response(long.R_MUSIC, ['music', 'sound'], single_response=True)
    response(long.R_NAV, ['navigation', 'navigate', 'map'], single_response=True)
    response(long.R_AC, ['a/c', 'cool', 'warm'], single_response=True)
    response(long.R_PILOT, ['auto-pilot', 'pilot', 'auto', 'autopilot'], single_response=True)
    response(long.R_PARK, ['parking', 'park'], single_response=True)
    response(long.R_HORN, ['horn', 'press-horn'], single_response=True)
    response(long.R_CONSUMPTION, ['consumtion', 'fuel'], single_response=True)
    response(long.R_CH, ['charging', 'charge'], single_response=True)
    response(long.R_SPEED, ['speed', 'fast'], single_response=True)
    response(long.R_MANUAL, ['manual', 'gear'], single_response=True)
    response(long.R_RADIO, ['radio', 'fm'], single_response=True)
    response(long.R_CAMERA, ['camera', 'record'], single_response=True)
    response(long.R_MOB, ['mobile-app', 'mobile'], single_response=True)
    response(long.R_BLUETOOTH, ['bluetooth', 'connect'], single_response=True)
    response(long.R_DOORS, ['door', 'doors'], single_response=True)
    response(long.R_CLOSE, ['close', 'lock'], single_response=True)
    response(long.R_WIPER, ['wiper', 'wipe'], single_response=True)
    response(long.R_STOP, ['stop', 'end'], single_response=True)
    


 
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


def main():
    # Testing the response system
    print("I'm an Autonomous Vehicle Bot AI: Hello, Are you ready to Start the trip? Please feel free to torn on the music, I can hear you even if you silently say any command. I recently received the Voice Recognition Sensitivity Award 2023! Ask  me  anything")
    while True:
        print('Lamborghini Bot: ' + get_response(input('You: ')))


main()