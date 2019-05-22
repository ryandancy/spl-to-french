#!usr/bin/env python
# -*- coding: utf-8 -*-
# Generates SPL that translates Langage de Programmation de Shakespeare (LPS) code from SPL.

import random
import math
import textwrap

random.seed(398457039457)  # for consistancy in output...probably

characters_dict = {
    'Achilles': 'Achilles',
    'Adonis': 'Adonis',
    'Adriana': 'Adriana',
    'Aegeon': 'Aegeon',
    'Aemilia': 'Aemilia',
    'Agamemnon': 'Agamemnon',
    'Agrippa': 'Agrippa',
    'Ajax': 'Ajax',
    'Alexander': 'Alexandre',
    'Alonso': 'Alonso',
    'Andromache': 'Andromache',
    'Angelo': 'Angelo',
    'Antiochus': 'Antiochus',
    'Antonio': 'Antonio',
    'Arthur': 'Arthur',
    'Autolycus': 'Autolycus',
    'Balthazar': 'Balthazar',
    'Banquo': 'Banquo',
    'Beatrice': 'Beatrice',
    'Benedick': 'Benedick',
    'Benvolio': 'Benvolio',
    'Bianca': 'Bianca',
    'Brabantio': 'Brabantio',
    'Brutus': 'Brutus',
    'Capulet': 'Capulet',
    'Cassandra': 'Cassandra',
    'Cassius': 'Cassius',
    'Cicero': 'Cicero',
    'Claudio': 'Claudio',
    'Claudius': 'Claudius',
    'Cleopatra': 'Cleopatra',
    'Cordelia': 'Cordelia',
    'Cornelius': 'Cornelius',
    'Cressida': 'Cressida',
    'Cymberline': 'Cymberline',
    'Demetrius': 'Demetrius',
    'Desdemona': 'Desdemona',
    'Dionyza': 'Dionyza',
    'Dogberry': 'Dogberry',
    'Don John': 'Don Jean',
    'Don Pedro': 'Don Pedro',
    'Donalbain': 'Donalbain',
    'Dorcas': 'Dorcas',
    'Duncan': 'Duncan',
    'Egeus': 'Egeus',
    'Emilia': 'Emilia',
    'Escalus': 'Escalus',
    'Falstaff': 'Falstaff',
    'Fenton': 'Fenton',
    'Ferdinand': 'Ferdinand',
    'Ford': 'Ford',
    'Fortinbras': 'Fortinbras',
    'Francisca': 'Francisca',
    'Gertrude': 'Gertrude',
    'Goneril': 'Goneril',
    'Hamlet': 'Hamlet',
    'Hecate': 'Hecate',
    'Hector': 'Hector',
    'Helen': 'Helen',
    'Helena': 'Helène',
    'Hermia': 'Hermia',
    'Hermonie': 'Hermonie',
    'Hippolyta': 'Hippolyta',
    'Horatio': 'Horatio',
    'Imogen': 'Imogen',
    'Isabella': 'Isabella',
    'Julia': 'Julia',
    'Juliet': 'Juliet',
    'Lennox': 'Lennox',
    'Leonato': 'Leonato',
    'Luciana': 'Luciana',
    'Lucio': 'Lucio',
    'Lychorida': 'Lychorida',
    'Lysander': 'Lysander',
    'Macbeth': 'Macbeth',
    'Macduff': 'Macduff',
    'Malcolm': 'Malcolm',
    'Mariana': 'Mariana',
    'Mercutio': 'Mercutio',
    'Miranda': 'Miranda',
    'Montague': 'Montague',
    'Mopsa': 'Mopsa',
    'Oberon': 'Oberon',
    'Octavia': 'Octavia',
    'Olivia': 'Olivia',
    'Ophelia': 'Ophelia',
    'Orlando': 'Orlando',
    'Orsino': 'Orsino',
    'Othello': 'Othello',
    'Page': 'Page',
    'Pandarus': 'Pandarus',
    'Pantino': 'Pantino',
    'Paris': 'Paris',
    'Pericles': 'Pericles',
    'Pinch': 'Pinch',
    'Polonius': 'Polonius',
    'Pompeius': 'Pompeius',
    'Portia': 'Portia',
    'Priam': 'Priam',
    'Prospero': 'Prospero',
    'Proteus': 'Proteus',
    'Publius': 'Publius',
    'Puck': 'Puck',
    'Regan': 'Regan',
    'Robin': 'Robin',
    'Romeo': 'Romeo',
    'Rosalind': 'Rosalind',
    'Sebastian': 'Sebastian',
    'Shallow': 'Shallow',
    'Shylock': 'Shylock',
    'Slender': 'Slender',
    'Solinus': 'Solinus',
    'Stephano': 'Stefan',
    'Thaisa': 'Thaisa',
    'Theseus': 'Theseus',
    'Thurio': 'Thurio',
    'Timon': 'Timon',
    'Titania': 'Titania',
    'Titus': 'Titus',
    'Troilus': 'Troilus',
    'Tybalt': 'Tybalt',
    'Ulysses': 'Ulysses',
    'Valentine': 'Valentine',
    'Venus': 'Venus',
    'Vincentio': 'Vincentio',
    'Viola': 'Viola'
}
characters = list(characters_dict.keys())
characters.sort()
random.shuffle(characters)

