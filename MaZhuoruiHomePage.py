# coding:utf-8

'''我的主页'''

import streamlit as st
from PIL import Image

page = st.sidebar.radio('首页', ['兴趣推荐', '图片处理工具', '智慧词典', '留言区'])


def img_change(img, rc, bc, gc):
    width, height = img.size
    img_array = img.load()

    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]

            img_array[x, y] = (r, g, b)

    return img


def page1():
    """兴趣推荐"""
    st.image('logo.png')
    st.write('动漫推荐')
    st.write('------------------------')
    st.write('你的名字。（君の名は。）')
    st.image('YourName.png')
    st.write('故事梗概:')
    text = '故事背景发生在适逢千年一遇彗星到访的日本' \
           '，生活在日本小镇的女高中生宫水三叶对于担' \
           '任镇长的父亲所举行的选举运动，还有家传神' \
           '社的古老习俗感到无聊乏味，对大城市充满憧' \
           '憬的她，甚至幻想着来世请做东京的帅哥！忽' \
           '然有一天三叶做了个自己变成男孩子的梦，在' \
           '陌生的房间，面对陌生的朋友，以及东京的街' \
           '道。虽然感到困惑，但少女对于能来到朝思暮' \
           '想的东京还是充满喜悦。与此同时，生活在东' \
           '京的男高中生立花泷也做了个奇怪的梦，他在' \
           '一个从未去过的深山小镇中，变成了女高中生' \
           '。少男少女就这样在梦中邂逅了彼此，并带着' \
           '“不论你在世界何方我一定会去见你”的信念去' \
           '寻找彼此.'
    st.write(text)
    st.link_button('跳转播放',
                   'https://www.bilibili.com/video/BV1x2421A7ef/?spm_id_from=333.337.search-card.all.click&vd_source=84eb51fed7fddda10924239bfef2ad92',
                   help='B站下架正版了，整个网友传的',
                   type='secondary',
                   use_container_width=True
                   )


def page2():
    """图片处理工具"""
    st.write(":sunglasses:图片处理小程序:sunglasses:")
    uploaded_file = st.file_uploader('上传图片', type=['png', 'jpg', 'jpeg'])

    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size

        img = Image.open(uploaded_file).copy()

        change_color_img = img_change(img, 1, 2, 0)


def page3():
    """智慧词典"""
    with open('WordsSpace.txt', 'r', encoding='utf-8') as WordsSpace:
        words_list = WordsSpace.read().split("\n")

        for i in range(len(words_list)):
            words_list[i] = words_list[i].split("#")

        words_dict = {}
        for i in words_list:
            words_dict[i[1]] = [int(i[0]), i[2]]

    with open('CheckOutTimes.txt', 'r', encoding='utf-8') as CheckOutTimes:
        times_list = CheckOutTimes.read().split("\n")

        for i in range(len(times_list)):
            times_list[i] = times_list[i].split("#")

        times_dict = {}
        for i in times_list:
            times_dict[int(i[0])] = int(i[1])

    word = st.text_input('请输入要查询的单词').lower()

    if word in words_dict:
        st.write(words_dict[word][1])
        n = words_dict[word][0]

        if n in words_dict:
            times_dict[n] += 1

        else:
            times_dict[n] = 1

        with open('CheckOutTimes.txt', 'w', encoding='utf-8') as CheckOutTimes:
            massage = ''
            for k, v in times_dict.items():
                massage += f'{k}#{v}\n'

            massage = massage[:-1]
            CheckOutTimes.write(massage)

        st.write('查询次数:', times_dict[int(n)])

        if word == 'balloon':
            st.balloons()

        if word == "snow":
            st.snow()

        if word == "code":
            code = """
def page3():
    with open('WordsSpace.txt', 'r', encoding='utf-8') as WordsSpace:
        words_list = WordsSpace.read().split("\n")

        for i in range(len(words_list)):
            words_list[i] = words_list[i].split("#")

        words_dict = {}
        for i in words_list:
            words_dict[i[1]] = [int(i[0]), i[2]]

    with open('CheckOutTimes.txt', 'r', encoding='utf-8') as CheckOutTimes:
        times_list = CheckOutTimes.read().split("\n")

        for i in range(len(times_list)):
            times_list[i] = times_list[i].split("#")

        times_dict = {}
        for i in times_list:
            times_dict[int(i[0])] = int(i[1])

    word = st.text_input('请输入要查询的单词').lower()

    if word in words_dict:
        st.write(words_dict[word][1])
        n = words_dict[word][0]

        if n in words_dict:
            times_dict[n] += 1

        else:
            times_dict[n] = 1

        with open('CheckOutTimes.txt', 'w', encoding='utf-8') as CheckOutTimes:
            massage = ''
            for k, v in times_dict.items():
                massage += f'{k}#{v}\n'

            massage = massage[:-1]
            CheckOutTimes.write(massage)

        st.write('查询次数:', times_dict[int(n)])

        if word == 'balloon':
            st.balloons()

        if word == "snow":
            st.snow()

    elif word:
        st.write("请在上方输入要查询的单词")
    else:
        st.write("此单词尚未收录，尽请期待")
        """
            st.code(code)

    elif word:
        st.write("请在上方输入要查询的单词")

    else:
        st.write("此单词尚未收录，尽请期待")


def page4():
    """留言区"""
    with open('LeaveMessage.txt', 'r', encoding='utf-8') as LeaveMessage:
        messages_list = LeaveMessage.read().split("\n")

        for i in range(len(messages_list)):
            messages_list[i] = messages_list[i].split("#")

        for i in messages_list:
            if i[1] == '阿短':
                with st.chat_message('😋'):
                    st.write(i[1] + ':' + i[2])

            elif i[1] == '编程猫':
                with st.chat_message('🎏'):
                    st.write(i[1] + ':' + i[2])

        name = st.selectbox('我是：', ['阿短', '编程猫'])
        new_message = st.text_input('想要说的话：')
        if st.button('留言'):
            messages_list.append([str(int(messages_list[-1][0]) + 1), name, new_message])

        with open('LeaveMessage.txt', 'w', encoding='utf-8') as LeaveMessage:
            message = ''
            for i in messages_list:
                message += f'{i[0]}#{i[1]}#{i[2]}\n'

            message = message[:-1]
            LeaveMessage.write(message)

def page5():
    """计算器"""
    st.write()


if page == '兴趣推荐':
    page1()
elif page == '图片处理工具':
    page2()
elif page == '智慧词典':
    page3()
elif page == '留言区':
    page4()
