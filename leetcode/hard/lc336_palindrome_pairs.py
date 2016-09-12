# coding=utf-8
"""
336. Palindrome Pairs

Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list,
so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
    Given words = ["bat", "tab", "cat"]
    Return [[0, 1], [1, 0]]
    The palindromes are ["battab", "tabbat"]

Example 2:
    Given words = ["abcd", "dcba", "lls", "s", "sssll"]
    Return [[0, 1], [1, 0], [3, 2], [2, 4]]
    The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
"""
from leetcode.utils.funcs import print_result


class Solution(object):

    # TODO: trie solution?

    @print_result
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # word:position映射表
        self.cache = {i: n for n, i in enumerate(words)}

        result = []
        for n, word in enumerate(words):
            if self.is_palindrome(word):  # 单词本身是回文
                if self.cache.get('', n) != n:  # 如果有空字符串，前后皆可拼接成回文
                    result.append([n, self.cache['']])
                    result.append([self.cache[''], n])

            if self.cache.get(word[::-1], n) != n:  # 单词逆序存在
                result.append([n, self.cache[word[::-1]]])

            for i in range(1, len(word)):  # 对每个单词做拆分
                if self.is_palindrome(word[:i]):  # 如果前半部分是回文
                    rw = word[i:][::-1]  # 后半部分逆转
                    if self.cache.get(rw, n) != n:  # 如果存在则拼到前面两个单词形成回文
                        result.append([self.cache[rw], n])

                if self.is_palindrome(word[i:]):  # 如果后半部分是回文
                    rw = word[:i][::-1]  # 前半部分逆转
                    if self.cache.get(rw, n) != n:  # 如果存在则拼到后面两个单词形成回文
                        result.append([n, self.cache[rw]])
        return result

    @print_result
    def palindromePairs1(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        self.cache = []
        result = []
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if self.is_palindrome(words[i] + words[j]):
                    result.append([i, j])

                if self.is_palindrome(words[j] + words[i]):
                    result.append([j, i])
        return result

    def is_palindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    assert sorted(s.palindromePairs(['a', ''])) == sorted([[0, 1], [1, 0]])
    assert sorted(s.palindromePairs(["bat", "tab", "cat"])) == sorted([[0, 1], [1, 0]])
    assert sorted(s.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])) == sorted(
        [[0, 1], [1, 0], [3, 2], [2, 4]])
    assert sorted(s.palindromePairs(
        ["ha", "eaebjghbjjheddgfa", "hhaccedbbdbciid", "ediihegjbefacccga", "hdbiiicacdcdf",
         "cefafdjbafbiahcc", "abhdedaagbbcibhbjbbd", "dcbefdcfceaiaahfejc", "jbhgfdcfihg", "g",
         "dbi", "hgabcfibbiddcji", "hjhdiiiaicij", "afbbcbdffeifafc", "abbihgiiif", "be", "j",
         "ecjefbbcjac", "eg", "ighcicacd", "eicceeaaefg", "ia", "fcfgjaijgdbchhfhddg", "aghecechf",
         "ihgcgafga", "bjfgdjba", "ab", "hhbjhe", "hhedaebbceeeja", "eabgicejiddiijjdbjjj", "icb",
         "eghhbhfajccb", "fideijjhheabhjfhh", "def", "bihfa", "hibhifghhddcijfcfebc", "hihdgbiijh",
         "jcibccjei", "bgdcdcbcjaicihjiafg", "jiie", "bbihfgcffheccdeddd", "hefea", "iagegahcehdcf",
         "fghhgcfigegcfbcde", "igbch", "cicdjechehfdiagcc", "djcieegaehigc", "hgajaehbdg",
         "ejbcdehfibdecgbhb", "bcbcfdgefffi", "aabjeadagfifeihjac", "hjhdgcaddbcf", "idiggbfihfiic",
         "gcffh", "e", "cfggajjfj", "gegedie", "achiajcjecja", "bbbcgjefbhhf", "iadjhigibgbh",
         "fgdbicdg", "jghfhhcahah", "hajjfaeahbhiijegab", "fafhba", "idhgehaiafhibe",
         "gjfcgjbejhjgfbg", "ajai", "gbhgefeicjeejhghcb", "i", "di", "hbcahahdfbdfcbffi",
         "hedigibfiacebff", "jcddfcjjagbbgh", "dchca", "hgagfghbbhb", "jidi", "cgcjcdhcejj",
         "chhdbhejijgaehbaic", "gabedga", "fjdbegjfjaeagei", "ifefffgd", "jghhhicgijjdeejc",
         "idadhej", "hgcgagfhhbj", "bhhhgbihga", "hgdjdehfi", "fbaciggbdg", "jdbj", "dhgeafc",
         "fjjjj", "djghaahiji", "bhegiaiicgijfjacgacj", "eaheeg", "hjdcedga", "dahbieb",
         "ejgahijifchajajee", "haejbc", "ebijhbf", "fed", "ddibabcdhdjdgeie", "ecg",
         "ihebibfhdifagdcdbjdi", "cghijahbedjccg", "egiaj", "egdhcbcihb", "adhbbdgcffcgggehgbi",
         "eaiii", "gagejb", "dfhccaadifhjjdfffiba", "bdhfhahdbefgifgdf", "eibhdehbfccbc",
         "jgbcgbebbjf", "feagecfhiafh", "ifagegfbaegefihifja", "iicgcchcie", "defjbi",
         "djdejegjefffbggcgf", "dejjggighbcgidjgfbc", "ebibeejhjchjadahcd", "ccidbehccbhfhbdj",
         "ibdbecfgicajdg", "eegjbgceifhfahjiefe", "bgfdddajeacjfddhheie", "egghhabi",
         "dafaidibhdebijhcji", "igj", "eihif", "hjjdcjcihi", "ihffbe", "bf", "ajdfbe", "jihcc",
         "cgejejhbfffjbca", "cajgii", "abceahigj", "hhbhehfbhfefajbiceia", "fgghdgfbbeicj",
         "ghhaibheccdgdabeaa", "ahidijigdfdbcefai", "jgahjjhdejc", "aabhjdfbeghffgiihhec",
         "fhdgfeiijga", "ffgjeiihgdhbidehgci", "jdcaaafe", "dbabfbfaheidce", "bcfeeihjdjgfh",
         "ifigghggicj", "biibie", "jajigfecdaagfeggjeh", "igidegf", "bffhefffjahgjbdijh",
         "egcbfjgc", "gbghhgdbb", "bghbijfeij", "hagfbg", "iiigdha", "cfdchgbabijjbidfje", "ggeee",
         "hidfaajfb", "cjab", "hgff", "daahgg", "cf", "fjhfaiheeicdib", "giegdhbajcgagf", "bbebjef",
         "f", "jhhiaebdcec", "fdjjjgaeeg", "ccbjaageiaddbc", "fijdjbijea", "jggj", "ieaaeiiddiaj",
         "ghg", "deiaicejhggcfchj", "hhhef", "fcecgfha", "hgejaji", "hce", "abfhgjegiefjb",
         "iijibjdheejaieiga", "jgbifgcjedi", "jfafebjfjadcibcbjdh", "ai", "hihjhcachbcghacib",
         "cicceaebdidgbef", "hecfiagefhhcjcbdhicd", "diafccjdb", "dffej", "giadddbjjigghbjbdfib",
         "ahd", "efafdc", "cgejjgjijh", "cjbf", "aceahd", "hcajghbdibfhb", "aacabbjhfjcge",
         "fhggbacdiaed", "bahehcjeifhcghdhi", "fbhdbajbcjdhe", "jbahjdiiffb", "dgechbigjabghchfbei",
         "ddbbbb", "ebiii", "jjbbgdcgdebijiejc", "jhjef", "ggbdgciibiif", "gice", "ffjccagjigbd",
         "jbefedejfcafhe", "dfd", "gbibjaachijbghhffbi", "fdddefbdjh", "aadjbjdfedc", "hbiecdjjfci",
         "jci", "jhj", "aejeieccbfi", "deid", "giggagjhcbgbbe", "jgfjfa", "jibhffhbae", "hd",
         "iedidfdachgcifbjag", "fjj", "hbbddajidfjiidd", "fgjggedajihdhjd", "ijgjbfjf",
         "gbjgdceeaej", "bgaijh", "egcgbegfadeibcfcebf", "bccaedehchiaed", "jgaebdedhbi",
         "hjafcghabb", "iiid", "aiaefejedcjhibbae", "fd", "bieciafejaa", "ihf", "aaaijicifa",
         "gegjgcceedi", "dbfbcggfdfa", "cdjb", "a", "ebcheedccdaaidjfi", "cchiaaagfghdhefjfiib",
         "ecdjca", "bdfgjcgcheebdggide", "jfigaciejefba", "idjgdbffch", "aaedgfgjhcbigbccgji",
         "gfehgjchgbejea", "dagbhdija", "bdhcfahifjbigj", "cifaeicajhfdgajjfj", "bhigd",
         "icbbacfejcddj", "dc", "cebgi", "cbicfejcjifiihd", "eeeic", "fbighdhg", "hjefedih", "b",
         "jheheehjcbhjadecb", "jeeidjdaiagcg", "dadhghdecedahbcicg", "edije", "jacdjiadbibejjccgd",
         "jdbdejehagjjfc", "fdcgbb", "fgihbdjchfgbjbafcfj", "dfbjfbidafegcfcgdcgf",
         "hiccidgdbbbbgijcf", "eagichhf", "ifhjbgheiaaagde", "bfggb", "bdfcjeihfdahec",
         "bjhbbedgaaacg", "eeaihbj", "ihfacji", "dajjaajdgjdjc", "jhibebgifihi",
         "jfaadbaeiiciehihecc", "hfhge", "bab", "eaecdfc", "dhejdcejhfbabddbb",
         "gfaiffdacigjeidead", "debbibeeajdf", "dfdbahhiigjiigdcd", "ejdhfhhchb",
         "aecjgajdbffeagahfc", "daaiheffhehcaiha", "gbjfbghecdbbcecj", "ghhahhffj", "fefdjg",
         "dijgbfjgbhfgafbicdgd", "cjhicaddjffgeeahd", "aaegbcgidchffhgiejgi", "hjcdaahbgfja",
         "aajidhfhfeg", "hhdageejf", "begiifeabcc", "aiaajehfb", "fegefijiheijhjejic", "d",
         "ghfadhbaegdeaaihghh", "h", "bjdadfcegjjcgjhjai", "iiifjiejeedibec", "adbcagchbhfcbdid",
         "hjgj", "afbhbidhh", "bjcchefiahghh", "ggefcifj", "gceddbfafebfegca",
         "adfgbhaiheehehabfbi", "ffjdfbabdadjf", "gajigbefifdbhfga", "jfhigiaaabffahhagbhc",
         "iffgiajcdfje", "ehjgafhbhcdjcechf", "bh", "ddajichiacfij", "jcbcjjaafhheahbejadf",
         "jagggdijggfacabcj", "ihgchcge", "bfbjgjfeg", "djica", "jcjidadjhd", "ahjajdhjhdgeaaehfh",
         "dhcjifcghjccjd", "bbj", "idbgejhcdg", "begfd", "edeajebcihghef", "ejhjh", "eceajiehdabg",
         "gdheijaeichacegdfa", "fhfafdddg", "jiibjdidbcfg", "gjjhagjjbgdbjiaf", "bb",
         "fcehjhfgjbhje", "jcgbcaghcbg", "afhegij", "fhbggicjjdjg", "cehdiibhibcicebfd",
         "ciabfjfgffcjgbjbjcd", "jdiei", "ebdhaahichcff", "gbejdachjdfec", "faahgjiddibbhdhgi",
         "aafeeadbdfcdibjdj", "ahaffe", "gjihhgegfh", "cgeededdifbbhcg", "bgf",
         "cahafcgfidgjgajajcb", "gacdhab", "id", "ccgeb", "hgiifeaiiaafcbh", "ffdcgfjggijhdggddhb",
         "idhhb", "gaif", "hefjahejhhhhhe", "dj", "hggeegcaiichegfedchf", "bc", "geiadbdgcaeii",
         "cgbggfbadcbfbhidhjg", "chijihchhgef", "edacjbjfjgbdecddg", "ggjjdddchdhii", "jigbd",
         "ifbajff", "ihdcfihcjfj", "ddbefaefa", "edbhgbcbhjgaeheeijgh", "ghcdjehfgb",
         "chfjdgjcdffj", "ffh", "dgc", "iaggidcacghjgahfeg", "dddbhbdcggbb", "baiiicibgej",
         "iaichdghc", "eddcdjaffebjdafagcie", "eiiachijhcf", "aajifgbdi", "hg", "bibjfg",
         "ibfdeaafbdfd", "idebdfffigifhiebjb", "jchgeffabfei", "eghjdcei", "jiafgdjadcchfe",
         "cbjbeejfihgdfheeb", "aiec", "biicjgcd", "dcfeh", "iehehiagjeeh", "bdj", "fi", "fage",
         "afjechgehgfchb", "ehia", "fadieabh", "bccaiidbiffbebedb", "gajjgaf", "ffii", "iidicfb",
         "ea", "ejdcfacacjhiffa", "ef", "hhhddgjaaidgdigc", "cicfcieiigiicif", "hah",
         "ahijijhhcddeabafcgj", "eefcicg", "gbfcifhiegaghhc", "faa", "gbihh", "idfdffif",
         "ifaijgdcefi", "ddfdbadhgabf", "gghhifiba", "cijadagjhjjacfif", "ibeffhdhhejfgebbdbf",
         "eeifidadeag", "aadcfjbcbegici", "eaaccfdd", "gdeacedgjbagb", "eahbdccfffgj",
         "hdceaaiacih", "fagcgfejbcfgacbai", "ghe", "fjdcahhdgcigcchgfhbh", "cafig", "jieebdi",
         "cjfhdajiejdhhig", "ahejhbjjjdeijcb", "bfbcjjccgi", "bedeji", "gajbgiafdh",
         "hjifeieiccgjjejei", "jdddjcjcjhjihdha", "hijheac", "dfffigfagibbca", "iacijdfjbafcjhffa",
         "cdeihee", "dgiaheaeii", "ehahbb", "jeeigigefaj", "fgaghcgbehfgeheacih",
         "aijbcbgibfbbcfjfffba", "abbaiaagcigjbdific", "bbacahj", "jdiehhddjjeiijgge",
         "hhigcgibhbdg", "aachgbagja", "edhb", "ajccifc", "fcdcjihjhaacdfehfchj", "bjcg", "bibbdbg",
         "jdjihegfdde", "hdjf"])) == sorted(
        [[190, 0], [243, 0], [0, 308], [0, 419], [9, 18], [9, 392],
         [54, 15], [203, 15], [15, 263], [75, 16], [16, 333], [16, 368],
         [18, 54], [18, 284], [21, 68], [21, 183], [183, 21], [243, 21],
         [26, 243], [263, 26], [285, 26], [370, 30], [33, 98], [98, 33],
         [414, 54], [416, 54], [68, 66], [68, 69], [68, 183], [361, 68],
         [68, 405], [69, 234], [69, 306], [69, 361], [361, 69],
         [87, 404], [89, 166], [98, 416], [166, 129], [129, 263],
         [166, 162], [224, 166], [236, 166], [405, 166], [166, 416],
         [423, 166], [173, 392], [183, 243], [210, 236], [306, 222],
         [222, 308], [306, 234], [306, 236], [243, 414], [257, 306],
         [323, 263], [263, 343], [343, 263], [370, 263], [306, 361],
         [368, 306], [312, 308], [308, 323], [308, 383], [392, 308],
         [333, 343], [350, 368], [438, 392]])

    print 'PASS'
