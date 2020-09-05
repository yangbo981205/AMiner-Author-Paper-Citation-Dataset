import linecache


file_author_path = r'Dataset/Author.txt'
with open(r'Dataset/CheckCoauthor.txt', 'w', encoding='UTF-8') as f_check_coauthor:
    with open(r'Dataset/Coauthor.txt', 'r', encoding='UTF-8') as f_coauthor:
        with open(r'Dataset/CheckPaperIsCCF_A.txt', 'r', encoding='UTF-8') as f_is_ccf_a:
            i = 1
            for line in f_coauthor:
                line = line.strip('\n')[1:].split()
                # print(line)
                author1 = linecache.getline(file_author_path, int(line[0])).strip('\n').split('--')[1]
                author2 = linecache.getline(file_author_path, int(line[1])).strip('\n').split('--')[1]
                # print(author1, '\t', author2)
                for line_ in f_is_ccf_a:
                    line_ = line_.strip('\n')
                    # print(line_)
                    if (author1 in line_) and (author2 in line_):
                        marks = str(1)
                        f_is_ccf_a.seek(0)
                        break
                    else:
                        marks = str(0)
                else:
                    f_is_ccf_a.seek(0)
                f_check_coauthor.write(line[0] + '/' + author1 + '--' + line[1] + '/' + author2 + '--' + marks + '\n')
                i += 1
                if (i-1) % 10000 == 0:
                    print("读取到第{}行".format(i-1))
                    break






