# pip install pyttsx3
# To know all the Default voices in your Laptop

import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice', voices[2].id)
    engine.say("Hello World!")
    engine.runAndWait()
    engine.stop()


# 0. David
# 1. Hayley
# 2. James
# 3. Heather
# 4. George
# 5. Hazel
# 6. Susan
# 7. Heera
# 8. Ravi
# 9. Catherine
# 10. Helen
# 11. Mark
# 12. ZiraPro
# 13. Zira
# 14. Helena
# 15. Hilda
# 16. Hemant
# 17. Kalpana
