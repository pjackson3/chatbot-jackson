"""Use the wordlists to respond to string inputs.

Copyright (C) Peter Jackson Link III.

This file is part of Chatbot.

    Chatbot is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Chatbot is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Chatbot.  If not, see <https://www.gnu.org/licenses/>.
"""

import random
from .dictionary_words import dictionary_words
from .random_words import random_words


def use_words(sentence: str) -> str:
    """Respond to a sentence with a smart reply."""
    # The list to hold matching responses.
    responses = []

    for word in sentence.split(' '):  # Seperate the words in the sentence.
        # Check if there is a "smart" response.
        if word.lower() in dictionary_words.keys():
            # Save responses into the array.
            responses.append(dictionary_words[word])

    if len(responses) > 0:
        return random.choice(responses)

    index = random.randint(0, len(random_words) - 1)

    response = random_words[index]

    random_words[index] = sentence

    return response
