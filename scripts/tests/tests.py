from scripts.tests.mark_attachments import ma_items
from scripts.tests.multi_vowel_attachments import mva_items

# Instantiate Tests
tests = []


def add_test(url, template, hash):
    tests.append({"url": url, "template": template, "hash": hash})


def add_side_by_side_test(url, title, items):
    hash = {
        "title": title,
        "items": items,
    }
    add_test(url, "side_by_side", hash)


def add_proof_sheet_test(url, title, items):
    hash = {
        "title": title,
        "items": items,
    }
    add_test(url, "proof", hash)


def dec2uni(decimal):
    return f"{format(ord(chr(decimal)), '04x')}"


# ASCII
items = []
for number in range(0, 128):
    items.append({"item": f"{chr(number)}", "description": dec2uni(number)})
add_side_by_side_test("ascii", "ASCII Range", items)

# Gurmukhi
# Gurmukhi block goes from U+0A00 to U+0A7F
# ord('\u0a00') = 2560
# ord('\u0a7f') = 2687
items = []
for number in range(2560, 2688):
    items.append({"item": f"{chr(number)}", "description": dec2uni(number)})
add_side_by_side_test("gurmukhi", "Gurmukhi Code Block", items)

# SPG
items = [
    {"item": "ਉਤ੍ਕਟ", "description": "small k"},
    {"item": "ਬ੍ਰਹ੍ਮ", "description": "half m"},
    {"item": "ਉਤਬ੍ਰਹਮਨੇਸ਼੍ਠੀਟ", "description": "small ṭ"},
    {"item": "ਧੵਾਨੰ", "description": "yakash"},
]
add_proof_sheet_test("spg", "SPG", items)

# Markup
items = [
    {"item": "\u0a28\u0a40\u0a02", "description": "Bindi After (ੀ + ਂ)"},
    {"item": "\u0a28\u0a40\u0a01", "description": "Bindi Before (ੀ + ਁ)"},
    {"item": "\u0a28\u0a40\u0a70", "description": "Tippi (ੀ + ੰ)"},
]
add_proof_sheet_test("markup", "Markup", items)

# Markup
items = [
    {"item": "ਯ", "description": "full yayya"},
    {"item": "ਯੈਂ", "description": "full yayya"},
    {"item": "ਯੂੰ", "description": "full yayya"},
    {"item": "ਯੌਂ", "description": "full yayya"},
    {"item": "ਯੀਂ", "description": "full yayya"},
    {"item": "ਯੂਜ਼ਿ", "description": "full yayya"},
    {"item": "ਯਾਰਿ", "description": "full yayya"},
    {"item": "ਹਯਾੱਤਿ", "description": "full yayya"},
    {"item": "ਪ੍ਰਿਯ", "description": "full yayya"},
    {"item": "ਹਮਾਯੂੰ", "description": "full yayya"},
    {"item": "ਭਯੋੁ", "description": "full yayya"},
    {"item": "ਯਕੀਨ", "description": "full yayya"},
    {"item": "꠳ਯ", "description": "half yayya"},
    {"item": "੍ਯ", "description": "half yayya"},
    {"item": "ਤ੍ਯ", "description": "half yayya"},
    {"item": "ਤ੍ਯੰ", "description": "half yayya, attachment on yayya"},
    {"item": "ਤ੍ਯਾ", "description": "half yayya, attachment on yayya"},
    {"item": "ਹ੍ਯਾਂ", "description": "half yayya, attachment on yayya"},
    {"item": "ਤ੍ਯਾਗਿ", "description": "half yayya, attachment on yayya"},
    {"item": "ਜ੍ਯੋਂ", "description": "half yayya, attachment on yayya"},
    {"item": "ਤ੍ਯੌਂ", "description": "half yayya, attachment on yayya"},
    {"item": "ਲ੍ਯੈਯੈ", "description": "half yayya, attachment on yayya"},
    {"item": "ਭਿ꠳ਯੋ", "description": "half yayya, attachment on pre"},
    {"item": "ਭਿ੍ਯੋ", "description": "half yayya, attachment on pre"},
    {"item": "ਕੀ꠳ਯੋ", "description": "half yayya, attachment on pre"},
    {"item": "ਕੀ੍ਯੋ", "description": "half yayya, attachment on pre"},
    {"item": "꠴ਯ", "description": "open-top yayya"},
    {"item": "ਤ꠴ਯਾ", "description": "open-top yayya"},
    {"item": "ਆ꠴ਯੋ", "description": "open-top yayya"},
    {"item": "ਪਾ꠴ਯਾ", "description": "open-top yayya"},
    {"item": "ਰਾ꠴ਯੰ", "description": "open-top yayya"},
    {"item": "ਦੇ꠴ਯੰ", "description": "open-top yayya"},
    {"item": "꠵ਯ", "description": "open-top half yayya"},
    {"item": "ਤ꠵ਯ", "description": "open-top half yayya"},
    {"item": "ਤ੍ਰਸ꠵ਯੋ", "description": "open-top half yayya"},
]
add_proof_sheet_test("yayya", "Yayya", items)

