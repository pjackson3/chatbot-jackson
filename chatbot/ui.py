"""The console user interface.

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

from chatbot.use_words import use_words


def ui():
    """Show the console user interface."""
    print("""

Chatbot  Copyright (C) 2020  Peter Jackson Link III
    This program comes with ABSOLUTELY NO WARRANTY.
    This is free software, and you are welcome to redistribute it
    under certain conditions. See COPYING for details.

Type something to the chatbot (no punctuation) \
and it will print something back.

""")


    while True:
        sentence = input("Type something: ")
        print(use_words(sentence))
