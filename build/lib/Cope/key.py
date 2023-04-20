from .imports import checkImport
from .decorators import todo
from .func import Signal

class KeyStandard:
    ascii = {
        "unknown":0,
        "space":32,
        "exclamation":33,
        "doubleQuote":34,
        "pound":35,
        "dollarSign":36,
        "percent":37,
        "andersand":38,
        "singleQuote":39,
        "openParen":40,
        "closeParen":41,
        "star":42,
        "plus":43,
        "comma":44,
        "minus":45,
        "period":46,
        "slash":47,
        "one":48,
        "two":49,
        "three":50,
        "four":51,
        "five":52,
        "six":53,
        "seven":54,
        "eight":55,
        "nine":56,
        "zero":57,
        "colon":58,
        "semicolon":59,
        "lessThan":60,
        "equals":61,
        "greaterThan":62,
        "question":63,
        "attersand":64,
        "A":65,
        "B":66,
        "C":67,
        "D":68,
        "E":69,
        "F":70,
        "G":71,
        "H":72,
        "I":73,
        "J":74,
        "K":75,
        "L":76,
        "M":77,
        "N":78,
        "O":79,
        "P":80,
        "Q":81,
        "R":82,
        "S":83,
        "T":84,
        "U":85,
        "V":86,
        "W":87,
        "X":88,
        "Y":89,
        "Z":90,
        "openSquareBracket":91,
        "backslash":92,
        "closeSquareBracket":93,
        "exponent":94,
        "underscore":95,
        "sidilla":96,
        "a":97,
        "b":98,
        "c":99,
        "d":100,
        "e":101,
        "f":102,
        "g":103,
        "h":104,
        "i":105,
        "j":106,
        "k":107,
        "l":108,
        "m":109,
        "n":110,
        "o":111,
        "p":112,
        "q":113,
        "r":114,
        "s":115,
        "t":116,
        "u":117,
        "v":118,
        "w":119,
        "x":120,
        "y":121,
        "z":122,
        "openCurlyBrace":123,
        "orLine":124,
        "closeCurlyBrace":125,
        "tilde":126,
        "F1":131,
        "F2":132,
        "F3":133,
        "F4":134,
        "F5":135,
        "F6":136,
        "F7":137,
        "F8":138,
        "F9":139,
        "F10":140,
        "F11":141,
        "F12":142,
        "F13":143,
        "F14":144,
        "F15":145,
        "F16":146,
        "F17":147,
        "F18":148,
        "F19":149,
        "F20":150,
        "F21":151,
        "F22":152,
        "F23":153,
        "F24":154,
        "F25":155,
        "F26":156,
        "F27":157,
        "F28":158,
        "F29":159,
        "F30":160,
        "escape":27,
        "delete":127,
        "ctrl":200,
        "rightCtrl": 206,
        "leftCtrl": 207,
        # I don't *think* there are left and right win keys
        "win":201,
        "shift":202,
        "rightShift": 208,
        "leftShift": 209,
        "alt":203,
        "rightAlt": 204,
        "leftAlt": 205,
        "backspace":300,
        "home":301,
        "end":302,
        "enter":303,
        "insert":304,
        "pageUp":305,
        "pageDown":306,
        "up":307,
        "down":308,
        "left":309,
        "right":310,
        "printScreen":311,
        "scrollLock":312,
        "pause":313,
        "stop":314,
        "next":315,
        "previous":316,
        "break_":317,
        "numLock":318,
        "cent":319,
        "volumeDown":320,
        "volumeUp":321,
        "mute":322,
        "menu":323,
        "refresh": 324,
        "back":325,
        "touchpadLock":326,
        "muteMic":327,
        "brightnessUp":328,
        "brightnessDown":329,
        "keypad0": 330,
        "keypad1": 331,
        "keypad2": 332,
        "keypad3": 333,
        "keypad4": 334,
        "keypad5": 335,
        "keypad6": 336,
        "keypad7": 337,
        "keypad8": 338,
        "keypad9": 339,
        "accept": 340,
        "add": 341,
        "apps": 342,
        "browserForward":342,
        "browserFavorites": 343,
        "browserHome": 344,
        "search": 345,
        "browserStop": 346,
        "clear": 347,
        "convert": 348,
        "execute": 349,
        "final": 350,
        "fn": 351,
        "hanguel": 352,
        "hangul": 353,
        "hanja": 354,
        "help": 355,
        # "home": 356,
        "junja": 357,
        "kana": 358,
        "kanji": 359,
        "launchApp1": 360,
        "launchApp2": 361,
        "launchMail": 362,
        "launchMediaSelect": 363,
        "changeMode": 364,
        "nonconvert": 365,
        "select": 366,
        "separator": 367,
        "sleep": 368,
        "leftWin": 369,
        "rightWin": 370,
        "yen": 371,
        "option": 372,
        "leftOption": 373,
        "rightOption": 374,
        "print": 376,
        "tab": 377,
        "capsLock": 378,
    }

    string = {
        "unknown": ascii["unknown"],
        "space": ascii["space"],
        'spacebar': ascii['space'],
        "exclamation": ascii["exclamation"],
        "exclamationMark": ascii["exclamation"],
        "exclamationPoint": ascii["exclamation"],
        "doubleQuote": ascii["doubleQuote"],
        "pound": ascii["pound"],
        "hashtag": ascii["pound"],
        "numSign": ascii["pound"],
        "numberSign": ascii["pound"],
        "dollarSign": ascii["dollarSign"],
        "dollar": ascii["dollarSign"],
        "percent": ascii["percent"],
        "andersand": ascii["andersand"],
        # "and": ascii["andersand"],
        "and_": ascii["andersand"],
        "singleQuote": ascii["singleQuote"],
        "openParen": ascii["openParen"],
        "openParenthesis": ascii["openParen"],
        "closeParen": ascii["closeParen"],
        "closeParenthesis": ascii["closeParen"],
        "star": ascii["star"],
        "times": ascii["star"],
        "plus": ascii["plus"],
        "comma": ascii["comma"],
        "minus": ascii["minus"],
        "period": ascii["period"],
        "dot": ascii["period"],
        "slash": ascii["slash"],
        "forwardSlash": ascii["slash"],
        "one": ascii["one"],
        "two": ascii["two"],
        "three": ascii["three"],
        "four": ascii["four"],
        "five": ascii["five"],
        "six": ascii["six"],
        "seven": ascii["seven"],
        "eight": ascii["eight"],
        "nine": ascii["nine"],
        "zero": ascii["zero"],
        "colon": ascii["colon"],
        "semicolon": ascii["semicolon"],
        "lessThan": ascii["lessThan"],
        "less": ascii["lessThan"],
        "equals": ascii["equals"],
        "greaterThan": ascii["greaterThan"],
        "greater": ascii["greaterThan"],
        "question": ascii["question"],
        "questionMark": ascii["question"],
        "attersand": ascii["attersand"],
        "at": ascii["attersand"],
        "A": ascii["A"],
        "B": ascii["B"],
        "C": ascii["C"],
        "D": ascii["D"],
        "E": ascii["E"],
        "F": ascii["F"],
        "G": ascii["G"],
        "H": ascii["H"],
        "I": ascii["I"],
        "J": ascii["J"],
        "K": ascii["K"],
        "L": ascii["L"],
        "M": ascii["M"],
        "N": ascii["N"],
        "O": ascii["O"],
        "P": ascii["P"],
        "Q": ascii["Q"],
        "R": ascii["R"],
        "S": ascii["S"],
        "T": ascii["T"],
        "U": ascii["U"],
        "V": ascii["V"],
        "W": ascii["W"],
        "X": ascii["X"],
        "Y": ascii["Y"],
        "Z": ascii["Z"],
        "openSquareBrace": ascii["openSquareBracket"],
        "openingSquareBrace": ascii['openSquareBracket'],
        "openSquareBracket": ascii['openSquareBracket'],
        "backslash": ascii["backslash"],
        "closeSquareBrace": ascii["closeSquareBracket"],
        "closingSquareBrace": ascii["closeSquareBracket"],
        "closeSquareBracket": ascii["closeSquareBracket"],
        "exponent": ascii["exponent"],
        "underscore": ascii["underscore"],
        "sidilla": ascii["sidilla"],
        "accent": ascii["sidilla"],
        "a": ascii["a"],
        "b": ascii["b"],
        "c": ascii["c"],
        "d": ascii["d"],
        "e": ascii["e"],
        "f": ascii["f"],
        "g": ascii["g"],
        "h": ascii["h"],
        "i": ascii["i"],
        "j": ascii["j"],
        "k": ascii["k"],
        "l": ascii["l"],
        "m": ascii["m"],
        "n": ascii["n"],
        "o": ascii["o"],
        "p": ascii["p"],
        "q": ascii["q"],
        "r": ascii["r"],
        "s": ascii["s"],
        "t": ascii["t"],
        "u": ascii["u"],
        "v": ascii["v"],
        "w": ascii["w"],
        "x": ascii["x"],
        "y": ascii["y"],
        "z": ascii["z"],
        "openCurlyBrace": ascii["openCurlyBrace"],
        "openingCurlyBrace": ascii["openCurlyBrace"],
        "openCurlyBracket": ascii["openCurlyBrace"],
        "openingCurlyBracket": ascii["openCurlyBrace"],
        "orLine": ascii["orLine"],
        "line": ascii["orLine"],
        "verticalSlash": ascii["orLine"],
        "closeCurlyBrace": ascii["closeCurlyBrace"],
        "closingCurlyBrace": ascii["closeCurlyBrace"],
        "closeCurlyBracket": ascii["closeCurlyBrace"],
        "closingCurlyBracket": ascii["closeCurlyBrace"],
        "tilde": ascii["tilde"],
        "F1": ascii["F1"],
        "F2": ascii["F2"],
        "F3": ascii["F3"],
        "F4": ascii["F4"],
        "F5": ascii["F5"],
        "F6": ascii["F6"],
        "F7": ascii["F7"],
        "F8": ascii["F8"],
        "F9": ascii["F9"],
        "F10": ascii["F10"],
        "F11": ascii["F11"],
        "F12": ascii["F12"],
        "F13": ascii["F13"],
        "F14": ascii["F14"],
        "F15": ascii["F15"],
        "F16": ascii["F16"],
        "F17": ascii["F17"],
        "F18": ascii["F18"],
        "F19": ascii["F19"],
        "F20": ascii["F20"],
        "F21": ascii["F21"],
        "F22": ascii["F22"],
        "F23": ascii["F23"],
        "F24": ascii["F24"],
        "F25": ascii["F25"],
        "F26": ascii["F26"],
        "F27": ascii["F27"],
        "F28": ascii["F28"],
        "F29": ascii["F29"],
        "F30": ascii["F30"],
        "f1": ascii["F1"],
        "f2": ascii["F2"],
        "f3": ascii["F3"],
        "f4": ascii["F4"],
        "f5": ascii["F5"],
        "f6": ascii["F6"],
        "f7": ascii["F7"],
        "f8": ascii["F8"],
        "f9": ascii["F9"],
        "f10": ascii["F10"],
        "f11": ascii["F11"],
        "f12": ascii["F12"],
        "f13": ascii["F13"],
        "f14": ascii["F14"],
        "f15": ascii["F15"],
        "f16": ascii["F16"],
        "f17": ascii["F17"],
        "f18": ascii["F18"],
        "f19": ascii["F19"],
        "f20": ascii["F20"],
        "f21": ascii["F21"],
        "f22": ascii["F22"],
        "f23": ascii["F23"],
        "f24": ascii["F24"],
        "f25": ascii["F25"],
        "f26": ascii["F26"],
        "f27": ascii["F27"],
        "f28": ascii["F28"],
        "f29": ascii["F29"],
        "f30": ascii["F30"],
        # "escape": ascii["escape"],
        # "delete": ascii["delete"],
        # "ctrl": ascii["ctrl"],
        "control": ascii["ctrl"],
        "win": ascii["win"],
        "command": ascii['win'],
        "cmd": ascii['win'],
        "windows": ascii['win'],
        "windowsKey": ascii['win'],
        "shift": ascii["shift"],
        # "alt": ascii["alt"],
        "rightCtrl": ascii["rightCtrl"],
        "ctrlRight": ascii["rightCtrl"],
        "leftCtrl": ascii["leftCtrl"],
        "ctrlLeft": ascii["leftCtrl"],
        "rightShift": ascii["rightShift"],
        "shiftRight": ascii["rightShift"],
        "leftShift": ascii["leftShift"],
        "shiftLeft": ascii["leftShift"],
        "rightAlt": ascii["rightAlt"],
        "altRight": ascii["rightAlt"],
        "leftAlt": ascii["leftAlt"],
        "altLeft": ascii["leftAlt"],
        "alternate": ascii["alt"],
        # "backspace": ascii["backspace"],
        # "home": ascii["home"],
        # "end": ascii["end"],
        # "enter": ascii["enter"],
        # "return": ascii["enter"],
        # "insert": ascii["insert"],
        "pageUp": ascii["pageUp"],
        "pageDown": ascii["pageDown"],
        "up": ascii["up"],
        # "down": ascii["down"],
        # "left": ascii["left"],
        "right": ascii["right"],
        "printScreen": ascii["printScreen"],
        # "prtscr": ascii['printScreen'],
        "prtScr": ascii['printScreen'],
        "PrtScr": ascii['printScreen'],
        "scrollLock": ascii["scrollLock"],
        # "pause": ascii["pause"],
        "play": ascii["pause"],
        # "stop": ascii["stop"],
        "forward": ascii["next"],
        "next": ascii["next"],
        "skip": ascii['next'],
        "skipAhead": ascii['next'],
        "skipForward": ascii['next'],
        "backward": ascii["previous"],
        "prev": ascii["previous"],
        "previous": ascii["previous"],
        "skipBack": ascii['previous'],
        "skipBackward": ascii['previous'],
        "break_": ascii["break_"],
        "numLock": ascii["numLock"],
        "cent": ascii["cent"],
        "\'": ascii["singleQuote"],
        "\"": ascii["doubleQuote"],
        "\\": ascii["backslash"],
        "`": ascii["sidilla"],
        "~": ascii["tilde"],
        "!": ascii["exclamation"],
        "@": ascii["attersand"],
        "#": ascii["pound"],
        "$": ascii["dollarSign"],
        "%": ascii["percent"],
        "^": ascii["exponent"],
        "&": ascii["andersand"],
        "*": ascii["star"],
        "(": ascii["openParen"],
        ")": ascii["closeParen"],
        "_": ascii["underscore"],
        "+": ascii["plus"],
        "{": ascii["openCurlyBrace"],
        "}": ascii["closeCurlyBrace"],
        "|": ascii["orLine"],
        ":": ascii["colon"],
        "<": ascii["lessThan"],
        ">": ascii["greaterThan"],
        "?": ascii["question"],
        "1": ascii["one"],
        "2": ascii["two"],
        "3": ascii["three"],
        "4": ascii["four"],
        "5": ascii["five"],
        "6": ascii["six"],
        "7": ascii["seven"],
        "8": ascii["eight"],
        "9": ascii["nine"],
        "0": ascii["zero"],
        "-": ascii["minus"],
        "=": ascii["equals"],
        "[": ascii["openSquareBracket"],
        "]": ascii["closeSquareBracket"],
        ",": ascii["comma"],
        ".": ascii["period"],
        "/": ascii["slash"],
        ';': ascii["semicolon"],
        "return": ascii["enter"],
        "and": ascii["andersand"],
        "volumeDown":ascii["volumeDown"],
        "volumeUp":ascii["volumeUp"],
        "mute":ascii["mute"],
        "menu":ascii["menu"],
        "refresh": ascii["refresh"],
        "back":ascii["back"],
        "touchpadLock":ascii["touchpadLock"],
        "lockTouchpad":ascii["touchpadLock"],
        "muteMic":ascii["muteMic"],
        "micMute":ascii["muteMic"],
        "brightnessUp":ascii["brightnessUp"],
        "brightnessDown":ascii["brightnessDown"],
        "keypad0": ascii["keypad0"],
        "kp0": ascii["keypad0"],
        "keypad1": ascii["keypad1"],
        "kp1": ascii["keypad1"],
        "keypad2": ascii["keypad2"],
        "kp2": ascii["keypad2"],
        "keypad3": ascii["keypad3"],
        "kp3": ascii["keypad3"],
        "keypad4": ascii["keypad4"],
        "kp4": ascii["keypad4"],
        "keypad5": ascii["keypad5"],
        "kp5": ascii["keypad5"],
        "keypad6": ascii["keypad6"],
        "kp6": ascii["keypad6"],
        "keypad7": ascii["keypad7"],
        "kp7": ascii["keypad7"],
        "keypad8": ascii["keypad8"],
        "kp8": ascii["keypad8"],
        "keypad9": ascii["keypad9"],
        "kp9": ascii["keypad9"],
        # Compatability with pyautogui
        '\t': ascii['tab'],
        '\\t': ascii['tab'],
        '   ': ascii['tab'],
        '\\n': ascii['enter'],
        '\n': ascii['enter'],
        '\\r': ascii['enter'],
        '\r': ascii['enter'],
        " ": ascii["space"],
        "accept": ascii["accept"],
        "add": ascii["add"],
        "alt": ascii["alt"],
        "altleft": ascii["leftAlt"],
        "altright": ascii["rightAlt"],
        "apps": ascii["apps"],
        "backspace": ascii["backspace"],
        "browserback": ascii["back"],
        "browserfavorites": ascii["browserFavorites"],
        "browserforward": ascii["browserForward"],
        "browserhome": ascii["browserHome"],
        "browserrefresh": ascii["refresh"],
        "browsersearch": ascii["search"],
        "browserstop": ascii["browserStop"],
        "capslock": ascii["capsLock"],
        "capsLock": ascii["capsLock"],
        "clear": ascii["clear"],
        "convert": ascii["convert"],
        "ctrl": ascii["ctrl"],
        "ctrlleft": ascii["leftCtrl"],
        "ctrlright": ascii["rightCtrl"],
        "decimal": ascii["period"],
        "del": ascii["delete"],
        "delete": ascii["delete"],
        "divide": ascii["slash"],
        # "down": ascii["down"],
        "end": ascii["end"],
        "enter": ascii["enter"],
        "esc": ascii["escape"],
        "escape": ascii["escape"],
        "execute": ascii["execute"],
        "option": ascii["option"],
        "final": ascii["final"],
        "fn": ascii["fn"],
        "hanguel": ascii["hanguel"],
        "hangul": ascii["hangul"],
        "hanja": ascii["hanja"],
        "help": ascii["help"],
        "home": ascii["home"],
        # "insert": ascii["insert"],
        "junja": ascii["junja"],
        "kana": ascii["kana"],
        "kanji": ascii["kanji"],
        "launchapp1": ascii["launchApp1"],
        "launchapp2": ascii["launchApp2"],
        "launchmail": ascii["launchMail"],
        "launchmediaselect": ascii["launchMediaSelect"],
        # "left": ascii["left"],
        "modechange": ascii["changeMode"],
        "multiply": ascii["star"],
        "nexttrack": ascii["next"],
        "nonconvert": ascii["nonconvert"],
        "num0": ascii["keypad0"],
        "num1": ascii["keypad1"],
        "num2": ascii["keypad2"],
        "num3": ascii["keypad3"],
        "num4": ascii["keypad4"],
        "num5": ascii["keypad5"],
        "num6": ascii["keypad6"],
        "num7": ascii["keypad7"],
        "num8": ascii["keypad8"],
        "num9": ascii["keypad9"],
        "numlock": ascii["numLock"],
        "pagedown": ascii["pageDown"],
        "pageup": ascii["pageUp"],
        # "pause": ascii["pause"],
        "pgdn": ascii["pageDown"],
        "pgup": ascii["pageUp"],
        "playpause": ascii["pause"],
        "prevtrack": ascii["back"],
        "print": ascii["print"],
        "printscreen": ascii["printScreen"],
        "prntscrn": ascii["printScreen"],
        "prtsc": ascii["printScreen"],
        # "prtscr": ascii["printScreen"],
        # "return": ascii["enter"],
        # "right": ascii["right"],
        "scrolllock": ascii["scrollLock"],
        "select": ascii["select"],
        "separator": ascii["orLine"],
        # "shift": ascii["shift"],
        "shiftleft": ascii["leftShift"],
        "shiftright": ascii["rightShift"],
        "sleep": ascii["sleep"],
        # "space": ascii["space"],
        "stop": ascii["stop"],
        "subtract": ascii["minus"],
        "tab": ascii["tab"],
        # "up": ascii["up"],
        "volumedown": ascii["volumeDown"],
        "volumemute": ascii["mute"],
        "volumeup": ascii["volumeUp"],
        # "win": ascii["win"],
        "winleft": ascii["leftWin"],
        "winright": ascii["rightWin"],
        "yen": ascii["yen"],
        # "command": ascii["win"],
        # "option": ascii["option"],
        "optionleft": ascii["leftOption"],
        "optionright": ascii["rightOption"],
    }

    # Qt = ({ } if not checkImport('pyside6', 'keyboard', fatal=False, printWarning=False) else {
    # })

    pynput = ({} if not checkImport('pynput', 'keyboard', fatal=False, printWarning=False) else {
        keyboard.Key.alt:               string['alt'],
        keyboard.Key.alt_gr:            string['alt'],
        keyboard.Key.alt_l:             string['leftAlt'],
        keyboard.Key.alt_r:             string['rightAlt'],
        keyboard.Key.backspace:         string['backspace'],
        keyboard.Key.caps_lock:         string['capsLock'],
        keyboard.Key.cmd:               string['cmd'],
        # keyboard.Key.cmd_l:             string['cmd_l'],
        # keyboard.Key.cmd_r:             string['cmd_r'],
        keyboard.Key.ctrl:              string['ctrl'],
        keyboard.Key.ctrl_l:            string['leftCtrl'],
        keyboard.Key.ctrl_r:            string['rightCtrl'],
        keyboard.Key.delete:            string['delete'],
        keyboard.Key.down:              string['down'],
        keyboard.Key.end:               string['end'],
        keyboard.Key.enter:             string['enter'],
        keyboard.Key.esc:               string['esc'],
        keyboard.Key.f1:                string['f1'],
        keyboard.Key.f2:                string['f2'],
        keyboard.Key.f3:                string['f3'],
        keyboard.Key.f4:                string['f4'],
        keyboard.Key.f5:                string['f5'],
        keyboard.Key.f6:                string['f6'],
        keyboard.Key.f7:                string['f7'],
        keyboard.Key.f8:                string['f8'],
        keyboard.Key.f9:                string['f9'],
        keyboard.Key.f10:               string['f10'],
        keyboard.Key.f11:               string['f11'],
        keyboard.Key.f12:               string['f12'],
        keyboard.Key.f13:               string['f13'],
        keyboard.Key.f14:               string['f14'],
        keyboard.Key.f15:               string['f15'],
        keyboard.Key.f16:               string['f16'],
        keyboard.Key.f17:               string['f17'],
        keyboard.Key.f18:               string['f18'],
        keyboard.Key.f19:               string['f19'],
        keyboard.Key.f20:               string['f20'],
        # keyboard.Key.f21:               string['f21'],
        # keyboard.Key.f22:               string['f22'],
        # keyboard.Key.f23:               string['f23'],
        # keyboard.Key.f24:               string['f24'],
        # keyboard.Key.f25:               string['f25'],
        # keyboard.Key.f26:               string['f26'],
        # keyboard.Key.f27:               string['f27'],
        # keyboard.Key.f28:               string['f28'],
        # keyboard.Key.f29:               string['f29'],
        # keyboard.Key.f30:               string['f30'],
        keyboard.Key.home:              string['home'],
        keyboard.Key.insert:            string['insert'],
        keyboard.Key.left:              string['left'],
        keyboard.Key.media_next:        string['next'],
        keyboard.Key.media_play_pause:  string['play'],
        keyboard.Key.media_previous:    string['previous'],
        keyboard.Key.media_volume_down: string['volumeDown'],
        keyboard.Key.media_volume_mute: string['mute'],
        keyboard.Key.media_volume_up:   string['volumeUp'],
        keyboard.Key.menu:              string['menu'],
        keyboard.Key.num_lock:          string['numLock'],
        keyboard.Key.page_down:         string['pageDown'],
        keyboard.Key.page_up:           string['pageUp'],
        keyboard.Key.pause:             string['pause'],
        keyboard.Key.print_screen:      string['printScreen'],
        keyboard.Key.right:             string['right'],
        keyboard.Key.scroll_lock:       string['scrollLock'],
        keyboard.Key.shift:             string['shift'],
        keyboard.Key.shift_l:           string['shiftLeft'],
        keyboard.Key.shift_r:           string['shiftRight'],
        keyboard.Key.space:             string['space'],
        keyboard.Key.tab:               string['tab'],
        keyboard.Key.up:                string['up'],
    })

    pyautogui = {}  # Just uses strings

    pygame = ({} if not checkImport('pygame', fatal=False, printWarning=False) else {
    })

    standards = (ascii, string, pynput, pyautogui, pygame)

