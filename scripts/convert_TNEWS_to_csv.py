'''TNEWS 今日头条中文新闻（短文本）分类转换为csv格式，并合并到一个文件中;
数据来源：<https://github.com/chineseGLUE/chineseGLUE>'''
import csv
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
    output_file = 'data/toutiao_category.csv'
    with codecs.open(output_file, 'w', encoding='utf-8') as csvout:
        writer = csv.writer(csvout)
        # 写入表头
        title_list = ('data_type', 'news_id', 'category_code', 'category', 'title', 'keywords')
        writer.writerow(title_list)
        # 提取数据集中的数据
        for data_type, input_file_name in input_files.items():
            logging.info('start to process file : {}'.format(input_file_name))
            with codecs.open(input_file_name, mode='r', encoding='utf8') as fread:
                line_index = 0
                for line in fread:
                    line = line.strip()
                    if len(line) < 0:
                        continue
                    line_pieces = line.split('_!_')
                    if len(line_pieces) != 5:
                        continue
                    row_data_line = [data_type]
                    row_data_line.extend(line_pieces)
                    writer.writerow(row_data_line)
                    line_index += 1
                    if line_index % 100:
                        logging.info('processed lines:{}'.format(line_index))
            logging.info('end to process file : {}'.format(input_file_name))
            logging.info('processed lines in this file:{}'.format(line_index))
