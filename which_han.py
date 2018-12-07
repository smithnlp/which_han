"""This is a tool which tries to decipher which Han dialect peculiarities are
present in any given string of non-standard Chinese text. It's intended users
are learners of Chinese who know enough of the language to know what they don't
know.
"""
import re
import jieba
from pprint import pprint


def check_yue(text):
    """See if there are Cantonese trigger-characters and/or other patterns.
    """
    status = False
    yue_vernacular_dict = {r'BB仔': ['BB jai', '嬰兒'],
                           r'一啲': ['yat di', '一些'],
                           r'上堂': ['seung tong', '上課'],
                           r'乜(咩)嘢': ['mat（me） ye', '什麼'],
                           r'今日': ['gam yat', '今天'],
                           r'仔女': ['jai nui', '兒女'],
                           # r'令': ['ling', '使'],
                           r'仲會': ['chung wui', '還會'],
                           r'仲有': ['chung yau', '還有'],
                           r'但係': ['daan hai', '但是'],
                           r'你哋': ['nei dei', '你們'],
                           r'佢': ['keui', '他/她/它/祂'],
                           r'佢哋': ['keui dei', '他/她/它/祂們'],
                           # r'係': ['hai', '是'],
                           r'俾/畀': ['bei', '給'],
                           r'做嘢': ['jou ye', '工作'],
                           r'先': ['sin', '才'],
                           r'冇': ['mou', '沒有'],
                           r'出貓': ['chyut maau', '作弊'],
                           r'加埋／同埋': ['ga maai／tongmaai', '一起'],
                           r'厠所': ['chi so', '洗手間'],
                           # r'同': ['tong', '和/跟'],
                           r'呢位': ['nei wai', '這位'],
                           r'呢度': ['lei dou', '這裡'],
                           r'呢種': ['nei chung', '這種'],
                           r'呢項': ['nei hong', '這項'],
                           r'咁': ['gam', '這麼'],
                           r'咗': ['jo', '了'],
                           r'咪': ['mi', '別／就'],
                           r'唔': ['ng', '不'],
                           r'唔係': ['ng hai', '不是'],
                           r'唔會': ['m wui', '不會'],
                           r'唔該你': ['m goi nei', '謝謝'],
                           r'唔該你…': ['m goi nei', '請你…'],
                           r'啱': ['ngaam', '對／是／正確'],
                           r'啱啱': ['ngaam ngaam', '剛剛'],
                           r'啲': ['di', '一點'],
                           r'喺': ['hai', '在'],
                           r'嗰位': ['go wai', '那位'],
                           r'嗰度': ['go dou', '那裡'],
                           r'嘅': ['ge', '的'],
                           # r'好': ['hou', '很'],
                           r'好似': ['hou chi', '好像'],
                           r'好冧': ['hou lam', '很甜蜜'],
                           r'定係': ['ding hai', '還是'],
                           r'家姐': ['ga je', '姐姐'],
                           r'將': ['jeung', '把'],
                           r'尋日/琴日': ['cham yat／kam yat', '昨天'],
                           r'屋企': ['nguhkei', '家'],
                           r'恰眼瞓': ['hap ngaan fan', '打瞌睡'],
                           r'我哋': ['ngoh dei', '我們'],
                           r'打喊露': ['da haam lou', '打呵欠'],
                           r'搵': ['wen', '找'],
                           r'攰': ['gui', '累'],
                           r'放工': ['fong gong', '下班'],
                           r'放飛機': ['fong fei gei', '失約 / 爽約'],
                           r'晏啲': ['ngaan di', '晚一點'],
                           r'晒／曬': ['saai', '完全／全部'],
                           r'沖涼': ['chung leung', '洗澡'],
                           r'無啦啦': ['mo la la', '無故'],
                           r'睇': ['tai', '看'],
                           r'睇戲': ['tai hei', '看電影'],
                           r'睇落／睇嚟': ['tai lok／tai lei', '看來'],
                           r'細': ['sai', '小'],
                           r'細佬': ['sai lou', '弟弟'],
                           r'細妹': ['sai mui', '妹妹'],
                           r'細路仔': ['sai lou jai', '小朋友'],
                           r'老公': ['lou gung', '丈夫'],
                           r'老婆': ['lou po', '妻子'],
                           r'聽日': ['ting yat', '明天'],
                           r'話我知': ['wa ngo ji', '告訴我'],
                           r'諗': ['lam', '想'],
                           r'諗計': ['lamgai', '想辦法'],
                           r'講': ['gong', '說'],
                           r'返去': ['fan heui', '回去'],
                           r'返學': ['faan hok', '上學'],
                           r'邊位': ['bin wai', '哪一位'],
                           r'邊個': ['bin go', '誰'],
                           r'邊度': ['bin dou', '哪裡'],
                           # r'都': ['dou', '也'],
                           r'鐘': ['jung', '小時'],
                           r'阿哥': ['a go', '哥哥'],
                           r'阿媽': ['a ma', '媽媽'],
                           r'阿爸': ['a ba', '爸爸'],
                           r'食': ['sik', '吃'],
                           r'食煙': ['sik yin', '抽煙'],
                           r'飲': ['yam', '喝'],
                           r'飲酒': ['yam jau', '喝酒'],
                           r'駛唔駛': ['sai m sai', '要不要'],
                           r'點樣': ['dim yeung', '如何/怎樣'],
                           r'點解': ['dim gaai', '為什麼']}
    for token, info in yue_vernacular_dict.items():
        m = re.search(r'(.{0,5})' + token + r'(.{0,5})', text)
        if m:
            print("Yue dialect detected!\t\t", m.group(1), "__", token, "__", m.group(2))
            status = True
    return status