adjectives_dict = {
    'amazing': 'extraordinaire',
    'beautiful': 'belle',
    'blossoming': 'fleuri',
    'bold': 'osé',
    'brave': 'courageux',
    'charming': 'charmant',
    'clearest': 'clair',
    'cunning': 'astucieux',
    'cute': 'mignon',
    'delicious': 'délicieux',
    'embroidered': 'brodé',
    'fair': 'claire',
    'fine': 'bonne',
    'gentle': 'gentil',
    'golden': 'doré',
    'good': 'bon',
    'handsome': 'beau',
    'happy': 'heureux',
    'healthy': 'sain',
    'honest': 'honnête',
    'lovely': 'charmant',
    'loving': 'affecteux',
    'mighty': 'puissant',
    'noble': 'noble',
    'peaceful': 'calm',
    'pretty': 'joli',
    'prompt': 'rapide',
    'proud': 'fier',
    'reddest': 'rouge',
    'rich': 'riche',
    'smooth': 'douce',
    'sunny': 'ensoleillé',
    'sweet': 'adorable',
    'sweetest': 'le plus adorable',
    'trustworthy': 'fiable',
    'warm': 'chaud',
    'young': 'jeune',
    'big': 'grand',
    'black': 'noir',
    'blue': 'bleu',
    'bluest': 'le plus bleu',
    'bottomless': 'sans fond',
    'furry': 'à poils',
    'green': 'vert',
    'hard': 'dur',
    'huge': 'énorme',
    'large': 'grande',
    'little': 'petit',
    'normal': 'normal',
    'old': 'vieux',
    'purple': 'violet',
    'red': 'rouge',
    'rural': 'rural',
    'small': 'modeste',
    'tiny': 'minuscule',
    'white': 'blanc',
    'yellow': 'jaune',
    'temporary': 'temporaire',
    'limiting': 'restrictif',
    'bad': 'méchant',
    'cowardly': 'lâche',
    'cursed': 'maudit',
    'damned': 'damné',
    'dirty': 'sale',
    'disgusting': 'dégoûtant',
    'distasteful': 'déplaisant',
    'dusty': 'poussiéreux',
    'evil': 'mauvais',
    'fat': 'gros',
    'fat-kidneyed': 'avec des reins grosses',
    'fatherless': 'sans père',
    'foul': 'ignoble',
    'hairy': 'poilu',
    'half-witted': 'idiot',
    'horrible': 'horrible',
    'horrid': 'épouvantable',
    'infected': 'infecté',
    'lying': 'qui ment',
    'miserable': 'misérable',
    'misused': 'abusé',
    'oozing': 'suintement',
    'rotten': 'pourri',
    'skilless': 'sans dons',
    'smelly': 'qui sent mauvais',
    'snotty': 'morveux',
    'sorry': 'désolé',
    'stinking': 'nauséabond',
    'stuffed': 'empaillé',
    'stupid': 'stupide',
    'tame': 'faiblard',
    'unpracticed': 'inexpérimenté',
    'vile': 'vil',
    'villainous': 'inflâme',
    'weak': 'faible',
    'worried': 'inquiet'
}
adjectives = list(adjectives_dict.keys())