class Key:
    """ A generalized Key class to bridge the gap between several standards.
        Mouse buttons are not included. Neither are controllers.
    """
    useRightLeft = False

    @staticmethod
    def dropRightLeft(key: "Key"):
        # We don't want to call __eq__() cause we use this function from there
        if key._key in (Key('rightCtrl')._key, Key('leftCtrl')._key):
            return Key('ctrl')
        elif key._key in (Key('rightShift')._key, Key('leftShift')._key):
            return Key('shift')
        elif key._key in (Key('rightAlt')._key, Key('leftAlt')._key):
            return Key('alt')
        elif key._key in (Key('rightWin')._key, Key('leftWin')._key):
            return Key('win')
        else:
            return key

    def __init__(self, key, standard=KeyStandard.string):
        if type(key) is type(self):
            self._param = key
            self.standard = key.standard
            self._key = key._key
            return
        elif key is None:
            self._param = None
            self.standard = standard
            self._key = 0
            return

        self._param = key
        self.standard = standard
        self._key = None

        if type(key) is int:
            if isBetween(key, 1, 9):
                self._key = key + 48
            elif key == 0:
                self._key = 57
        else:
            # Their error is better than mine anyway
            try:
                self._key = self.standard[key]
            except KeyError as err:
                for standard in KeyStandard.standards:
                    if key in standard.keys():
                        self._key = standard[key]
                # See if it's cased weird before we give up
                try:
                    self._key = self.standard[key.lower()]
                except:
                    pass
                # If it's still not set, which means it's not in any standard
                if self._key is None:
                    raise err
                    # raise KeyError(f"{key} is not a valid key for the given standard (It might not be implemented yet)")

    def __eq__(self, other):
        try:
            a = self  if self.useRightLeft else self.dropRightLeft(self)
            b = other if self.useRightLeft else self.dropRightLeft(Key(other))
        except:
            raise KeyError(f"Cannot compare types of {type(other).__name__} and Key")

        # if type(other) is Key:
        return a._key == b._key

        # This *should* be replaced by just calling other with the Key constructor above
        # for standard in KeyStandard.standards:
        #     if other in standard.keys():
        #         return debug(a._key == standard[b], clr=3)

    def __hash__(self):
        return hash(self._key)

    # # This doesn't work, I don't know why.
    def __getattr__(self, key):
        debug()
        return Key(key)

    def __str__(self):
        return invertDict(KeyStandard.ascii)[self._key]

    # @todo("Figure out prototyping (look here: https://www.geeksforgeeks.org/prototype-method-python-design-patterns/)")
    def __add__(self, other):
        if type(other) is Key:
            return KeyShortcut(self, other)
        elif type(other) is KeyShortcut:
            other.keys += (self,)
        else:
            raise TypeError(f"Can only add Keys (not {type(other).__name__}) together to make KeyShortcuts")

