"""将通用的关系抽取数据转换为bert所需格式"""
import codecs


def read_file_iter(file_name, keep_original=False):
    """ 读取文件内容，使用迭代器返回.

        @params:
            file_name - 文件路径.
            keep_original - 保持文件内容不变，默认会去掉空行以及每一行的左右空格.

        @return:
            On success - 文件内容迭代器.
    """
    with codecs.open(file_name, mode='r', encoding='utf8') as fr:
        if keep_original:
            for line in fr:
                yield line
        else:
            # 去掉空行以及每一行的左右空格
            for line in fr:
                yield line


if __name__ == "__main__":
    file_in = 'data/relation/val.conll'
    file_out = 'data/relation/bert/val.conll'
    file_iter = read_file_iter(file_in)
    bert_data = list()
    entity_flag = False
    print('===========提取组装bert所需数据==============')
    for line in file_iter:
        if '\t' in line:
            word, tag = line.split('\t')
            if tag.startswith('B-'):  # 实体标志周围，增加[SEP]标志
                entity_flag = True
                bert_data.append('[SEP]')
                bert_data.append('{}'.format(word))
            elif tag.startswith('I-'):
                bert_data.append('{}'.format(word))
            else:
                if entity_flag:
                    entity_flag = False
                    bert_data.append('[SEP]')
                bert_data.append(word)
        else:
            if entity_flag:
                entity_flag = False
                bert_data.append('[SEP]')
            bert_data.append(line.strip())
    print('===========数据输出==============')
    print(len(bert_data))
    print(bert_data[:20])
    with codecs.open(file_out, mode='w', encoding='utf8') as fw:
        for line in bert_data:
            fw.write('{}\n'.format(line))