posnouns_dict = {
    'angel': 'ange',
    'day': 'journée',
    'flower': 'fleur',
    'girl': 'fille',
    'happiness': 'bonheur',
    'heaven': 'paradis',
    'hero': 'héros',
    'joy': 'joie',
    'king': 'roi',
    'kingdom': 'royaume',
    'kitten': 'chaton',
    'lady': 'dame',
    'lord': 'maître',
    'lover': 'amant',
    'plum': 'prune',
    'pony': 'poney',
    'prince': 'prince',
    'rose': 'rose',
    'summer': 'été',
    'warrior': 'guerrier',
    'spaceman': 'astronaute',
    'animal': 'animal',
    'aunt': 'tante',
    'brother': 'frère',
    'cat': 'chat',
    'chihuahua': 'chihuahua',
    'cousin': 'cousin',
    'cow': 'vache',
    'daughter': 'fille',
    'door': 'porte',
    'face': 'visage',
    'factor': 'facteur',
    'father': 'père',
    'fellow': 'gars',
    'flatterer': 'flatteur',
    'granddaughter': 'petite-fille',
    'grandfather': 'grand-père',
    'grandmother': 'grand-mère',
    'grandson': 'petit-fils',
    'hair': 'cheveux',
    'hamster': 'hamster',
    'horse': 'cheval',
    'infancy': 'petite enfance',
    'infant': 'enfant',
    'lamp': 'lampe',
    'lantern': 'lanterne',
    'man': 'homme',
    'mistletoe': 'gui',
    'moon': 'lune',
    'morning': 'matin',
    'mother': 'mère',
    'nephew': 'neveu',
    'niece': 'nièce',
    'nose': 'nez',
    'purse': 'sac à main',
    'road': 'rue',
    'roman': 'romain',
    'servant': 'domestique',
    'sister': 'soeur',
    'sky': 'ciel',
    'son': 'fils',
    'squirrel': 'écureuil',
    'stone wall': 'mur de pierre',
    'thing': 'chose',
    'town': 'ville',
    'tree': 'arbre',
    'uncle': 'oncle',
    'value': 'valeur',
    'variable': 'variable',
    'varlet': 'valet',
    'virgin': 'vierge',
    'wind': 'vent',
    'woman': 'femme'
}
posnouns = list(posnouns_dict.keys())

negnouns_dict = {
    'apple': 'pomme',
    'hell': 'enfer',
    'bastard': 'connard',
    'beggar': 'mendiant',
    'blister': 'ampoule',
    'codpiece': 'braguette',
    'coward': 'lâche',
    'curse': 'malédiction',
    'death': 'mort',
    'devil': 'diable',
    'draught': 'dames',
    'famine': 'famine',
    'flirt-gill': 'femme dévergonté',
    'goat': 'chèvre',
    'hate': 'haine',
    'hog': 'goinfre',
    'hound': 'chien',
    'ignorance': 'ignorance',
    'leech': 'sangsue',
    'lie': 'mensonge',
    'pig': 'cochon',
    'plague': 'peste',
    'starvation': 'famine',
    'tear': 'larme',
    'toad': 'crapaud',
    'war': 'guerre',
    'wolf': 'loup'
}
negnouns = list(negnouns_dict.keys())