# Subscript Numerals
items = [
    {"item": "ਮਾਝ₁", "description": "Subscript 1"},
    {"item": "ਬੈਰਾਗਣਿ₁", "description": "Subscript 1"},
    {"item": "ਤਿਪਦੇ₁₅", "description": "Subscript 1 & 5"},
    {"item": "ਮਾਲਾ₂", "description": "Subscript 2"},
    {"item": "ਕਾਫੀ₂", "description": "Subscript 2"},
    {"item": "ਚਾਰਤੁਕੇ₂", "description": "Subscript 2"},
    {"item": "ਪੰਚਪਦੇ₂", "description": "Subscript 2"},
    {"item": "ਦੁਪਦੇ₂", "description": "Subscript 2"},
    {"item": "ਤਿਪਦੇ₃", "description": "Subscript 3"},
    {"item": "ਚਉਪਦੇ₄", "description": "Subscript 4"},
    {"item": "ਪੂਰਬੀ₄", "description": "Subscript 4"},
    {"item": "ਗਉੜੀ₅", "description": "Subscript 5"},
    {"item": "ਪੰਚਪਦੇ₆", "description": "Subscript 6"},
    {"item": "ਗਉੜੀ₈", "description": "Subscript 8"},
    {"item": "ਟੈਸਟ₇", "description": "Subscript 7"},
    {"item": "ਟੈਸਟ₉", "description": "Subscript 9"},
    {"item": "ਟੈਸਟ₀", "description": "Subscript 0"},
]
add_proof_sheet_test("subnum", "Subscript Numerals", items)

# Diacritics
items = [
    {"item": "ਕ੍ਰਾਂ", "description": ""},
    {"item": "ਸ੍ਵਾਂ", "description": ""},
    {"item": "ਨ੍ਰਿੱ", "description": ""},
    {"item": "ਨੵਿੰ", "description": ""},
    {"item": "ਮ੍ਰਿੱ", "description": ""},
    {"item": "ਭ੍ਰਿੰ", "description": ""},
    {"item": "ਕ੍ਰੁੱ", "description": ""},
    {"item": "ਨ੍ਹੈਂ", "description": ""},
    {"item": "ਹ੍ਵੈੁ", "description": ""},
    {"item": "ਖ਼ੁੱਦ", "description": ""},
    {"item": "ਖ਼ੁੱਰੋ", "description": ""},
    {"item": "ਨੑੁ", "description": ""},
    {"item": "ਹੁਂ", "description": ""},
    {"item": "ਦੇਂ", "description": ""},
    {"item": "ਤੀੰ", "description": ""},
    {"item": "ਕੀੰ", "description": ""},
    {"item": "ਨੀੰ", "description": ""},
    {"item": "\u0a28\u0a40\u0a70", "description": ""},
    {"item": "ਧ੍ਰੂ", "description": ""},
    {"item": "ਸ੍ਯ", "description": ""},
    {"item": "ਸ੍ਟ", "description": ""},
    {"item": "ਸ੍ਨੰ", "description": ""},
    {"item": "ਸ੍ਤ", "description": ""},
    {"item": "ਸ੍ਚ", "description": ""},
    {"item": "ਸ੍ਵਾ", "description": ""},
    {"item": "ਖੵ", "description": ""},
    {"item": "ੜ੍ਹੂ", "description": ""},
    {"item": "ਮੵਿਾ", "description": ""},
    {"item": "ਧੵਿਾ", "description": ""},
    {"item": "ਥੵੰਤ", "description": ""},
    {"item": "\u0a32\u0a75\u0a3f\u0a4b", "description": ""},
]
add_proof_sheet_test("diacritics", "Diacritics", items)

