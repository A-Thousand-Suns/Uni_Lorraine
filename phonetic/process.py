path = r'E:\编程文件\python\Uni Lorraine\phonetic\Input_File.txt'
out_path = r'E:\编程文件\python\Uni Lorraine\phonetic\out.txt'
vowels_orth = ['a', 'e', 'i', 'o', 'u', 'y', 'é', 'è', 'ê', 'î', 'ô',
               'â', 'ê', 'ë', 'ï', 'à', 'ù', 'û']
vowels_phone = ['a', 'e', 'i', 'u', 'o', 'y', 'E', '9', '2', 'O', '*',
                '@', '1', '5']
stop_consonants = ['p', 't', 'k', 'b', 'd', 'g']
fricatives = ['f', 's', 'S', 'v', 'z', 'Z']
liquids = ['R', 'l']
nasals = ['m', 'n', 'N', 'G']
semi_vowels = ['w', 'j', '8']
consonants = stop_consonants + fricatives + liquids +nasals + semi_vowels


with open(path, 'r', encoding='utf-8') as file:

    for line in file.readlines():

        num = 0
        word = line.split()[0]
        phonetic = line.split()[1]
        result_word = ''
        result1 = ''
        result_phonetic = []
        result_seg = []

        for letter in word:

            if letter in vowels_orth:

                result_word += 'V'

            else:

                result_word += 'C'

        for ph in phonetic:

            if ph in vowels_phone:

                result1 += 'V'

            else:

                result1 += 'C'


        print(word + ' ' + result_word)
        print(phonetic)
        result_seg.append(word)
        result_seg.append(result_word)
        result_seg.append(phonetic)
        result_seg.append(result1)

        while num < len(phonetic)-1:

            if (phonetic[num] in vowels_phone) and (phonetic[num+1] in vowels_phone):

                result_phonetic.append(phonetic[:num+1])
                # print(phonetic[:num+1])
                phonetic = phonetic[num+1:]
                num = 0

            else:
                num += 1
        # print(phonetic)
        result_phonetic.append(phonetic)
        result = ''
        print('after vv:', result_phonetic)


        num_vcv = 0

        while num_vcv <= len(result_phonetic)-1:

            part = result_phonetic[num_vcv]

            if len(part)<3:

                num_vcv += 1
                continue

            num = 1

            while (num<len(part)-1):

                if (part[num-1] in vowels_phone) and (part[num+1] in vowels_phone) and (part[num] in consonants):

                    result_phonetic[num_vcv] = part[:num]
                    part = part[num:]
                    result_phonetic.insert(num_vcv+1, part)
                    break

                num += 1

            num_vcv += 1

        print('after vcv:', result_phonetic)


        # next:ccvv
        num_ccvv = 0

        while num_ccvv <= len(result_phonetic)-1:

            if (len(result_phonetic[num_ccvv]) < 4):

                num_ccvv += 1
                continue

            part = result_phonetic[num_ccvv]
            num = 1

            while (num < len(part)-2):

                if(part[num-1] in vowels_phone) and (part[num+2] in vowels_phone) and (part[num+1] in consonants) and (part[num] in consonants):

                    if (part[num] in liquids) and (part[num+1] in liquids):

                        result_phonetic[num_ccvv] = part[:num+1]
                        # print('change', part[:num+1])
                        part = part[num+1: ]
                        result_phonetic.insert(num_ccvv+1, part)
                        break

                    if (part[num] not in liquids) and (part[num] not in semi_vowels) and ((part[num+1] in liquids) or (part[num+1] in semi_vowels)):
                        result_phonetic[num_ccvv] = part[:num]
                        # print('change', part[:num + 1])
                        part = part[num:]
                        result_phonetic.insert(num_ccvv + 1, part)
                        break

                    if (part[num] in liquids) and (part[num+1] not in liquids) and (part[num+1] not in semi_vowels):

                        result_phonetic[num_ccvv] = part[:num + 1]
                        # print('change', part[:num + 1])
                        part = part[num + 1:]
                        result_phonetic.insert(num_ccvv + 1, part)
                        break

                    if (part[num] in semi_vowels):

                        result_phonetic[num_ccvv] = part[:num + 1]
                        # print('change', part[:num + 1])
                        part = part[num + 1:]
                        result_phonetic.insert(num_ccvv + 1, part)
                        break

                    if (part[num] not in liquids) and (part[num] not in semi_vowels) and (part[num+1] not in liquids) and (part[num+1] not in semi_vowels):
                        result_phonetic[num_ccvv] = part[:num + 1]
                        # print('change', part[:num + 1])
                        part = part[num + 1:]
                        result_phonetic.insert(num_ccvv + 1, part)
                        break

                num += 1

            num_ccvv += 1

        print('after ccvv', result_phonetic)

        # start cccvv
        num_cccvv = 0

        while num_cccvv <= len(result_phonetic)-1:

            if (len(result_phonetic[num_cccvv])<5):

                num_cccvv += 1
                continue

            part = result_phonetic[num_cccvv]
            num = 1

            while num < len(part)-3:

                if (part[num-1] in vowels_phone) and (part[num+3] in vowels_phone) and (part[num] in consonants) and (part[num+1] in consonants) and (part[num+2] in consonants):

                    if (part[num] not in liquids) and (part[num] not in semi_vowels) and (part[num+1] in liquids) and (part[num+2] in semi_vowels):

                        result_phonetic[num_cccvv] = part[:num]
                        # print('change', part[:num + 1])
                        part = part[num:]
                        result_phonetic.insert(num_cccvv + 1, part)
                        break

                    if (part[num] not in liquids) and (part[num] not in semi_vowels) and (part[num+1] not in liquids) and (part[num+1] not in semi_vowels) and (part[num+2] not in liquids) and (part[num+2] not in semi_vowels):
                        result_phonetic[num_cccvv] = part[:num+1]
                        # print('change', part[:num + 1])
                        part = part[num+1:]
                        result_phonetic.insert(num_cccvv + 1, part)
                        break



                num += 1

            num_cccvv += 1




        print('after cccvv', result_phonetic)
        result_seg.append(result_phonetic)
        print('result', result_seg)
        result2 = ''
        result3 = ''

        with open(out_path, 'a', encoding='utf-8') as out_file:

            out_file.write(result_seg[0] + ' ')
            out_file.write(result_seg[1] + ' ')
            out_file.write(result_seg[2] + ' ')
            out_file.write(result_seg[3] + ' ')

            for i in result_seg[4]:

                result2 += i+'-'

            result2 = result2[:-1]
            out_file.write(result2 + ' ')

            for i in result2:

                if i=='-':

                    result3 += i

                elif i in vowels_phone:
                    result3 += 'V'

                else:
                    result3 += 'C'

            out_file.write(result3 +'\n')

        print('-----------')