translation = dict({
    'a': 'un',
    'an': 'une',
    'the': 'la',
    'am': 'suis',
    'are': 'êtes',
    'art': 'es',
    'be': 'être',
    'is': 'est',
    'me': 'moi',
    'mine': 'mes',
    'my': 'mon',
    'myself': 'moi-même',
    'punier': 'plus chétif',
    'smaller': 'plus petit',
    'worse': 'pire',
    'nothing': 'rien',
    'zero': 'zéro',
    'better': 'meilleur',
    'bigger': 'plus grand',
    'fresher': 'plus impertinent',
    'friendlier': 'plus aimable',
    'jollier': 'plus enjoué',
    'nicer': 'plus gentil',
    'thee': 'te',
    'thou': 'tu',
    'you': 'vous',
    'thine': 'ta',
    'thy': 'ton',
    'your': 'votre',
    'thyself': 'toi-même',
    'yourself': 'vous-même',
    'his': 'son',
    'her': 'sa',
    'its': 'son',
    'their': 'leur',
    'scene': 'scène',
    'act': 'numèro',
    'of': 'de',
    'sum': 'somme',
    'difference': 'différence',
    'product': 'produit',
    'quotient': 'quotient',
    'between': 'entre',
    'square': 'élever au carré',
    'cube': 'élever au cube',
    'twice': 'deux fois',
    'root': 'racine',
    'and': 'et',
    'heart': 'coeur',  # C doesn't support œ
    'listen': 'écouter',
    'mind': 'espirit',
    'speak': 'parler',
    'open': 'ouvre',
    'as': 'que',
    'more': 'plus',
    'equal': 'égal',
    'greater': 'meilleur',
    'remember': 'se souvenir de',
    'recall': 'se rappeler',
    'if': 'si',
    'so': "c'est",
    'not': 'pas',
    'let': 'laissez',
    'us': 'nous',
    'we': 'on',
    'shall': 'doit',
    'enter': 'entrer',
    'exit': 'sortie',
    'exeunt': 'ils sortent',
    'return': 'revenir',
    'proceed': 'procéder',
    'to': 'à',
    'tale': 'histoire',
    # These are required because for some reason, MMDCVI -> MCI was happening
    'M': 'M',
    'D': 'D',
    'C': 'C',
    'L': 'L',
    'X': 'X',
    'V': 'V',
    'I': 'I'
}, **characters_dict, **adjectives_dict, **posnouns_dict, **negnouns_dict)

translation = {k: v for key, val in translation.items()
                    for k, v in ((key, val), (key.capitalize(), val.capitalize()))}

class Tree:
    
    def __init__(self, parent, value=None):
        self.children = []
        self.parent = parent
        if self.parent is not None:
            self.parent.children.append(self)
        self.value = value
    
    def concat_all_values(self):
        res = self.value
        node = self.parent
        while node is not None and node.value is not None:
            res += node.value
            node = node.parent
        return res[::-1]
    
    def __eq__(self, other):
        return (isinstance(other, Tree) and self.value == other.value) or self.value == other
    
    def __hash__(self):
        return hash(self.value)

translation_tree = Tree(None)
for original in translation.keys():
    node = translation_tree
    for ch in original:
        if ch in node.children:
            node = node.children[node.children.index(ch)]
        else:
            node = Tree(node, ch)

roman_numerals = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
roman_values = list(roman_numerals.keys())
roman_values.sort()
roman_values = roman_values[::-1]
def roman_numeral(n):
    if n in roman_values:
        return roman_numerals[n]
    else:
        for value in roman_values:
            if value < n:
                return roman_numerals[value] + roman_numeral(n - value)

