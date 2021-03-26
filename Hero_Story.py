# Set up dictionary
hero_story = {"beginning": "Once upon a time there was a brave hero called Perseus.",
              "middle": "This hero battled dragons and monsters from the back of the legendary Pegasus.",
              "end": "One day however, Perseus fell in battle and was slain."
              }

print(hero_story)           # Print entire dictionary
print(type(hero_story))     # Print dictionary type (dictionary)
print(hero_story.keys())    # Print keys in the dictionary
print(hero_story.values())  # Print values in the dictionary

for item in hero_story:     # Cycle through each key in the dictionary to print the value
    print(hero_story[item])

hero_story["hero"] = "Perseus"  # Add a new 'hero' key with 'Perseus' value

print(hero_story)       # Print dictionary again to test 'hero' and 'Perseus' have been added