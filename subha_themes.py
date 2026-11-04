#Words and phrases extracted from Tagore's "Subha" for synthetic reading experiment.
#
# Author: Khushi Jha, Monsoon Semester 2026
# Department of Humanities and Social Sciences, IIT (ISM) Dhanbad
#
# How this file was made:
#   1. A local LLM (qwen2.5:7b via Ollama) was given prompt.txt for each
#      10-sentence window of the three stages (see extract_themes.py).
#   2. Every expression it returned was checked against the story; those not
#      found in the text were discarded (results/llm_extraction.json).
#   3. Author annotation: the remaining lists were read against the story and
#        - items with no analytical function were removed
#          (e.g. "noticed", "idle", "door", "houses", "deity");
#        - items placed under the wrong dimension were moved
#          (e.g. "speech of the dark eyes" from structure to voice,
#           "only increased her value" from affect to structure);
#        - character names on their own were removed;
#        - a few expressions the model missed were added; each is marked
#          "# added" so the LLM's contribution and the author's stay separate.
#
# Dimensions: Voice = voice and silence; Nature = nature and non-human
# kinship; Structure = social and patriarchal structure; Affect = affect
# and being.

themes = {

    # --------------------------
    # STAGE I  (Chandipur: childhood)
    # --------------------------

    "Stage_I_Voice": [
        "dumb",
        "silent",
        "speak",
        "speech",
        "language",
        "eyes",
        "lips",
        "long lashes",
        "speech of the dark eyes",
        "dumb girl's language",
        "signs and gestures",
        "murmur",
        "voice",
        "songs",
        "crying",
        "rustle",
        "weeping",
        "sighing",
    ],

    "Stage_I_Nature": [
        "sky",
        "moon",
        "stars",
        "river",
        "stream",
        "brook",
        "water",
        "trees",
        "birds",
        "cows",
        "lonely, awful giant",
        "dumb nature",                          # added
        "lonely grandeur like nature's own",    # added
    ],

    "Stage_I_Structure": [
        "father's house",
        "cost and difficulty",
        "parents' minds",
        "mother looked upon her as a deformity in herself",
        "mother",
        "father",
        "daughters",
        "hamlet",
        "village",
        "villagers",
        "wealth",
        "work",
    ],

    "Stage_I_Affect": [
        "silent weight",                        # added
        "curse",
        "pain",
        "fault",
        "shame",
        "aversion",
        "anxiety",
        "companionless",
        "heart",
        "trembling",
    ],

    # --------------------------
    # STAGE II  (growing up, friendship, marriage talk)
    # --------------------------

    "Stage_II_Voice": [
        "speech",
        "language",
        "taciturnity",
        "silent",
        "could not speak",
        "quiet",
        "look",
        "questioned",
        "answer",
        "arms",
        "neck",
        "cheek",
        "rub",
    ],

    "Stage_II_Nature": [
        "goats",
        "kitten",
        "tamarind",
        "river",
        "full moon",
        "lonely subha",
        "sleeping earth",
        "skirts of this silent troubled mother",
    ],

    "Stage_II_Structure": [
        "thought of her marriage",
        "parents",
        "anxious care",
        "people blamed them",
        "even talked of making them outcasts",
        "banikantha was well off",
        "fish-curry twice daily",
        "enemies",
    ],

    "Stage_II_Affect": [
        "anguish",
        "equality",
        "friendship",
        "attachment",
        "burden",
        "strong young life",
        "joy",
        "sadness",
        "inexpressible consciousness",
        "central places of the sea",
        "illimitable loneliness",
        "passed beyond",
    ],

    # --------------------------
    # STAGE III  (leaving Chandipur, Calcutta, marriage)
    # --------------------------

    "Stage_III_Voice": [
        "dumb",
        "speech",
        "language",
        "eyes",
        "gaze",
        "tears",
        "weeping",
        "not a word did they vouchsafe",
        "clasped their necks",
        "looked into their faces",
        "scolded",
    ],

    "Stage_III_Nature": [
        "tree",
        "cow-shed",
        "her dear river",
        "earth, her strong silent mother",
        "threw her arms about earth",
        "flung herself down on her grassy couch",
        "stricken doe",
        "hunter's face",
        "dumb animal",                          # added
    ],

    "Stage_III_Structure": [
        "women interfered",
        "father and mother",
        "calcutta",
        "bridegroom",
        "bridegroom came with a friend to inspect the bride",
        "dressed her up with great care",
        "imprisoned her hair",
        "hung her about with ornaments",
        "did her best to kill her natural beauty",
        "mother called her instructions aloud",
        "the great man, after scanning her a long time",
        "would presently prove a useful possession",
        "only increased her value",
        "delivered over their dumb girl into another's hands",
        "married",
        "marriage",
        "caste",
    ],

    "Stage_III_Affect": [
        "vague fear",
        "heart was heavy with tears",
        "silent agony",
        "burst out weeping",
        "do not let me leave you, mother",
        "eyes filled with tears",
        "parents were dizzy with anxiety and fear",
        "must have a tender heart",
        "voiceless weeping",                    # added
        "searcher of hearts",                   # added
    ]
}