class Lines:
    
    def __init__(self, orderer):
        self.scenes = []
        self.orderer = orderer
        self.characters = [orderer]
        self._character_on_stage = None
    
    def add_scene(self):
        self.scenes.append([])
        return len(self.scenes)
    
    def add_line(self, scene, target, value):
        scene -= 1
        if self._character_on_stage != target:
            if self._character_on_stage is not None:
                self.scenes[scene].append('\n[Exit ' + self._character_on_stage + ']')
            self.scenes[scene].append('[Enter ' + target + ']\n')
            self._character_on_stage = target
        self.scenes[scene].append(self.orderer + ':')
        self.scenes[scene].append('  ' + value)
    
    def add_character(self, character_name):
        self.characters.append(character_name)
    
    def _optimize(self):
        for scene, lines in enumerate(self.scenes):
            redundant_lines = []
            has_speaker = False
            for lineno, line in enumerate(lines):
                if line == self.orderer + ':':
                    if not has_speaker:
                        has_speaker = True
                    else:
                        redundant_lines.append(lineno)
                elif line.strip().startswith('[') or line.startswith('\nScene') or line.startswith('\nAct'):
                    has_speaker = False
            
            for lineno in reversed(redundant_lines):
                del self.scenes[scene][lineno]
    
    def get(self):
        self._optimize()
        
        res = ['A tale of a ' + spl_set(2**random.randint(0, 5), setter=False) + '.\n']
        for character in self.characters:
            res.append(character + ', a ' + spl_set(2**random.randint(0, 5), setter=False) + '.')
        res.append('\nAct I: A ' + spl_set(2**random.randint(0, 5), setter=False) + '.')
        for scene, lines in enumerate(self.scenes):
            res.append('\nScene ' + roman_numeral(scene + 1) + ': A ' + spl_set(2**random.randint(0, 5), setter=False) + '.\n')
            if scene == 0:
                res.append('[Enter ' + self.orderer + ']')
            res.extend(lines)
        res.append('[Exeunt]')
        res.append('')  # Newlines at the ends of files are good, right?
        
        for lineno, line in enumerate(res):
            if len(line) > 80:  # We'll just wrap to 80 columns, that sounds good.
                wrapped = [('' if i == 0 else '  ') + line for i, line in enumerate(textwrap.wrap(line, 78, break_on_hyphens=False))]
                res[lineno] = '\n'.join(wrapped)
        
        return res

lines = Lines(characters[0])
del characters[0]

def ispow2(n):
    return n != 0 and (abs(n) & (abs(n) - 1)) == 0