def check_wu(text):
    """See if there are characteristically Wu-dialect linguistic features.
    """
    status = False
    wu_vernacular_subs = {'不': ['və', [r'勿', r'弗', r'佛', r'拂', r'阀', r'Ve']],
                          '的': ['e or ge', [r'额', r'呃', r'俄', r'饿', r'厄', r'格', r'咯', r'歌', r'嘎', r'嘚']],
                          '我们': ['a la', [r'阿拉', r'啊拉', r'阿啦']],
                          '什么': ['sa', [r'啥', r'撒', r'萨']],
                          '很': ['lao', [r'老', r'牢']],
                          # '这': ['ge', [r'个']],
                          '谢谢': ['xia xia', [r'下下']],
                          '好': ['ling', [r'灵']],
                          '在': ['lele or lala', [r'了了', r'拉拉']],
                          '时间': ['chen guang', [r'辰光', r'晨光', r'承光']],
                          '那': ['he', [r'許']],
                          '洗': ['da', [r'汏']],
                          '藏': ['kang', [r'囥']],
                          '斜': ['ge', [r'隑']],
                          '二十': ['nie', [r'廿']],
                          '人': ['zhu or ning', [r'宁']]}
    wu_vernacular_triggers = {r'戆': ['gang', 'stupid'],
                              r'侬': ['nong', 'you', '你'],
                              r'覅': ['fiao', 'wu + yao', '不要']}
    for token, info in wu_vernacular_subs.items():
        for i in info[1]:
            m = re.search(r'(.{0,5})' + i + r'(.{0,5})', text)
            if m:
                print("Wu dialect detected!\t\t", m.group(1), "__", i, "__", m.group(2))
                status = True
    for token, info in wu_vernacular_triggers.items():
        m = re.search(r'(.{0,5})' + token + r'(.{0,5})', text)
        if m:
            print("Wu dialect detected!\t\t", m.group(1), "__", token, "__", m.group(2))
            status = True
    return status


def main():
    """Take some string of Hanzi characters submitted by the user check for
    dialect traits.
    """
    print('\n')
    running = input("Paste some non-standard Chinese text and this program will try to decipher which Han variety it represents and explain the distinguishing features.\n\nYOUR TEXT: ")  # noqa
    # tokens = jieba.cut(running, cut_all=False)
    print('\n')
    print('Checking for dialect traits......', flush=True)
    print('\n')
    print('If found, unique characters will be shown in context and surrounded by "__"', flush=True)
    print('\n')
    yue_features = check_yue(running)
    print('\n')
    wu_features = check_wu(running)
    print('\n')
    if not yue_features and not wu_features:
        print('\n')
        print("Sorry, couldn't find anything!")
        print('\n')


if __name__ == '__main__':
    main()
