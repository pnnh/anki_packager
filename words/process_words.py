import csv
import os
import re

def clean_word(word):
    """
    清理单词：去除前后的括号
    """
    # 去除前后的括号
    while word.startswith('(') and word.endswith(')'):
        word = word[1:-1]
    return word.strip()

def is_valid_word(word):
    """
    校验单词是否合法（包含字母、数字、连字符、空格、撇号）
    """
    # 允许字母（a-z, A-Z）、数字、连字符、空格、撇号
    pattern = r'^[a-zA-Z0-9\s\-\']+$'
    return bool(re.match(pattern, word))

def split_words(word):
    """
    拆分包含/的单词，返回单词列表
    """
    if '/' in word:
        # 按 / 拆分
        parts = word.split('/')
        return [p.strip() for p in parts if p.strip()]
    else:
        return [word]

def process_csv_to_txt(csv_filename):
    """
    读取CSV文件第一列的单词，校验并去重后写入同名的txt文件
    非法的和重复的单词写入-errors.txt文件
    """
    # 获取文件名（不含扩展名）
    base_name = os.path.splitext(csv_filename)[0]
    txt_filename = base_name + '.txt'
    error_filename = base_name + '-errors.txt'
    
    # 用于存储合法的去重单词
    valid_words = set()
    # 用于记录所有单词的出现次数（原始单词）
    word_count = {}
    # 用于存储非法单词及其原因
    invalid_words = {}
    # 用于存储重复的单词
    duplicate_words = {}
    
    # 读取CSV文件第一列
    with open(csv_filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row:  # 确保行不为空
                original_word = row[0].strip()  # 获取第一列并去除首尾空格
                if original_word:  # 确保单词不为空
                    # 统计原始单词出现次数
                    word_count[original_word] = word_count.get(original_word, 0) + 1
                    
                    # 清理单词（去除括号）
                    cleaned_word = clean_word(original_word)
                    
                    # 拆分包含/的单词
                    word_parts = split_words(cleaned_word)
                    
                    # 处理每个部分
                    all_parts_valid = True
                    for part in word_parts:
                        if part:
                            # 校验单词是否合法
                            if is_valid_word(part):
                                valid_words.add(part)
                            else:
                                all_parts_valid = False
                                # 找出非法字符
                                illegal_chars = set(re.findall(r'[^a-zA-Z0-9\s\-\']', part))
                                # 只记录原始单词一次
                                if original_word not in invalid_words:
                                    invalid_words[original_word] = f"包含非法字符: {', '.join(sorted(illegal_chars))}"
    
    # 找出重复的单词（出现次数 > 1）
    for word, count in word_count.items():
        if count > 1:
            # 清理并拆分来检查是否有合法部分
            cleaned = clean_word(word)
            parts = split_words(cleaned)
            has_valid_part = any(is_valid_word(p) for p in parts if p)
            if has_valid_part:
                duplicate_words[word] = count
    
    # 将合法且去重后的单词排序并写入txt文件
    sorted_valid_words = sorted(valid_words)
    
    with open(txt_filename, 'w', encoding='utf-8') as txtfile:
        for word in sorted_valid_words:
            txtfile.write(word + '\n')
    
    # 将非法单词和重复单词写入errors文件
    with open(error_filename, 'w', encoding='utf-8') as errorfile:
        if invalid_words:
            errorfile.write("=" * 50 + '\n')
            errorfile.write("非法单词（包含不允许的字符）\n")
            errorfile.write("=" * 50 + '\n')
            for word, reason in sorted(invalid_words.items()):
                errorfile.write(f"{word} - {reason}\n")
            errorfile.write('\n')
        
        if duplicate_words:
            errorfile.write("=" * 50 + '\n')
            errorfile.write("重复单词（出现次数 > 1）\n")
            errorfile.write("=" * 50 + '\n')
            for word, count in sorted(duplicate_words.items()):
                errorfile.write(f"{word} (出现 {count} 次)\n")
    
    # 输出统计信息
    print(f"处理完成！")
    print(f"原始行数: {sum(word_count.values())}")
    print(f"原始不同单词数: {len(word_count)}")
    print(f"合法且去重后单词数: {len(valid_words)}")
    print(f"非法单词数: {len(invalid_words)}")
    print(f"重复单词数: {len(duplicate_words)}")
    print(f"输出文件: {txt_filename}")
    print(f"错误文件: {error_filename}")

if __name__ == '__main__': 
    csv_file = 'COCA20000原始.csv'
    
    if os.path.exists(csv_file):
        process_csv_to_txt(csv_file)
    else:
        print(f"文件 {csv_file} 不存在！")
     