pows2 = [x for exp in range(31, -1, -1) for x in (2**exp, -2**exp)]
def spl_set(n, setter=True, recursive=False):
    # Sum powers of 2 & -2
    res = []
    if ispow2(n):
        for _ in range(int(math.log2(abs(n)))):
            res.append(random.choice(adjectives))
        res.append(random.choice((negnouns, posnouns)[int((math.copysign(1, n) + 1) // 2)]))
    else:
        # Max size of C int is 2**31-1...I think
        closest_pow2 = min(pows2, key=lambda x: abs(x - n))
        res.append('the sum of')
        res.extend(spl_set(closest_pow2, setter=False, recursive=True))
        res.append('and')
        res.extend(spl_set(n - closest_pow2, setter=False, recursive=True))
    
    if recursive:
        return res
    elif setter:
        return random.choice(['You {}!', 'Thou art {}.', 'You are {}.', 'Thou art {}!', 'You are {}!']).format(' '.join(res))
    else:
        return ' '.join(res)

# The first character is the orderer
# Initialize all the char characters.
scene1 = lines.add_scene()
chars_to_characters = {}
non_word_chars = ' \r\n\t;,:.[]?!()'
# This string includes every Latin alphabet character, all the diacratics used in French (and then some), plus auxilary punctuation
# NOTE: Œ/œ are not included because their code points are > 255, which C does not support
for ch in "AaÀàÂâÆæBbCcÇçDdEeÈèÉéÊêËëFfGgHhIiÎîÏïJjKkLlMmNnOoÔôPpQqRrSsTtUuÙùÛûVvWwXxYyZz'-:" + non_word_chars:
    chars_to_characters[ord(ch)] = characters[0]
    lines.add_character(characters[0])
    lines.add_line(scene1, characters[0], spl_set(ord(ch)))
    del characters[0]

currentchar = characters[0]
lines.add_character(currentchar)
del characters[0]

outputter = characters[0]
lines.add_character(outputter)
del characters[0]

# Here's the algorithm:
# For each possible first letter, we jump to a scene handling it if it is the first letter.
# If we don't recognize the next letter as part of a word, we output
# the translation if there is one, and we jump back to the beginning.
speak_scene = lines.add_scene()
lines.add_line(speak_scene, currentchar, 'Speak {} mind{}'.format(random.choice(['your', 'thy']), random.choice(['.', '!'])))
root_scene = lines.add_scene()
lines.add_line(scene1, currentchar, '{} proceed to scene {}.'.format(random.choice(['Let us', 'We shall']), roman_numeral(root_scene)))

def gen(node, scene_num):
    global root_scene, speak_scene, lines, translation, translation_tree
    
    lines.add_line(scene_num, currentchar, 'Open your mind{}'.format(random.choice(['.', '!'])))
    
    # If the char is a non-word char, jump back to the beginning
    if node == translation_tree:
        for nwc in non_word_chars:
            lines.add_line(scene_num, currentchar, random.choice(['Art thou as {} as a {}?', 'Are you as {} as a {}?'])
                                                   .format(random.choice(adjectives), chars_to_characters[ord(nwc)]))
            lines.add_line(scene_num, currentchar, 'If so, {} return to scene {}.'.format(random.choice(['let us', 'we shall']),
                                                                                          roman_numeral(speak_scene)))
    
    for child in node.children:
        lines.add_line(scene_num, currentchar, random.choice(['Art thou as {} as a {}?', 'Are you as {} as a {}?'])
                                               .format(random.choice(adjectives), chars_to_characters[ord(child.value)]))
        new_scene = lines.add_scene()
        lines.add_line(scene_num, currentchar, 'If so, {} proceed to scene {}.'.format(random.choice(['let us', 'we shall']),
                                                                                       roman_numeral(new_scene)))
        gen(child, new_scene)
    
    # If control flows to this part, the next character is not part of the word
    if node == translation_tree:
        # -1 is EOF
        lines.add_line(scene_num, currentchar, random.choice(['Art thou as {} as a {}?', 'Are you as {} as a {}?'])
                                               .format(random.choice(adjectives), random.choice(negnouns)))
        new_scene = lines.add_scene()
        lines.add_line(scene_num, currentchar, 'If so, {} return to scene {}.'.format(random.choice(['let us', 'we shall']),
                                                                                      roman_numeral(new_scene)))
        lines.add_line(scene_num, currentchar, '{} proceed to scene {}.'.format(random.choice(['Let us', 'We shall']), roman_numeral(scene_num)))
    else:
        word = node.concat_all_values()
        if word in translation:
            for ch in translation[word]:
                lines.add_line(scene_num, outputter, random.choice([
                    'Thou art as {} as a {}.', 'You are as {} as a {}.', 'Thou art as {} as a {}!', 'You are as {} as a {}!'
                ]).format(random.choice(adjectives), chars_to_characters[ord(ch)]))
                lines.add_line(scene_num, outputter, 'Speak {} mind{}'.format(
                    random.choice(['your', 'thy']), random.choice(['.', '!'])
                ))
    
        lines.add_line(scene_num, currentchar, '{} return to scene {}.'.format(random.choice(['Let us', 'We shall']), roman_numeral(speak_scene)))

gen(translation_tree, root_scene)

with open('translate.spl', 'w', encoding='utf-8') as out:
    out.write('\n'.join(lines.get()))