items = ma_items
add_proof_sheet_test("mark-attachments", "Mark Attachments", items)

items = mva_items
add_proof_sheet_test("multi-vowel-attachments", "Multiple Vowel Attachments", items)


items = [
    {"item": "ਦੇਂਹਿ", "description": "Bindi between vowels"},
    {"item": "ਹੋਂਹਿ", "description": "Bindi between vowels"},
    {"item": "ਰੋਂਦੇ", "description": "Bindi between vowels"},
    {"item": "ਲੈਂਦਿਆਂ", "description": "Bindi between vowels"},
    {"item": "ਸਾਂਤਿ", "description": "Bindi between vowels"},
    {"item": "ਐਂਠੈ", "description": "Bindi between vowels"},
    {"item": "ਐਂਠੇ", "description": "Bindi between vowels"},
    {"item": "ਭੰਨੇ", "description": "Tippi + pre/above attachment"},
    {"item": "ਅੰਤਿ", "description": "Tippi + pre/above attachment"},
    {"item": "ਅੰਮ੍ਰਿਤਸਰ", "description": "Tippi + pre/above attachment"},
    {"item": "ਙੰਙੈ", "description": "Tippi + pre/above attachment"},
    {"item": "ਅੰਙੈ", "description": "Tippi + pre/above attachment"},
    {"item": "ਰੰਙੈ", "description": "Tippi + pre/above attachment"},
    {"item": "ਕਿੰਨੇ", "description": "Tippi + pre/above attachment"},
    {"item": "ਮੁੰਨੇ", "description": "Tippi + pre/above attachment"},
    {"item": "ਮੰਨੈ", "description": "Tippi + pre/above attachment"},
]
add_proof_sheet_test("db-words", "DB Words", items)


items = [
    {
        "item": "",
        "description": "theory that a few numbers come from the same letter as they are described with. notables include 1, 2, 3, 4, 5, 6. see also evolution of numbers: Georges Ifrah, The Universal History of Numbers pp 368-396.",
    },
    {"item": "੧ੲ੧ੲ", "description": "੧ ਇੱਕ"},
    {"item": "੨ਦ੨ਦ", "description": "੨ ਦੋ"},
    {"item": "੩ਤ੩ਤ", "description": "੩ ਤਿੰਨ"},
    {"item": "੪ਚ੪ਚ", "description": "੪ ਚਾਰ"},
    {"item": "੫ਪ੫ਪ", "description": "੫ ਪੰਜ"},
    {"item": "੬ਛ੬ਛ", "description": "੬ ਛੇ"},
    {"item": "੭ਸ੭ਸ", "description": "੭ ਸੱਤ"},
    {"item": "੮ਅ੮ਅ", "description": "੮ ਅੱਠ"},
    {"item": "੯ਨ੯ਨ", "description": "੯ ਨੌਂ"},
]
add_proof_sheet_test("letter-numbers", "Letter-Number Comparison", items)

items = [{"item": "ਲੰ", "description": ""}]
add_side_by_side_test("nasal-attachment", "Nasalizations", items)
