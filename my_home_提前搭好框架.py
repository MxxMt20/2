'''我的主页'''
import streamlit as st
from PIL import Image


page = st.sidebar.radio('我的首页', ['整合包推荐', '游戏分享图片处理工具', '指定查找', '我的留言区','滑动条_应用'])



def page_1():
    '''整合包推荐'''

    tab1,tab2,tab3 = st.tabs(["冒险","科技","魔改"])
    with tab1:
        st.write('limit小火柴的乌托邦')
        st.image('wtb.png')    
        st.write('传送门 → https://note.youdao.com/s/7BOzSgLt')
        st.write('夸克网盘传送门 → https://pan.quark.cn/s/eaea50184e65')
        st.write('---------------------------------------------------------------')

        st.write('[TFC:TAW]群峦传说·异世界行纪')
        st.image('qr.jpg')    
        st.write('传送门 → https://www.mcmod.cn/modpack/805.html')
        st.write('---------------------------------------------------------------')

        st.write('[TWR]冬季救援')
        st.image('djjy.jpg')    
        st.write('传送门 → https://www.mcmod.cn/modpack/273.html')
        st.write('---------------------------------------------------------------')

        st.write('水星迫降重制版 Mercury landing')
        st.image('sxpj.jpg')    
        st.write('传送门 → https://www.mcmod.cn/modpack/429.html')
        st.write('---------------------------------------------------------------')

        
    with tab2:
        st.write('[IF2]无限:重生')
        st.image('cs.jpg')    
        st.write('传送门 → https://www.mcmod.cn/modpack/753.html')
        st.write('---------------------------------------------------------------')

        st.write('[PTY]寄生科技')
        st.image('pty.jpg')    
        st.write('传送门 → https://www.mcmod.cn/modpack/652.html')
        st.write('---------------------------------------------------------------')
        
    with tab3:
        st.write('[FMN]勿忘我')
        st.image('www.jpg')    
        st.write('传送门 → https://www.mcmod.cn/modpack/787.html')
        st.write('---------------------------------------------------------------')

        st.write('合虚为实：原子空间')
        st.image('ato.jpg')    
        st.write('传送门 → https://www.mcmod.cn/modpack/240.html')
        st.write('---------------------------------------------------------------')


    

def page_2():
    '''游戏分享图片处理工具'''
    st.write(":sunglasses:图片处理小程序:sunglasses:")

    uploaded_file = st.file_uploader("上传图片",type=['png','jpeg','jpg'])
    if uploaded_file:
        #file_name = uploaded_file.name
        #file_type = uploaded_file.type
        #file_size = uploaded_file.size 
        img = Image.open(uploaded_file)
        tab1,tab2,tab3,tab4 = st.tabs(["原图","改色1","改色2","改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))   
def img_change(img,rc,gc,bc):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x, y][gc]
            b = img_array[x,y][bc]
            img_array[x,y]=(r,g,b)        
    return img



    
def page_3():
    '''指定查找'''
    st.write('指定查找')
    with open('ss.txt','r',encoding='utf-8')as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i]= words_list[i].split('#')
    words_dict ={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]
        
    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict ={}
    for i in times_list:
        times_dict[int(i[0])]= int(i[1])
    word = st.text_input('请输入进行査询')
    if word in words_dict:
        st.write(words_dict[word][1])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n]+= 1
        else:
            times_dict[n]=1
            with open('check_out_times.txt','w',encoding='utf-8')as f:
                message = ''
                for k,v in times_dict.items():
                    message += str(k)+'#'+str(v)+'\n'
                message = message[:-1]
                f.write(message)
        st.write('查询次数:', times_dict[n])



def page_4():
    '''我的留言区'''
    st.write('我的留言区')
    with open('kk.txt','r',encoding='utf-8') as f:
        messages_list=f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1]=='生存类':
            with st.chat_message('1'):
                st.write(i[1],':',i[2])
        elif i[1]=='科技类':
            with st.chat_message('2'):
                st.write(i[1],':',i[2])
        elif i[1]=='魔改类':
            with st.chat_message('2'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是.….',['生存类','科技类','魔改类'])
    new_message = st.text_input('想要说的话......')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open('kk.txt','w',encoding='utf-8')as f:
            message = ''
            for i in messages_list:
                message += i[0] +'#'+ i[1]+'#'+ i[2] +'\n'
            message = message[:-1]
            f.write(message)

def page_5():
    '''滑动条_应用'''
    import streamlit as st
    
    # 滑动条st.slider()
    number1 = st.slider('数据1：', 1, 100, 50)
    number2, number3 = st.slider('数据2和3：', 1, 10, (4, 6))
    st.write('数据1：', number1)
    st.write('数据2-3：', number2, '-', number3)
    
    # 如何创建滑动条？
    # 滑动条中可以有几个数据点？
    
    # 挑战：显示七色彩虹的一部分，如“红橙黄绿”、“黄绿蓝靛紫”……
    st.write('----')
    msg_lst = ['红', '橙', '黄', '绿', '蓝', '靛', '紫']
    begin, end = st.slider('选择显示的彩虹：', 1, len(msg_lst), (1, len(msg_lst)))
    message = ''
    for i in range(begin-1, end):
        message += msg_lst[i]
    st.write(message)












    
if page == '整合包推荐':
    page_1()
elif page == '游戏分享图片处理工具':
    page_2()
elif page == '指定查找':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '滑动条_应用':
    page_5()


#python -m streamlit run my_home_提前搭好框架.py