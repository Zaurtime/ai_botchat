import re
import long_responses as long

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
     message_certainty = 0
      has_required_words = True

# Counts how many words are present in each predefined message
for word in user_message:
        if word in recognised_words:
            message_certainty += 1
