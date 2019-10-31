'''TNEWS 今日头条中文新闻（短文本）分类转换为txt格式,标签\t文本;
数据来源：<https://github.com/chineseGLUE/chineseGLUE>'''
import codecs
# 日志初始化
import logging

logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logging.info('logging test')


if __name__ == "__main__":
    input_files = {
        'dev': 'data/toutiao_category_dev.txt',
        'test': 'data/toutiao_category_test.txt',
        'train': 'data/toutiao_category_train.txt'
    } 
    output_file = 'data/toutiao_category_{}_v1.txt'
    # 提取数据集中的数据
    # title_list = ('news_id', 'category_code', 'category', 'title', 'keywords')
    for data_type, input_file_name in input_files.items():
        logging.info('start to process file : {}'.format(input_file_name))
        output_file_name = output_file.format(data_type)
        with codecs.open(output_file_name, mode='w', encoding='utf8') as fw:
            with codecs.open(input_file_name, mode='r', encoding='utf8') as fread:
                line_index = 0
                for line in fread:
                    line = line.strip()
                    if len(line) < 0:
                        continue
                    line_pieces = line.split('_!_')
                    if len(line_pieces) != 5:
                        continue
                    category = line_pieces[2]
                    title = line_pieces[3]
                    keywords = line_pieces[4]
                    text = '{}{}'.format(title, keywords).replace('\t', '').replace('\r', '').replace('\n', '').strip()
                    if len(text) < 2 or len(category) < 1:
                        continue
                    label = category
                    fw.write('{}\t{}\n'.format(label, text))
                    line_index += 1
                    if line_index % 100:
                        logging.info('{} : processed lines:{}'.format(data_type, line_index))
            logging.info('end to process file : {}'.format(input_file_name))
            logging.info('processed lines in this file:{}'.format(line_index))
