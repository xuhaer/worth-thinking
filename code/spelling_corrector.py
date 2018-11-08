''' authur : Peter Norvig
    detail : http://norvig.com/spell-correct.html
'''

import re
from collections import Counter


def words(text):
    return re.findall(r'\w+', text.lower())


WORDS = Counter(words(open('big.txt').read()))


def P(word, N=sum(WORDS.values())):
    "Probability of `word`."
    return WORDS[word] / N


def correction(word): 
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)


def candidates(word): 
    """Generate possible spelling corrections for word.
    （1）如果word是文本库现有的词，说明该词拼写正确，直接返回这个词；
    （2）如果word不是现有的词，则返回"编辑距离"为1的词之中，在文本库出现频率最高的那个词；
    （3）如果"编辑距离"为1的词，都不是文本库现有的词，则返回"编辑距离"为2的词中，出现频率最高的那个词；
    （4）如果上述三条规则，都无法得到结果，则直接返回word。"""
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])


def known(words):
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)


def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)] # 将单词依次分割成两部分，如'ant'-->[('','ant'),('a','bc')....]
    deletes    = [L + R[1:]               for L, R in splits if R] # 依次删除单词的一个字母:['nt','ac','ab']
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1] #依次交换单词的邻近两位['nat','acb',..]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters] #将单词的字母依次替换为其它字母
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word):
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))
