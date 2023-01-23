import re
import long_responses as long

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
     message_certainty = 0
      has_required_words = True

# Counts how many words are present in each predefined message
for word in user_message:
        if word in recognised_words:
            message_certainty += 1

# Calculates the percent
percentage = float(message_certainty) / float(len(recognised_words))

#Check strings
for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

 if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0
