import re
import long_responses as long

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
     message_certainty = 0
      has_required_words = True