# TODO add an entered trigger and exited trigger for on pressed vs on released
class KeyShortcut:
    """ Triggers when all the specified keys are being held at the same time """
    def __init__(self, *keys:Key, useRightLeft=False):
        self.useRightLeft = useRightLeft
        self.triggered = Signal()
        self.keys = keys
        self.heldKeys = set()
        if Key('shift') in self.keys:
            debug("Shift (just shift) doesn't work with KeyShortcuts at the moment. No clue why. Please fix my code or use a different key.", clr=RED)

    def update(self, key, pressed):
        key = Key(key) if self.useRightLeft else Key.dropRightLeft(Key(key))

        debug(key, 'shortcut update key', clr=2)

        # debug(self.heldKeys, clr=3)
        if pressed:
            self.heldKeys.add(key)
        else:
            # if key == Key('shift'):
                # self.heldKeys.clear()
            # else:
            try:
                self.heldKeys.remove(key)
            except KeyError:
                self.heldKeys.clear()

        # debug(self.heldKeys, clr=4)

        valid = True
        for i in self.keys:
            if i not in self.heldKeys:
                valid = False
                break

        if valid:
            debug("Shortcut Triggered!")
            self.triggered.call()

# @todo
class KeyChord:
    pass

class KeySequence:
    triggered = Signal()

    def __init__(self, *keySequence):
        self.sequence = keySequence
        self.activeMods = dict(zip(modifierKeys, (False,) * len(modifierKeys)))
        self.currentSequence = []

    def update(self, key, pressed):
        todo('not finished', blocking=True)
        if key in modifierKeys:
            self.activeMods[key] = pressed

        self.currentSequence.append(key)

        valid = True
        for i in self.keys:
            if i in modifierKeys:
                if not self.activeMods[i]:
                    valid = False
            else:
                if key != i:
                    valid = False

        if valid:
            triggered.call()
        else:
            self.currentSequence = []
